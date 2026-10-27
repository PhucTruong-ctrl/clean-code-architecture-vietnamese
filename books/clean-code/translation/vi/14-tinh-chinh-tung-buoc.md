# Chương 14: Tinh chỉnh từng bước

Nghiên cứu tình huống về bộ phân tích đối số dòng lệnh

Chương này là một nghiên cứu tình huống về quá trình tinh chỉnh từng bước. Bạn sẽ thấy một mô-đun khởi đầu tốt nhưng không mở rộng được. Sau đó, bạn sẽ thấy mô-đun được tái cấu trúc và làm sạch ra sao.

Hẳn ai trong chúng ta cũng từng phải phân tích đối số dòng lệnh. Nếu không có sẵn tiện ích phù hợp, ta chỉ việc duyệt mảng chuỗi được truyền vào hàm `main`. Có nhiều tiện ích tốt từ nhiều nguồn khác nhau, nhưng không tiện ích nào làm đúng mọi thứ tôi muốn. Vậy nên, dĩ nhiên tôi quyết định tự viết một cái. Tôi gọi nó là `Args`.

`Args` rất dễ dùng. Bạn chỉ cần khởi tạo lớp `Args` với các đối số đầu vào và một chuỗi định dạng, rồi truy vấn đối tượng `Args` để lấy giá trị của các đối số. Hãy xem ví dụ đơn giản sau:

**Đoạn mã 14-1**  
**Cách dùng Args đơn giản**

```java
public static void main(String[] args) {
  try {
    Args arg = new Args("l,p#,d*", args);
    boolean logging = arg.getBoolean('l');
    int port = arg.getInt('p');
    String directory = arg.getString('d');
    executeApplication(logging, port, directory);
  } catch (ArgsException e) {
    System.out.printf("Argument error: %s\n", e.errorMessage());
  }
}
```

Bạn thấy cách dùng đơn giản thế nào. Ta chỉ cần tạo một thể hiện của lớp `Args` với hai tham số. Tham số đầu tiên là chuỗi định dạng, hay lược đồ: `"l,p#,d*"`. Chuỗi này định nghĩa ba đối số dòng lệnh. Đối số đầu tiên, `-l`, là kiểu boolean. Đối số thứ hai, `-p`, là kiểu số nguyên. Đối số thứ ba, `-d`, là kiểu chuỗi. Tham số thứ hai của hàm dựng `Args` đơn giản là mảng đối số dòng lệnh được truyền vào `main`.

Nếu hàm dựng kết thúc mà không ném `ArgsException`, các đối số dòng lệnh đầu vào đã được phân tích và đối tượng `Args` sẵn sàng để truy vấn. Những phương thức như `getBoolean`, `getInteger` và `getString` cho phép ta truy cập giá trị của các đối số theo tên.

Nếu có vấn đề trong chuỗi định dạng hoặc trong chính các đối số dòng lệnh, một `ArgsException` sẽ được ném ra. Bạn có thể gọi phương thức `errorMessage` của ngoại lệ để lấy mô tả tiện dụng về lỗi đã xảy ra.

## Cài đặt Args

Đoạn mã 14-2 là phần cài đặt lớp `Args`. Hãy đọc thật kỹ. Tôi đã dụng công chăm chút phong cách và cấu trúc, hy vọng bạn thấy đáng để noi theo.

**Đoạn mã 14-2**  
**Args.java**

```java
package com.objectmentor.utilities.args;

import static com.objectmentor.utilities.args.ArgsException.ErrorCode.*;
import java.util.*;
public class Args {
  private Map<Character, ArgumentMarshaler> marshalers;
  private Set<Character> argsFound;
  private ListIterator<String> currentArgument;

  public Args(String schema, String[] args) throws ArgsException {
    marshalers = new HashMap<Character, ArgumentMarshaler>();
    argsFound = new HashSet<Character>();

    parseSchema(schema);
    parseArgumentStrings(Arrays.asList(args));
  }
  private void parseSchema(String schema) throws ArgsException {
    for (String element : schema.split(","))
      if (element.length() > 0)
        parseSchemaElement(element.trim());
  }

  private void parseSchemaElement(String element) throws ArgsException {
    char elementId = element.charAt(0);
    String elementTail = element.substring(1);
    validateSchemaElementId(elementId);
    if (elementTail.length() == 0)
      marshalers.put(elementId, new BooleanArgumentMarshaler());
    else if (elementTail.equals("*"))
      marshalers.put(elementId, new StringArgumentMarshaler());
    else if (elementTail.equals("#"))
      marshalers.put(elementId, new IntegerArgumentMarshaler());
    else if (elementTail.equals("##"))
      marshalers.put(elementId, new DoubleArgumentMarshaler());
    else if (elementTail.equals("[*]"))
      marshalers.put(elementId, new StringArrayArgumentMarshaler());
    else
      throw new ArgsException(INVALID_ARGUMENT_FORMAT, elementId, elementTail);
  }

  private void validateSchemaElementId(char elementId) throws ArgsException {
    if (!Character.isLetter(elementId))
      throw new ArgsException(INVALID_ARGUMENT_NAME, elementId, null);
  }

  private void parseArgumentStrings(List<String> argsList) throws ArgsException
  {
    for (currentArgument = argsList.listIterator(); currentArgument.hasNext();)
    {
      String argString = currentArgument.next();
      if (argString.startsWith("-")) {
        parseArgumentCharacters(argString.substring(1));
      } else {
        currentArgument.previous();
        break;
      }
    }
  }

  private void parseArgumentCharacters(String argChars) throws ArgsException {
    for (int i = 0; i < argChars.length(); i++)
      parseArgumentCharacter(argChars.charAt(i));
  }

  private void parseArgumentCharacter(char argChar) throws ArgsException {
    ArgumentMarshaler m = marshalers.get(argChar);
    if (m == null) {
      throw new ArgsException(UNEXPECTED_ARGUMENT, argChar, null);
    } else {
      argsFound.add(argChar);
      try {
        m.set(currentArgument);
      } catch (ArgsException e) {
        e.setErrorArgumentId(argChar);
        throw e;
      }
    }
  }

  public boolean has(char arg) {
    return argsFound.contains(arg);
  }

  public int nextArgument() {
    return currentArgument.nextIndex();
  }

  public boolean getBoolean(char arg) {
    return BooleanArgumentMarshaler.getValue(marshalers.get(arg));
  }

  public String getString(char arg) {
    return StringArgumentMarshaler.getValue(marshalers.get(arg));
  }
  public int getInt(char arg) {
    return IntegerArgumentMarshaler.getValue(marshalers.get(arg));
  }

  public double getDouble(char arg) {
    return DoubleArgumentMarshaler.getValue(marshalers.get(arg));
  }

  public String[] getStringArray(char arg) {
    return StringArrayArgumentMarshaler.getValue(marshalers.get(arg));
  }
}
```

Bạn có thể đọc đoạn mã này từ trên xuống dưới mà không phải nhảy qua lại hay nhìn trước nhiều. Có lẽ bạn chỉ cần nhìn trước để tìm định nghĩa `ArgumentMarshaler`, phần tôi cố ý bỏ đi. Đọc kỹ đoạn mã này xong, hẳn bạn đã hiểu giao diện `ArgumentMarshaler` và các lớp phái sinh của nó làm gì. Giờ tôi sẽ cho bạn xem một vài lớp đó, từ Đoạn mã 14-3 đến Đoạn mã 14-6.

**Đoạn mã 14-3**  
**ArgumentMarshaler.java**

```java
public interface ArgumentMarshaler {
  void set(Iterator<String> currentArgument) throws ArgsException;
}
```

**Đoạn mã 14-4**  
**BooleanArgumentMarshaler.java**

```java
public class BooleanArgumentMarshaler implements ArgumentMarshaler {
  private boolean booleanValue = false;

  public void set(Iterator<String> currentArgument) throws ArgsException {
    booleanValue = true;
  }

  public static boolean getValue(ArgumentMarshaler am) {
    if (am != null && am instanceof BooleanArgumentMarshaler)
      return ((BooleanArgumentMarshaler) am).booleanValue;
    else
      return false;
  }
}
```

**Đoạn mã 14-5**  
**StringArgumentMarshaler.java**

```java
import static com.objectmentor.utilities.args.ArgsException.ErrorCode.*;

public class StringArgumentMarshaler implements ArgumentMarshaler {
  private String stringValue = "";
  public void set(Iterator<String> currentArgument) throws ArgsException {
    try {
      stringValue = currentArgument.next();
    } catch (NoSuchElementException e) {
      throw new ArgsException(MISSING_STRING);
    }
  }

  public static String getValue(ArgumentMarshaler am) {
    if (am != null && am instanceof StringArgumentMarshaler)
      return ((StringArgumentMarshaler) am).stringValue;
    else
      return "";
  }
}
```

**Đoạn mã 14-6**  
**IntegerArgumentMarshaler.java**

```java
import static com.objectmentor.utilities.args.ArgsException.ErrorCode.*;

public class IntegerArgumentMarshaler implements ArgumentMarshaler {
  private int intValue = 0;

  public void set(Iterator<String> currentArgument) throws ArgsException {
    String parameter = null;
    try {
      parameter = currentArgument.next();
      intValue = Integer.parseInt(parameter);
    } catch (NoSuchElementException e) {
      throw new ArgsException(MISSING_INTEGER);
    } catch (NumberFormatException e) {
      throw new ArgsException(INVALID_INTEGER, parameter);
    }
  }

  public static int getValue(ArgumentMarshaler am) {
    if (am != null && am instanceof IntegerArgumentMarshaler)
      return ((IntegerArgumentMarshaler) am).intValue;
    else
      return 0;
  }
}
```

Các lớp phái sinh `ArgumentMarshaler` còn lại chỉ lặp lại mô thức này cho số thực dấu phẩy động và mảng chuỗi; đưa chúng vào đây sẽ khiến chương này rườm rà. Tôi để phần đó làm bài tập cho bạn.

Có thể còn một thông tin khác khiến bạn băn khoăn: định nghĩa các hằng mã lỗi. Chúng nằm trong lớp `ArgsException` (Đoạn mã 14-7).

**Đoạn mã 14-7**  
**ArgsException.java**

```java
import static com.objectmentor.utilities.args.ArgsException.ErrorCode.*;

public class ArgsException extends Exception {
  private char errorArgumentId = '\0';
  private String errorParameter = null;
  private ErrorCode errorCode = OK;

  public ArgsException() {}

  public ArgsException(String message) {super(message);}

  public ArgsException(ErrorCode errorCode) {
    this.errorCode = errorCode;
  }
  public ArgsException(ErrorCode errorCode, String errorParameter) {
    this.errorCode = errorCode;
    this.errorParameter = errorParameter;
  }
  public ArgsException(ErrorCode errorCode,
                       char errorArgumentId, String errorParameter) {
    this.errorCode = errorCode;
    this.errorParameter = errorParameter;
    this.errorArgumentId = errorArgumentId;
  }

  public char getErrorArgumentId() {
    return errorArgumentId;
  }
  public void setErrorArgumentId(char errorArgumentId) {
    this.errorArgumentId = errorArgumentId;
  }
  public String getErrorParameter() {
    return errorParameter;
  }

  public void setErrorParameter(String errorParameter) {
    this.errorParameter = errorParameter;
  }

  public ErrorCode getErrorCode() {
    return errorCode;
  }

  public void setErrorCode(ErrorCode errorCode) {
    this.errorCode = errorCode;
  }

  public String errorMessage() {
    switch (errorCode) {
      case OK:
        return "TILT: Should not get here.";
      case UNEXPECTED_ARGUMENT:
        return String.format("Argument -%c unexpected.", errorArgumentId);
      case MISSING_STRING:
        return String.format("Could not find string parameter for -%c.",
                             errorArgumentId);
      case INVALID_INTEGER:
        return String.format("Argument -%c expects an integer but was '%s'.",
                             errorArgumentId, errorParameter);
      case MISSING_INTEGER:
        return String.format("Could not find integer parameter for -%c.",
                             errorArgumentId);
      case INVALID_DOUBLE:
        return String.format("Argument -%c expects a double but was '%s'.",
                             errorArgumentId, errorParameter);
      case MISSING_DOUBLE:
        return String.format("Could not find double parameter for -%c.",
                             errorArgumentId);
      case INVALID_ARGUMENT_NAME:
        return String.format("'%c' is not a valid argument name.",
                             errorArgumentId);
      case INVALID_ARGUMENT_FORMAT:
        return String.format("'%s' is not a valid argument format.",
                             errorParameter);
    }
    return "";
  }

  public enum ErrorCode {
    OK, INVALID_ARGUMENT_FORMAT, UNEXPECTED_ARGUMENT, INVALID_ARGUMENT_NAME,
    MISSING_STRING,
    MISSING_INTEGER, INVALID_INTEGER,
    MISSING_DOUBLE, INVALID_DOUBLE}
}
```

Thật đáng kinh ngạc là một ý tưởng đơn giản như vậy lại cần đến ngần ấy mã để triển khai đầy đủ chi tiết. Một lý do là Java khá rườm rà. Là ngôn ngữ định kiểu tĩnh, Java đòi hỏi nhiều từ ngữ để thỏa mãn hệ thống kiểu. Trong Ruby, Python hay Smalltalk, chương trình này ngắn hơn nhiều.¹

Hãy đọc lại đoạn mã một lần nữa. Chú ý cách đặt tên, kích thước các hàm và định dạng mã. Nếu là lập trình viên giàu kinh nghiệm, có thể bạn sẽ bắt bẻ đôi chỗ về phong cách hay cấu trúc. Dù vậy, tôi hy vọng nhìn chung bạn sẽ thấy chương trình được viết gọn gàng, có cấu trúc sạch sẽ.

Chẳng hạn, hẳn bạn thấy rõ cách bổ sung một kiểu đối số mới, như ngày tháng hay số phức, và việc đó chỉ tốn chút công sức. Tóm lại, chỉ cần tạo một lớp phái sinh mới của `ArgumentMarshaler`, thêm một hàm `getXXX` và một nhánh `case` trong hàm `parseSchemaElement`. Có lẽ cũng cần thêm một `ArgsException.ErrorCode` mới cùng thông báo lỗi tương ứng.

### Tôi đã làm việc này như thế nào?

Để bạn yên tâm, tôi không viết chương trình này từ đầu đến cuối theo đúng hình thức hiện tại. Quan trọng hơn, tôi không mong bạn viết được chương trình sạch sẽ, tao nhã chỉ trong một lượt. Nếu vài thập kỷ qua dạy cho chúng ta điều gì, thì đó là lập trình thiên về tay nghề hơn khoa học. Muốn viết mã sạch, trước hết bạn phải viết mã bẩn, rồi làm sạch nó.

Điều này hẳn không làm bạn ngạc nhiên. Ta đã học được sự thật đó từ hồi tiểu học, khi thầy cô cố (thường là vô ích) khuyên ta viết bản nháp cho các bài luận. Họ bảo rằng ta nên viết bản nháp đầu, rồi bản thứ hai, sau đó viết thêm vài bản nữa cho đến khi có bản cuối cùng. Họ muốn ta hiểu rằng viết một bài luận sạch sẽ là quá trình tinh chỉnh từng bước.

¹ Gần đây tôi viết lại mô-đun này bằng Ruby. Bản đó chỉ bằng một phần bảy kích thước và có cấu trúc nhỉnh hơn đôi chút.

Hầu hết lập trình viên mới vào nghề, cũng như hầu hết học sinh tiểu học, không làm theo lời khuyên ấy. Họ tin rằng mục tiêu chính là làm cho chương trình chạy được. Khi chương trình đã “chạy được”, họ chuyển sang việc tiếp theo, để mặc nó trong tình trạng mà họ đã khiến nó “chạy được”. Hầu hết lập trình viên dày dạn đều biết đó là tự sát nghề nghiệp.

## Args: bản nháp đầu tiên

Đoạn mã 14-8 cho thấy một phiên bản cũ hơn của lớp `Args`. Nó “chạy được”. Và nó bừa bộn.

**Đoạn mã 14-8**  
**Args.java (bản nháp đầu tiên)**

```java
import java.text.ParseException;
import java.util.*;

public class Args {
  private String schema;
  private String[] args;
  private boolean valid = true;
  private Set<Character> unexpectedArguments = new TreeSet<Character>();
  private Map<Character, Boolean> booleanArgs =
    new HashMap<Character, Boolean>();
  private Map<Character, String> stringArgs = new HashMap<Character, String>();
  private Map<Character, Integer> intArgs = new HashMap<Character, Integer>();
  private Set<Character> argsFound = new HashSet<Character>();
  private int currentArgument;
  private char errorArgumentId = '\0';
  private String errorParameter = "TILT";
  private ErrorCode errorCode = ErrorCode.OK;

  private enum ErrorCode {
    OK, MISSING_STRING, MISSING_INTEGER, INVALID_INTEGER, UNEXPECTED_ARGUMENT}
  public Args(String schema, String[] args) throws ParseException {
    this.schema = schema;
    this.args = args;
    valid = parse();
  }

  private boolean parse() throws ParseException {
    if (schema.length() == 0 && args.length == 0)
      return true;
    parseSchema();
    try {
      parseArguments();
    } catch (ArgsException e) {
    }
    return valid;
  }
  private boolean parseSchema() throws ParseException {
    for (String element : schema.split(",")) {
      if (element.length() > 0) {
        String trimmedElement = element.trim();
        parseSchemaElement(trimmedElement);
      }
    }
    return true;
  }

  private void parseSchemaElement(String element) throws ParseException {
    char elementId = element.charAt(0);
    String elementTail = element.substring(1);
    validateSchemaElementId(elementId);
    if (isBooleanSchemaElement(elementTail))
      parseBooleanSchemaElement(elementId);
    else if (isStringSchemaElement(elementTail))
      parseStringSchemaElement(elementId);
    else if (isIntegerSchemaElement(elementTail)) {
      parseIntegerSchemaElement(elementId);
    } else {
      throw new ParseException(
        String.format("Argument: %c has invalid format: %s.",
                      elementId, elementTail), 0);
    }
  }
  private void validateSchemaElementId(char elementId) throws ParseException {
    if (!Character.isLetter(elementId)) {
      throw new ParseException(
        "Bad character:" + elementId + "in Args format: " + schema, 0);
    }
  }

  private void parseBooleanSchemaElement(char elementId) {
    booleanArgs.put(elementId, false);
  }
  private void parseIntegerSchemaElement(char elementId) {
    intArgs.put(elementId, 0);
  }

  private void parseStringSchemaElement(char elementId) {
    stringArgs.put(elementId, "");
  }

  private boolean isStringSchemaElement(String elementTail) {
    return elementTail.equals("*");
  }

  private boolean isBooleanSchemaElement(String elementTail) {
    return elementTail.length() == 0;
  }

  private boolean isIntegerSchemaElement(String elementTail) {
    return elementTail.equals("#");
  }
  private boolean parseArguments() throws ArgsException {
    for (currentArgument = 0; currentArgument < args.length; currentArgument++)
    {
      String arg = args[currentArgument];
      parseArgument(arg);
    }
    return true;
  }

  private void parseArgument(String arg) throws ArgsException {
    if (arg.startsWith("-"))
      parseElements(arg);
  }

  private void parseElements(String arg) throws ArgsException {
    for (int i = 1; i < arg.length(); i++)
      parseElement(arg.charAt(i));
  }

  private void parseElement(char argChar) throws ArgsException {
    if (setArgument(argChar))
      argsFound.add(argChar);
    else {
      unexpectedArguments.add(argChar);
      errorCode = ErrorCode.UNEXPECTED_ARGUMENT;
      valid = false;
    }
  }
  private boolean setArgument(char argChar) throws ArgsException {
    if (isBooleanArg(argChar))
      setBooleanArg(argChar, true);
    else if (isStringArg(argChar))
      setStringArg(argChar);
    else if (isIntArg(argChar))
      setIntArg(argChar);
    else
      return false;

    return true;
  }
  private boolean isIntArg(char argChar) {return intArgs.containsKey(argChar);}

  private void setIntArg(char argChar) throws ArgsException {
    currentArgument++;
    String parameter = null;
    try {
      parameter = args[currentArgument];
      intArgs.put(argChar, new Integer(parameter));
    } catch (ArrayIndexOutOfBoundsException e) {
      valid = false;
      errorArgumentId = argChar;
      errorCode = ErrorCode.MISSING_INTEGER;
      throw new ArgsException();
    } catch (NumberFormatException e) {
      valid = false;
      errorArgumentId = argChar;
      errorParameter = parameter;
      errorCode = ErrorCode.INVALID_INTEGER;
      throw new ArgsException();
    }
  }
  private void setStringArg(char argChar) throws ArgsException {
    currentArgument++;
    try {
      stringArgs.put(argChar, args[currentArgument]);
    } catch (ArrayIndexOutOfBoundsException e) {
      valid = false;
      errorArgumentId = argChar;
      errorCode = ErrorCode.MISSING_STRING;
      throw new ArgsException();
    }
  }
  private boolean isStringArg(char argChar) {
    return stringArgs.containsKey(argChar);
  }

  private void setBooleanArg(char argChar, boolean value) {
    booleanArgs.put(argChar, value);
  }
  private boolean isBooleanArg(char argChar) {
    return booleanArgs.containsKey(argChar);
  }

  public int cardinality() {
    return argsFound.size();
  }

  public String usage() {
    if (schema.length() > 0)
      return "-[" + schema + "]";
    else
      return "";
  }

  public String errorMessage() throws Exception {
    switch (errorCode) {
      case OK:
        throw new Exception("TILT: Should not get here.");
      case UNEXPECTED_ARGUMENT:
        return unexpectedArgumentMessage();
      case MISSING_STRING:
        return String.format("Could not find string parameter for -%c.",
                             errorArgumentId);
      case INVALID_INTEGER:
        return String.format("Argument -%c expects an integer but was '%s'.",
                             errorArgumentId, errorParameter);
      case MISSING_INTEGER:
        return String.format("Could not find integer parameter for -%c.",
                             errorArgumentId);
    }
    return "";
  }
  private String unexpectedArgumentMessage() {
    StringBuffer message = new StringBuffer("Argument(s) -");
    for (char c : unexpectedArguments) {
      message.append(c);
    }
    message.append(" unexpected.");

    return message.toString();
  }

  private boolean falseIfNull(Boolean b) {
    return b != null && b;
  }

  private int zeroIfNull(Integer i) {
    return i == null ? 0 : i;
  }

  private String blankIfNull(String s) {
    return s == null ? "" : s;
  }

  public String getString(char arg) {
    return blankIfNull(stringArgs.get(arg));
  }
  public int getInt(char arg) {
    return zeroIfNull(intArgs.get(arg));
  }

  public boolean getBoolean(char arg) {
    return falseIfNull(booleanArgs.get(arg));
  }

  public boolean has(char arg) {
    return argsFound.contains(arg);
  }

  public boolean isValid() {
    return valid;
  }

  private class ArgsException extends Exception {
  }
}
```

Tôi hy vọng phản ứng ban đầu của bạn trước đống mã này là: “May mà anh ấy không để nó nguyên như vậy!” Nếu đúng thế, hãy nhớ người khác cũng sẽ nghĩ vậy về đoạn mã nháp bạn để lại.

Nói “bản nháp đầu tiên” có lẽ là cách gọi tử tế nhất cho đoạn mã này. Rõ ràng nó còn đang dang dở. Chỉ riêng số lượng biến thể hiện đã đủ ngợp. Những chuỗi kỳ quặc như `"TILT"`, các `HashSet` và `TreeSet`, cùng những khối try-catch-catch, tất cả hợp lại thành một đống đang thối rữa.

Tôi không định viết ra một đống thối rữa như vậy. Thật ra, tôi đã cố giữ mọi thứ tương đối ngăn nắp. Bạn có thể nhận ra điều đó qua cách tôi đặt tên hàm và biến, cũng như cấu trúc sơ sài của chương trình. Nhưng rõ ràng tôi đã để vấn đề vượt khỏi tầm kiểm soát.

Mớ hỗn độn ấy hình thành dần dần. Các phiên bản trước đó không hề tệ đến thế. Chẳng hạn, Đoạn mã 14-9 cho thấy phiên bản cũ hơn, khi mới chỉ xử lý được đối số boolean.

**Đoạn mã 14-9**  
**Args.java (chỉ có boolean)**

```java
package com.objectmentor.utilities.getopts;

import java.util.*;
public class Args {
  private String schema;
  private String[] args;
  private boolean valid;
  private Set<Character> unexpectedArguments = new TreeSet<Character>();
  private Map<Character, Boolean> booleanArgs =
    new HashMap<Character, Boolean>();
  private int numberOfArguments = 0;

  public Args(String schema, String[] args) {
    this.schema = schema;
    this.args = args;
    valid = parse();
  }
  public boolean isValid() {
    return valid;
  }

  private boolean parse() {
    if (schema.length() == 0 && args.length == 0)
      return true;
    parseSchema();
    parseArguments();
    return unexpectedArguments.size() == 0;
  }

  private boolean parseSchema() {
    for (String element : schema.split(",")) {
      parseSchemaElement(element);
    }
    return true;
  }

  private void parseSchemaElement(String element) {
    if (element.length() == 1) {
      parseBooleanSchemaElement(element);
    }
  }

  private void parseBooleanSchemaElement(String element) {
    char c = element.charAt(0);
    if (Character.isLetter(c)) {
      booleanArgs.put(c, false);
    }
  }

  private boolean parseArguments() {
    for (String arg : args)
      parseArgument(arg);
    return true;
  }
  private void parseArgument(String arg) {
    if (arg.startsWith("-"))
      parseElements(arg);
  }

  private void parseElements(String arg) {
    for (int i = 1; i < arg.length(); i++)
      parseElement(arg.charAt(i));
  }

  private void parseElement(char argChar) {
    if (isBoolean(argChar)) {
      numberOfArguments++;
      setBooleanArg(argChar, true);
    } else
      unexpectedArguments.add(argChar);
  }

  private void setBooleanArg(char argChar, boolean value) {
    booleanArgs.put(argChar, value);
  }

  private boolean isBoolean(char argChar) {
    return booleanArgs.containsKey(argChar);
  }

  public int cardinality() {
    return numberOfArguments;
  }

  public String usage() {
    if (schema.length() > 0)
      return "-["+schema+"]";
    else
      return "";
  }

  public String errorMessage() {
    if (unexpectedArguments.size() > 0) {
      return unexpectedArgumentMessage();
    } else
      return "";
  }
  private String unexpectedArgumentMessage() {
    StringBuffer message = new StringBuffer("Argument(s) -");
    for (char c : unexpectedArguments) {
      message.append(c);
    }
    message.append(" unexpected.");
    return message.toString();
  }

  public boolean getBoolean(char arg) {
    return booleanArgs.get(arg);
  }
}
```

Dù có thể bắt bẻ nhiều điểm trong đoạn mã này, nó thực ra cũng không tệ lắm. Nó gọn, đơn giản và dễ hiểu. Tuy vậy, ngay trong đoạn mã này đã lộ ra những mầm mống của đống thối rữa về sau. Có thể thấy rõ nó đã phát triển thành mớ hỗn độn kia như thế nào.

Lưu ý rằng mớ hỗn độn về sau chỉ có thêm hai kiểu đối số so với phiên bản này: `String` và số nguyên. Chỉ thêm hai kiểu đối số mà tác động tiêu cực lên mã lại rất lớn. Từ một thứ có thể bảo trì tương đối dễ dàng, nó biến thành thứ mà tôi nghĩ sẽ đầy lỗi và khiếm khuyết.

Tôi bổ sung hai kiểu đối số đó từng bước. Trước tiên, tôi thêm đối số `String`, tạo ra phiên bản sau:

**Đoạn mã 14-10**  
**Args.java (boolean và String)**

```java
package com.objectmentor.utilities.getopts;

import java.text.ParseException;
import java.util.*;
public class Args {
  private String schema;
  private String[] args;
  private boolean valid = true;
  private Set<Character> unexpectedArguments = new TreeSet<Character>();
  private Map<Character, Boolean> booleanArgs =
    new HashMap<Character, Boolean>();
  private Map<Character, String> stringArgs =
    new HashMap<Character, String>();
  private Set<Character> argsFound = new HashSet<Character>();
  private int currentArgument;
  private char errorArgument = '\0';
  enum ErrorCode {
    OK, MISSING_STRING}

  private ErrorCode errorCode = ErrorCode.OK;
  public Args(String schema, String[] args) throws ParseException {
    this.schema = schema;
    this.args = args;
    valid = parse();
  }

  private boolean parse() throws ParseException {
    if (schema.length() == 0 && args.length == 0)
      return true;
    parseSchema();
    parseArguments();
    return valid;
  }
  private boolean parseSchema() throws ParseException {
    for (String element : schema.split(",")) {
      if (element.length() > 0) {
        String trimmedElement = element.trim();
        parseSchemaElement(trimmedElement);
      }
    }
    return true;
  }

  private void parseSchemaElement(String element) throws ParseException {
    char elementId = element.charAt(0);
    String elementTail = element.substring(1);
    validateSchemaElementId(elementId);
    if (isBooleanSchemaElement(elementTail))
      parseBooleanSchemaElement(elementId);
    else if (isStringSchemaElement(elementTail))
      parseStringSchemaElement(elementId);
  }

  private void validateSchemaElementId(char elementId) throws ParseException {
    if (!Character.isLetter(elementId)) {
      throw new ParseException(
        "Bad character:" + elementId + "in Args format: " + schema, 0);
    }
  }

  private void parseStringSchemaElement(char elementId) {
    stringArgs.put(elementId, "");
  }

  private boolean isStringSchemaElement(String elementTail) {
    return elementTail.equals("*");
  }

  private boolean isBooleanSchemaElement(String elementTail) {
    return elementTail.length() == 0;
  }

  private void parseBooleanSchemaElement(char elementId) {
    booleanArgs.put(elementId, false);
  }

  private boolean parseArguments() {
    for (currentArgument = 0; currentArgument < args.length; currentArgument++)
    {
      String arg = args[currentArgument];
      parseArgument(arg);
    }
    return true;
  }

  private void parseArgument(String arg) {
    if (arg.startsWith("-"))
      parseElements(arg);
  }

  private void parseElements(String arg) {
    for (int i = 1; i < arg.length(); i++)
      parseElement(arg.charAt(i));
  }

  private void parseElement(char argChar) {
    if (setArgument(argChar))
      argsFound.add(argChar);
    else {
      unexpectedArguments.add(argChar);
      valid = false;
    }
  }

  private boolean setArgument(char argChar) {
    boolean set = true;
    if (isBoolean(argChar))
      setBooleanArg(argChar, true);
    else if (isString(argChar))
      setStringArg(argChar, "");
    else
      set = false;

    return set;
  }

  private void setStringArg(char argChar, String s) {
    currentArgument++;
    try {
      stringArgs.put(argChar, args[currentArgument]);
    } catch (ArrayIndexOutOfBoundsException e) {
      valid = false;
      errorArgument = argChar;
      errorCode = ErrorCode.MISSING_STRING;
    }
  }

  private boolean isString(char argChar) {
    return stringArgs.containsKey(argChar);
  }

  private void setBooleanArg(char argChar, boolean value) {
    booleanArgs.put(argChar, value);
  }

  private boolean isBoolean(char argChar) {
    return booleanArgs.containsKey(argChar);
  }

  public int cardinality() {
    return argsFound.size();
  }

  public String usage() {
    if (schema.length() > 0)
      return "-[" + schema + "]";
    else
      return "";
  }

  public String errorMessage() throws Exception {
    if (unexpectedArguments.size() > 0) {
      return unexpectedArgumentMessage();
    } else
      switch (errorCode) {
        case MISSING_STRING:
          return String.format("Could not find string parameter for -%c.",
                               errorArgument);
        case OK:
          throw new Exception("TILT: Should not get here.");
      }
    return "";
  }

  private String unexpectedArgumentMessage() {
    StringBuffer message = new StringBuffer("Argument(s) -");
    for (char c : unexpectedArguments) {
      message.append(c);
    }
    message.append(" unexpected.");

    return message.toString();
  }

  public boolean getBoolean(char arg) {
    return falseIfNull(booleanArgs.get(arg));
  }

  private boolean falseIfNull(Boolean b) {
    return b == null ? false : b;
  }

  public String getString(char arg) {
    return blankIfNull(stringArgs.get(arg));
  }

  private String blankIfNull(String s) {
    return s == null ? "" : s;
  }

  public boolean has(char arg) {
    return argsFound.contains(arg);
  }

  public boolean isValid() {
    return valid;
  }
}
```

Bạn thấy mọi thứ bắt đầu vượt tầm kiểm soát. Vẫn chưa đến nỗi quá tệ, nhưng mớ hỗn độn rõ ràng đang lớn dần. Nó đã thành một đống bừa bộn, dù chưa thối rữa hẳn. Phải đến khi thêm kiểu đối số số nguyên, đống ấy mới thực sự lên men và bốc mùi.

### Thế là tôi dừng lại

Tôi còn ít nhất hai kiểu đối số nữa cần bổ sung, và có thể đoán chúng sẽ khiến mọi chuyện tệ hơn nhiều. Nếu cứ húc đầu tiến lên, có lẽ tôi vẫn làm cho chúng chạy được, nhưng sẽ để lại một đống hỗn độn quá lớn để sửa. Nếu muốn cấu trúc mã này còn bảo trì được, thì phải sửa ngay lúc này.

Vì vậy, tôi ngừng thêm tính năng và bắt đầu tái cấu trúc. Vừa mới bổ sung đối số `String` và số nguyên, tôi nhận ra mỗi kiểu đối số đòi hỏi mã mới ở ba nơi chính. Trước hết, mỗi kiểu cần có cách phân tích phần tử trong lược đồ để chọn `HashMap` tương ứng. Kế đến, cần phân tích các chuỗi dòng lệnh và chuyển chúng sang kiểu thực. Cuối cùng, mỗi kiểu cần một phương thức `getXXX` để trả lại giá trị đúng kiểu cho bên gọi.

Nhiều kiểu khác nhau nhưng có các phương thức tương tự, nghe giống một lớp. Và thế là ý tưởng `ArgumentMarshaler` ra đời.

### Từng bước một

Một trong những cách tốt nhất để phá hỏng chương trình là thay đổi lớn cấu trúc của nó dưới danh nghĩa cải tiến. Có chương trình không bao giờ hồi phục sau những “cải tiến” như thế. Vấn đề là rất khó làm cho chương trình hoạt động lại đúng như trước khi được “cải tiến”.

Để tránh chuyện đó, tôi dùng kỷ luật Phát triển dựa trên kiểm thử (TDD). Một trong những nguyên lý trung tâm của cách làm này là luôn giữ cho hệ thống chạy được. Nói cách khác, khi dùng TDD, tôi không được phép tạo ra thay đổi khiến hệ thống hỏng. Mọi thay đổi tôi thực hiện đều phải giữ cho hệ thống hoạt động như trước.

Muốn làm được vậy, tôi cần một bộ kiểm thử tự động có thể chạy bất cứ lúc nào để xác nhận hành vi của hệ thống không đổi. Với lớp `Args`, tôi đã tạo một bộ kiểm thử đơn vị và kiểm thử chấp nhận trong lúc xây nên đống thối rữa ấy. Các kiểm thử đơn vị được viết bằng Java và chạy bằng JUnit. Các kiểm thử chấp nhận được viết thành những trang wiki trong FitNesse. Tôi có thể chạy chúng bất cứ khi nào, và nếu chúng đạt, tôi tự tin rằng hệ thống hoạt động đúng như đã đặc tả.

Sau đó, tôi tiến hành rất nhiều thay đổi nhỏ. Mỗi thay đổi đưa cấu trúc hệ thống đến gần hơn với ý tưởng `ArgumentMarshaler`, đồng thời vẫn giữ cho hệ thống hoạt động. Thay đổi đầu tiên là thêm bộ khung `ArgumentMarshaller` vào cuối đống mã thối rữa (Đoạn mã 14-11).

**Đoạn mã 14-11**  
**ArgumentMarshaller được thêm vào Args.java**

```java
private class ArgumentMarshaler {
    private boolean booleanValue = false;

    public void setBoolean(boolean value) {
      booleanValue = value;
    }

    public boolean getBoolean() {return booleanValue;}
  }

  private class BooleanArgumentMarshaler extends ArgumentMarshaler {
  }

  private class StringArgumentMarshaler extends ArgumentMarshaler {
  }
  private class IntegerArgumentMarshaler extends ArgumentMarshaler {
  }
}
```

Rõ ràng việc này không thể làm hỏng gì. Tiếp đó, tôi thực hiện thay đổi đơn giản nhất có thể, sao cho gây ảnh hưởng ít nhất. Tôi đổi `HashMap` dành cho các đối số boolean để nó lưu `ArgumentMarshaler`.

```java
private Map<Character, ArgumentMarshaler> booleanArgs =
  new HashMap<Character, ArgumentMarshaler>();
```

Điều này làm hỏng vài câu lệnh, tôi nhanh chóng sửa chúng.

```java
...
private void parseBooleanSchemaElement(char elementId) {
  booleanArgs.put(elementId, new BooleanArgumentMarshaler());
}
..
```
```java
private void setBooleanArg(char argChar, boolean value) {
  booleanArgs.get(argChar).setBoolean(value);
}
...
public boolean getBoolean(char arg) {
  return falseIfNull(booleanArgs.get(arg).getBoolean());
}
```

Bạn có thể thấy các thay đổi này nằm đúng ở những nơi tôi vừa nói: phân tích, thiết lập và lấy giá trị của kiểu đối số. Đáng tiếc là dù thay đổi nhỏ, một số kiểm thử bắt đầu thất bại. Nếu xem kỹ `getBoolean`, bạn sẽ thấy rằng khi gọi hàm với `'y'` mà không có đối số `y`, `booleanArgs.get('y')` sẽ trả về `null` và hàm ném `NullPointerException`. Hàm `falseIfNull` vốn được dùng để xử lý trường hợp này, nhưng thay đổi của tôi khiến nó không còn phù hợp.

Tinh thần phát triển tăng dần đòi hỏi tôi phải sửa lỗi này ngay trước khi làm bất cứ thay đổi nào khác. Thật ra, cách sửa không khó. Tôi chỉ cần chuyển chỗ kiểm tra `null`. Thứ cần kiểm tra không còn là giá trị boolean bị `null`, mà là `ArgumentMarshaller`.

Trước tiên, tôi bỏ lời gọi `falseIfNull` khỏi hàm `getBoolean`. Giờ nó vô ích, nên tôi cũng xóa luôn hàm đó. Kiểm thử vẫn thất bại theo cách cũ, vì vậy tôi tin rằng mình chưa gây ra lỗi mới.

```java
public boolean getBoolean(char arg) {
  return booleanArgs.get(arg).getBoolean();
}
```

Tiếp theo, tôi tách hàm thành hai dòng và đưa `ArgumentMarshaler` vào biến riêng tên là `argumentMarshaller`. Tôi không thích cái tên dài dòng này; nó thừa thãi và làm hàm thêm rối. Vì vậy tôi rút gọn thành `am` [N5].

```java
public boolean getBoolean(char arg) {
  Args.ArgumentMarshaler am = booleanArgs.get(arg);
  return am.getBoolean();
}
```

Rồi tôi thêm phần phát hiện `null`.

```java
public boolean getBoolean(char arg) {
  Args.ArgumentMarshaler am = booleanArgs.get(arg);
  return am != null && am.getBoolean();
}
```

## Đối số kiểu chuỗi

Việc bổ sung các đối số kiểu chuỗi rất giống với việc bổ sung đối số boolean. Tôi phải đổi `HashMap` rồi làm cho các hàm phân tích, thiết lập và lấy giá trị hoạt động. Phần tiếp theo hẳn sẽ không có gì bất ngờ, ngoại trừ có lẽ việc tôi dường như đang đưa toàn bộ phần cài đặt marshaling vào lớp cơ sở `ArgumentMarshaler` thay vì phân tán nó xuống các lớp dẫn xuất.

```java
private Map<Character, ArgumentMarshaler> stringArgs =
    new HashMap<Character, ArgumentMarshaler>();
...
private void parseStringSchemaElement(char elementId) {
  stringArgs.put(elementId, new StringArgumentMarshaler());
}
...
private void setStringArg(char argChar) throws ArgsException {
  currentArgument++;
  try {
    stringArgs.get(argChar).setString(args[currentArgument]);
  } catch (ArrayIndexOutOfBoundsException e) {
    valid = false;
    errorArgumentId = argChar;
    errorCode = ErrorCode.MISSING_STRING;
    throw new ArgsException();
  }
}
...
public String getString(char arg) {
  Args.ArgumentMarshaler am = stringArgs.get(arg);
  return am == null ? "" : am.getString();
}
...
private class ArgumentMarshaler {
  private boolean booleanValue = false;
  private String stringValue;

  public void setBoolean(boolean value) {
    booleanValue = value;
  }
  public boolean getBoolean() {
    return booleanValue;
  }

  public void setString(String s) {
    stringValue = s;
  }
  public String getString() {
    return stringValue == null ? "" : stringValue;
  }
}
```

Một lần nữa, tôi thực hiện các thay đổi từng bước một để kiểm thử vẫn chạy được, dù chưa nhất thiết phải đạt. Khi một kiểm thử hỏng, tôi bảo đảm nó chạy đạt trở lại rồi mới tiếp tục thay đổi.

Đến đây chắc bạn đã thấy ý định của tôi. Sau khi chuyển toàn bộ hành vi marshaling hiện có vào lớp cơ sở `ArgumentMarshaler`, tôi sẽ bắt đầu đẩy hành vi đó xuống các lớp dẫn xuất. Nhờ vậy, tôi có thể giữ cho mọi thứ tiếp tục hoạt động trong khi dần thay đổi cấu trúc chương trình.

Bước tiếp theo hiển nhiên là chuyển chức năng xử lý đối số số nguyên vào `ArgumentMarshaler`. Lần này cũng không có gì bất ngờ.

```java
private Map<Character, ArgumentMarshaler> intArgs =
     new HashMap<Character, ArgumentMarshaler>();
...
private void parseIntegerSchemaElement(char elementId) {
  intArgs.put(elementId, new IntegerArgumentMarshaler());
}
...
private void setIntArg(char argChar) throws ArgsException {
  currentArgument++;
  String parameter = null;
  try {
    parameter = args[currentArgument];
    intArgs.get(argChar).setInteger(Integer.parseInt(parameter));
  } catch (ArrayIndexOutOfBoundsException e) {
    valid = false;
    errorArgumentId = argChar;
    errorCode = ErrorCode.MISSING_INTEGER;
    throw new ArgsException();
  } catch (NumberFormatException e) {
    valid = false;
    errorArgumentId = argChar;
    errorParameter = parameter;
    errorCode = ErrorCode.INVALID_INTEGER;
    throw new ArgsException();
  }
}
...
public int getInt(char arg) {
  Args.ArgumentMarshaler am = intArgs.get(arg);
  return am == null ? 0 : am.getInteger();
}
...
private class ArgumentMarshaler {
  private boolean booleanValue = false;
  private String stringValue;
  private int integerValue;

  public void setBoolean(boolean value) {
    booleanValue = value;
  }

  public boolean getBoolean() {
    return booleanValue;
  }
  public void setString(String s) {
    stringValue = s;
  }
  public String getString() {
    return stringValue == null ? "" : stringValue;
  }

  public void setInteger(int i) {
    integerValue = i;
  }

  public int getInteger() {
    return integerValue;
  }
}
```

Sau khi chuyển toàn bộ phần marshaling vào `ArgumentMarshaler`, tôi bắt đầu đẩy chức năng xuống các lớp dẫn xuất. Bước đầu tiên là chuyển hàm `setBoolean` vào `BooleanArgumentMarshaller` và bảo đảm nó được gọi đúng. Vì thế, tôi tạo một phương thức `set` trừu tượng.

```java
private abstract class ArgumentMarshaler {
  protected boolean booleanValue = false;
  private String stringValue;
  private int integerValue;

  public void setBoolean(boolean value) {
    booleanValue = value;
  }

  public boolean getBoolean() {
    return booleanValue;
  }

  public void setString(String s) {
    stringValue = s;
  }

  public String getString() {
    return stringValue == null ? "" : stringValue;
  }

  public void setInteger(int i) {
    integerValue = i;
  }
  public int getInteger() {
    return integerValue;
  }
  public abstract void set(String s);
}
```

Sau đó tôi cài đặt phương thức `set` trong `BooleanArgumentMarshaller`.

```java
private class BooleanArgumentMarshaler extends ArgumentMarshaler {
  public void set(String s) {
    booleanValue = true;
  }
}
```

Cuối cùng, tôi thay lời gọi `setBoolean` bằng lời gọi `set`.

```java
private void setBooleanArg(char argChar, boolean value) {
  booleanArgs.get(argChar).set("true");
}
```

Tất cả kiểm thử vẫn đạt. Vì thay đổi này đưa `set` xuống `BooleanArgumentMarshaler`, tôi xóa phương thức `setBoolean` khỏi lớp cơ sở `ArgumentMarshaler`.

Lưu ý rằng phương thức trừu tượng `set` nhận đối số kiểu `String`, nhưng phần cài đặt trong `BooleanArgumentMarshaller` không dùng đến nó. Tôi đưa đối số đó vào vì biết rằng `StringArgumentMarshaller` và `IntegerArgumentMarshaller` sẽ dùng.

Tiếp theo, tôi muốn chuyển phương thức `get` xuống `BooleanArgumentMarshaler`. Việc chuyển các hàm `get` luôn xấu xí, vì kiểu trả về phải là `Object`, và trong trường hợp này còn phải ép kiểu thành `Boolean`.

```java
public boolean getBoolean(char arg) {
  Args.ArgumentMarshaler am = booleanArgs.get(arg);
  return am != null && (Boolean)am.get();
}
```

Chỉ để mã biên dịch được, tôi thêm hàm `get` vào `ArgumentMarshaler`.

```java
private abstract class ArgumentMarshaler {
  ...

  public Object get() {
    return null;
  }
}
```

Mã biên dịch được, nhưng đương nhiên kiểm thử thất bại. Để kiểm thử đạt trở lại, chỉ cần khai báo `get` là trừu tượng và cài đặt nó trong `BooleanAgumentMarshaler`.

```java
private abstract class ArgumentMarshaler {
  protected boolean booleanValue = false;
  ...
  public abstract Object get();
}

private class BooleanArgumentMarshaler extends ArgumentMarshaler {
  public void set(String s) {
    booleanValue = true;
  }
  public Object get() {
    return booleanValue;
  }
}
```

Một lần nữa, kiểm thử đều đạt. Vậy cả `get` lẫn `set` đều đã được chuyển xuống `BooleanArgumentMarshaler`! Nhờ đó, tôi có thể xóa hàm `getBoolean` cũ khỏi `ArgumentMarshaler`, chuyển biến `booleanValue` kiểu `protected` xuống `BooleanArgumentMarshaler` và đặt nó thành `private`.

Tôi làm tương tự với kiểu chuỗi. Tôi chuyển cả `set` lẫn `get` xuống lớp con, xóa các hàm không dùng và chuyển các biến.

```java
private void setStringArg(char argChar) throws ArgsException {
  currentArgument++;
  try {
    stringArgs.get(argChar).set(args[currentArgument]);
  } catch (ArrayIndexOutOfBoundsException e) {
    valid = false;
    errorArgumentId = argChar;
    errorCode = ErrorCode.MISSING_STRING;
    throw new ArgsException();
  }
}
...
public String getString(char arg) {
  Args.ArgumentMarshaler am = stringArgs.get(arg);
  return am == null ? "" : (String) am.get();
}
...
private abstract class ArgumentMarshaler {
  private int integerValue;

  public void setInteger(int i) {
    integerValue = i;
  }

  public int getInteger() {
    return integerValue;
  }

  public abstract void set(String s);

  public abstract Object get();
}
private class BooleanArgumentMarshaler extends ArgumentMarshaler {
  private boolean booleanValue = false;
  public void set(String s) {
    booleanValue = true;
  }
  public Object get() {
    return booleanValue;
  }
}

private class StringArgumentMarshaler extends ArgumentMarshaler {
  private String stringValue = "";
  public void set(String s) {
    stringValue = s;
  }

  public Object get() {
    return stringValue;
  }
}
private class IntegerArgumentMarshaler extends ArgumentMarshaler {

  public void set(String s) {

  }

  public Object get() {
    return null;
  }
}
}
```

Cuối cùng, tôi lặp lại quá trình này với số nguyên. Việc đó phức tạp hơn đôi chút vì số nguyên cần được phân tích cú pháp, và thao tác phân tích có thể ném ngoại lệ. Nhưng kết quả tốt hơn, vì toàn bộ khái niệm `NumberFormatException` được giấu bên trong `IntegerArgumentMarshaler`.

```java
private boolean isIntArg(char argChar) {return intArgs.containsKey(argChar);}

private void setIntArg(char argChar) throws ArgsException {
  currentArgument++;
  String parameter = null;
  try {
    parameter = args[currentArgument];
    intArgs.get(argChar).set(parameter);
  } catch (ArrayIndexOutOfBoundsException e) {
    valid = false;
    errorArgumentId = argChar;
    errorCode = ErrorCode.MISSING_INTEGER;
    throw new ArgsException();
  } catch (ArgsException e) {
    valid = false;
    errorArgumentId = argChar;
    errorParameter = parameter;
    errorCode = ErrorCode.INVALID_INTEGER;
    throw e;
  }
}
...
private void setBooleanArg(char argChar) {
  try {
    booleanArgs.get(argChar).set("true");
  } catch (ArgsException e) {
  }
}
...
public int getInt(char arg) {
  Args.ArgumentMarshaler am = intArgs.get(arg);
  return am == null ? 0 : (Integer) am.get();
}
...
private abstract class ArgumentMarshaler {
  public abstract void set(String s) throws ArgsException;
  public abstract Object get();
}
...
private class IntegerArgumentMarshaler extends ArgumentMarshaler {
  private int intValue = 0;
  public void set(String s) throws ArgsException {
    try {
      intValue = Integer.parseInt(s);
    } catch (NumberFormatException e) {
      throw new ArgsException();
    }
  }

  public Object get() {
    return intValue;
  }
}
```

Dĩ nhiên, kiểm thử vẫn tiếp tục đạt. Tiếp theo, tôi loại bỏ ba map riêng biệt ở đầu thuật toán. Điều này khiến toàn hệ thống trở nên tổng quát hơn. Tuy nhiên, tôi không thể xóa chúng ngay vì như vậy hệ thống sẽ hỏng. Thay vào đó, tôi thêm một `Map` mới dành cho `ArgumentMarshaler`, rồi lần lượt đổi các phương thức để dùng map này thay cho ba map ban đầu.

```java
public class Args {
...
  private Map<Character, ArgumentMarshaler> booleanArgs =
    new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> stringArgs =
    new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> intArgs =
    new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> marshalers =
    new HashMap<Character, ArgumentMarshaler>();
...
  private void parseBooleanSchemaElement(char elementId) {
    ArgumentMarshaler m = new BooleanArgumentMarshaler();
    booleanArgs.put(elementId, m);
    marshalers.put(elementId, m);
  }

  private void parseIntegerSchemaElement(char elementId) {
    ArgumentMarshaler m = new IntegerArgumentMarshaler();
    intArgs.put(elementId, m);
    marshalers.put(elementId, m);
  }

  private void parseStringSchemaElement(char elementId) {
    ArgumentMarshaler m = new StringArgumentMarshaler();
    stringArgs.put(elementId, m);
    marshalers.put(elementId, m);
  }
```

Tất nhiên, mọi kiểm thử vẫn đạt. Tiếp theo, tôi đổi `isBooleanArg` từ dạng này:

```java
private boolean isBooleanArg(char argChar) {
  return booleanArgs.containsKey(argChar);
}
```

sang dạng này:

```java
private boolean isBooleanArg(char argChar) {
  ArgumentMarshaler m = marshalers.get(argChar);
  return m instanceof BooleanArgumentMarshaler;
}
```

Kiểm thử vẫn đạt. Vì vậy, tôi thực hiện thay đổi tương tự với `isIntArg` và `isStringArg`.

```java
private boolean isIntArg(char argChar) {
  ArgumentMarshaler m = marshalers.get(argChar);
  return m instanceof IntegerArgumentMarshaler;
}
private boolean isStringArg(char argChar) {
  ArgumentMarshaler m = marshalers.get(argChar);
  return m instanceof StringArgumentMarshaler;
}
```

Kiểm thử vẫn đạt. Vì vậy, tôi loại bỏ các lần gọi `marshalers.get` bị lặp như sau:

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  if (isBooleanArg(m))
    setBooleanArg(argChar);
  else if (isStringArg(m))
    setStringArg(argChar);
  else if (isIntArg(m))
    setIntArg(argChar);
  else
    return false;
  return true;
}

private boolean isIntArg(ArgumentMarshaler m) {
  return m instanceof IntegerArgumentMarshaler;
}
private boolean isStringArg(ArgumentMarshaler m) {
  return m instanceof StringArgumentMarshaler;
}
private boolean isBooleanArg(ArgumentMarshaler m) {
  return m instanceof BooleanArgumentMarshaler;
}
```

Ba hàm `isxxxArg` giờ chẳng còn lý do tồn tại. Vì vậy, tôi đưa nội dung của chúng vào ngay chỗ gọi.

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  if (m instanceof BooleanArgumentMarshaler)
    setBooleanArg(argChar);
  else if (m instanceof StringArgumentMarshaler)
    setStringArg(argChar);
  else if (m instanceof IntegerArgumentMarshaler)
    setIntArg(argChar);
  else
    return false;

  return true;
}
```

Tiếp theo, tôi bắt đầu dùng map `marshalers` trong các hàm `set`, bỏ dần việc dùng ba map kia. Tôi bắt đầu với boolean.

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  if (m instanceof BooleanArgumentMarshaler)
    setBooleanArg(m);
  else if (m instanceof StringArgumentMarshaler)
    setStringArg(argChar);
  else if (m instanceof IntegerArgumentMarshaler)
    setIntArg(argChar);
  else
    return false;

  return true;
}
...
private void setBooleanArg(ArgumentMarshaler m) {
  try {
    m.set("true"); // was: booleanArgs.get(argChar).set("true");
  } catch (ArgsException e) {
  }
}
```

Kiểm thử vẫn đạt, nên tôi làm tương tự với chuỗi và số nguyên. Nhờ vậy, tôi có thể gộp một phần mã xử lý ngoại lệ xấu xí vào hàm `setArgument`.

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  try {
    if (m instanceof BooleanArgumentMarshaler)
      setBooleanArg(m);
    else if (m instanceof StringArgumentMarshaler)
      setStringArg(m);
    else if (m instanceof IntegerArgumentMarshaler)
      setIntArg(m);
    else
      return false;
  } catch (ArgsException e) {
    valid = false;
    errorArgumentId = argChar;
    throw e;
  }
  return true;
}
private void setIntArg(ArgumentMarshaler m) throws ArgsException {
  currentArgument++;
  String parameter = null;
  try {
    parameter = args[currentArgument];
    m.set(parameter);
  } catch (ArrayIndexOutOfBoundsException e) {
    errorCode = ErrorCode.MISSING_INTEGER;
    throw new ArgsException();
  } catch (ArgsException e) {
    errorParameter = parameter;
    errorCode = ErrorCode.INVALID_INTEGER;
    throw e;
  }
}

private void setStringArg(ArgumentMarshaler m) throws ArgsException {
  currentArgument++;
  try {
    m.set(args[currentArgument]);
  } catch (ArrayIndexOutOfBoundsException e) {
    errorCode = ErrorCode.MISSING_STRING;
    throw new ArgsException();
  }
}
```

Tôi sắp có thể loại bỏ ba map cũ. Trước tiên, tôi cần đổi hàm `getBoolean` từ dạng này:

```java
public boolean getBoolean(char arg) {
  Args.ArgumentMarshaler am = booleanArgs.get(arg);
  return am != null && (Boolean) am.get();
}
```

sang dạng này:

```java
public boolean getBoolean(char arg) {
  Args.ArgumentMarshaler am = marshalers.get(arg);
  boolean b = false;
  try {
    b = am != null && (Boolean) am.get();
  } catch (ClassCastException e) {
    b = false;
  }
  return b;
}
```

Thay đổi cuối cùng này có thể khiến bạn ngạc nhiên. Vì sao đột nhiên tôi lại xử lý `ClassCastException`? Bởi vì tôi có một bộ kiểm thử đơn vị và một bộ kiểm thử chấp nhận riêng, viết bằng FitNesse. Hóa ra các kiểm thử FitNesse bảo đảm rằng nếu gọi `getBoolean` với một đối số không phải boolean thì kết quả là `false`. Bộ kiểm thử đơn vị thì không kiểm tra điều đó. Cho đến lúc này, tôi chỉ chạy kiểm thử đơn vị.²

Thay đổi này cho phép tôi bỏ thêm một chỗ dùng map boolean:

```java
private void parseBooleanSchemaElement(char elementId) {
  ArgumentMarshaler m = new BooleanArgumentMarshaler();
  booleanArgs.put(elementId, m);
  marshalers.put(elementId, m);
}
```

Giờ ta có thể xóa map boolean.

```java
public class Args {
...
  private Map<Character, ArgumentMarshaler> booleanArgs =
  new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> stringArgs =
  new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> intArgs =
  new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> marshalers =
  new HashMap<Character, ArgumentMarshaler>();
...
```

Tiếp theo, tôi chuyển các đối số kiểu chuỗi và số nguyên theo cách tương tự, đồng thời chỉnh sửa đôi chút phần boolean.

```java
private void parseBooleanSchemaElement(char elementId) {
  marshalers.put(elementId, new BooleanArgumentMarshaler());
}
```

². Để tránh gặp thêm bất ngờ kiểu này, tôi bổ sung một kiểm thử đơn vị mới gọi toàn bộ kiểm thử FitNesse.

```java
private void parseIntegerSchemaElement(char elementId) {
  marshalers.put(elementId, new IntegerArgumentMarshaler());
}

private void parseStringSchemaElement(char elementId) {
  marshalers.put(elementId, new StringArgumentMarshaler());
}
...
public String getString(char arg) {
  Args.ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? "" : (String) am.get();
  } catch (ClassCastException e) {
    return "";
  }
}

public int getInt(char arg) {
  Args.ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? 0 : (Integer) am.get();
  } catch (Exception e) {
    return 0;
  }
}
...
public class Args {
...
  private Map<Character, ArgumentMarshaler> stringArgs =
  new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> intArgs =
  new HashMap<Character, ArgumentMarshaler>();
  private Map<Character, ArgumentMarshaler> marshalers =
  new HashMap<Character, ArgumentMarshaler>();
...
```

Tiếp theo, tôi gộp ba hàm phân tích vào một, vì giờ chúng chẳng còn làm được bao nhiêu:

```java
private void parseSchemaElement(String element) throws ParseException {
  char elementId = element.charAt(0);
  String elementTail = element.substring(1);
  validateSchemaElementId(elementId);
  if (isBooleanSchemaElement(elementTail))
    marshalers.put(elementId, new BooleanArgumentMarshaler());
  else if (isStringSchemaElement(elementTail))
    marshalers.put(elementId, new StringArgumentMarshaler());
  else if (isIntegerSchemaElement(elementTail)) {
    marshalers.put(elementId, new IntegerArgumentMarshaler());
  } else {
    throw new ParseException(String.format(
    "Argument: %c has invalid format: %s.", elementId, elementTail), 0);
  }
}
```

Được rồi, giờ hãy nhìn lại toàn bộ cấu trúc. Đoạn mã 14-12 trình bày hình thức hiện tại của lớp `Args`.

**Đoạn mã 14-12**
**Args.java (Sau lần tái cấu trúc đầu tiên)**

```java
package com.objectmentor.utilities.getopts;

import java.text.ParseException;
import java.util.*;

public class Args {
  private String schema;
  private String[] args;
  private boolean valid = true;
  private Set<Character> unexpectedArguments = new TreeSet<Character>();
  private Map<Character, ArgumentMarshaler> marshalers =
  new HashMap<Character, ArgumentMarshaler>();
  private Set<Character> argsFound = new HashSet<Character>();
  private int currentArgument;
  private char errorArgumentId = '\0';
  private String errorParameter = "TILT";
  private ErrorCode errorCode = ErrorCode.OK;
  private enum ErrorCode {
    OK, MISSING_STRING, MISSING_INTEGER, INVALID_INTEGER, UNEXPECTED_ARGUMENT}

  public Args(String schema, String[] args) throws ParseException {
    this.schema = schema;
    this.args = args;
    valid = parse();
  }

  private boolean parse() throws ParseException {
    if (schema.length() == 0 && args.length == 0)
      return true;
    parseSchema();
    try {
      parseArguments();
    } catch (ArgsException e) {
    }
    return valid;
  }

  private boolean parseSchema() throws ParseException {
    for (String element : schema.split(",")) {
      if (element.length() > 0) {
        String trimmedElement = element.trim();
        parseSchemaElement(trimmedElement);
      }
    }
    return true;
  }

  private void parseSchemaElement(String element) throws ParseException {
    char elementId = element.charAt(0);
    String elementTail = element.substring(1);
    validateSchemaElementId(elementId);
    if (isBooleanSchemaElement(elementTail))
      marshalers.put(elementId, new BooleanArgumentMarshaler());
    else if (isStringSchemaElement(elementTail))
      marshalers.put(elementId, new StringArgumentMarshaler());
    else if (isIntegerSchemaElement(elementTail)) {
      marshalers.put(elementId, new IntegerArgumentMarshaler());
    } else {
      throw new ParseException(String.format(
      "Argument: %c has invalid format: %s.", elementId, elementTail), 0);
    }
  }

  private void validateSchemaElementId(char elementId) throws ParseException {
    if (!Character.isLetter(elementId)) {
      throw new ParseException(
      "Bad character:" + elementId + "in Args format: " + schema, 0);
    }
  }
  private boolean isStringSchemaElement(String elementTail) {
    return elementTail.equals("*");
  }

  private boolean isBooleanSchemaElement(String elementTail) {
    return elementTail.length() == 0;
  }

  private boolean isIntegerSchemaElement(String elementTail) {
    return elementTail.equals("#");
  }

  private boolean parseArguments() throws ArgsException {
    for (currentArgument=0; currentArgument<args.length; currentArgument++) {
      String arg = args[currentArgument];
      parseArgument(arg);
    }
    return true;
  }

  private void parseArgument(String arg) throws ArgsException {
    if (arg.startsWith("-"))
      parseElements(arg);
  }

  private void parseElements(String arg) throws ArgsException {
    for (int i = 1; i < arg.length(); i++)
      parseElement(arg.charAt(i));
  }

  private void parseElement(char argChar) throws ArgsException {
    if (setArgument(argChar))
      argsFound.add(argChar);
    else {
      unexpectedArguments.add(argChar);
      errorCode = ErrorCode.UNEXPECTED_ARGUMENT;
      valid = false;
    }
  }
```

**Đoạn mã 14-12 (tiếp)**
**Args.java (Sau lần tái cấu trúc đầu tiên)**

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  try {
    if (m instanceof BooleanArgumentMarshaler)
      setBooleanArg(m);
    else if (m instanceof StringArgumentMarshaler)
      setStringArg(m);
    else if (m instanceof IntegerArgumentMarshaler)
      setIntArg(m);
    else
      return false;
  } catch (ArgsException e) {
    valid = false;
    errorArgumentId = argChar;
    throw e;
  }
  return true;
}

private void setIntArg(ArgumentMarshaler m) throws ArgsException {
  currentArgument++;
  String parameter = null;
  try {
    parameter = args[currentArgument];
    m.set(parameter);
  } catch (ArrayIndexOutOfBoundsException e) {
    errorCode = ErrorCode.MISSING_INTEGER;
    throw new ArgsException();
  } catch (ArgsException e) {
    errorParameter = parameter;
    errorCode = ErrorCode.INVALID_INTEGER;
    throw e;
  }
}

private void setStringArg(ArgumentMarshaler m) throws ArgsException {
  currentArgument++;
  try {
    m.set(args[currentArgument]);
  } catch (ArrayIndexOutOfBoundsException e) {
    errorCode = ErrorCode.MISSING_STRING;
    throw new ArgsException();
  }
}

private void setBooleanArg(ArgumentMarshaler m) {
  try {
    m.set("true");
  } catch (ArgsException e) {
  }
}

public int cardinality() {
  return argsFound.size();
}
```

**Đoạn mã 14-12 (tiếp)**
**Args.java (Sau lần tái cấu trúc đầu tiên)**

```java
public String usage() {
  if (schema.length() > 0)
    return "-[" + schema + "]";
  else
    return "";
}

public String errorMessage() throws Exception {
  switch (errorCode) {
    case OK:
      throw new Exception("TILT: Should not get here.");
    case UNEXPECTED_ARGUMENT:
      return unexpectedArgumentMessage();
    case MISSING_STRING:
      return String.format("Could not find string parameter for -%c.",
                           errorArgumentId);
    case INVALID_INTEGER:
      return String.format("Argument -%c expects an integer but was '%s'.",
                           errorArgumentId, errorParameter);
    case MISSING_INTEGER:
      return String.format("Could not find integer parameter for -%c.",
                           errorArgumentId);
  }
  return "";
}

private String unexpectedArgumentMessage() {
  StringBuffer message = new StringBuffer("Argument(s) -");
  for (char c : unexpectedArguments) {
    message.append(c);
  }
  message.append(" unexpected.");

  return message.toString();
}
public boolean getBoolean(char arg) {
  Args.ArgumentMarshaler am = marshalers.get(arg);
  boolean b = false;
  try {
    b = am != null && (Boolean) am.get();
  } catch (ClassCastException e) {
    b = false;
  }
  return b;
}

public String getString(char arg) {
  Args.ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? "" : (String) am.get();
  } catch (ClassCastException e) {
    return "";
  }
}
```

**Đoạn mã 14-12 (tiếp)**
**Args.java (Sau lần tái cấu trúc đầu tiên)**

```java
public int getInt(char arg) {
  Args.ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? 0 : (Integer) am.get();
  } catch (Exception e) {
    return 0;
  }
}

public boolean has(char arg) {
  return argsFound.contains(arg);
}

public boolean isValid() {
  return valid;
}

private class ArgsException extends Exception {
}

private abstract class ArgumentMarshaler {
  public abstract void set(String s) throws ArgsException;
  public abstract Object get();
}
private class BooleanArgumentMarshaler extends ArgumentMarshaler {
  private boolean booleanValue = false;

  public void set(String s) {
    booleanValue = true;
  }

  public Object get() {
    return booleanValue;
  }
}
private class StringArgumentMarshaler extends ArgumentMarshaler {
  private String stringValue = "";

  public void set(String s) {
    stringValue = s;
  }

  public Object get() {
    return stringValue;
  }
}

private class IntegerArgumentMarshaler extends ArgumentMarshaler {
  private int intValue = 0;

  public void set(String s) throws ArgsException {
    try {
      intValue = Integer.parseInt(s);
    } catch (NumberFormatException e) {
      throw new ArgsException();
    }
  }

  public Object get() {
    return intValue;
  }
}
}
```

Sau tất cả công việc ấy, kết quả hơi đáng thất vọng. Cấu trúc có khá hơn đôi chút, nhưng tất cả biến vẫn nằm ở đầu lớp; trong `setArgument` vẫn còn một nhánh rẽ kiểu dữ liệu thật kinh khủng; các hàm `set` đều rất xấu. Chưa kể đến toàn bộ phần xử lý lỗi. Chúng ta còn nhiều việc phải làm.

Tôi rất muốn loại bỏ nhánh rẽ kiểu dữ liệu trong `setArgument` [G23]. Điều tôi muốn ở `setArgument` là một lời gọi duy nhất đến `ArgumentMarshaler.set`. Như vậy, tôi cần chuyển `setIntArg`, `setStringArg` và `setBooleanArg` xuống các lớp dẫn xuất `ArgumentMarshaler` tương ứng. Nhưng có một vấn đề.

Nếu xem kỹ `setIntArg`, bạn sẽ thấy nó dùng hai biến thực thể: `args` và `currentArg`. Muốn chuyển `setIntArg` xuống `BooleanArgumentMarshaler`, tôi phải truyền cả `args` lẫn `currentArgs` làm đối số cho hàm. Làm vậy không ổn [F1]. Tôi muốn chỉ truyền một đối số thay vì hai. May thay, có một giải pháp đơn giản. Ta có thể chuyển mảng `args` thành danh sách rồi truyền một `Iterator` xuống các hàm `set`. Tôi đã thực hiện việc này qua mười bước, sau mỗi bước đều chạy được tất cả kiểm thử. Nhưng tôi sẽ chỉ trình bày kết quả. Có lẽ bạn sẽ hình dung được phần lớn các bước nhỏ đó.

```java
public class Args {
  private String schema;
  private String[] args;
  private boolean valid = true;
  private Set<Character> unexpectedArguments = new TreeSet<Character>();
  private Map<Character, ArgumentMarshaler> marshalers =
  new HashMap<Character, ArgumentMarshaler>();
  private Set<Character> argsFound = new HashSet<Character>();
  private Iterator<String> currentArgument;
  private char errorArgumentId = '\0';
  private String errorParameter = "TILT";
  private ErrorCode errorCode = ErrorCode.OK;
  private List<String> argsList;

  private enum ErrorCode {
    OK, MISSING_STRING, MISSING_INTEGER, INVALID_INTEGER, UNEXPECTED_ARGUMENT}

  public Args(String schema, String[] args) throws ParseException {
    this.schema = schema;
    argsList = Arrays.asList(args);
    valid = parse();
  }

  private boolean parse() throws ParseException {
    if (schema.length() == 0 && argsList.size() == 0)
      return true;
    parseSchema();
    try {
      parseArguments();
    } catch (ArgsException e) {
    }
    return valid;
  }
  ---
  private boolean parseArguments() throws ArgsException {
    for (currentArgument = argsList.iterator(); currentArgument.hasNext();) {
      String arg = currentArgument.next();
      parseArgument(arg);
    }

    return true;
  }
  ---
  private void setIntArg(ArgumentMarshaler m) throws ArgsException {
    String parameter = null;
    try {
      parameter = currentArgument.next();
      m.set(parameter);
    } catch (NoSuchElementException e) {
      errorCode = ErrorCode.MISSING_INTEGER;
      throw new ArgsException();
    } catch (ArgsException e) {
      errorParameter = parameter;
      errorCode = ErrorCode.INVALID_INTEGER;
      throw e;
    }
  }

  private void setStringArg(ArgumentMarshaler m) throws ArgsException {
    try {
      m.set(currentArgument.next());
    } catch (NoSuchElementException e) {
      errorCode = ErrorCode.MISSING_STRING;
      throw new ArgsException();
    }
  }
```

Đây là những thay đổi đơn giản, sau mỗi thay đổi tất cả kiểm thử vẫn chạy đạt. Giờ ta có thể bắt đầu chuyển các hàm `set` xuống các lớp dẫn xuất tương ứng. Trước tiên, tôi cần thay đổi `setArgument` như sau:

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  if (m == null)
    return false;
  try {
    if (m instanceof BooleanArgumentMarshaler)
      setBooleanArg(m);
    else if (m instanceof StringArgumentMarshaler)
      setStringArg(m);
    else if (m instanceof IntegerArgumentMarshaler)
      setIntArg(m);
    else
      return false;
  } catch (ArgsException e) {
    valid = false;
    errorArgumentId = argChar;
    throw e;
  }
  return true;
}
```

Thay đổi này quan trọng vì ta muốn loại bỏ hoàn toàn chuỗi `if-else`. Do đó, trước hết cần đưa điều kiện báo lỗi ra khỏi chuỗi đó.

Giờ ta có thể bắt đầu chuyển các hàm `set`. Hàm `setBooleanArg` rất đơn giản, nên ta chuẩn bị nó trước. Mục tiêu là đổi hàm `setBooleanArg` để nó chỉ chuyển tiếp lời gọi đến `BooleanArgumentMarshaler`.

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  if (m == null)
    return false;
  try {
    if (m instanceof BooleanArgumentMarshaler)
      setBooleanArg(m, currentArgument);
    else if (m instanceof StringArgumentMarshaler)
      setStringArg(m);
    else if (m instanceof IntegerArgumentMarshaler)
      setIntArg(m);
  } catch (ArgsException e) {
    valid = false;
    errorArgumentId = argChar;
    throw e;
  }
  return true;
}
---
private void setBooleanArg(ArgumentMarshaler m,
                           Iterator<String> currentArgument)
                           throws ArgsException {
  try {
    m.set("true");
  } catch (ArgsException e) {
  }
}
```

Chẳng phải ta vừa mới đưa phần xử lý ngoại lệ vào đó sao? Trong quá trình tái cấu trúc, việc đưa một thứ vào để rồi lại lấy nó ra là chuyện thường gặp. Các bước nhỏ và yêu cầu giữ cho kiểm thử luôn chạy khiến ta phải di chuyển mọi thứ nhiều lần. Tái cấu trúc cũng giống như giải khối Rubik. Cần rất nhiều bước nhỏ để đạt mục tiêu lớn. Mỗi bước mở đường cho bước tiếp theo.

Vì sao ta truyền iterator vào khi `setBooleanArg` chắc chắn không cần đến nó? Vì `setIntArg` và `setStringArg` sẽ cần! Và vì tôi muốn chuyển cả ba hàm này thông qua một phương thức trừu tượng trong `ArgumentMarshaller`, nên phải truyền iterator cho `setBooleanArg`.

`setBooleanArg` trở nên thừa. Nếu trong `ArgumentMarshaler` có phương thức `set`, ta có thể gọi trực tiếp. Vậy đã đến lúc tạo phương thức đó. Bước đầu tiên là thêm phương thức trừu tượng mới vào `ArgumentMarshaler`.

```java
private abstract class ArgumentMarshaler {
  public abstract void set(Iterator<String> currentArgument)
                       throws ArgsException;
  public abstract void set(String s) throws ArgsException;
  public abstract Object get();
}
```

Dĩ nhiên, việc này làm hỏng tất cả lớp dẫn xuất. Vậy hãy cài đặt phương thức mới trong từng lớp.

```java
private class BooleanArgumentMarshaler extends ArgumentMarshaler {
  private boolean booleanValue = false;

  public void set(Iterator<String> currentArgument) throws ArgsException {
    booleanValue = true;
  }

  public void set(String s) {
    booleanValue = true;
  }

  public Object get() {
    return booleanValue;
  }
}

private class StringArgumentMarshaler extends ArgumentMarshaler {
  private String stringValue = "";

  public void set(Iterator<String> currentArgument) throws ArgsException {
  }

  public void set(String s) {
    stringValue = s;
  }

  public Object get() {
    return stringValue;
  }
}

private class IntegerArgumentMarshaler extends ArgumentMarshaler {
  private int intValue = 0;

  public void set(Iterator<String> currentArgument) throws ArgsException {
  }
  public void set(String s) throws ArgsException {
    try {
      intValue = Integer.parseInt(s);
    } catch (NumberFormatException e) {
      throw new ArgsException();
    }
  }

  public Object get() {
    return intValue;
  }
}
```

Giờ ta có thể xóa `setBooleanArg`!

```java
private boolean setArgument(char argChar) throws ArgsException {
    ArgumentMarshaler m = marshalers.get(argChar);
    if (m == null)
      return false;
    try {
      if (m instanceof BooleanArgumentMarshaler)
        m.set(currentArgument);
      else if (m instanceof StringArgumentMarshaler)
        setStringArg(m);
      else if (m instanceof IntegerArgumentMarshaler)
        setIntArg(m);
      } catch (ArgsException e) {
        valid = false;
        errorArgumentId = argChar;
        throw e;
      }
      return true;
}
```

Tất cả kiểm thử đều qua, và phương thức `set` đã được chuyển xuống `BooleanArgumentMarshaler`!

Giờ ta làm tương tự với chuỗi và số nguyên.

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  if (m == null)
    return false;
  try {
    if (m instanceof BooleanArgumentMarshaler)
      m.set(currentArgument);
    else if (m instanceof StringArgumentMarshaler)
      m.set(currentArgument);
    else if (m instanceof IntegerArgumentMarshaler)
      m.set(currentArgument);
  } catch (ArgsException e) {
    valid = false;
    errorArgumentId = argChar;
    throw e;
  }
  return true;
}
---
private class StringArgumentMarshaler extends ArgumentMarshaler {
  private String stringValue = "";

  public void set(Iterator<String> currentArgument) throws ArgsException {
    try {
      stringValue = currentArgument.next();
    } catch (NoSuchElementException e) {
      errorCode = ErrorCode.MISSING_STRING;
      throw new ArgsException();
    }
  }

  public void set(String s) {
  }

  public Object get() {
    return stringValue;
  }
}

private class IntegerArgumentMarshaler extends ArgumentMarshaler {
  private int intValue = 0;
public void set(Iterator<String> currentArgument) throws ArgsException {
  String parameter = null;
  try {
    parameter = currentArgument.next();
    set(parameter);
  } catch (NoSuchElementException e) {
    errorCode = ErrorCode.MISSING_INTEGER;
    throw new ArgsException();
  } catch (ArgsException e) {
    errorParameter = parameter;
    errorCode = ErrorCode.INVALID_INTEGER;
    throw e;
  }
}
  public void set(String s) throws ArgsException {
    try {
      intValue = Integer.parseInt(s);
    } catch (NumberFormatException e) {
      throw new ArgsException();
    }
  }

  public Object get() {
    return intValue;
  }
}
```

Và thế là có thể tung đòn kết liễu: bỏ hẳn đoạn rẽ nhánh theo kiểu dữ liệu! Chạm đích!

```java
private boolean setArgument(char argChar) throws ArgsException {
  ArgumentMarshaler m = marshalers.get(argChar);
  if (m == null)
    return false;
  try {
    m.set(currentArgument);
    return true;
  } catch (ArgsException e) {
    valid = false;
    errorArgumentId = argChar;
    throw e;
  }
}
```

Giờ ta có thể bỏ một số hàm cũ kỹ trong `IntegerArgumentMarshaler` và dọn nó gọn hơn.

```java
private class IntegerArgumentMarshaler extends ArgumentMarshaler {
  private int intValue = 0

  public void set(Iterator<String> currentArgument) throws ArgsException {
    String parameter = null;
    try {
      parameter = currentArgument.next();
      intValue = Integer.parseInt(parameter);
    } catch (NoSuchElementException e) {
      errorCode = ErrorCode.MISSING_INTEGER;
      throw new ArgsException();
    } catch (NumberFormatException e) {
      errorParameter = parameter;
      errorCode = ErrorCode.INVALID_INTEGER;
      throw new ArgsException();
    }
  }
  public Object get() {
    return intValue;
  }
}
```

Ta cũng có thể đổi `ArgumentMarshaler` thành một interface.

```java
private interface ArgumentMarshaler {
  void set(Iterator<String> currentArgument) throws ArgsException;
  Object get();
}
```

Giờ hãy xem việc thêm kiểu đối số mới vào cấu trúc này dễ đến đâu. Ta chỉ cần rất ít thay đổi, và các thay đổi đó nên được cô lập. Trước tiên, ta thêm một ca kiểm thử để xác nhận đối số kiểu double hoạt động đúng.

```java
public void testSimpleDoublePresent() throws Exception {
  Args args = new Args("x##", new String[] {"-x","42.3"});
  assertTrue(args.isValid());
  assertEquals(1, args.cardinality());
  assertTrue(args.has('x'));
  assertEquals(42.3, args.getDouble('x'), .001);
}
```

Tiếp theo, ta dọn mã phân tích schema và thêm phần nhận diện `##` cho kiểu đối số double.

```java
private void parseSchemaElement(String element) throws ParseException {
  char elementId = element.charAt(0);
  String elementTail = element.substring(1);
  validateSchemaElementId(elementId);
  if (elementTail.length() == 0)
    marshalers.put(elementId, new BooleanArgumentMarshaler());
  else if (elementTail.equals("*"))
    marshalers.put(elementId, new StringArgumentMarshaler());
  else if (elementTail.equals("#"))
    marshalers.put(elementId, new IntegerArgumentMarshaler());
    else if (elementTail.equals("##"))
      marshalers.put(elementId, new DoubleArgumentMarshaler());
    else
      throw new ParseException(String.format(
         "Argument: %c has invalid format: %s.", elementId, elementTail), 0);
}
```

Tiếp theo, ta viết lớp `DoubleArgumentMarshaler`.

```java
private class DoubleArgumentMarshaler implements ArgumentMarshaler {
  private double doubleValue = 0;

  public void set(Iterator<String> currentArgument) throws ArgsException {
    String parameter = null;
    try {
      parameter = currentArgument.next();
      doubleValue = Double.parseDouble(parameter);
    } catch (NoSuchElementException e) {
      errorCode = ErrorCode.MISSING_DOUBLE;
      throw new ArgsException();
    } catch (NumberFormatException e) {
      errorParameter = parameter;
      errorCode = ErrorCode.INVALID_DOUBLE;
      throw new ArgsException();
    }
  }

  public Object get() {
    return doubleValue;
  }
}
```

Việc này buộc ta phải thêm một `ErrorCode` mới.

```java
private enum ErrorCode {
    OK, MISSING_STRING, MISSING_INTEGER, INVALID_INTEGER, UNEXPECTED_ARGUMENT,
    MISSING_DOUBLE, INVALID_DOUBLE}
```

Và cần thêm hàm `getDouble`.

```java
public double getDouble(char arg) {
  Args.ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? 0 : (Double) am.get();
  } catch (Exception e) {
    return 0.0;
  }
}
```

Tất cả kiểm thử đều qua! Việc này khá nhẹ nhàng. Giờ hãy kiểm tra xem phần xử lý lỗi có hoạt động đúng không. Ca kiểm thử tiếp theo xác nhận rằng lỗi được báo khi truyền một chuỗi không thể phân tích vào đối số `##`.

```java
public void testInvalidDouble() throws Exception {
  Args args = new Args("x##", new String[] {"-x","Forty two"});
  assertFalse(args.isValid());
  assertEquals(0, args.cardinality());
  assertFalse(args.has('x'));
  assertEquals(0, args.getInt('x'));
  assertEquals("Argument -x expects a double but was 'Forty two'.",
               args.errorMessage());
}
---
public String errorMessage() throws Exception {
   switch (errorCode) {
     case OK:
       throw new Exception("TILT: Should not get here.");
     case UNEXPECTED_ARGUMENT:
       return unexpectedArgumentMessage();
     case MISSING_STRING:
       return String.format("Could not find string parameter for -%c.",
                               errorArgumentId);
     case INVALID_INTEGER:
       return String.format("Argument -%c expects an integer but was '%s'.",
                               errorArgumentId, errorParameter);
     case MISSING_INTEGER:
       return String.format("Could not find integer parameter for -%c.",
                               errorArgumentId);
     case INVALID_DOUBLE:
       return String.format("Argument -%c expects a double but was '%s'.",
                               errorArgumentId, errorParameter);
     case MISSING_DOUBLE:
       return String.format("Could not find double parameter for -%c.",
                               errorArgumentId);
   }
   return "";
}
```

Ca này qua đúng như dự kiến. Ta viết nó chỉ để đầy đủ.

Mã xử lý ngoại lệ khá xấu và không thực sự thuộc về lớp `Args`. Ta cũng đang ném `ParseException`, vốn chẳng thuộc về ta. Vậy hãy gộp tất cả ngoại lệ vào một lớp `ArgsException` rồi chuyển lớp đó sang module riêng.

```java
public class ArgsException extends Exception {
  private char errorArgumentId = '\0';
  private String errorParameter = "TILT";
  private ErrorCode errorCode = ErrorCode.OK;
  public ArgsException() {}

  public ArgsException(String message) {super(message);}

  public enum ErrorCode {
    OK, MISSING_STRING, MISSING_INTEGER, INVALID_INTEGER, UNEXPECTED_ARGUMENT,
    MISSING_DOUBLE, INVALID_DOUBLE}
}
---
public class Args {
  ...
  private char errorArgumentId = '\0';
  private String errorParameter = "TILT";
  private ArgsException.ErrorCode errorCode = ArgsException.ErrorCode.OK;
  private List<String> argsList;

  public Args(String schema, String[] args) throws ArgsException {
    this.schema = schema;
    argsList = Arrays.asList(args);
    valid = parse();
  }

  private boolean parse() throws ArgsException {
    if (schema.length() == 0 && argsList.size() == 0)
      return true;
    parseSchema();
    try {
      parseArguments();
    } catch (ArgsException e) {
    }
    return valid;
  }

  private boolean parseSchema() throws ArgsException {
    ...
  }

  private void parseSchemaElement(String element) throws ArgsException {
    ...
    else
      throw new ArgsException(
         String.format("Argument: %c has invalid format: %s.",
                       elementId,elementTail));
  }
  private void validateSchemaElementId(char elementId) throws ArgsException {
    if (!Character.isLetter(elementId)) {
      throw new ArgsException(
        "Bad character:" + elementId + "in Args format: " + schema);
    }
  }
  ...

  private void parseElement(char argChar) throws ArgsException {
    if (setArgument(argChar))
      argsFound.add(argChar);
    else {
      unexpectedArguments.add(argChar);
      errorCode = ArgsException.ErrorCode.UNEXPECTED_ARGUMENT;
      valid = false;
    }
  }
  ...
```

```java
private class StringArgumentMarshaler implements ArgumentMarshaler {
  private String stringValue = "";

  public void set(Iterator<String> currentArgument) throws ArgsException {
    try {
      stringValue = currentArgument.next();
    } catch (NoSuchElementException e) {
      errorCode = ArgsException.ErrorCode.MISSING_STRING;
      throw new ArgsException();
    }
  }

  public Object get() {
    return stringValue;
  }
}

private class IntegerArgumentMarshaler implements ArgumentMarshaler {
  private int intValue = 0;

  public void set(Iterator<String> currentArgument) throws ArgsException {
    String parameter = null;
    try {
      parameter = currentArgument.next();
      intValue = Integer.parseInt(parameter);
    } catch (NoSuchElementException e) {
      errorCode = ArgsException.ErrorCode.MISSING_INTEGER;
      throw new ArgsException();
    } catch (NumberFormatException e) {
      errorParameter = parameter;
      errorCode = ArgsException.ErrorCode.INVALID_INTEGER;
      throw new ArgsException();
    }
  }

  public Object get() {
    return intValue;
  }
}

private class DoubleArgumentMarshaler implements ArgumentMarshaler {
  private double doubleValue = 0;
  public void set(Iterator<String> currentArgument) throws ArgsException {
    String parameter = null;
    try {
      parameter = currentArgument.next();
      doubleValue = Double.parseDouble(parameter);
    } catch (NoSuchElementException e) {
      errorCode = ArgsException.ErrorCode.MISSING_DOUBLE;
      throw new ArgsException();
    } catch (NumberFormatException e) {
      errorParameter = parameter;
      errorCode = ArgsException.ErrorCode.INVALID_DOUBLE;
      throw new ArgsException();
    }
  }

  public Object get() {
    return doubleValue;
  }
}
```

Thế là tốt. Ngoại lệ duy nhất `Args` ném ra giờ là `ArgsException`. Chuyển `ArgsException` sang module riêng cũng giúp ta chuyển nhiều mã hỗ trợ xử lý lỗi ra khỏi module `Args` và đưa vào module đó. Đây là nơi tự nhiên, hợp lý để đặt chúng, nhờ vậy việc dọn module `Args` sau này sẽ dễ hơn nhiều.

Như vậy, ngoại lệ và mã lỗi đã được tách hoàn toàn khỏi module `Args`. (Xem Đoạn mã 14-13 đến Đoạn mã 14-16.) Việc này được thực hiện qua khoảng 30 bước nhỏ, giữ cho các kiểm thử qua sau từng bước.

**Đoạn mã 14-13**
**ArgsTest.java**

```java
package com.objectmentor.utilities.args;

import junit.framework.TestCase;
public class ArgsTest extends TestCase {
  public void testCreateWithNoSchemaOrArguments() throws Exception {
    Args args = new Args("", new String[0]);
    assertEquals(0, args.cardinality());
  }

    public void testWithNoSchemaButWithOneArgument() throws Exception {
      try {
        new Args("", new String[]{"-x"});
        fail();
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.UNEXPECTED_ARGUMENT,
                     e.getErrorCode());
        assertEquals('x', e.getErrorArgumentId());
      }
    }
    public void testWithNoSchemaButWithMultipleArguments() throws Exception {
      try {
        new Args("", new String[]{"-x", "-y"});
        fail();
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.UNEXPECTED_ARGUMENT,
                     e.getErrorCode());
        assertEquals('x', e.getErrorArgumentId());
      }

    }
    public void testNonLetterSchema() throws Exception {
      try {
        new Args("*", new String[]{});
        fail("Args constructor should have thrown exception");
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.INVALID_ARGUMENT_NAME,
                     e.getErrorCode());
        assertEquals('*', e.getErrorArgumentId());
      }
    }
    public void testInvalidArgumentFormat() throws Exception {
      try {
        new Args("f~", new String[]{});
        fail("Args constructor should have throws exception");
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.INVALID_FORMAT, e.getErrorCode());
        assertEquals('f', e.getErrorArgumentId());
      }
    }

    public void testSimpleBooleanPresent() throws Exception {
      Args args = new Args("x", new String[]{"-x"});
      assertEquals(1, args.cardinality());
      assertEquals(true, args.getBoolean('x'));
    }
    public void testSimpleStringPresent() throws Exception {
      Args args = new Args("x*", new String[]{"-x", "param"});
      assertEquals(1, args.cardinality());
      assertTrue(args.has('x'));
      assertEquals("param", args.getString('x'));
    }
    public void testMissingStringArgument() throws Exception {
      try {
        new Args("x*", new String[]{"-x"});
        fail();
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.MISSING_STRING, e.getErrorCode());
        assertEquals('x', e.getErrorArgumentId());
      }
    }

    public void testSpacesInFormat() throws Exception {
      Args args = new Args("x, y", new String[]{"-xy"});
      assertEquals(2, args.cardinality());
      assertTrue(args.has('x'));
      assertTrue(args.has('y'));
    }
    public void testSimpleIntPresent() throws Exception {
      Args args = new Args("x#", new String[]{"-x", "42"});
      assertEquals(1, args.cardinality());
      assertTrue(args.has('x'));
      assertEquals(42, args.getInt('x'));
    }

    public void testInvalidInteger() throws Exception {
      try {
        new Args("x#", new String[]{"-x", "Forty two"});
```

**Đoạn mã 14-13 (tiếp)**
**ArgsTest.java**

```java
          fail();
        } catch (ArgsException e) {
          assertEquals(ArgsException.ErrorCode.INVALID_INTEGER, e.getErrorCode());
          assertEquals('x', e.getErrorArgumentId());
          assertEquals("Forty two", e.getErrorParameter());
        }

    }

    public void testMissingInteger() throws Exception {
      try {
        new Args("x#", new String[]{"-x"});
        fail();
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.MISSING_INTEGER, e.getErrorCode());
        assertEquals('x', e.getErrorArgumentId());
      }
    }

    public void testSimpleDoublePresent() throws Exception {
      Args args = new Args("x##", new String[]{"-x", "42.3"});
      assertEquals(1, args.cardinality());
      assertTrue(args.has('x'));
      assertEquals(42.3, args.getDouble('x'), .001);
    }

    public void testInvalidDouble() throws Exception {
      try {
        new Args("x##", new String[]{"-x", "Forty two"});
        fail();
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.INVALID_DOUBLE, e.getErrorCode());
        assertEquals('x', e.getErrorArgumentId());
        assertEquals("Forty two", e.getErrorParameter());
      }
    }
    public void testMissingDouble() throws Exception {
      try {
        new Args("x##", new String[]{"-x"});
        fail();
      } catch (ArgsException e) {
        assertEquals(ArgsException.ErrorCode.MISSING_DOUBLE, e.getErrorCode());
        assertEquals('x', e.getErrorArgumentId());
      }
    }
}
```

**Đoạn mã 14-14**
**ArgsExceptionTest.java**

```java
public class ArgsExceptionTest extends TestCase {
  public void testUnexpectedMessage() throws Exception {
    ArgsException e =
```

**Đoạn mã 14-14 (tiếp)**
**ArgsExceptionTest.java**

```java
      new ArgsException(ArgsException.ErrorCode.UNEXPECTED_ARGUMENT,
                        'x', null);
    assertEquals("Argument -x unexpected.", e.errorMessage());
  }

  public void testMissingStringMessage() throws Exception {
    ArgsException e = new ArgsException(ArgsException.ErrorCode.MISSING_STRING,
                                        'x', null);
    assertEquals("Could not find string parameter for -x.", e.errorMessage());
  }
  public void testInvalidIntegerMessage() throws Exception {
    ArgsException e =
      new ArgsException(ArgsException.ErrorCode.INVALID_INTEGER,
                        'x', "Forty two");
    assertEquals("Argument -x expects an integer but was 'Forty two'.",
                 e.errorMessage());
  }

  public void testMissingIntegerMessage() throws Exception {
    ArgsException e =
      new ArgsException(ArgsException.ErrorCode.MISSING_INTEGER, 'x', null);
    assertEquals("Could not find integer parameter for -x.", e.errorMessage());
  }
  public void testInvalidDoubleMessage() throws Exception {
    ArgsException e = new ArgsException(ArgsException.ErrorCode.INVALID_DOUBLE,
                                        'x', "Forty two");
    assertEquals("Argument -x expects a double but was 'Forty two'.",
                 e.errorMessage());
  }

  public void testMissingDoubleMessage() throws Exception {
    ArgsException e = new ArgsException(ArgsException.ErrorCode.MISSING_DOUBLE,
                                        'x', null);
    assertEquals("Could not find double parameter for -x.", e.errorMessage());
  }
}
```

**Đoạn mã 14-15**
**ArgsException.java**

```java
public class ArgsException extends Exception {
  private char errorArgumentId = '\0';
  private String errorParameter = "TILT";
  private ErrorCode errorCode = ErrorCode.OK;
  public ArgsException() {}

  public ArgsException(String message) {super(message);}

  public ArgsException(ErrorCode errorCode) {
    this.errorCode = errorCode;
  }
```

**Đoạn mã 14-15 (tiếp)**
**ArgsException.java**

```java
  public ArgsException(ErrorCode errorCode, String errorParameter) {
    this.errorCode = errorCode;
    this.errorParameter = errorParameter;
  }

  public ArgsException(ErrorCode errorCode, char errorArgumentId,
                       String errorParameter) {
    this.errorCode = errorCode;
    this.errorParameter = errorParameter;
    this.errorArgumentId = errorArgumentId;
  }

  public char getErrorArgumentId() {
    return errorArgumentId;
  }

  public void setErrorArgumentId(char errorArgumentId) {
    this.errorArgumentId = errorArgumentId;
  }

  public String getErrorParameter() {
    return errorParameter;
  }

  public void setErrorParameter(String errorParameter) {
    this.errorParameter = errorParameter;
  }

  public ErrorCode getErrorCode() {
    return errorCode;
  }

  public void setErrorCode(ErrorCode errorCode) {
    this.errorCode = errorCode;
  }
  public String errorMessage() throws Exception {
    switch (errorCode) {
      case OK:
        throw new Exception("TILT: Should not get here.");
      case UNEXPECTED_ARGUMENT:
        return String.format("Argument -%c unexpected.", errorArgumentId);
      case MISSING_STRING:
        return String.format("Could not find string parameter for -%c.",
                             errorArgumentId);
      case INVALID_INTEGER:
        return String.format("Argument -%c expects an integer but was '%s'.",
                             errorArgumentId, errorParameter);
      case MISSING_INTEGER:
        return String.format("Could not find integer parameter for -%c.",
                             errorArgumentId);
      case INVALID_DOUBLE:
        return String.format("Argument -%c expects a double but was '%s'.",
                             errorArgumentId, errorParameter);
      case MISSING_DOUBLE:
        return String.format("Could not find double parameter for -%c.",
                             errorArgumentId);
    }
    return "";
  }

  public enum ErrorCode {
    OK, INVALID_FORMAT, UNEXPECTED_ARGUMENT, INVALID_ARGUMENT_NAME,
    MISSING_STRING,
    MISSING_INTEGER, INVALID_INTEGER,
    MISSING_DOUBLE, INVALID_DOUBLE}
}
```

**Đoạn mã 14-16**
**Args.java**

```java
public class Args {
  private String schema;
  private Map<Character, ArgumentMarshaler> marshalers =
    new HashMap<Character, ArgumentMarshaler>();
  private Set<Character> argsFound = new HashSet<Character>();
  private Iterator<String> currentArgument;
  private List<String> argsList;

  public Args(String schema, String[] args) throws ArgsException {
    this.schema = schema;
    argsList = Arrays.asList(args);
    parse();
  }

  private void parse() throws ArgsException {
    parseSchema();
    parseArguments();
  }
  private boolean parseSchema() throws ArgsException {
    for (String element : schema.split(",")) {
      if (element.length() > 0) {
        parseSchemaElement(element.trim());
      }
    }
    return true;
  }

  private void parseSchemaElement(String element) throws ArgsException {
    char elementId = element.charAt(0);
    String elementTail = element.substring(1);
    validateSchemaElementId(elementId);
    if (elementTail.length() == 0)
      marshalers.put(elementId, new BooleanArgumentMarshaler());
    else if (elementTail.equals("*"))
      marshalers.put(elementId, new StringArgumentMarshaler());
    else if (elementTail.equals("#"))
      marshalers.put(elementId, new IntegerArgumentMarshaler());
    else if (elementTail.equals("##"))
      marshalers.put(elementId, new DoubleArgumentMarshaler());
    else
      throw new ArgsException(ArgsException.ErrorCode.INVALID_FORMAT,
                              elementId, elementTail);
  }

  private void validateSchemaElementId(char elementId) throws ArgsException {
    if (!Character.isLetter(elementId)) {
      throw new ArgsException(ArgsException.ErrorCode.INVALID_ARGUMENT_NAME,
                              elementId, null);
    }
  }

  private void parseArguments() throws ArgsException {
    for (currentArgument = argsList.iterator(); currentArgument.hasNext();) {
      String arg = currentArgument.next();
      parseArgument(arg);
    }
  }

  private void parseArgument(String arg) throws ArgsException {
    if (arg.startsWith("-"))
      parseElements(arg);
  }

  private void parseElements(String arg) throws ArgsException {
    for (int i = 1; i < arg.length(); i++)
      parseElement(arg.charAt(i));
  }

  private void parseElement(char argChar) throws ArgsException {
    if (setArgument(argChar))
      argsFound.add(argChar);
    else {
      throw new ArgsException(ArgsException.ErrorCode.UNEXPECTED_ARGUMENT,
                              argChar, null);
    }
  }
  private boolean setArgument(char argChar) throws ArgsException {
    ArgumentMarshaler m = marshalers.get(argChar);
    if (m == null)
      return false;
    try {
      m.set(currentArgument);
      return true;
    } catch (ArgsException e) {
      e.setErrorArgumentId(argChar);
      throw e;
    }
  }
```

```java
public int cardinality() {
  return argsFound.size();
}

public String usage() {
  if (schema.length() > 0)
    return "-[" + schema + "]";
  else
    return "";
}
public boolean getBoolean(char arg) {
  ArgumentMarshaler am = marshalers.get(arg);
  boolean b = false;
  try {
    b = am != null && (Boolean) am.get();
  } catch (ClassCastException e) {
    b = false;
  }
  return b;
}
public String getString(char arg) {
  ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? "" : (String) am.get();
  } catch (ClassCastException e) {
    return "";
  }
}

public int getInt(char arg) {
  ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? 0 : (Integer) am.get();
  } catch (Exception e) {
    return 0;
  }
}

public double getDouble(char arg) {
  ArgumentMarshaler am = marshalers.get(arg);
  try {
    return am == null ? 0 : (Double) am.get();
  } catch (Exception e) {
    return 0.0;
  }
}
public boolean has(char arg) {
  return argsFound.contains(arg);
}
```

Phần lớn thay đổi trong lớp `Args` là xóa mã. Nhiều đoạn mã chỉ được chuyển từ `Args` sang `ArgsException`. Tốt. Chúng tôi cũng chuyển toàn bộ `ArgumentMarshaler` sang các tệp riêng. Còn tốt hơn.

Phần lớn thiết kế phần mềm tốt chỉ là phân chia hợp lý, tạo chỗ thích hợp cho từng loại mã. Tách biệt các mối quan tâm giúp mã dễ hiểu và dễ bảo trì hơn.

Điều đáng chú ý là phương thức `errorMessage` của `ArgsException`. Rõ ràng, đưa phần định dạng thông báo lỗi vào `Args` là vi phạm SRP. `Args` nên tập trung xử lý đối số, không phải định dạng thông báo lỗi. Nhưng liệu đưa phần định dạng thông báo lỗi vào `ArgsException` có thật sự hợp lý?

Thành thật mà nói, đây là một sự thỏa hiệp. Người dùng không thích các thông báo lỗi do `ArgsException` cung cấp sẽ phải tự viết thông báo riêng. Nhưng việc có sẵn các thông báo lỗi tiện dùng cũng có giá trị đáng kể.

Đến đây hẳn đã rõ rằng ta chỉ còn cách giải pháp cuối cùng ở đầu chương một khoảng ngắn. Tôi để phần biến đổi cuối cùng lại làm bài tập cho bạn.

## Kết luận

Mã chạy được thôi thì chưa đủ. Mã chạy được thường vẫn hỏng nặng. Lập trình viên chỉ hài lòng với việc mã chạy được đang hành xử thiếu chuyên nghiệp. Họ có thể lo rằng mình không đủ thời gian cải thiện cấu trúc và thiết kế mã, nhưng tôi không đồng ý. Không gì gây tác động xấu lâu dài đến một dự án phát triển bằng mã tồi. Tiến độ tồi có thể sửa lại, yêu cầu tồi có thể xác định lại, động lực nhóm tồi có thể khôi phục. Nhưng mã tồi sẽ mục ruỗng và lên men, trở thành gánh nặng không thể tránh khỏi kéo cả nhóm xuống. Tôi đã nhiều lần chứng kiến các nhóm gần như đình trệ vì trong lúc vội vã, họ tạo ra một mớ mã độc hại rồi mãi mãi bị nó chi phối.

Dĩ nhiên, có thể dọn mã tồi, nhưng cái giá rất đắt. Khi mã mục ruỗng, các module len lỏi vào nhau, tạo ra vô số phụ thuộc ngầm và rối rắm. Tìm rồi phá vỡ những phụ thuộc cũ là việc dài hơi, gian nan. Trong khi đó, giữ mã sạch lại khá dễ. Nếu sáng bạn làm một module rối tung, chiều vẫn có thể dọn nó. Tốt hơn nữa, nếu bạn vừa làm nó rối cách đây năm phút, hãy dọn ngay bây giờ, việc đó rất dễ.

Vậy nên, hãy liên tục giữ cho mã sạch và đơn giản hết mức có thể. Đừng bao giờ để nó bắt đầu mục ruỗng.
