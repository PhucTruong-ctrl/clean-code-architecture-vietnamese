# Chương 4: Chú thích

> “Đừng chú thích mã xấu, hãy viết lại nó.”
>
> Brian W. Kernighan và P. J. Plaugher[^1]

Không gì hữu ích bằng một chú thích đặt đúng chỗ. Không gì làm rối một module bằng những chú thích tầm phào và giáo điều. Không gì tai hại bằng một chú thích cũ kỹ, nát bấy, đang lan truyền dối trá và thông tin sai lạc.

Chú thích không giống *Schindler's List*. Chúng không phải là “điều thiện thuần khiết”. Thật vậy, trong trường hợp tốt nhất, chú thích chỉ là một thứ xấu nhưng cần thiết. Nếu ngôn ngữ lập trình của chúng ta đủ biểu cảm, hoặc nếu chúng ta đủ tài để vận dụng tinh tế những ngôn ngữ ấy mà diễn đạt ý định của mình, thì chúng ta sẽ không cần chú thích nhiều, có lẽ chẳng cần chút nào.

Cách dùng đúng đắn của chú thích là bù đắp cho thất bại của chúng ta trong việc diễn đạt bản thân bằng mã. Bạn để ý tôi đã dùng từ thất bại. Tôi nói thật đấy. Chú thích luôn là những thất bại. Chúng ta phải có chúng vì không phải lúc nào cũng tìm ra cách diễn đạt bản thân mà không cần đến chúng, nhưng dùng chúng không phải là chuyện đáng ăn mừng.

Vậy nên khi rơi vào tình huống cần viết một chú thích, hãy nghĩ cho kỹ và xem có cách nào xoay ngược tình thế mà diễn đạt ý mình bằng mã không. Mỗi lần diễn đạt bản thân bằng mã, bạn nên tự khen mình. Mỗi lần viết chú thích, bạn nên nhăn mặt và cảm thấy thất bại trong khả năng diễn đạt.

Vì sao tôi lại chê chú thích đến thế? Vì chúng nói dối. Không phải lúc nào cũng vậy, và không phải cố ý, nhưng quá thường xuyên. Chú thích càng cũ, càng xa đoạn mã nó mô tả, thì càng dễ sai hẳn. Lý do đơn giản. Lập trình viên không thể duy trì chúng một cách thực tế.

Mã thay đổi và tiến hóa. Từng khối mã chuyển từ chỗ này sang chỗ khác. Những khối ấy phân nhánh, sinh sôi rồi lại hợp nhất thành những con quái vật lai. Đáng tiếc là chú thích không phải lúc nào cũng đi theo chúng, không thể lúc nào cũng đi theo. Và rất thường xuyên, chú thích bị tách khỏi đoạn mã nó mô tả, trở thành những mẩu ghi chú mồ côi ngày càng kém chính xác. Chẳng hạn, hãy xem chuyện gì đã xảy ra với chú thích này và dòng mã mà nó định mô tả:

```java
MockRequest request;
private final String HTTP_DATE_REGEXP =
  "[SMTWF][a-z]{2}\\,\\s[0-9]{2}\\s[JFMASOND][a-z]{2}\\s"+
  "[0-9]{4}\\s[0-9]{2}\\:[0-9]{2}\\:[0-9]{2}\\sGMT";
private Response response;
private FitNesseContext context;
private FileResponder responder;
private Locale saveLocale;
// Ví dụ: "Tue, 02 Apr 2003 22:18:49 GMT"
```

Những biến thực thể khác, có lẽ được thêm vào sau, đã chen vào giữa hằng HTTP_DATE_REGEXP và chú thích giải thích nó.

Có thể lập luận rằng lập trình viên nên đủ kỷ luật để giữ chú thích ở trạng thái được sửa chữa tốt, vẫn liên quan và chính xác. Tôi đồng ý, họ nên như vậy. Nhưng tôi thà rằng năng lượng ấy được dồn vào việc làm cho mã rõ ràng và biểu cảm đến mức không cần đến chú thích ngay từ đầu.

Chú thích không chính xác còn tệ hơn hẳn không có chú thích. Chúng đánh lừa và dẫn sai. Chúng đặt ra những kỳ vọng sẽ không bao giờ được đáp ứng. Chúng đặt ra những quy tắc cũ không cần, hoặc không nên, tuân theo nữa.

Sự thật chỉ có thể tìm thấy ở một nơi: mã. Chỉ mã mới thật sự cho bạn biết nó làm gì. Đó là nguồn thông tin chính xác duy nhất. Vì vậy, dù chú thích đôi khi là cần thiết, chúng ta sẽ dồn năng lượng đáng kể để giảm thiểu chúng.

## Chú thích không bù đắp được cho mã tồi

Một trong những động cơ phổ biến để viết chú thích là mã tồi. Chúng ta viết một module và biết nó khó hiểu, lộn xộn. Chúng ta biết nó là một mớ hỗn độn. Thế là tự nhủ: “Ồ, tốt hơn mình nên chú thích chỗ đó!” Không! Tốt hơn bạn nên dọn nó đi!

Mã rõ ràng, biểu cảm với ít chú thích vượt xa mã rối rắm, phức tạp với nhiều chú thích. Thay vì dành thời gian viết những chú thích giải thích mớ hỗn độn mình vừa tạo ra, hãy dành thời gian dọn mớ hỗn độn ấy.

## Tự diễn đạt bằng mã

Chắc chắn có những lúc mã là phương tiện giải thích kém cỏi. Đáng tiếc, nhiều lập trình viên lại suy ra rằng mã hiếm khi, nếu có, là phương tiện giải thích tốt. Điều này hoàn toàn sai. Bạn thích thấy cái nào hơn? Cái này:

```java
// Kiểm tra xem nhân viên có đủ điều kiện hưởng phúc lợi đầy đủ không
if ((employee.flags & HOURLY_FLAG) &&
    (employee.age > 65))
```

Hay cái này?

```java
if (employee.isEligibleForFullBenefits())
```

Chỉ cần vài giây suy nghĩ là có thể giải thích phần lớn ý định của mình bằng mã. Trong nhiều trường hợp, đó đơn giản là chuyện tạo ra một hàm nói đúng điều bạn muốn viết trong chú thích.

## Chú thích tốt

Một số chú thích là cần thiết hoặc có ích. Chúng ta sẽ xem vài chú thích mà tôi cho là xứng đáng với số bit chúng chiếm. Tuy vậy, hãy nhớ rằng chú thích thật sự tốt duy nhất là chú thích bạn tìm được cách để không phải viết.

### Chú thích pháp lý

Đôi khi chuẩn lập trình của công ty buộc chúng ta phải viết một số chú thích vì lý do pháp lý. Chẳng hạn, các tuyên bố về bản quyền và tác quyền là thứ cần thiết và hợp lý để đặt trong chú thích ở đầu mỗi tệp nguồn.

Đây là ví dụ về phần đầu chú thích chuẩn mà chúng tôi đặt ở đầu mọi tệp nguồn trong FitNesse. Tôi vui mừng nói rằng IDE của chúng tôi tự động thu gọn chú thích này để nó không làm rối mắt.

```java
// Bản quyền (C) 2003,2004,2005 thuộc Object Mentor, Inc. Bảo lưu mọi quyền.
// Phát hành theo các điều khoản của Giấy phép Công cộng GNU phiên bản 2 hoặc mới hơn.
```

Những chú thích như thế không nên là hợp đồng hay những cuốn sách luật đồ sộ. Khi có thể, hãy tham chiếu đến một giấy phép chuẩn hoặc tài liệu bên ngoài thay vì đưa toàn bộ điều khoản và điều kiện vào chú thích.

### Chú thích cung cấp thông tin

Đôi khi việc cung cấp thông tin cơ bản bằng một chú thích là hữu ích. Chẳng hạn, hãy xét chú thích giải thích giá trị trả về của một phương thức trừu tượng:

```java
// Trả về một thực thể Responder đang được kiểm thử.
protected abstract Responder responderInstance();
```

Một chú thích như thế đôi khi có ích, nhưng tốt hơn là dùng tên hàm để truyền đạt thông tin khi có thể. Chẳng hạn, trong trường hợp này, có thể làm chú thích thành dư thừa bằng cách đổi tên hàm: responderBeingTested.

Đây là một trường hợp khá hơn:

```java
// định dạng khớp kk:mm:ss EEE, MMM dd, yyyy
Pattern timeMatcher = Pattern.compile(
  "\\d*:\\d*:\\d* \\w*, \\w* \\d*, \\d*");
```

Trong trường hợp này, chú thích cho ta biết biểu thức chính quy định khớp một thời gian và ngày tháng được định dạng bằng hàm SimpleDateFormat.format với chuỗi định dạng đã chỉ định. Dù vậy, sẽ tốt hơn và rõ hơn nếu đoạn mã này được chuyển vào một lớp chuyên biệt chuyển đổi định dạng ngày và giờ. Khi đó chú thích có lẽ sẽ thừa.

### Giải thích ý định

Đôi khi một chú thích vượt ra ngoài thông tin hữu ích về cách hiện thực và cho biết ý định đằng sau một quyết định. Trong trường hợp sau, ta thấy một quyết định thú vị được ghi lại bằng chú thích. Khi so sánh hai đối tượng, tác giả quyết định rằng anh ta muốn xếp các đối tượng thuộc lớp của mình cao hơn đối tượng thuộc bất kỳ lớp nào khác.

```java
public int compareTo(Object o)
{
  if(o instanceof WikiPagePath)
  {
     WikiPagePath p = (WikiPagePath) o;
     String compressedName = StringUtil.join(names, "");
     String compressedArgumentName = StringUtil.join(p.names, "");
     return compressedName.compareTo(compressedArgumentName);
  }
  return 1; // chúng ta lớn hơn vì chúng ta đúng kiểu.
}
```

Đây là một ví dụ còn tốt hơn. Có thể bạn không đồng ý với cách lập trình viên giải quyết vấn đề, nhưng ít nhất bạn biết anh ta đang cố làm gì.

```java
public void testConcurrentAddWidgets() throws Exception {
  WidgetBuilder widgetBuilder =
     new WidgetBuilder(new Class[]{BoldWidget.class});
  String text = "'''bold text'''";
  ParentWidget parent =
     new BoldWidget(new MockWidgetRoot(), "'''bold text'''");
  AtomicBoolean failFlag = new AtomicBoolean();
  failFlag.set(false);
  //Đây là nỗ lực tốt nhất của chúng ta để tạo ra một điều kiện tranh chấp
  //bằng cách tạo ra số lượng lớn luồng.
  for (int i = 0; i < 25000; i++) {
     WidgetBuilderThread widgetBuilderThread =
        new WidgetBuilderThread(widgetBuilder, text, parent, failFlag);
     Thread thread = new Thread(widgetBuilderThread);
     thread.start();
  }
  assertEquals(false, failFlag.get());
}
```

### Làm rõ

Đôi khi chỉ cần dịch nghĩa của một đối số hoặc giá trị trả về khó hiểu thành thứ dễ đọc. Nói chung, tốt hơn là tìm cách làm cho đối số hay giá trị trả về ấy tự nó rõ ràng; nhưng khi nó thuộc thư viện chuẩn, hoặc nằm trong mã bạn không thể sửa, thì một chú thích làm rõ hữu ích có thể có giá trị.

```java
public void testCompareTo() throws Exception
{
  WikiPagePath a = PathParser.parse("PageA");
  WikiPagePath ab = PathParser.parse("PageA.PageB");
  WikiPagePath b = PathParser.parse("PageB");
  WikiPagePath aa = PathParser.parse("PageA.PageA");
  WikiPagePath bb = PathParser.parse("PageB.PageB");
  WikiPagePath ba = PathParser.parse("PageB.PageA");
    assertTrue(a.compareTo(a) == 0);    // a == a
    assertTrue(a.compareTo(b) != 0);    // a != b
    assertTrue(ab.compareTo(ab) == 0); // ab == ab
    assertTrue(a.compareTo(b) == -1); // a < b
    assertTrue(aa.compareTo(ab) == -1); // aa < ab
    assertTrue(ba.compareTo(bb) == -1); // ba < bb
    assertTrue(b.compareTo(a) == 1);    // b > a
    assertTrue(ab.compareTo(aa) == 1); // ab > aa
    assertTrue(bb.compareTo(ba) == 1); // bb > ba
}
```

Tất nhiên, có một rủi ro đáng kể là chú thích làm rõ lại sai. Hãy xem lại ví dụ trước và thấy việc kiểm chứng chúng đúng là khó đến mức nào. Điều này giải thích cả vì sao cần làm rõ lẫn vì sao nó rủi ro. Vậy nên trước khi viết những chú thích như thế, hãy cẩn thận xem có cách nào tốt hơn không, rồi cẩn thận hơn nữa để chúng chính xác.

### Cảnh báo hậu quả

![Cảnh báo hậu quả](assets/illustrations/04-warning-of-consequences.png){w=169}

Đôi khi hữu ích khi cảnh báo các lập trình viên khác về những hậu quả nhất định. Chẳng hạn, đây là chú thích giải thích vì sao một ca kiểm thử cụ thể bị tắt:

```java
// Đừng chạy trừ khi bạn
// có thời gian rảnh rỗi.
public void _testWithReallyBigFile()
{
  writeLinesToFile(10000000);

    response.setBody(testFile);
    response.readyToSend(this);
    String responseString = output.toString();
    assertSubString("Content-Length: 1000000000", responseString);
    assertTrue(bytesSent > 1000000000);
}
```

Tất nhiên, ngày nay chúng ta sẽ tắt ca kiểm thử bằng annotation @Ignore kèm một chuỗi giải thích thích hợp, chẳng hạn `@Ignore("Takes too long to run")`. Nhưng quay lại thời trước JUnit 4, đặt dấu gạch dưới trước tên phương thức là một quy ước phổ biến. Chú thích này, dù cợt nhả, truyền đạt ý khá tốt.

Đây là một ví dụ khác, sâu sắc hơn:

```java
public static SimpleDateFormat makeStandardHttpDateFormat()
{
  //SimpleDateFormat không an toàn với luồng,
  //nên chúng ta cần tạo từng thực thể một cách độc lập.
  SimpleDateFormat df = new SimpleDateFormat("EEE, dd MMM yyyy HH:mm:ss z");
  df.setTimeZone(TimeZone.getTimeZone("GMT"));
  return df;
}
```

Có thể bạn phàn nàn rằng có những cách tốt hơn để giải quyết vấn đề này. Tôi có thể đồng ý với bạn. Nhưng chú thích như đưa ra ở đây là hoàn toàn hợp lý. Nó sẽ ngăn một lập trình viên quá hăng hái dùng khởi tạo tĩnh nhân danh hiệu quả.

### Chú thích TODO

Đôi khi để lại ghi chú “Việc cần làm” dưới dạng chú thích `//TODO` là hợp lý. Trong trường hợp sau, chú thích TODO giải thích vì sao hàm có một cách hiện thực thoái hóa và tương lai của hàm ấy nên ra sao.

```java
//TODO-MdM những thứ này không cần thiết
// Chúng tôi kỳ vọng thứ này sẽ biến mất khi chúng tôi làm mô hình checkout
protected VersionInfo makeVersion() throws Exception
{
  return null;
}
```

TODO là những việc mà lập trình viên nghĩ nên làm, nhưng vì lý do nào đó chưa thể làm ngay. Nó có thể là lời nhắc xóa một tính năng đã bị đánh dấu lỗi thời, hoặc lời cầu xin ai đó xem giúp một vấn đề. Nó có thể là yêu cầu ai đó nghĩ ra cái tên hay hơn, hoặc lời nhắc thực hiện một thay đổi phụ thuộc vào một sự kiện đã lên kế hoạch. Dù TODO có thể là gì đi nữa, nó không phải cái cớ để mã tồi nằm lại trong hệ thống.

Ngày nay, hầu hết IDE tốt cung cấp thao tác và tính năng đặc biệt để tìm mọi chú thích TODO, nên chúng khó có thể bị thất lạc. Dù vậy, bạn không muốn mã của mình bị rải rác đầy TODO. Vì thế hãy quét qua chúng thường xuyên và loại bỏ những cái có thể loại bỏ.

### Khuếch đại

Một chú thích có thể được dùng để khuếch đại tầm quan trọng của một thứ mà nếu không thì có vẻ chẳng đáng kể.

```java
String listItemContent = match.group(3).trim();
// việc trim thật sự quan trọng. Nó loại bỏ những dấu
// cách ở đầu có thể khiến mục này bị nhận nhầm
// là một danh sách khác.
new ListItemWidget(this, listItemContent, this.level + 1);
return buildList(text.substring(match.end()));
```

### Javadoc trong API công khai

Không gì hữu ích và thỏa mãn bằng một API công khai được mô tả tốt. Javadoc cho thư viện Java chuẩn là một ví dụ điển hình. Khó có thể viết chương trình Java mà không có chúng.

Nếu bạn đang viết một API công khai thì chắc chắn bạn nên viết javadoc tử tế cho nó. Nhưng hãy nhớ phần còn lại của lời khuyên trong chương này. Javadoc có thể gây hiểu nhầm, phi cục bộ và thiếu trung thực y như bất kỳ loại chú thích nào khác.

## Chú thích xấu

Hầu hết chú thích đều rơi vào loại này. Thường chúng là nạng hoặc cái cớ cho mã tồi, hay lời biện hộ cho những quyết định thiếu thỏa đáng, chẳng khác gì lập trình viên tự nói chuyện với chính mình.

### Nói lảm nhảm

Đặt đại một chú thích chỉ vì bạn thấy nên làm thế hoặc vì quy trình đòi hỏi là một mánh tạm bợ. Nếu đã quyết định viết chú thích, hãy dành đủ thời gian để chắc rằng đó là chú thích tốt nhất bạn có thể viết.

Đây là ví dụ về một trường hợp tôi tìm thấy trong FitNesse, nơi một chú thích đáng lẽ có thể thật sự hữu ích. Nhưng tác giả đang vội hoặc chỉ không để ý lắm. Sự lảm nhảm của anh ta để lại một điều bí ẩn:

```java
public void loadProperties()
{
  try
  {
    String propertiesPath = propertiesLocation + "/" + PROPERTIES_FILE;
    FileInputStream propertiesStream = new FileInputStream(propertiesPath);
    loadedProperties.load(propertiesStream);
  }
  catch(IOException e)
  {
     // Không có tệp properties nghĩa là mọi giá trị mặc định đã được nạp
  }
}
```

Chú thích trong khối catch ấy nghĩa là gì? Rõ ràng nó có ý nghĩa với tác giả, nhưng ý nghĩa không truyền đạt được rõ lắm. Có vẻ như nếu ta gặp IOException thì nghĩa là không có tệp properties; và trong trường hợp đó mọi giá trị mặc định đã được nạp. Nhưng ai nạp mọi giá trị mặc định? Chúng được nạp trước lời gọi loadProperties.load ư? Hay loadProperties.load bắt ngoại lệ, nạp các giá trị mặc định, rồi chuyển ngoại lệ cho chúng ta bỏ qua? Hay loadProperties.load nạp mọi giá trị mặc định trước khi thử nạp tệp? Tác giả đang cố tự an ủi về việc mình để khối catch trống ư? Hay, và đây mới là khả năng đáng sợ, tác giả đang tự nhủ phải quay lại đây sau và viết đoạn mã nạp các giá trị mặc định?

Cách duy nhất của chúng ta là xem mã ở những phần khác của hệ thống để tìm ra chuyện gì đang diễn ra. Bất kỳ chú thích nào buộc bạn phải tìm sang module khác để hiểu nghĩa của chính nó là đã thất bại trong việc truyền đạt, và không đáng với số bit nó chiếm.

### Chú thích dư thừa

Đoạn mã 4-1 cho thấy một hàm đơn giản với chú thích đầu hàm hoàn toàn dư thừa. Đọc chú thích có lẽ còn lâu hơn đọc chính đoạn mã.

**Đoạn mã 4-1**
**waitForClose**

```java
// Phương thức tiện ích trả về khi this.closed là true. Ném ngoại lệ
// nếu hết thời gian chờ.
public synchronized void waitForClose(final long timeoutMillis)
throws Exception
{
   if(!closed)
   {
     wait(timeoutMillis);
     if(!closed)
        throw new Exception("MockResponseSender could not be closed");
   }
}
```

Chú thích này phục vụ mục đích gì? Chắc chắn nó không cung cấp nhiều thông tin hơn đoạn mã. Nó không biện minh cho đoạn mã, cũng không cho biết ý định hay lý do. Nó không dễ đọc hơn đoạn mã. Thật vậy, nó kém chính xác hơn đoạn mã và dụ người đọc chấp nhận sự thiếu chính xác ấy thay cho hiểu biết thật sự. Nó giống như một anh bán xe cũ khéo mồm trấn an bạn rằng bạn không cần nhìn dưới nắp ca-pô.

Giờ hãy xét cả một loạt javadoc vô dụng và dư thừa trong Đoạn mã 4-2, lấy từ Tomcat. Những chú thích này chỉ làm rối và che khuất đoạn mã. Chúng không phục vụ mục đích ghi chép tài liệu nào cả. Tệ hơn nữa, tôi chỉ cho bạn thấy vài cái đầu tiên. Còn nhiều cái nữa trong module này.

**Đoạn mã 4-2**
**ContainerBase.java (Tomcat)**

```java
public abstract class ContainerBase
  implements Container, Lifecycle, Pipeline,
  MBeanRegistration, Serializable {
   /**
    * Độ trễ xử lý của thành phần này.
    */
   protected int backgroundProcessorDelay = -1;

   /**
    * Hỗ trợ sự kiện vòng đời của thành phần này.
    */
   protected LifecycleSupport lifecycle =
     new LifecycleSupport(this);

   /**
    * Các listener sự kiện container của Container này.
    */
   protected ArrayList listeners = new ArrayList();

   /**
    * Cách hiện thực Loader gắn với
    * Container này.
    */
   protected Loader loader = null;

   /**
    * Cách hiện thực Logger gắn với
    * Container này.
    */
   protected Log logger = null;

   /**
    * Tên logger liên quan.
    */
   protected String logName = null;
```

**Đoạn mã 4-2 (tiếp theo)**
**ContainerBase.java (Tomcat)**

```java
  /**
   * Cách hiện thực Manager gắn với
   * Container này.
   */
  protected Manager manager = null;

  /**
   * Cluster gắn với Container này.
   */
  protected Cluster cluster = null;

  /**
   * Tên dễ đọc của Container này.
   */
  protected String name = null;

  /**
   * Container cha mà Container này là con.
   */
  protected Container parent = null;

  /**
   * Class loader cha được cấu hình khi chúng ta cài một
   * Loader.
   */
  protected ClassLoader parentClassLoader = null;

  /**
   * Đối tượng Pipeline gắn với
   * Container này.
   */
  protected Pipeline pipeline = new StandardPipeline(this);

  /**
   * Realm gắn với Container này.
   */
  protected Realm realm = null;


  /**
   * Đối tượng DirContext chứa tài nguyên gắn với
   * Container này.
   */
  protected DirContext resources = null;
```

### Chú thích gây hiểu nhầm

Đôi khi, với tất cả thiện ý, một lập trình viên viết trong chú thích của mình một câu không đủ chính xác để đúng. Hãy nghĩ thêm một chút về chú thích vừa dư thừa vừa tinh vi gây hiểu nhầm mà ta đã thấy ở Đoạn mã 4-1.

Bạn có phát hiện ra chú thích ấy gây hiểu nhầm ở đâu không? Phương thức không trả về khi this.closed trở thành true. Nó trả về nếu this.closed đang là true; nếu không, nó chờ một khoảng thời gian mù và sau đó ném ngoại lệ nếu this.closed vẫn chưa true.

Mẩu thông tin sai lạc tinh vi này, được bọc trong một chú thích khó đọc hơn cả thân đoạn mã, có thể khiến một lập trình viên khác vô tư gọi hàm này với kỳ vọng nó sẽ trả về ngay khi this.closed trở thành true. Anh lập trình viên tội nghiệp ấy rồi sẽ thấy mình trong một phiên gỡ lỗi, cố tìm ra vì sao mã của mình chạy chậm đến thế.

### Chú thích bị bắt buộc

Thật nực cười khi có một quy tắc nói rằng mọi hàm phải có javadoc, hoặc mọi biến phải có chú thích. Những chú thích như thế chỉ làm rối mã, lan truyền dối trá và góp phần gây nhầm lẫn, mất trật tự nói chung.

Chẳng hạn, javadoc bắt buộc cho mọi hàm dẫn đến những thứ quái dị như Đoạn mã 4-3. Mớ rối rắm này chẳng thêm gì và chỉ làm mờ đoạn mã, tạo ra khả năng cho dối trá và dẫn sai.

**Đoạn mã 4-3**

```java
  /**
    *
    * @param title Tiêu đề của CD
    * @param author Tác giả của CD
    * @param tracks Số bài hát trên CD
    * @param durationInMinutes Thời lượng của CD tính bằng phút
    */
  public void addCD(String title, String author,
                       int tracks, int durationInMinutes) {
      CD cd = new CD();
      cd.title = title;
      cd.author = author;
      cd.tracks = tracks;
      cd.duration = duration;
      cdList.add(cd);
  }
```

### Chú thích nhật ký

Đôi khi người ta thêm một chú thích vào đầu module mỗi lần sửa nó. Những chú thích này tích tụ thành một loại nhật ký, hay sổ ghi, ghi lại mọi thay đổi từng được thực hiện. Tôi đã từng thấy những module với hàng chục trang ghi chép nhật ký nối dài như thế.

```java
  * Thay đổi (từ 11-Oct-2001)
  * --------------------------
  * 11-Oct-2001 : Tổ chức lại lớp và chuyển nó sang package mới
  *               com.jrefinery.date (DG);
  * 05-Nov-2001 : Thêm phương thức getDescription(), và loại bỏ lớp NotableDate
  *               (DG);
  * 12-Nov-2001 : IBD yêu cầu phương thức setDescription(), vì lớp NotableDate
  *               đã bị bỏ (DG); Sửa getPreviousDayOfWeek(),
  *               getFollowingDayOfWeek() và getNearestDayOfWeek() để khắc phục
  *               lỗi (DG);
  * 05-Dec-2001 : Sửa lỗi trong lớp SpreadsheetDate (DG);
  * 29-May-2002 : Chuyển các hằng tháng vào một giao diện riêng
  *               (MonthConstants) (DG);
  * 27-Aug-2002 : Sửa lỗi trong phương thức addMonths(), cảm ơn N???levka Petr (DG);
  * 03-Oct-2002 : Sửa các lỗi do Checkstyle báo (DG);
  * 13-Mar-2003 : Hiện thực Serializable (DG);
  * 29-May-2003 : Sửa lỗi trong phương thức addMonths (DG);
  * 04-Sep-2003 : Hiện thực Comparable. Cập nhật javadoc của isInRange (DG);
  * 05-Jan-2005 : Sửa lỗi trong phương thức addYears() (1096282) (DG);
```

Xưa kia có lý do chính đáng để tạo và duy trì những ghi chép nhật ký này ở đầu mỗi module. Chúng ta chưa có hệ thống quản lý mã nguồn làm việc đó thay mình. Ngày nay, những cuốn nhật ký dài này chỉ là thêm một mớ rối rắm làm mờ module. Chúng nên được xóa hoàn toàn.

### Chú thích ồn ào

Đôi khi bạn thấy những chú thích chẳng là gì ngoài tiếng ồn. Chúng nhắc lại điều hiển nhiên và không cung cấp thông tin mới.

```java
/**
 * Hàm khởi tạo mặc định.
 */
protected AnnualDateRule() {
}
```

Không, thật sao? Hay thế này:

```java
/** Ngày trong tháng. */
    private int dayOfMonth;
```

Và đây là tấm gương mẫu mực của sự dư thừa:

```java
/**
 * Trả về ngày trong tháng.
 *
 * @return ngày trong tháng.
 */
public int getDayOfMonth() {
  return dayOfMonth;
}
```

Những chú thích này ồn ào đến mức chúng ta học cách phớt lờ chúng. Khi đọc mã, mắt ta chỉ lướt qua chúng. Cuối cùng chú thích bắt đầu nói dối khi đoạn mã xung quanh thay đổi.

Chú thích đầu tiên trong Đoạn mã 4-4 có vẻ hợp lý.[^2] Nó giải thích vì sao khối catch bị bỏ qua. Nhưng chú thích thứ hai là tiếng ồn thuần túy. Có vẻ lập trình viên đã quá bực mình vì phải viết các khối try/catch trong hàm này đến mức cần xả bực.

**Đoạn mã 4-4**
**startSending**

```java
   private void startSending()
   {
     try
     {
        doSending();
     }
     catch(SocketException e)
     {
        // bình thường. ai đó đã dừng yêu cầu.
     }
     catch(Exception e)
     {
        try
        {
          response.add(ErrorResponder.makeExceptionString(e));
          response.closeAll();
        }
        catch(Exception e1)
        {
          //Cho tôi xin!
        }
     }
   }
```

Thay vì xả bực trong một chú thích vô giá trị và ồn ào, lập trình viên nên nhận ra rằng có thể giải tỏa sự bực bội của mình bằng cách cải thiện cấu trúc mã. Anh ta nên dồn năng lượng vào việc tách khối try/catch cuối cùng thành một hàm riêng, như trong Đoạn mã 4-5.

**Đoạn mã 4-5**
**startSending (đã tái cấu trúc)**

```java
   private void startSending()
   {
     try
     {
        doSending();
     }
```

**Đoạn mã 4-5 (tiếp theo)**
**startSending (đã tái cấu trúc)**

```java
     catch(SocketException e)
     {
       // bình thường. ai đó đã dừng yêu cầu.
     }
     catch(Exception e)
     {
       addExceptionAndCloseResponse(e);
     }
 }
 private void addExceptionAndCloseResponse(Exception e)
 {
   try
   {
      response.add(ErrorResponder.makeExceptionString(e));
      response.closeAll();
   }
   catch(Exception e1)
   {
   }
 }
```

Hãy thay cám dỗ tạo tiếng ồn bằng quyết tâm làm sạch mã của bạn. Bạn sẽ thấy nó khiến bạn thành một lập trình viên giỏi hơn và vui hơn.

### Tiếng ồn đáng sợ

Javadoc cũng có thể ồn ào. Những javadoc sau (từ một thư viện mã nguồn mở nổi tiếng) phục vụ mục đích gì? Trả lời: không gì cả. Chúng chỉ là những chú thích dư thừa, ồn ào, được viết ra từ một mong muốn đặt nhầm chỗ là cung cấp tài liệu.

```java
/** Tên. */
private String name;
/** Phiên bản. */
private String version;

/** licenceName. */
private String licenceName;

/** Phiên bản. */
private String info;
```

Hãy đọc lại những chú thích này kỹ hơn. Bạn có thấy lỗi cắt dán không? Nếu tác giả không để ý khi viết (hoặc dán) chú thích, thì tại sao người đọc lại được kỳ vọng thu được lợi ích từ chúng?

### Đừng dùng chú thích khi có thể dùng hàm hay biến

Hãy xét đoạn mã sau:

```java
// module trong danh sách toàn cục <mod> có phụ thuộc vào
// subsystem mà chúng ta là một phần không?
if (smodule.getDependSubsystems().contains(subSysMod.getSubSystem()))
```

Có thể viết lại mà không cần chú thích như sau:

```java
ArrayList moduleDependees = smodule.getDependSubsystems();
String ourSubSystem = subSysMod.getSubSystem();
if (moduleDependees.contains(ourSubSystem))
```

Tác giả đoạn mã gốc có lẽ đã viết chú thích trước (khó có vậy) rồi viết mã để thỏa mãn chú thích. Tuy nhiên, sau đó tác giả nên tái cấu trúc mã như tôi đã làm, để có thể xóa chú thích.

### Điểm đánh dấu vị trí

Đôi khi lập trình viên thích đánh dấu một vị trí cụ thể trong tệp nguồn. Chẳng hạn, gần đây tôi thấy dòng này trong một chương trình đang xem qua:

```java
// Hành động //////////////////////////////////
```

Có những lúc hiếm hoi mà việc gom một số hàm lại dưới một tấm băng rôn như thế là hợp lý. Nhưng nói chung chúng là mớ rối rắm nên được loại bỏ, nhất là chuỗi dấu gạch chéo ồn ào ở cuối.

Hãy nghĩ thế này. Một tấm băng rôn gây giật mình và hiển nhiên nếu bạn không thường thấy băng rôn. Vì thế hãy dùng chúng thật tiết kiệm, và chỉ khi lợi ích đáng kể. Nếu dùng băng rôn quá nhiều, chúng sẽ chìm vào tiếng ồn nền và bị phớt lờ.

### Chú thích trên ngoặc đóng

Đôi khi lập trình viên đặt những chú thích đặc biệt trên dấu ngoặc đóng, như trong Đoạn mã 4-6. Dù điều này có thể hợp lý với những hàm dài, cấu trúc lồng sâu, nó chỉ làm rối những hàm nhỏ và được đóng gói mà chúng ta ưa thích. Vì vậy nếu bạn thấy mình muốn đánh dấu ngoặc đóng, hãy thử rút ngắn hàm của mình.

**Đoạn mã 4-6**
**wc.java**

```java
public class wc {
  public static void main(String[] args) {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String line;
    int lineCount = 0;
    int charCount = 0;
    int wordCount = 0;
    try {
      while ((line = in.readLine()) != null) {
        lineCount++;
        charCount += line.length();
        String words[] = line.split("\\W");
        wordCount += words.length;
      } //while
      System.out.println("wordCount = " + wordCount);
      System.out.println("lineCount = " + lineCount);
      System.out.println("charCount = " + charCount);
    } // try
    catch (IOException e) {
      System.err.println("Error:" + e.getMessage());
    } //catch
  } //main
}
```

### Ghi công và dòng tác giả

```java
/* Thêm bởi Rick */
```

Hệ thống quản lý mã nguồn rất giỏi ghi nhớ ai đã thêm cái gì, khi nào. Không cần làm ô nhiễm mã bằng những dòng tác giả nhỏ xíu. Có thể bạn nghĩ những chú thích như thế hữu ích để giúp người khác biết nên trao đổi với ai về đoạn mã. Nhưng thực tế là chúng có xu hướng nán lại hàng năm trời, ngày càng kém chính xác và kém liên quan.

Một lần nữa, hệ thống quản lý mã nguồn là nơi tốt hơn cho loại thông tin này.

### Mã bị chú thích hóa

Ít thực hành nào đáng ghét bằng việc chú thích hóa mã. Đừng làm thế!

```java
InputStreamResponse response = new InputStreamResponse();
response.setBody(formatter.getResultStream(), formatter.getByteCount());
//    InputStream resultsStream = formatter.getResultStream();
//    StreamReader reader = new StreamReader(resultsStream);
//    response.setContent(reader.read(formatter.getByteCount()));
```

Người khác thấy đoạn mã bị chú thích hóa ấy sẽ không đủ can đảm xóa nó. Họ nghĩ nó nằm đó vì một lý do nào đó và quá quan trọng để xóa. Thế là mã bị chú thích hóa đọng lại như cặn dưới đáy một chai rượu vang tồi.

Hãy xét đoạn này từ apache commons:

```java
this.bytePos = writeBytes(pngIdBytes, 0);
//hdrPos = bytePos;
writeHeader();
writeResolution();
//dataPos = bytePos;
if (writeImageData()) {
     writeEnd();
     this.pngBytes = resizeByteArray(this.pngBytes, this.maxPos);
}
else {
     this.pngBytes = null;
}
return this.pngBytes;
```

Vì sao hai dòng mã ấy bị chú thích hóa? Chúng có quan trọng không? Chúng được để lại làm lời nhắc cho một thay đổi sắp tới ư? Hay chúng chỉ là rác mà ai đó chú thích hóa từ nhiều năm trước và đơn giản là không buồn dọn?

Đã có thời, vào những năm sáu mươi, chú thích hóa mã có thể hữu ích. Nhưng chúng ta đã có hệ thống quản lý mã nguồn tốt từ rất lâu rồi. Những hệ thống ấy sẽ nhớ mã giúp chúng ta. Chúng ta không phải chú thích hóa nó nữa. Cứ xóa mã đi. Chúng ta sẽ không mất nó đâu. Hứa đấy.

### Chú thích HTML

HTML trong chú thích mã nguồn là một điều ghê tởm, như bạn có thể thấy khi đọc đoạn mã dưới đây. Nó khiến chú thích khó đọc ngay tại nơi duy nhất mà chúng phải dễ đọc: trình soạn thảo/IDE. Nếu chú thích sẽ được một công cụ nào đó (như Javadoc) trích xuất để xuất hiện trên một trang Web, thì công cụ ấy, chứ không phải lập trình viên, nên có trách nhiệm trang trí chú thích bằng HTML thích hợp.

```java
/**
 * Tác vụ chạy các kiểm thử fit.
 * Tác vụ này chạy các kiểm thử fitnesse và công bố kết quả.
 * <p/>
 * <pre>
 * Cách dùng:
 * &lt;taskdef name=&quot;execute-fitnesse-tests&quot;
 *      classname=&quot;fitnesse.ant.ExecuteFitnesseTestsTask&quot;
 *      classpathref=&quot;classpath&quot; /&gt;
 * HOẶC
 * &lt;taskdef classpathref=&quot;classpath&quot;
 *              resource=&quot;tasks.properties&quot; /&gt;
 * <p/>
 * &lt;execute-fitnesse-tests
 *      suitepage=&quot;FitNesse.SuiteAcceptanceTests&quot;
 *      fitnesseport=&quot;8082&quot;
 *      resultsdir=&quot;${results.dir}&quot;
 *      resultshtmlpage=&quot;fit-results.html&quot;
 *      classpathref=&quot;classpath&quot; /&gt;
 * </pre>
 */
```

### Thông tin phi cục bộ

Nếu buộc phải viết chú thích, hãy chắc rằng nó mô tả đoạn mã nằm gần nó. Đừng đưa thông tin toàn hệ thống vào ngữ cảnh của một chú thích cục bộ. Chẳng hạn, xét chú thích javadoc dưới đây. Ngoài việc dư thừa kinh khủng, nó còn cung cấp thông tin về cổng mặc định. Vậy mà hàm hoàn toàn không kiểm soát được giá trị mặc định đó. Chú thích không mô tả hàm mà mô tả một phần khác, xa hơn nhiều, của hệ thống. Tất nhiên không có gì bảo đảm chú thích này sẽ được sửa khi đoạn mã chứa giá trị mặc định thay đổi.

```java
  /**
    * Cổng mà fitnesse sẽ chạy trên đó. Mặc định là <b>8082</b>.
    *
    * @param fitnessePort
    */
  public void setFitnessePort(int fitnessePort)
  {
      this.fitnessePort = fitnessePort;
  }
```

### Quá nhiều thông tin

Đừng đưa những thảo luận lịch sử thú vị hay mô tả chi tiết không liên quan vào chú thích. Chú thích dưới đây được trích từ một module kiểm tra rằng một hàm có thể mã hóa và giải mã base64. Ngoài số RFC, người đọc đoạn mã này không cần thông tin uyên bác chứa trong chú thích.

```java
/*
      RFC 2045 - Multipurpose Internet Mail Extensions (MIME)
      Part One: Format of Internet Message Bodies
      section 6.8. Base64 Content-Transfer-Encoding
      Quá trình mã hóa biểu diễn các nhóm 24 bit đầu vào thành chuỗi
      đầu ra gồm 4 ký tự được mã hóa. Đi từ trái sang phải, một
      nhóm đầu vào 24 bit được tạo bằng cách ghép 3 nhóm đầu vào 8 bit.
      24 bit này sau đó được xử lý như 4 nhóm 6 bit ghép lại, mỗi
      nhóm được dịch thành một chữ số trong bảng chữ cái base64.
      Khi mã hóa một dòng bit bằng bảng mã base64, dòng bit
      phải được giả định là có thứ tự bit có nghĩa nhất đứng trước.
      Nghĩa là bit đầu tiên trong dòng sẽ là bit bậc cao trong
      byte 8 bit đầu tiên, và bit thứ tám sẽ là bit bậc thấp trong
      byte 8 bit đầu tiên, cứ thế tiếp tục.
*/
```

### Liên hệ không hiển nhiên

Mối liên hệ giữa một chú thích và đoạn mã nó mô tả phải hiển nhiên. Nếu bạn đã bỏ công viết chú thích, ít nhất bạn cũng muốn người đọc có thể nhìn chú thích và đoạn mã mà hiểu chú thích đang nói về cái gì.

Chẳng hạn, hãy xét chú thích này lấy từ apache commons:

```java
/*
 * bắt đầu với một mảng đủ lớn để chứa toàn bộ pixel
 * (cộng thêm byte bộ lọc), và thêm 200 byte cho thông tin header
 */
this.pngBytes = new byte[((this.width + 1) * this.height * 3) + 200];
```

Byte bộ lọc là gì? Nó liên quan đến +1 ư? Hay đến *3? Cả hai? Một pixel có phải một byte không? Vì sao 200? Mục đích của chú thích là giải thích đoạn mã không tự giải thích được. Thật đáng tiếc khi một chú thích lại cần chú thích cho chính nó.

### Đầu hàm

Hàm ngắn không cần nhiều mô tả. Một cái tên chọn kỹ cho hàm nhỏ chỉ làm một việc thường tốt hơn một chú thích đầu hàm.

### Javadoc trong mã không công khai

Javadoc hữu ích cho API công khai bao nhiêu thì lại là thứ đáng ghét với mã không dành cho công chúng bấy nhiêu. Sinh trang javadoc cho các lớp và hàm bên trong một hệ thống nói chung không hữu ích, còn sự trang trọng thừa thãi của các chú thích javadoc chẳng qua chỉ là rác rưởi và thứ gây phân tâm.

### Ví dụ

Tôi viết module trong Đoạn mã 4-7 cho XP Immersion lần đầu. Nó nhằm làm ví dụ về phong cách viết mã và chú thích tồi. Kent Beck sau đó tái cấu trúc đoạn mã này thành dạng dễ chịu hơn nhiều trước mặt vài chục sinh viên nhiệt tình. Về sau tôi chuyển thể ví dụ cho cuốn *Agile Software Development, Principles, Patterns, and Practices* và bài đầu tiên trong loạt bài Craftsman của tôi đăng trên tạp chí *Software Development*.

Điều tôi thấy hấp dẫn ở module này là đã có thời nhiều người trong chúng ta sẽ coi nó là “được ghi chép tài liệu tốt”. Giờ chúng ta thấy nó là một mớ hỗn độn nhỏ. Hãy xem bạn tìm được bao nhiêu vấn đề chú thích khác nhau.

**Đoạn mã 4-7**
**GeneratePrimes.java**

```java
/**
 * Lớp này sinh các số nguyên tố tới một giới hạn tối đa
 * do người dùng chỉ định. Thuật toán dùng là Sàng Eratosthenes.
 * <p>
 * Eratosthenes xứ Cyrene, sinh khoảng 276 TCN, tại Cyrene, Libya,
 * mất khoảng 194, tại Alexandria. Người đầu tiên tính được
 * chu vi Trái Đất. Cũng nổi tiếng nhờ làm việc trên
 * lịch với năm nhuận và điều hành thư viện ở Alexandria.
 * <p>
 * Thuật toán khá đơn giản. Cho một mảng số nguyên
 * bắt đầu từ 2. Gạch bỏ mọi bội số của 2. Tìm số nguyên
 * chưa bị gạch kế tiếp, và gạch bỏ mọi bội số của nó.
 * Lặp lại cho đến khi bạn đã vượt qua căn bậc hai của giá trị
 * tối đa.
 *
 * @author Alphonse
 * @version 13 Feb 2002 atp
 */
import java.util.*;

public class GeneratePrimes
{
  /**
    * @param maxValue là giới hạn sinh số.
    */
  public static int[] generatePrimes(int maxValue)
  {
     if (maxValue >= 2) // trường hợp hợp lệ duy nhất
     {
       // khai báo
       int s = maxValue + 1; // kích thước mảng
       boolean[] f = new boolean[s];
       int i;

       // khởi tạo mảng thành true.
       for (i = 0; i < s; i++)
         f[i] = true;

       // loại bỏ các số đã biết không phải số nguyên tố
       f[0] = f[1] = false;

       // sàng
       int j;
       for (i = 2; i < Math.sqrt(s) + 1; i++)
       {
         if (f[i]) // nếu i chưa bị gạch, gạch bỏ các bội số của nó.
         {
           for (j = 2 * i; j < s; j += i)
              f[j] = false; // bội số không phải số nguyên tố
         }
       }
       // có bao nhiêu số nguyên tố?
       int count = 0;
       for (i = 0; i < s; i++)
       {
         if (f[i])
           count++; // tăng biến đếm.
       }
       int[] primes = new int[count];
       // chuyển các số nguyên tố vào kết quả
       for (i = 0, j = 0; i < s; i++)
       {
         if (f[i])             // nếu là số nguyên tố
           primes[j++] = i;
       }

       return primes; // trả về các số nguyên tố
     }
     else // maxValue < 2
       return new int[0]; // trả về mảng null nếu đầu vào không hợp lệ.
  }
}
```

Trong Đoạn mã 4-8, bạn thấy một phiên bản đã tái cấu trúc của cùng module. Hãy để ý rằng việc dùng chú thích được tiết chế đáng kể. Cả module chỉ có hai chú thích. Cả hai đều mang tính giải thích.

**Đoạn mã 4-8**
**PrimeGenerator.java (đã tái cấu trúc)**

```java
/**
 * Lớp này sinh các số nguyên tố tới một giới hạn tối đa
 * do người dùng chỉ định. Thuật toán dùng là Sàng Eratosthenes.
 * Cho một mảng số nguyên bắt đầu từ 2:
 * Tìm số nguyên chưa bị gạch đầu tiên, và gạch bỏ mọi
```

**Đoạn mã 4-8 (tiếp theo)**
**PrimeGenerator.java (đã tái cấu trúc)**

```java
 * bội số của nó. Lặp lại cho đến khi không còn bội số
 * nào trong mảng.
 */

public class PrimeGenerator
{
  private static boolean[] crossedOut;
  private static int[] result;

  public static int[] generatePrimes(int maxValue)
  {
    if (maxValue < 2)
      return new int[0];
    else
    {
      uncrossIntegersUpTo(maxValue);
      crossOutMultiples();
      putUncrossedIntegersIntoResult();
      return result;
    }
  }

  private static void uncrossIntegersUpTo(int maxValue)
  {
    crossedOut = new boolean[maxValue + 1];
    for (int i = 2; i < crossedOut.length; i++)
      crossedOut[i] = false;
  }

  private static void crossOutMultiples()
  {
    int limit = determineIterationLimit();
    for (int i = 2; i <= limit; i++)
      if (notCrossed(i))
        crossOutMultiplesOf(i);
  }
  private static int determineIterationLimit()
  {
    // Mọi bội số trong mảng đều có một ước nguyên tố
    // nhỏ hơn hoặc bằng căn bậc hai của kích thước mảng,
    // nên ta không cần gạch bỏ bội số của những số
    // lớn hơn căn bậc hai đó.
    double iterationLimit = Math.sqrt(crossedOut.length);
    return (int) iterationLimit;
  }
  private static void crossOutMultiplesOf(int i)
  {
    for (int multiple = 2*i;
         multiple < crossedOut.length;
         multiple += i)
      crossedOut[multiple] = true;
  }
```

**Đoạn mã 4-8 (tiếp theo)**
**PrimeGenerator.java (đã tái cấu trúc)**

```java
  private static boolean notCrossed(int i)
  {
    return crossedOut[i] == false;
  }

  private static void putUncrossedIntegersIntoResult()
  {
    result = new int[numberOfUncrossedIntegers()];
    for (int j = 0, i = 2; i < crossedOut.length; i++)
      if (notCrossed(i))
        result[j++] = i;
  }

  private static int numberOfUncrossedIntegers()
  {
    int count = 0;
    for (int i = 2; i < crossedOut.length; i++)
      if (notCrossed(i))
        count++;

      return count;
  }
}
```

Có thể dễ dàng lập luận rằng chú thích đầu là dư thừa vì nó đọc rất giống chính hàm generatePrimes. Tuy vậy, tôi nghĩ chú thích ấy giúp người đọc làm quen với thuật toán, nên tôi nghiêng về việc giữ lại.

Lập luận thứ hai gần như chắc chắn là cần thiết. Nó giải thích lý do dùng căn bậc hai làm giới hạn vòng lặp. Tôi không tìm được cái tên biến đơn giản nào, cũng không tìm được cấu trúc mã nào khác làm rõ điểm này. Mặt khác, việc dùng căn bậc hai có thể chỉ là thói tự phụ. Tôi có thật sự tiết kiệm được nhiều thời gian đến thế khi giới hạn vòng lặp ở căn bậc hai không? Việc tính căn bậc hai có thể tốn nhiều thời gian hơn phần tôi tiết kiệm được không?

Điều này đáng để nghĩ. Dùng căn bậc hai làm giới hạn vòng lặp làm hài lòng con người hacker C và hợp ngữ trong tôi, nhưng tôi không tin nó đáng với thời gian và công sức mà mọi người khác sẽ bỏ ra để hiểu nó.

## Tài liệu tham khảo

[KP78]: Kernighan and Plaugher, *The Elements of Programming Style*, 2d. ed., McGraw-Hill, 1978.

[^1]: [KP78], tr. 144.

[^2]: Xu hướng hiện nay là các IDE kiểm tra chính tả trong chú thích sẽ là một liều thuốc an ủi cho những người đọc nhiều mã như chúng ta.
