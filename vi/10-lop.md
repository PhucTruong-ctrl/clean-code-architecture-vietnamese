# Chương 10: Lớp

> với Jeff Langr

Cho đến nay, trong cuốn sách này, chúng ta tập trung vào cách viết tốt từng dòng và từng khối mã. Chúng ta đã tìm hiểu kỹ cách tổ chức các hàm cho đúng và cách chúng tương tác với nhau. Nhưng dù đã quan tâm đến khả năng diễn đạt của các câu lệnh mã và những hàm cấu thành nên chúng đến đâu, mã vẫn chưa sạch nếu chúng ta chưa chú ý đến những cấp độ tổ chức mã cao hơn. Hãy nói về các lớp sạch.

## Tổ chức lớp
Theo quy ước Java tiêu chuẩn, một lớp nên bắt đầu bằng danh sách biến. Nếu có hằng tĩnh công khai thì đặt chúng lên đầu. Tiếp theo là các biến tĩnh riêng tư, rồi đến các biến thực thể riêng tư. Hiếm khi có lý do chính đáng để khai báo biến công khai.

Các hàm công khai nên đứng sau danh sách biến. Chúng tôi thường đặt các hàm tiện ích riêng tư mà một hàm công khai gọi đến ngay sau chính hàm công khai đó. Cách này tuân theo quy tắc đi từng bước và giúp chương trình đọc như một bài báo.

### Đóng gói
Chúng tôi muốn giữ biến và hàm tiện ích ở phạm vi riêng tư, nhưng không quá cứng nhắc. Đôi khi cần đặt một biến hoặc hàm tiện ích ở phạm vi protected để kiểm thử có thể truy cập. Với chúng tôi, kiểm thử là ưu tiên hàng đầu. Nếu một ca kiểm thử trong cùng gói cần gọi một hàm hoặc truy cập một biến, chúng tôi sẽ đặt nó ở phạm vi protected hoặc phạm vi gói. Tuy nhiên, trước tiên chúng tôi sẽ tìm cách duy trì tính riêng tư. Nới lỏng đóng gói luôn là lựa chọn cuối cùng.

## Lớp phải nhỏ!
Quy tắc đầu tiên dành cho lớp là phải nhỏ. Quy tắc thứ hai là phải nhỏ hơn nữa. Không, chúng tôi sẽ không lặp lại nguyên văn chương Hàm. Nhưng cũng như với hàm, kích thước nhỏ là quy tắc hàng đầu khi thiết kế lớp. Cũng như với hàm, câu hỏi đầu tiên luôn là: “Nhỏ đến mức nào?”

Với hàm, chúng ta đo kích thước bằng cách đếm số dòng vật lý. Với lớp, chúng ta dùng một thước đo khác: đếm số trách nhiệm.¹

Đoạn mã 10-1 phác họa lớp SuperDashboard, với khoảng 70 phương thức công khai. Hầu hết nhà phát triển đều đồng ý rằng nó hơi quá “siêu” về kích thước. Một số người có thể gọi SuperDashboard là “lớp Thần”.

**Đoạn mã 10-1**  
**Quá nhiều trách nhiệm**

```java
public class SuperDashboard extends JFrame implements MetaDataUser
   public String getCustomizerLanguagePath()
   public void setSystemConfigPath(String systemConfigPath)
   public String getSystemConfigDocument()
   public void setSystemConfigDocument(String systemConfigDocument)
   public boolean getGuruState()
   public boolean getNoviceState()
   public boolean getOpenSourceState()
   public void showObject(MetaObject object)
   public void showProgress(String s)
```

¹ [RDD].

**Đoạn mã 10-1 (tiếp)**  
**Quá nhiều trách nhiệm**

```java
   public boolean isMetadataDirty()
   public void setIsMetadataDirty(boolean isMetadataDirty)
   public Component getLastFocusedComponent()
   public void setLastFocused(Component lastFocused)
   public void setMouseSelectState(boolean isMouseSelected)
   public boolean isMouseSelected()
   public LanguageManager getLanguageManager()
   public Project getProject()
   public Project getFirstProject()
   public Project getLastProject()
   public String getNewProjectName()
   public void setComponentSizes(Dimension dim)
   public String getCurrentDir()
   public void setCurrentDir(String newDir)
   public void updateStatus(int dotPos, int markPos)
   public Class[] getDataBaseClasses()
   public MetadataFeeder getMetadataFeeder()
   public void addProject(Project project)
   public boolean setCurrentProject(Project project)
   public boolean removeProject(Project project)
   public MetaProjectHeader getProgramMetadata()
   public void resetDashboard()
   public Project loadProject(String fileName, String projectName)
   public void setCanSaveMetadata(boolean canSave)
   public MetaObject getSelectedObject()
   public void deselectObjects()
   public void setProject(Project project)
   public void editorAction(String actionName, ActionEvent event)
   public void setMode(int mode)
   public FileManager getFileManager()
   public void setFileManager(FileManager fileManager)
   public ConfigManager getConfigManager()
   public void setConfigManager(ConfigManager configManager)
   public ClassLoader getClassLoader()
   public void setClassLoader(ClassLoader classLoader)
   public Properties getProps()
   public String getUserHome()
   public String getBaseDir()
   public int getMajorVersionNumber()
   public int getMinorVersionNumber()
   public int getBuildNumber()
   public MetaObject pasting(
      MetaObject target, MetaObject pasted, MetaProject project)
   public void processMenuItems(MetaObject metaObject)
   public void processMenuSeparators(MetaObject metaObject)
   public void processTabPages(MetaObject metaObject)
   public void processPlacement(MetaObject object)
   public void processCreateLayout(MetaObject object)
   public void updateDisplayLayer(MetaObject object, int layerIndex)
   public void propertyEditedRepaint(MetaObject object)
   public void processDeleteObject(MetaObject object)
   public boolean getAttachedToDesigner()
   public void processProjectChangedState(boolean hasProjectChanged)
   public void processObjectNameChanged(MetaObject object)
   public void runProject()
```

**Đoạn mã 10-1 (tiếp)**  
**Quá nhiều trách nhiệm**

```java
   public void setAçowDragging(boolean allowDragging)
   public boolean allowDragging()
   public boolean isCustomizing()
   public void setTitle(String title)
   public IdeMenuBar getIdeMenuBar()
   public void showHelper(MetaObject metaObject, String propertyName)
   // ... many non-public methods follow ...
}
```

Nhưng nếu SuperDashboard chỉ chứa các phương thức trong Đoạn mã 10-2 thì sao?

**Đoạn mã 10-2**  
**Đủ nhỏ chưa?**

```java
public class SuperDashboard extends JFrame implements MetaDataUser
    public Component getLastFocusedComponent()
    public void setLastFocused(Component lastFocused)
    public int getMajorVersionNumber()
    public int getMinorVersionNumber()
    public int getBuildNumber()
}
```

Năm phương thức đâu có nhiều, phải không? Trong trường hợp này thì có, vì dù số phương thức ít, SuperDashboard vẫn có quá nhiều trách nhiệm.

Tên lớp nên mô tả những trách nhiệm mà lớp đảm nhận. Thực ra, đặt tên có lẽ là cách đầu tiên giúp xác định kích thước lớp. Nếu không thể nghĩ ra một cái tên ngắn gọn cho lớp thì có lẽ lớp đó quá lớn. Tên lớp càng mơ hồ, khả năng nó có quá nhiều trách nhiệm càng cao. Chẳng hạn, những tên lớp có các từ chung chung như Processor, Manager hay Super thường báo hiệu một sự gộp trách nhiệm không hợp lý.

Ta cũng nên có thể mô tả ngắn gọn lớp trong khoảng 25 từ, không dùng các từ “if”, “and”, “or” hay “but”. Ta sẽ mô tả SuperDashboard thế nào? “SuperDashboard cung cấp quyền truy cập vào thành phần gần nhất giữ tiêu điểm, đồng thời cho phép theo dõi số phiên bản và số build.” Từ “and” đầu tiên là dấu hiệu SuperDashboard đang gánh quá nhiều trách nhiệm.

### Nguyên tắc trách nhiệm đơn nhất
Nguyên tắc trách nhiệm đơn nhất (Single Responsibility Principle, SRP)² nói rằng một lớp hay mô-đun chỉ nên có một lý do để thay đổi. Nguyên tắc này vừa định nghĩa trách nhiệm, vừa đưa ra nguyên tắc kinh nghiệm về kích thước lớp. Mỗi lớp nên có một trách nhiệm, tức một lý do để thay đổi.

² Bạn có thể đọc thêm nhiều hơn về nguyên tắc này trong [PPP].

Lớp SuperDashboard có vẻ nhỏ trong Đoạn mã 10-2 nhưng lại có hai lý do để thay đổi. Thứ nhất, nó theo dõi thông tin phiên bản, dường như cần cập nhật mỗi khi phát hành phần mềm. Thứ hai, nó quản lý các thành phần Java Swing (nó là lớp dẫn xuất của JFrame, biểu diễn của Swing cho cửa sổ GUI cấp cao nhất). Chắc chắn ta sẽ muốn cập nhật số phiên bản nếu thay đổi mã Swing, nhưng điều ngược lại không nhất thiết đúng: ta có thể thay đổi thông tin phiên bản do những thay đổi ở phần mã khác trong hệ thống.

Cố gắng xác định trách nhiệm, tức lý do để thay đổi, thường giúp chúng ta nhận ra và tạo ra những trừu tượng tốt hơn trong mã. Ta có thể dễ dàng tách cả ba phương thức của SuperDashboard liên quan đến thông tin phiên bản vào một lớp riêng tên là Version. (Xem Đoạn mã 10-3.) Lớp Version là một cấu trúc có tiềm năng được tái sử dụng cao trong các ứng dụng khác!

**Đoạn mã 10-3**  
**Lớp có một trách nhiệm**

```java
public class Version {
    public int getMajorVersionNumber()
    public int getMinorVersionNumber()
    public int getBuildNumber()
}
```

SRP là một trong những khái niệm quan trọng nhất trong thiết kế hướng đối tượng. Đây cũng là một trong những khái niệm đơn giản nhất để hiểu và tuân theo. Thế nhưng, lạ thay, SRP thường là nguyên tắc thiết kế lớp bị lạm dụng nhiều nhất. Chúng tôi thường xuyên gặp những lớp làm quá nhiều việc. Vì sao?

Làm cho phần mềm hoạt động và làm cho phần mềm sạch là hai hoạt động rất khác nhau. Hầu hết chúng ta có khả năng tập trung hữu hạn, nên thường chú trọng làm cho mã chạy được hơn là tổ chức và giữ mã sạch. Điều đó hoàn toàn hợp lý. Trong hoạt động lập trình cũng như trong chương trình, duy trì sự phân tách mối quan tâm quan trọng ngang nhau.

Vấn đề là quá nhiều người trong chúng ta nghĩ rằng công việc đã xong khi chương trình chạy được. Chúng ta không chuyển sang mối quan tâm còn lại là tổ chức và sự sạch sẽ. Thay vì quay lại chia những lớp phình to thành các đơn vị tách biệt, mỗi đơn vị chỉ có một trách nhiệm, chúng ta chuyển sang vấn đề tiếp theo.

Đồng thời, nhiều nhà phát triển lo rằng có nhiều lớp nhỏ, mỗi lớp làm một việc, sẽ khiến bức tranh tổng thể khó hiểu hơn. Họ ngại phải lần từ lớp này sang lớp khác mới tìm ra cách một phần công việc lớn được thực hiện.

Tuy nhiên, một hệ thống có nhiều lớp nhỏ không có nhiều bộ phận chuyển động hơn hệ thống có vài lớp lớn. Hệ thống chỉ có vài lớp lớn cũng cần học hỏi ngần ấy điều. Vậy câu hỏi là: Bạn muốn sắp xếp công cụ vào những hộp đựng có nhiều ngăn nhỏ, mỗi ngăn chứa một bộ phận được xác định và dán nhãn rõ ràng? Hay muốn có vài ngăn rồi quăng mọi thứ vào đó?

Hệ thống đủ lớn nào cũng chứa nhiều logic và độ phức tạp. Mục tiêu hàng đầu khi quản lý độ phức tạp ấy là tổ chức sao cho nhà phát triển biết tìm gì ở đâu và tại mỗi thời điểm chỉ cần hiểu phần phức tạp bị ảnh hưởng trực tiếp. Ngược lại, hệ thống có các lớp lớn đa dụng luôn cản trở chúng ta bằng cách buộc ta lội qua hàng đống thứ chưa cần biết lúc này.

Nhắc lại các ý trên để nhấn mạnh: chúng ta muốn hệ thống gồm nhiều lớp nhỏ, không phải vài lớp lớn. Mỗi lớp nhỏ đóng gói một trách nhiệm, có một lý do để thay đổi và cộng tác với một vài lớp khác để tạo ra các hành vi mong muốn của hệ thống.

### Độ gắn kết
Lớp nên có ít biến thực thể. Mỗi phương thức của lớp nên thao tác trên một hoặc nhiều biến đó. Nói chung, một phương thức thao tác càng nhiều biến thì càng gắn kết với lớp của nó. Lớp mà mọi biến đều được mọi phương thức sử dụng đạt độ gắn kết tối đa.

Nhìn chung, tạo ra những lớp gắn kết tối đa vừa không khả thi vừa không nên làm. Tuy vậy, chúng ta muốn độ gắn kết cao. Độ gắn kết cao nghĩa là các phương thức và biến của lớp phụ thuộc lẫn nhau và kết hợp thành một chỉnh thể logic.

Hãy xem cách cài đặt Stack trong Đoạn mã 10-4. Đây là một lớp có độ gắn kết rất cao. Trong ba phương thức, chỉ có size() không dùng cả hai biến.

**Đoạn mã 10-4**  
**Stack.java, một lớp gắn kết**

```java
public class Stack {
  private int topOfStack = 0;
  List<Integer> elements = new LinkedList<Integer>();
    public int size() {
      return topOfStack;
    }

    public void push(int element) {
      topOfStack++;
      elements.add(element);
    }

    public int pop() throws PoppedWhenEmpty {
      if (topOfStack == 0)
        throw new PoppedWhenEmpty();
      int element = elements.get(--topOfStack);
      elements.remove(topOfStack);
      return element;
    }
}
```

Chiến lược giữ hàm nhỏ và danh sách tham số ngắn đôi khi dẫn đến việc có thêm nhiều biến thực thể chỉ được một nhóm phương thức sử dụng. Khi vậy, gần như luôn có ít nhất một lớp khác đang cố tách ra khỏi lớp lớn. Bạn nên thử tách các biến và phương thức thành hai hay nhiều lớp để các lớp mới có độ gắn kết cao hơn.

### Duy trì độ gắn kết tạo ra nhiều lớp nhỏ
Chỉ riêng việc chia các hàm lớn thành hàm nhỏ hơn đã làm số lớp tăng lên. Hãy xét một hàm lớn có nhiều biến được khai báo bên trong. Giả sử bạn muốn tách một phần nhỏ của hàm đó thành hàm riêng. Tuy nhiên, đoạn mã muốn tách sử dụng bốn biến được khai báo trong hàm. Bạn có phải truyền cả bốn biến ấy vào hàm mới làm đối số không?

Không hề! Nếu đưa bốn biến đó thành biến thực thể của lớp, ta có thể tách đoạn mã mà không cần truyền biến nào. Việc chia hàm thành các phần nhỏ sẽ rất dễ dàng.

Đáng tiếc, điều này cũng làm lớp mất độ gắn kết vì nó tích lũy ngày càng nhiều biến thực thể chỉ tồn tại để một vài hàm dùng chung. Nhưng khoan đã! Nếu có vài hàm muốn dùng chung những biến nhất định thì chẳng phải chúng hợp thành một lớp riêng sao? Đúng vậy. Khi lớp mất độ gắn kết, hãy tách nó ra!

Vì thế, chia một hàm lớn thành nhiều hàm nhỏ thường tạo cơ hội tách thêm một số lớp nhỏ. Cách này giúp chương trình có tổ chức tốt hơn và cấu trúc minh bạch hơn.

Để minh họa ý mình, hãy dùng một ví dụ lâu đời trong cuốn sách tuyệt vời Literate Programming của Knuth.³ Đoạn mã 10-5 trình bày phiên bản Java của chương trình PrintPrimes của Knuth. Công bằng mà nói, đây không phải chương trình do ông viết nguyên dạng, mà là bản do công cụ WEB của ông xuất ra. Tôi dùng nó vì đây là điểm khởi đầu tuyệt vời để chia một hàm lớn thành nhiều hàm và lớp nhỏ hơn.

**Đoạn mã 10-5**  
**PrintPrimes.java**

```java
package literatePrimes;

public class PrintPrimes {
  public static void main(String[] args) {
    final int M = 1000;
    final int RR = 50;
    final int CC = 4;
    final int WW = 10;
    final int ORDMAX = 30;
    int P[] = new int[M + 1];
    int PAGENUMBER;
    int PAGEOFFSET;
    int ROWOFFSET;
    int C;
    int J;
    int K;
    boolean JPRIME;
    int ORD;
    int SQUARE;
    int N;
    int MULT[] = new int[ORDMAX + 1];

    J = 1;
    K = 1;
    P[1] = 2;
    ORD = 2;
    SQUARE = 9;

    while (K < M) {
      do {
        J = J + 2;
        if (J == SQUARE) {
           ORD = ORD + 1;
           SQUARE = P[ORD] * P[ORD];
           MULT[ORD - 1] = J;
        }
        N = 2;
        JPRIME = true;
        while (N < ORD && JPRIME) {
           while (MULT[N] < J)
             MULT[N] = MULT[N] + P[N] + P[N];
           if (MULT[N] == J)
             JPRIME = false;
           N = N + 1;
        }
      } while (!JPRIME);
      K = K + 1;
      P[K] = J;
    }
    {
      PAGENUMBER = 1;
      PAGEOFFSET = 1;
      while (PAGEOFFSET <= M) {
        System.out.println("The First " + M +
                              " Prime Numbers --- Page " + PAGENUMBER);
        System.out.println("");
        for (ROWOFFSET = PAGEOFFSET; ROWOFFSET < PAGEOFFSET + RR; ROWOFFSET++){
           for (C = 0; C < CC;C++)
             if (ROWOFFSET + C * RR <= M)
               System.out.format("%10d", P[ROWOFFSET + C * RR]);
           System.out.println("");
        }
        System.out.println("\f");
        PAGENUMBER = PAGENUMBER + 1;
        PAGEOFFSET = PAGEOFFSET + RR * CC;
      }
    }
  }
}
```

³ [Knuth92].

Chương trình này, được viết thành một hàm duy nhất, là một mớ hỗn độn. Cấu trúc lồng sâu, vô số biến kỳ quặc và kết cấu phụ thuộc chặt chẽ. Ít nhất, nên chia hàm lớn duy nhất ấy thành vài hàm nhỏ hơn.

Đoạn mã 10-6 đến 10-8 cho thấy kết quả sau khi chia mã trong Đoạn mã 10-5 thành các lớp và hàm nhỏ hơn, đồng thời chọn tên có ý nghĩa cho những lớp, hàm và biến đó.

**Đoạn mã 10-6**  
**PrimePrinter.java (đã tái cấu trúc)**

```java
package literatePrimes;

public class PrimePrinter {
  public static void main(String[] args) {
    final int NUMBER_OF_PRIMES = 1000;
    int[] primes = PrimeGenerator.generate(NUMBER_OF_PRIMES);

        final int ROWS_PER_PAGE = 50;
        final int COLUMNS_PER_PAGE = 4;
        RowColumnPagePrinter tablePrinter =
          new RowColumnPagePrinter(ROWS_PER_PAGE,
                                   COLUMNS_PER_PAGE,
                                   "The First " + NUMBER_OF_PRIMES +
                                     " Prime Numbers");

        tablePrinter.print(primes);
    }

}
```

**Đoạn mã 10-7**  
**RowColumnPagePrinter.java**

```java
package literatePrimes;

import java.io.PrintStream;

public class RowColumnPagePrinter {
  private int rowsPerPage;
  private int columnsPerPage;
  private int numbersPerPage;
  private String pageHeader;
  private PrintStream printStream;

    public RowColumnPagePrinter(int rowsPerPage,
                                int columnsPerPage,
                                String pageHeader) {
      this.rowsPerPage = rowsPerPage;
      this.columnsPerPage = columnsPerPage;
      this.pageHeader = pageHeader;
      numbersPerPage = rowsPerPage * columnsPerPage;
      printStream = System.out;
    }
```

**Đoạn mã 10-7 (tiếp)**  
**RowColumnPagePrinter.java**

```java
    public void print(int data[]) {
      int pageNumber = 1;
      for (int firstIndexOnPage = 0;
           firstIndexOnPage < data.length;
           firstIndexOnPage += numbersPerPage) {
        int lastIndexOnPage =
          Math.min(firstIndexOnPage + numbersPerPage - 1,
                   data.length - 1);
        printPageHeader(pageHeader, pageNumber);
        printPage(firstIndexOnPage, lastIndexOnPage, data);
        printStream.println("\f");
        pageNumber++;
      }
    }
    private void printPage(int firstIndexOnPage,
                           int lastIndexOnPage,
                           int[] data) {
      int firstIndexOfLastRowOnPage =
        firstIndexOnPage + rowsPerPage - 1;
      for (int firstIndexInRow = firstIndexOnPage;
           firstIndexInRow <= firstIndexOfLastRowOnPage;
           firstIndexInRow++) {
        printRow(firstIndexInRow, lastIndexOnPage, data);
        printStream.println("");
      }
    }

    private void printRow(int firstIndexInRow,
                          int lastIndexOnPage,
                          int[] data) {
      for (int column = 0; column < columnsPerPage; column++) {
        int index = firstIndexInRow + column * rowsPerPage;
        if (index <= lastIndexOnPage)
          printStream.format("%10d", data[index]);
      }
    }

    private void printPageHeader(String pageHeader,
                                 int pageNumber) {
      printStream.println(pageHeader + " --- Page " + pageNumber);
      printStream.println("");
    }

    public void setOutput(PrintStream printStream) {
      this.printStream = printStream;
    }
}
```

**Đoạn mã 10-8**  
**PrimeGenerator.java**

```java
package literatePrimes;

import java.util.ArrayList;

public class PrimeGenerator {
  private static int[] primes;
  private static ArrayList<Integer> multiplesOfPrimeFactors;

  protected static int[] generate(int n) {
    primes = new int[n];
    multiplesOfPrimeFactors = new ArrayList<Integer>();
    set2AsFirstPrime();
    checkOddNumbersForSubsequentPrimes();
    return primes;
  }

  private static void set2AsFirstPrime() {
    primes[0] = 2;
    multiplesOfPrimeFactors.add(2);
  }

  private static void checkOddNumbersForSubsequentPrimes() {
    int primeIndex = 1;
    for (int candidate = 3;
         primeIndex < primes.length;
         candidate += 2) {
      if (isPrime(candidate))
        primes[primeIndex++] = candidate;
    }
  }

  private static boolean isPrime(int candidate) {
    if (isLeastRelevantMultipleOfNextLargerPrimeFactor(candidate)) {
      multiplesOfPrimeFactors.add(candidate);
      return false;
    }
    return isNotMultipleOfAnyPreviousPrimeFactor(candidate);
  }

  private static boolean
  isLeastRelevantMultipleOfNextLargerPrimeFactor(int candidate) {
    int nextLargerPrimeFactor = primes[multiplesOfPrimeFactors.size()];
    int leastRelevantMultiple = nextLargerPrimeFactor * nextLargerPrimeFactor;
    return candidate == leastRelevantMultiple;
  }
  private static boolean
  isNotMultipleOfAnyPreviousPrimeFactor(int candidate) {
    for (int n = 1; n < multiplesOfPrimeFactors.size(); n++) {
      if (isMultipleOfNthPrimeFactor(candidate, n))
        return false;
    }
```

**Đoạn mã 10-8 (tiếp)**  
**PrimeGenerator.java**

```java
        return true;
    }

    private static boolean
    isMultipleOfNthPrimeFactor(int candidate, int n) {
      return
        candidate == smallestOddNthMultipleNotLessThanCandidate(candidate, n);
    }

    private static int
    smallestOddNthMultipleNotLessThanCandidate(int candidate, int n) {
      int multiple = multiplesOfPrimeFactors.get(n);
      while (multiple < candidate)
        multiple += 2 * primes[n];
      multiplesOfPrimeFactors.set(n, multiple);
      return multiple;
    }
}
```

Điều đầu tiên bạn có thể nhận thấy là chương trình dài hơn hẳn. Nó tăng từ hơn một trang một chút lên gần ba trang. Có vài lý do cho sự gia tăng này. Thứ nhất, chương trình sau tái cấu trúc dùng tên biến dài hơn và mô tả rõ hơn. Thứ hai, chương trình dùng khai báo hàm và lớp để bổ sung lời giải thích cho mã. Thứ ba, chúng ta dùng khoảng trắng và kỹ thuật định dạng để giữ chương trình dễ đọc.

Hãy chú ý chương trình được chia thành ba trách nhiệm chính. Chương trình chính nằm riêng trong lớp PrimePrinter. Trách nhiệm của nó là xử lý môi trường thực thi. Lớp này sẽ thay đổi nếu cách gọi chương trình thay đổi. Chẳng hạn, nếu chuyển chương trình thành dịch vụ SOAP, đây là lớp sẽ bị ảnh hưởng.

RowColumnPagePrinter hiểu rõ cách định dạng danh sách số thành các trang có số hàng và cột nhất định. Nếu cần thay đổi định dạng đầu ra thì lớp này sẽ bị ảnh hưởng.

Lớp PrimeGenerator biết cách tạo danh sách số nguyên tố. Hãy lưu ý rằng lớp này không được thiết kế để khởi tạo thành đối tượng. Lớp chỉ là một phạm vi hữu ích để khai báo và ẩn các biến. Lớp này sẽ thay đổi nếu thuật toán tính số nguyên tố thay đổi.

Đây không phải là viết lại! Chúng ta không bắt đầu lại từ đầu để viết lại chương trình. Thật vậy, nếu xem kỹ hai chương trình, bạn sẽ thấy chúng dùng cùng một thuật toán và cơ chế để hoàn thành công việc.

Thay đổi được thực hiện bằng cách viết một bộ kiểm thử xác minh chính xác hành vi của chương trình đầu tiên. Sau đó, vô số thay đổi nhỏ được thực hiện, mỗi lần một thay đổi. Sau mỗi thay đổi, chương trình được chạy để bảo đảm hành vi không đổi. Từng bước nhỏ nối tiếp nhau, chương trình đầu tiên được làm sạch và chuyển thành chương trình thứ hai.

## Tổ chức để thay đổi
Với hầu hết hệ thống, thay đổi diễn ra liên tục. Mỗi thay đổi đều khiến chúng ta đối mặt với nguy cơ phần còn lại của hệ thống không còn hoạt động như dự định. Trong một hệ thống sạch, chúng ta tổ chức các lớp sao cho giảm rủi ro khi thay đổi.

Lớp Sql trong Đoạn mã 10-9 dùng để tạo các chuỗi SQL đúng định dạng từ siêu dữ liệu phù hợp. Công việc vẫn đang tiếp diễn nên lớp này chưa hỗ trợ các chức năng SQL như câu lệnh update. Khi cần để lớp Sql hỗ trợ câu lệnh update, chúng ta sẽ phải “mở” lớp này để sửa đổi. Vấn đề của việc mở một lớp là nó tạo ra rủi ro. Bất kỳ sửa đổi nào cũng có thể làm hỏng phần mã khác trong lớp. Phải kiểm thử lại toàn bộ.

**Đoạn mã 10-9**  
**Lớp phải mở để thay đổi**

```java
public class Sql {
   public Sql(String table, Column[] columns)
   public String create()
   public String insert(Object[] fields)
   public String selectAll()
   public String findByKey(String keyColumn, String keyValue)
   public String select(Column column, String pattern)
   public String select(Criteria criteria)
   public String preparedInsert()
   private String columnList(Column[] columns)
   private String valuesList(Object[] fields, final Column[] columns)
   private String selectWithCriteria(String criteria)
   private String placeholderList(Column[] columns)
}
```

Lớp Sql phải thay đổi khi thêm một kiểu câu lệnh mới. Nó cũng phải thay đổi khi sửa chi tiết của một kiểu câu lệnh, chẳng hạn nếu cần sửa chức năng select để hỗ trợ truy vấn con. Hai lý do thay đổi này cho thấy lớp Sql vi phạm SRP.

Ta có thể nhận ra vi phạm SRP này chỉ bằng cách xem xét tổ chức. Dàn ý phương thức của Sql cho thấy có những phương thức riêng tư như selectWithCriteria dường như chỉ liên quan đến câu lệnh select.

Hành vi của phương thức riêng tư chỉ áp dụng cho một phần nhỏ của lớp có thể là một nguyên tắc kinh nghiệm hữu ích để nhận biết những khu vực tiềm năng cần cải thiện. Tuy nhiên, động lực chính để hành động nên đến từ chính những thay đổi của hệ thống. Nếu cho rằng lớp Sql đã hoàn chỉnh về mặt logic thì không cần lo chuyện tách trách nhiệm. Nếu trong tương lai gần chúng ta không cần chức năng update thì cứ để yên Sql. Nhưng ngay khi thấy mình phải mở một lớp, ta nên cân nhắc sửa lại thiết kế.

Nếu cân nhắc một giải pháp như trong Đoạn mã 10-10 thì sao? Mỗi phương thức giao diện công khai được định nghĩa trong Sql trước đó ở Đoạn mã 10-9 được tái cấu trúc thành một lớp dẫn xuất riêng của Sql. Lưu ý các phương thức riêng tư như valuesList được chuyển trực tiếp đến nơi cần dùng. Hành vi riêng tư dùng chung được tách vào hai lớp tiện ích là Where và ColumnList.

**Đoạn mã 10-10**  
**Một tập hợp các lớp khép kín**

```java
abstract public class Sql {
   public Sql(String table, Column[] columns)
   abstract public String generate();
}

public class CreateSql extends Sql {
   public CreateSql(String table, Column[] columns)
   @Override public String generate()
}
public class SelectSql extends Sql {
   public SelectSql(String table, Column[] columns)
   @Override public String generate()
}
public class InsertSql extends Sql {
   public InsertSql(String table, Column[] columns, Object[] fields)
   @Override public String generate()
   private String valuesList(Object[] fields, final Column[] columns)
}

public class SelectWithCriteriaSql extends Sql {
   public SelectWithCriteriaSql(
      String table, Column[] columns, Criteria criteria)
   @Override public String generate()
}

public class SelectWithMatchSql extends Sql {
   public SelectWithMatchSql(
      String table, Column[] columns, Column column, String pattern)
   @Override public String generate()
}

public class FindByKeySql extends Sql
   public FindByKeySql(
      String table, Column[] columns, String keyColumn, String keyValue)
   @Override public String generate()
}

public class PreparedInsertSql extends Sql {
   public PreparedInsertSql(String table, Column[] columns)
   @Override public String generate() {
   private String placeholderList(Column[] columns)
}

public class Where {
   public Where(String criteria)
   public String generate()
}
```

**Đoạn mã 10-10 (tiếp)**  
**Một tập hợp các lớp khép kín**

```java
public class ColumnList {
   public ColumnList(Column[] columns)
   public String generate()
}
```

Mã trong mỗi lớp trở nên đơn giản đến mức không thể hơn. Thời gian cần thiết để hiểu bất kỳ lớp nào giảm xuống gần như bằng không. Rủi ro một hàm làm hỏng hàm khác nhỏ đến mức không đáng kể. Xét từ góc độ kiểm thử, việc chứng minh mọi phần logic trong giải pháp này đều đúng cũng dễ hơn, vì các lớp tách biệt với nhau.

Điều cũng quan trọng không kém là khi cần thêm các câu lệnh update, không lớp hiện có nào phải thay đổi! Chúng ta viết logic tạo câu lệnh update trong một lớp con mới của Sql tên là UpdateSql. Không đoạn mã nào khác trong hệ thống bị hỏng vì thay đổi này.

Logic Sql được tái cấu trúc của chúng ta đại diện cho giải pháp tốt nhất ở mọi phương diện. Nó tuân theo SRP. Nó cũng tuân theo một nguyên tắc thiết kế lớp hướng đối tượng quan trọng khác, gọi là Nguyên tắc Mở-Đóng, hay OCP:⁴ lớp nên mở để mở rộng nhưng đóng với sửa đổi. Lớp Sql sau tái cấu trúc mở để cho phép bổ sung chức năng mới qua kế thừa, nhưng ta có thể thực hiện thay đổi này mà vẫn giữ mọi lớp khác đóng. Chỉ cần đưa lớp UpdateSql vào.

Chúng ta muốn cấu trúc hệ thống sao cho phải động đến ít thứ nhất có thể khi cập nhật tính năng mới hoặc thay đổi tính năng hiện có. Trong một hệ thống lý tưởng, chúng ta bổ sung tính năng bằng cách mở rộng hệ thống, không phải bằng cách sửa đổi mã hiện có.

### Cách ly khỏi thay đổi
Nhu cầu sẽ thay đổi, vì thế mã cũng sẽ thay đổi. Từ những bài học hướng đối tượng cơ bản, chúng ta biết có các lớp cụ thể, chứa chi tiết cài đặt (mã), và các lớp trừu tượng, chỉ biểu diễn khái niệm. Lớp khách phụ thuộc vào chi tiết cụ thể sẽ gặp rủi ro khi những chi tiết đó thay đổi. Ta có thể đưa vào giao diện và lớp trừu tượng để giúp cách ly tác động của những chi tiết ấy.

Sự phụ thuộc vào chi tiết cụ thể gây khó khăn cho việc kiểm thử hệ thống. Nếu đang xây dựng lớp Portfolio và lớp này phụ thuộc vào API TokyoStockExchange bên ngoài để tính giá trị danh mục đầu tư, các ca kiểm thử sẽ bị ảnh hưởng bởi tính biến động của việc tra cứu ấy. Thật khó viết kiểm thử khi cứ năm phút lại nhận được một kết quả khác!

Thay vì thiết kế Portfolio phụ thuộc trực tiếp vào TokyoStockExchange, ta tạo giao diện StockExchange khai báo một phương thức duy nhất:

```java
public interface StockExchange {
   Money currentPrice(String symbol);
}
```

⁴ [PPP].

Ta thiết kế TokyoStockExchange để cài đặt giao diện này. Đồng thời, ta bảo đảm hàm khởi tạo của Portfolio nhận một tham chiếu StockExchange làm đối số:

```java
public class Portfolio {
   private StockExchange exchange;
   public Portfolio(StockExchange exchange) {
      this.exchange = exchange;
   }
   // ...
}
```

Giờ đây, kiểm thử có thể tạo một cách cài đặt StockExchange có thể kiểm thử, mô phỏng TokyoStockExchange. Cách cài đặt kiểm thử này sẽ cố định giá trị hiện tại cho mọi mã cổ phiếu được dùng trong kiểm thử. Nếu ca kiểm thử mô phỏng việc mua năm cổ phiếu Microsoft cho danh mục đầu tư, ta lập trình cách cài đặt kiểm thử để luôn trả về 100 đô la cho mỗi cổ phiếu Microsoft. Cách cài đặt kiểm thử của giao diện StockExchange chỉ còn là một tra cứu bảng đơn giản. Sau đó, ta có thể viết một kiểm thử mong đợi tổng giá trị danh mục là 500 đô la.

```java
public class PortfolioTest {
  private FixedStockExchangeStub exchange;
  private Portfolio portfolio;
    @Before
    protected void setUp() throws Exception {
      exchange = new FixedStockExchangeStub();
      exchange.fix("MSFT", 100);
      portfolio = new Portfolio(exchange);
    }

    @Test
    public void GivenFiveMSFTTotalShouldBe500() throws Exception {
      portfolio.add(5, "MSFT");
      Assert.assertEquals(500, portfolio.value());
    }
}
```

Nếu một hệ thống được tách rời đủ tốt để kiểm thử theo cách này, nó cũng sẽ linh hoạt hơn và khuyến khích tái sử dụng. Thiếu sự phụ thuộc có nghĩa là các thành phần của hệ thống được cách ly với nhau và với những thay đổi tốt hơn. Sự cách ly này giúp hiểu từng thành phần của hệ thống dễ hơn.

Bằng cách giảm thiểu sự phụ thuộc theo cách này, các lớp của chúng ta tuân theo một nguyên tắc thiết kế lớp khác gọi là Nguyên tắc Đảo ngược Phụ thuộc (Dependency Inversion Principle, DIP).⁵ Về bản chất, DIP nói rằng các lớp nên phụ thuộc vào trừu tượng, không phải chi tiết cụ thể.

Thay vì phụ thuộc vào chi tiết cài đặt của lớp TokyoStockExchange, lớp Portfolio giờ đây phụ thuộc vào giao diện StockExchange. Giao diện StockExchange biểu diễn khái niệm trừu tượng về việc yêu cầu giá hiện tại của một mã cổ phiếu. Sự trừu tượng này cách ly mọi chi tiết cụ thể của việc lấy giá, bao gồm cả nguồn cung cấp giá đó.

⁵ [PPP].

## Tài liệu tham khảo
[RDD]: Object Design: Roles, Responsibilities, and Collaborations, Rebecca Wirfs-Brock et al., Addison-Wesley, 2002.

[PPP]: Agile Software Development: Principles, Patterns, and Practices, Robert C. Martin, Prentice Hall, 2002.

[Knuth92]: Literate Programming, Donald E. Knuth, Center for the Study of language and Information, Leland Stanford Junior University, 1992.
