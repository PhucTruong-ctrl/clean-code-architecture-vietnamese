# Chương 5: Định dạng

Khi người ta nhìn vào bên trong, chúng ta muốn họ ấn tượng với sự gọn gàng, nhất quán và chăm chút đến từng chi tiết mà họ nhìn thấy. Chúng ta muốn họ sững sờ vì trật tự ngăn nắp. Chúng ta muốn họ nhướng mày khi cuộn qua các module. Chúng ta muốn họ cảm nhận rằng những người chuyên nghiệp đã làm việc ở đây. Còn nếu thay vào đó họ thấy một mớ mã lộn xộn như thể được viết bởi một lũ thủy thủ say rượu, họ sẽ kết luận rằng sự cẩu thả ấy cũng lan ra mọi khía cạnh khác của dự án.

Bạn nên chăm chút để mã của mình được định dạng đẹp. Bạn nên chọn một bộ quy tắc đơn giản chi phối định dạng mã, rồi áp dụng chúng một cách nhất quán. Nếu làm việc trong một nhóm, cả nhóm nên thống nhất một bộ quy tắc định dạng duy nhất và mọi thành viên đều tuân theo. Có một công cụ tự động áp dụng những quy tắc đó cho bạn sẽ rất hữu ích.

## Mục đích của định dạng

Trước hết, hãy nói cho rõ. Định dạng mã là chuyện quan trọng. Nó quan trọng đến mức không thể bỏ qua, và cũng quan trọng đến mức không nên đối xử với nó như một tôn giáo. Định dạng mã là chuyện giao tiếp, mà giao tiếp là ưu tiên hàng đầu trong công việc của một nhà phát triển chuyên nghiệp.

Có lẽ bạn từng nghĩ rằng “làm cho nó chạy được” mới là ưu tiên hàng đầu của một nhà phát triển chuyên nghiệp. Tôi hy vọng đến giờ cuốn sách này đã giúp bạn từ bỏ ý nghĩ đó. Chức năng bạn viết hôm nay rất có thể sẽ thay đổi trong bản phát hành tới, nhưng khả năng đọc của mã sẽ ảnh hưởng sâu sắc đến mọi thay đổi về sau. Phong cách lập trình và khả năng đọc tạo ra những tiền lệ còn tiếp tục ảnh hưởng đến khả năng bảo trì và khả năng mở rộng rất lâu sau khi mã gốc đã bị sửa đến mức không còn nhận ra. Phong cách và kỷ luật của bạn còn lại, dù mã của bạn thì không.

Vậy những vấn đề định dạng nào giúp chúng ta giao tiếp tốt nhất?

## Định dạng theo chiều dọc

Bắt đầu với kích thước theo chiều dọc. Một tệp nguồn nên lớn đến mức nào? Trong Java, kích thước tệp gắn chặt với kích thước lớp. Chúng ta sẽ bàn về kích thước lớp khi bàn về lớp. Còn lúc này, hãy chỉ xét kích thước tệp.

Hầu hết tệp nguồn Java lớn cỡ nào? Hóa ra kích thước trải rất rộng, và phong cách cũng khác nhau đáng kể. Hình 5-1 cho thấy một vài khác biệt đó.

Hình vẽ mô tả bảy dự án khác nhau: Junit, FitNesse, testNG, Time and Money, JDepend, Ant và Tomcat. Các đường thẳng đứng xuyên qua mỗi hộp cho biết độ dài tệp nhỏ nhất và lớn nhất trong dự án. Chiếc hộp thể hiện khoảng một phần ba số tệp (một độ lệch chuẩn[^1]). Điểm giữa của hộp là giá trị trung bình. Như vậy, kích thước tệp trung bình trong dự án FitNesse vào khoảng 65 dòng, và khoảng một phần ba số tệp nằm trong khoảng 40 đến hơn 100 dòng. Tệp lớn nhất của FitNesse dài khoảng 400 dòng, tệp nhỏ nhất 6 dòng. Lưu ý đây là thang log, nên chênh lệch nhỏ về vị trí theo chiều dọc ứng với chênh lệch rất lớn về kích thước tuyệt đối.

**Hình 5-1**
**Phân bố độ dài tệp theo thang LOG (chiều cao hộp = sigma)**

Junit, FitNesse và Time and Money được tạo nên từ những tệp tương đối nhỏ. Không tệp nào vượt quá 500 dòng và phần lớn dưới 200 dòng. Ngược lại, Tomcat và Ant có những tệp dài hàng nghìn dòng, gần một nửa trong số đó vượt 200 dòng.

Điều đó nói lên gì? Có vẻ vẫn có thể xây những hệ thống đáng kể (FitNesse gần 50.000 dòng) từ những tệp thường dài 200 dòng, với giới hạn trên là 500. Đây không nên là quy tắc cứng nhắc, nhưng là điều rất đáng mong muốn. Tệp nhỏ thường dễ hiểu hơn tệp lớn.

### Ẩn dụ tờ báo

Hãy nghĩ đến một bài báo được viết tốt. Bạn đọc nó từ trên xuống. Ở đầu bài, bạn chờ đợi một dòng tít cho biết câu chuyện nói về điều gì, giúp bạn quyết định có muốn đọc hay không. Đoạn đầu tiên tóm tắt toàn bộ câu chuyện, giấu đi mọi chi tiết và chỉ đưa ra những khái niệm khái quát. Càng xuống dưới, chi tiết càng nhiều, cho đến khi bạn có đủ ngày tháng, tên người, trích dẫn, tuyên bố và những chi tiết vụn vặt khác.

Chúng ta muốn tệp nguồn giống như một bài báo. Cái tên phải đơn giản nhưng có tính giải thích. Chỉ riêng cái tên đã đủ cho biết ta đang ở đúng module hay không. Phần trên cùng của tệp nguồn nên trình bày những khái niệm và thuật toán mức cao. Càng xuống dưới, chi tiết càng tăng, cho đến cuối tệp là những hàm và chi tiết mức thấp nhất.

Một tờ báo gồm nhiều bài; phần lớn rất ngắn. Một số bài dài hơn chút. Rất ít bài chứa đủ chữ cho cả một trang. Chính điều đó làm tờ báo dễ dùng. Nếu tờ báo chỉ là một câu chuyện dài gồm một mớ lộn xộn các sự kiện, ngày tháng và tên riêng, hẳn chúng ta sẽ chẳng buồn đọc.

### Độ thoáng dọc giữa các khái niệm

Gần như mọi đoạn mã đều được đọc từ trái sang phải, từ trên xuống dưới. Mỗi dòng là một biểu thức hoặc một mệnh đề, mỗi nhóm dòng là một ý trọn vẹn. Các ý đó nên được ngăn cách bằng dòng trống.

Xét Đoạn mã 5-1. Những dòng trống ngăn cách khai báo package, các câu lệnh import và từng hàm. Quy tắc cực kỳ đơn giản này có ảnh hưởng sâu sắc đến bố cục thị giác của mã. Mỗi dòng trống là một tín hiệu thị giác đánh dấu một khái niệm mới, tách biệt. Khi lướt xuống đoạn mã, mắt bạn bị hút về dòng đầu tiên sau mỗi dòng trống.

**Đoạn mã 5-1**
**BoldWidget.java**

```java
package fitnesse.wikitext.widgets;

import java.util.regex.*;

public class BoldWidget extends ParentWidget {
  public static final String REGEXP = "'''.+?'''";
  private static final Pattern pattern = Pattern.compile("'''(.+?)'''",
    Pattern.MULTILINE + Pattern.DOTALL
  );

  public BoldWidget(ParentWidget parent, String text) throws Exception {
    super(parent);
    Matcher match = pattern.matcher(text);
    match.find();
    addChildWidgets(match.group(1));
  }

  public String render() throws Exception {
    StringBuffer html = new StringBuffer("<b>");
    html.append(childHtml()).append("</b>");
    return html.toString();
  }
}
```

Bỏ những dòng trống đó đi, như trong Đoạn mã 5-2, lại có tác dụng che khuất khả năng đọc của mã một cách đáng kinh ngạc.

**Đoạn mã 5-2**
**BoldWidget.java**

```java
package fitnesse.wikitext.widgets;
import java.util.regex.*;
public class BoldWidget extends ParentWidget {
  public static final String REGEXP = "'''.+?'''";
  private static final Pattern pattern = Pattern.compile("'''(.+?)'''",
    Pattern.MULTILINE + Pattern.DOTALL);
  public BoldWidget(ParentWidget parent, String text) throws Exception {
    super(parent);
    Matcher match = pattern.matcher(text);
    match.find();
    addChildWidgets(match.group(1));}
  public String render() throws Exception {
    StringBuffer html = new StringBuffer("<b>");
    html.append(childHtml()).append("</b>");
    return html.toString();
  }
}
```

Hiệu ứng này còn rõ hơn khi bạn làm mờ mắt đi. Ở ví dụ thứ nhất, những nhóm dòng khác nhau nổi bật lên; còn ví dụ thứ hai trông như một mớ lẫn lộn. Khác biệt giữa hai đoạn mã chỉ là một chút độ thoáng theo chiều dọc.

### Độ đặc theo chiều dọc

Nếu độ thoáng phân tách các khái niệm thì độ đặc theo chiều dọc ngụ ý sự gắn bó chặt chẽ. Vì thế những dòng mã liên quan chặt với nhau nên xuất hiện sát nhau theo chiều dọc. Hãy để ý những chú thích vô ích trong Đoạn mã 5-3 đã phá vỡ sự gắn bó giữa hai biến thực thể như thế nào.

**Đoạn mã 5-3**

```java
public class ReporterConfig {

  /**
   * Tên lớp của reporter listener
   */
  private String m_className;

  /**
   * Các thuộc tính của reporter listener
   */
  private List<Property> m_properties = new ArrayList<Property>();

  public void addProperty(Property property) {
    m_properties.add(property);
  }
```

Đoạn mã 5-4 dễ đọc hơn nhiều. Nó vừa một “tầm mắt”, ít nhất là với tôi. Tôi có thể nhìn vào và thấy ngay đây là một lớp có hai biến và một phương thức, mà không phải xoay đầu hay đảo mắt nhiều. Đoạn mã trước buộc tôi phải cử động mắt và đầu nhiều hơn hẳn mới hiểu được ngang ấy.

**Đoạn mã 5-4**

```java
public class ReporterConfig {
  private String m_className;
  private List<Property> m_properties = new ArrayList<Property>();

  public void addProperty(Property property) {
    m_properties.add(property);
  }
```

### Khoảng cách dọc

Bạn đã bao giờ quanh quẩn trong một lớp, nhảy từ hàm này sang hàm kia, cuộn lên cuộn xuống tệp nguồn, cố đoán xem các hàm liên hệ và vận hành ra sao, rồi cuối cùng lạc trong một mớ rối ren? Bạn đã bao giờ lần ngược chuỗi kế thừa để tìm định nghĩa của một biến hay một hàm? Điều đó thật bực bội, vì bạn đang cố hiểu hệ thống làm gì, nhưng lại tiêu tốn thời gian và sức lực tinh thần vào việc tìm và nhớ xem các mảnh nằm ở đâu.

Những khái niệm liên quan chặt chẽ nên được đặt gần nhau theo chiều dọc [G10]. Rõ ràng quy tắc này không áp dụng cho những khái niệm thuộc về các tệp khác nhau. Nhưng khi ấy, những khái niệm liên quan chặt chẽ cũng không nên bị tách sang các tệp khác nhau, trừ khi bạn có lý do rất chính đáng. Đây cũng là một trong những lý do nên tránh biến protected.

Với những khái niệm liên quan chặt đến mức cùng thuộc một tệp nguồn, khoảng cách dọc giữa chúng nên phản ánh mức độ quan trọng của khái niệm này đối với việc hiểu khái niệm kia. Chúng ta muốn tránh buộc người đọc phải nhảy nhót qua các tệp nguồn và các lớp.

#### Khai báo biến

Biến nên được khai báo càng gần nơi sử dụng càng tốt. Vì các hàm của chúng ta rất ngắn, biến cục bộ nên xuất hiện ở đầu mỗi hàm, như trong hàm hơi dài này từ Junit4.3.1.

```java
private static void readPreferences() {
  InputStream is= null;
  try {
    is= new FileInputStream(getPreferencesFile());
    setPreferences(new Properties(getPreferences()));
    getPreferences().load(is);
  } catch (IOException e) {
    try {
      if (is != null)
        is.close();
    } catch (IOException e1) {
    }
  }
}
```

Biến điều khiển của vòng lặp thường nên được khai báo ngay trong câu lệnh lặp, như trong hàm nhỏ xinh này cũng từ nguồn đó.

```java
public int countTestCases() {
  int count= 0;
  for (Test each : tests)
    count += each.countTestCases();
  return count;
}
```

Trong vài trường hợp hiếm, biến có thể được khai báo ở đầu một khối hoặc ngay trước một vòng lặp trong một hàm khá dài. Bạn có thể thấy một biến như vậy trong đoạn trích giữa một hàm rất dài của TestNG.

```java
...
for (XmlTest test : m_suite.getTests()) {
  TestRunner tr = m_runnerFactory.newTestRunner(this, test);
  tr.addListener(m_textReporter);
  m_testRunners.add(tr);

  invoker = tr.getInvoker();

  for (ITestNGMethod m : tr.getBeforeSuiteMethods()) {
    beforeSuiteMethods.put(m.getMethod(), m);
  }
  for (ITestNGMethod m : tr.getAfterSuiteMethods()) {
    afterSuiteMethods.put(m.getMethod(), m);
  }
}
...
```

Ngược lại, biến thực thể nên được khai báo ở đầu lớp. Điều này không làm tăng khoảng cách dọc của những biến ấy, vì trong một lớp được thiết kế tốt, chúng được nhiều phương thức của lớp dùng đến, nếu không nói là tất cả.

Đã có nhiều tranh luận về chỗ đặt biến thực thể. Trong C++, chúng tôi thường áp dụng cái gọi là quy tắc cái kéo, đặt toàn bộ biến thực thể xuống cuối. Tuy vậy, quy ước phổ biến trong Java là đặt tất cả ở đầu lớp. Tôi không thấy lý do gì để theo một quy ước khác. Điều quan trọng là biến thực thể phải được khai báo ở một chỗ ai cũng biết. Mọi người đều phải biết đi đâu để xem các khai báo.

Xét trường hợp kỳ lạ của lớp TestSuite trong JUnit 4.3.1. Tôi đã lược bớt rất nhiều trong lớp này để làm rõ ý. Nếu nhìn khoảng giữa đoạn mã, bạn sẽ thấy hai biến thực thể được khai báo ở đó. Khó mà giấu chúng ở một chỗ tốt hơn. Người đọc mã này chỉ có thể tình cờ vấp phải các khai báo ấy (như tôi đã từng).

```java
public class TestSuite implements Test {
  static public Test createTest(Class<? extends TestCase> theClass,
                                String name) {
    ...
  }

  public static Constructor<? extends TestCase>
  getTestConstructor(Class<? extends TestCase> theClass)
  throws NoSuchMethodException {
    ...
  }

  public static Test warning(final String message) {
    ...
  }

  private static String exceptionToString(Throwable t) {
    ...
  }
  private String fName;

  private Vector<Test> fTests= new Vector<Test>(10);

  public TestSuite() {
  }

  public TestSuite(final Class<? extends TestCase> theClass) {
    ...
  }

  public TestSuite(Class<? extends TestCase> theClass, String name) {
    ...
  }
  ... ... ... ... ...
}
```

#### Các hàm phụ thuộc

Nếu một hàm gọi hàm khác, hai hàm nên ở gần nhau theo chiều dọc, và nếu có thể thì hàm gọi nằm trên hàm được gọi. Điều này cho chương trình một dòng chảy tự nhiên. Nếu quy ước được tuân thủ đáng tin cậy, người đọc có thể yên tâm rằng định nghĩa của hàm sẽ xuất hiện ngay sau chỗ nó được dùng. Xét đoạn trích từ FitNesse trong Đoạn mã 5-5. Hãy để ý hàm trên cùng gọi những hàm bên dưới nó, và những hàm đó lại gọi những hàm dưới chúng. Điều này giúp dễ tìm các hàm được gọi và làm tăng mạnh khả năng đọc của cả module.

**Đoạn mã 5-5**
**WikiPageResponder.java**

```java
public class WikiPageResponder implements SecureResponder {
  protected WikiPage page;
  protected PageData pageData;
  protected String pageTitle;
  protected Request request;
  protected PageCrawler crawler;

  public Response makeResponse(FitNesseContext context, Request request)
    throws Exception {
    String pageName = getPageNameOrDefault(request, "FrontPage");
```

**Đoạn mã 5-5 (tiếp theo)**
**WikiPageResponder.java**

```java
    loadPage(pageName, context);
    if (page == null)
      return notFoundResponse(context, request);
    else
      return makePageResponse(context);
  }

  private String getPageNameOrDefault(Request request, String defaultPageName)
  {
    String pageName = request.getResource();
    if (StringUtil.isBlank(pageName))
      pageName = defaultPageName;

    return pageName;
  }

  protected void loadPage(String resource, FitNesseContext context)
    throws Exception {
    WikiPagePath path = PathParser.parse(resource);
    crawler = context.root.getPageCrawler();
    crawler.setDeadEndStrategy(new VirtualEnabledPageCrawler());
    page = crawler.getPage(context.root, path);
    if (page != null)
      pageData = page.getData();
  }

  private Response notFoundResponse(FitNesseContext context, Request request)
    throws Exception {
    return new NotFoundResponder().makeResponse(context, request);
  }

  private SimpleResponse makePageResponse(FitNesseContext context)
    throws Exception {
    pageTitle = PathParser.render(crawler.getFullPath(page));
    String html = makeHtml(context);

    SimpleResponse response = new SimpleResponse();
    response.setMaxAge(0);
    response.setContent(html);
    return response;
  }
...
```

Nhân đây, đoạn trích này là một ví dụ hay về việc giữ hằng ở đúng mức [G35]. Hằng "FrontPage" lẽ ra có thể bị chôn trong hàm getPageNameOrDefault, nhưng làm vậy sẽ giấu một hằng ai cũng biết và ai cũng chờ đợi vào một hàm có mức thấp không thích hợp. Tốt hơn là truyền hằng đó từ nơi hợp lý để biết nó xuống nơi thực sự dùng nó.

#### Gần gũi về khái niệm

Một số đoạn mã muốn ở gần những đoạn khác. Giữa chúng có một sự gần gũi nhất định về khái niệm. Sự gần gũi càng mạnh thì khoảng cách dọc giữa chúng càng nên nhỏ.

Như đã thấy, sự gần gũi này có thể dựa trên phụ thuộc trực tiếp, chẳng hạn hàm này gọi hàm kia, hoặc một hàm dùng một biến. Nhưng còn những nguyên nhân khác. Sự gần gũi cũng có thể đến từ việc một nhóm hàm cùng thực hiện một thao tác tương tự. Xét đoạn mã sau từ Junit 4.3.1:

```java
public class Assert {
  static public void assertTrue(String message, boolean condition) {
    if (!condition)
      fail(message);
  }

  static public void assertTrue(boolean condition) {
    assertTrue(null, condition);
  }

  static public void assertFalse(String message, boolean condition) {
    assertTrue(message, !condition);
  }

  static public void assertFalse(boolean condition) {
    assertFalse(null, condition);
  }
...
```

Những hàm này có sự gần gũi mạnh về khái niệm vì chúng dùng chung một cách đặt tên và thực hiện những biến thể của cùng một nhiệm vụ cơ bản. Việc chúng gọi nhau chỉ là chuyện phụ. Kể cả khi không gọi nhau, chúng vẫn muốn ở gần nhau.

![Khoảng cách dọc](assets/illustrations/05-vertical-distance.png){w=139}

### Thứ tự dọc

Nói chung, chúng ta muốn các phụ thuộc gọi hàm hướng xuống dưới. Nghĩa là hàm được gọi nên nằm dưới hàm gọi nó[^2]. Điều này tạo ra một dòng chảy đẹp từ mức cao xuống mức thấp trong module mã nguồn.

Như trong các bài báo, chúng ta chờ đợi những khái niệm quan trọng nhất xuất hiện trước, và được diễn đạt với ít chi tiết gây nhiễu nhất. Chúng ta chờ đợi những chi tiết mức thấp xuất hiện sau cùng. Nhờ vậy, ta có thể lướt qua tệp nguồn, nắm được ý chính từ vài hàm đầu mà không phải đắm mình vào chi tiết. Đoạn mã 5-5 được tổ chức theo cách này. Có lẽ còn những ví dụ hay hơn ở Đoạn mã 15-5 trang 263 và Đoạn mã 3-7 trang 50.

## Định dạng theo chiều ngang

Một dòng nên rộng bao nhiêu? Để trả lời, hãy xem các dòng trong những chương trình điển hình rộng ra sao. Một lần nữa, ta xét bảy dự án. Hình 5-2 cho thấy phân bố độ dài dòng của cả bảy dự án. Sự đều đặn thật ấn tượng, nhất là quanh mốc 45 ký tự. Thật vậy, mỗi độ dài từ 20 đến 60 chiếm khoảng 1 phần trăm tổng số dòng. Cộng lại là 40 phần trăm! Có lẽ khoảng 30 phần trăm nữa có độ rộng dưới 10 ký tự. Nhớ rằng đây là thang log, nên đoạn sụt giảm trông có vẻ tuyến tính sau mốc 80 ký tự thực ra rất đáng kể. Lập trình viên rõ ràng thích dòng ngắn.

**Hình 5-2**
**Phân bố độ rộng dòng trong Java**

Điều này gợi ý rằng ta nên cố giữ dòng ngắn. Giới hạn 80 cột kiểu Hollerith ngày xưa hơi tùy tiện, và tôi không phản đối việc dòng dài tới 100, thậm chí 120 ký tự. Nhưng vượt xa hơn thì có lẽ chỉ là cẩu thả.

Tôi từng theo quy tắc rằng không bao giờ phải cuộn sang phải. Nhưng màn hình ngày nay quá rộng cho quy tắc đó, và các lập trình viên trẻ có thể thu nhỏ phông chữ đến mức nhét được 200 ký tự lên màn hình. Đừng làm vậy. Cá nhân tôi đặt giới hạn ở 120.

### Độ thoáng và độ đặc theo chiều ngang

Chúng ta dùng khoảng trắng theo chiều ngang để liên kết những thứ liên quan chặt và tách rời những thứ ít liên quan hơn. Xét hàm sau:

```java
private void measureLine(String line) {
  lineCount++;
  int lineSize = line.length();
  totalChars += lineSize;
  lineWidthHistogram.addLine(lineSize, lineCount);
  recordWidestLine(lineSize);
}
```

Tôi đặt khoảng trắng quanh các toán tử gán để làm chúng nổi bật. Câu lệnh gán có hai thành phần chính, tách biệt: vế trái và vế phải. Khoảng trắng làm rõ sự tách biệt đó.

Ngược lại, tôi không đặt khoảng trắng giữa tên hàm và dấu ngoặc mở. Lý do là hàm và các đối số của nó gắn bó chặt với nhau. Tách chúng ra sẽ khiến chúng trông rời rạc thay vì liền một khối. Tôi tách các đối số bên trong ngoặc bằng khoảng trắng để làm nổi bật dấu phẩy và cho thấy các đối số tách biệt nhau.

Một cách dùng khác của khoảng trắng là làm nổi bật độ ưu tiên của toán tử.

```java
public class Quadratic {
  public static double root1(double a, double b, double c) {
    double determinant = determinant(a, b, c);
    return (-b + Math.sqrt(determinant)) / (2*a);
  }

  public static double root2(int a, int b, int c) {
    double determinant = determinant(a, b, c);
    return (-b - Math.sqrt(determinant)) / (2*a);
  }

  private static double determinant(double a, double b, double c) {
    return b*b - 4*a*c;
  }
}
```

Hãy để ý các phương trình đọc trôi chảy đến mức nào. Các thừa số không có khoảng trắng giữa chúng vì chúng có độ ưu tiên cao. Các số hạng được ngăn bằng khoảng trắng vì phép cộng và phép trừ có độ ưu tiên thấp hơn.

Đáng tiếc, phần lớn công cụ định dạng lại mã không nhận biết độ ưu tiên của toán tử và áp đặt một kiểu khoảng cách như nhau ở mọi chỗ. Vì thế những khoảng cách tinh tế như trên dễ bị mất đi sau khi bạn định dạng lại mã.

### Căn lề ngang

Hồi còn viết hợp ngữ[^3], tôi dùng căn lề ngang để làm nổi bật một số cấu trúc. Khi chuyển sang viết C, rồi C++, và cuối cùng là Java, tôi vẫn tiếp tục cố xếp thẳng tên các biến trong một nhóm khai báo, hoặc xếp thẳng các giá trị bên phải trong một loạt câu lệnh gán. Mã của tôi khi đó có lẽ trông như thế này:

```java
public class FitNesseExpediter implements ResponseSender
{
  private Socket            socket;
  private InputStream       input;
  private OutputStream      output;
  private Request           request;
  private Response          response;
  private FitNesseContext   context;
  protected long            requestParsingTimeLimit;
  private long              requestProgress;
  private long              requestParsingDeadline;
  private boolean           hasError;

  public FitNesseExpediter(Socket          s,
                            FitNesseContext context) throws Exception
  {
    this.context =          context;
    socket =                s;
    input =                 s.getInputStream();
    output =                s.getOutputStream();
    requestParsingTimeLimit = 10000;
  }
```

Nhưng tôi nhận ra kiểu căn lề này không hữu ích. Việc căn lề dường như nhấn mạnh sai thứ và kéo mắt tôi rời khỏi ý định thật. Chẳng hạn, trong danh sách khai báo trên, bạn dễ bị cám dỗ đọc thẳng xuống danh sách tên biến mà không nhìn kiểu của chúng. Tương tự, trong danh sách câu lệnh gán, bạn dễ bị cám dỗ nhìn thẳng xuống danh sách giá trị bên phải mà không hề thấy toán tử gán. Tệ hơn, các công cụ định dạng tự động thường xóa bỏ kiểu căn lề này.

Vậy nên cuối cùng, tôi không làm kiểu đó nữa. Ngày nay tôi thích những khai báo và phép gán không căn lề, như dưới đây, vì chúng chỉ ra một khiếm khuyết quan trọng. Nếu tôi có những danh sách dài cần căn lề, vấn đề nằm ở độ dài của danh sách chứ không phải ở việc thiếu căn lề. Độ dài danh sách khai báo trong FitNesseExpediter dưới đây cho thấy lớp này nên được tách ra.

```java
public class FitNesseExpediter implements ResponseSender
{
  private Socket socket;
  private InputStream input;
  private OutputStream output;
  private Request request;
  private Response response;
  private FitNesseContext context;
  protected long requestParsingTimeLimit;
  private long requestProgress;
  private long requestParsingDeadline;
  private boolean hasError;

  public FitNesseExpediter(Socket s, FitNesseContext context) throws Exception
  {
    this.context = context;
    socket = s;
    input = s.getInputStream();
    output = s.getOutputStream();
    requestParsingTimeLimit = 10000;
  }
```

### Thụt lề

Một tệp nguồn là một hệ thứ bậc, gần giống một dàn ý. Có thông tin liên quan đến toàn bộ tệp, đến từng lớp trong tệp, đến các phương thức trong lớp, đến các khối trong phương thức, và đệ quy đến các khối trong khối. Mỗi mức của hệ thứ bậc này là một phạm vi, nơi có thể khai báo tên và nơi các khai báo cùng câu lệnh thực thi được diễn giải.

Để hệ thứ bậc các phạm vi này hiện ra trước mắt, ta thụt lề các dòng mã nguồn tương ứng với vị trí của chúng trong hệ thứ bậc. Những câu lệnh ở mức tệp, như phần lớn khai báo lớp, không thụt lề. Các phương thức trong một lớp thụt vào một mức so với lớp. Phần thân của những phương thức đó thụt vào một mức so với khai báo phương thức. Phần thân của các khối thụt vào một mức so với khối chứa chúng, và cứ thế.

Lập trình viên dựa rất nhiều vào cách thụt lề này. Họ nhìn theo mép trái để biết một dòng thuộc phạm vi nào. Nhờ đó họ có thể nhanh chóng nhảy qua những phạm vi không liên quan đến việc đang làm, chẳng hạn phần thân của câu lệnh if hay while. Họ quét mép trái để tìm khai báo phương thức mới, biến mới, thậm chí lớp mới. Không có thụt lề, con người gần như không thể đọc nổi chương trình.

Xét hai chương trình sau, giống hệt nhau về cú pháp và ngữ nghĩa:

```java
public class FitNesseServer implements SocketServer { private FitNesseContext
context; public FitNesseServer(FitNesseContext context) { this.context =
context; } public void serve(Socket s) { serve(s, 10000); } public void
serve(Socket s, long requestTimeout) { try { FitNesseExpediter sender = new
FitNesseExpediter(s, context);
sender.setRequestParsingTimeLimit(requestTimeout); sender.start(); }
catch(Exception e) { e.printStackTrace(); } } }

-----

public class FitNesseServer implements SocketServer {
  private FitNesseContext context;

  public FitNesseServer(FitNesseContext context) {
    this.context = context;
  }

  public void serve(Socket s) {
    serve(s, 10000);
  }
  public void serve(Socket s, long requestTimeout) {
    try {
      FitNesseExpediter sender = new FitNesseExpediter(s, context);
      sender.setRequestParsingTimeLimit(requestTimeout);
      sender.start();
    }
    catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

Mắt bạn nhanh chóng nhận ra cấu trúc của tệp được thụt lề. Gần như ngay lập tức bạn thấy các biến, hàm khởi tạo, hàm truy cập và phương thức. Chỉ mất vài giây để nhận ra đây là một kiểu giao diện đơn giản cho socket, có cơ chế hết giờ. Còn phiên bản không thụt lề gần như không thể xuyên qua nếu không nghiên cứu kỹ.

#### Phá vỡ thụt lề

Đôi khi ta bị cám dỗ phá vỡ quy tắc thụt lề với những câu lệnh if ngắn, vòng lặp while ngắn hoặc hàm ngắn. Mỗi lần chiều theo cám dỗ ấy, tôi gần như luôn quay lại thêm thụt lề vào. Vì vậy tôi tránh thu gọn các phạm vi về một dòng như thế này:

```java
public class CommentWidget extends TextWidget
{
  public static final String REGEXP = "^#[^\r\n]*(?:(?:\r\n)|\n|\r)?";
  public CommentWidget(ParentWidget parent, String text){super(parent, text);}
  public String render() throws Exception {return ""; }
}
```

Thay vào đó, tôi thích mở rộng và thụt lề các phạm vi, như thế này:

```java
public class CommentWidget extends TextWidget {
  public static final String REGEXP = "^#[^\r\n]*(?:(?:\r\n)|\n|\r)?";

  public CommentWidget(ParentWidget parent, String text) {
    super(parent, text);
  }

  public String render() throws Exception {
    return "";
  }
}
```

### Thân rỗng

Đôi khi phần thân của câu lệnh while hoặc for là một thân rỗng, như dưới đây. Tôi không thích kiểu cấu trúc này và cố tránh chúng. Khi không tránh được, tôi bảo đảm thân rỗng được thụt lề đúng và bao trong ngoặc nhọn. Không thể kể hết số lần tôi bị lừa bởi một dấu chấm phẩy nằm im lìm ở cuối vòng lặp while, cùng dòng. Trừ khi bạn làm cho dấu chấm phẩy ấy hiện ra bằng cách thụt nó vào một dòng riêng, nó quá khó thấy.

```java
while (dis.read(buf, 0, readBufferSize) != -1)
  ;
```

## Luật chơi của nhóm

![Luật chơi của nhóm](assets/illustrations/05-team-rules.png){w=177}

Mỗi lập trình viên có quy tắc định dạng mình thích. Nhưng khi làm việc trong nhóm thì phải theo luật chơi chung.

Một nhóm phát triển nên thống nhất một phong cách định dạng duy nhất, rồi mọi thành viên trong nhóm đều dùng phong cách đó. Chúng ta muốn phần mềm có một phong cách nhất quán. Chúng ta không muốn nó trông như được viết bởi một đám người mỗi người một ý.

Khi bắt đầu dự án FitNesse năm 2002, tôi ngồi lại với nhóm để bàn ra một phong cách lập trình. Việc đó mất khoảng 10 phút. Chúng tôi quyết định đặt ngoặc nhọn ở đâu, thụt lề mấy dấu cách, đặt tên lớp, biến và phương thức ra sao, vân vân. Rồi chúng tôi mã hóa những quy tắc ấy vào công cụ định dạng mã của IDE và giữ nguyên từ đó đến nay. Đó không phải những quy tắc tôi thích; đó là quy tắc do nhóm quyết định. Là một thành viên của nhóm, tôi tuân theo chúng khi viết mã trong dự án FitNesse.

Hãy nhớ, một hệ thống phần mềm tốt được tạo nên từ những tài liệu đọc trôi chảy. Chúng cần có một phong cách nhất quán và mượt mà. Người đọc cần có thể tin rằng những động tác định dạng đã thấy ở tệp nguồn này sẽ mang cùng ý nghĩa ở những tệp khác. Điều cuối cùng chúng ta muốn là làm tăng thêm độ phức tạp cho mã nguồn bằng cách viết nó trong một mớ phong cách cá nhân khác nhau.

## Quy tắc định dạng của Uncle Bob

Những quy tắc cá nhân tôi dùng rất đơn giản và được minh họa bằng mã trong Đoạn mã 5-6. Hãy coi đây là một ví dụ cho thấy mã chính là tài liệu chuẩn lập trình tốt nhất.

**Đoạn mã 5-6**
**CodeAnalyzer.java**

```java
public class CodeAnalyzer implements JavaFileAnalysis {
  private int lineCount;
  private int maxLineWidth;
  private int widestLineNumber;
  private LineWidthHistogram lineWidthHistogram;
  private int totalChars;

  public CodeAnalyzer() {
    lineWidthHistogram = new LineWidthHistogram();
  }
  public static List<File> findJavaFiles(File parentDirectory) {
    List<File> files = new ArrayList<File>();
    findJavaFiles(parentDirectory, files);
    return files;
  }

  private static void findJavaFiles(File parentDirectory, List<File> files) {
    for (File file : parentDirectory.listFiles()) {
      if (file.getName().endsWith(".java"))
        files.add(file);
      else if (file.isDirectory())
        findJavaFiles(file, files);
    }
  }

  public void analyzeFile(File javaFile) throws Exception {
    BufferedReader br = new BufferedReader(new FileReader(javaFile));
    String line;
    while ((line = br.readLine()) != null)
      measureLine(line);
  }

  private void measureLine(String line) {
    lineCount++;
    int lineSize = line.length();
    totalChars += lineSize;
    lineWidthHistogram.addLine(lineSize, lineCount);
    recordWidestLine(lineSize);
  }
  private void recordWidestLine(int lineSize) {
    if (lineSize > maxLineWidth) {
      maxLineWidth = lineSize;
      widestLineNumber = lineCount;
    }
  }

  public int getLineCount() {
    return lineCount;
  }

  public int getMaxLineWidth() {
    return maxLineWidth;
  }
```

**Đoạn mã 5-6 (tiếp theo)**
**CodeAnalyzer.java**

```java
  public int getWidestLineNumber() {
    return widestLineNumber;
  }

  public LineWidthHistogram getLineWidthHistogram() {
    return lineWidthHistogram;
  }

  public double getMeanLineWidth() {
    return (double)totalChars/lineCount;
  }

  public int getMedianLineWidth() {
    Integer[] sortedWidths = getSortedWidths();
    int cumulativeLineCount = 0;
    for (int width : sortedWidths) {
      cumulativeLineCount += lineCountForWidth(width);
      if (cumulativeLineCount > lineCount/2)
        return width;
    }
    throw new Error("Cannot get here");
  }

  private int lineCountForWidth(int width) {
    return lineWidthHistogram.getLinesforWidth(width).size();
  }

  private Integer[] getSortedWidths() {
    Set<Integer> widths = lineWidthHistogram.getWidths();
    Integer[] sortedWidths = (widths.toArray(new Integer[0]));
    Arrays.sort(sortedWidths);
    return sortedWidths;
  }
}
```

[^1]: Chiếc hộp thể hiện sigma/2 ở trên và dưới giá trị trung bình. Vâng, tôi biết phân bố độ dài tệp không phải phân bố chuẩn, nên độ lệch chuẩn không chính xác về mặt toán học. Nhưng ở đây chúng ta không cố đạt độ chính xác. Chúng ta chỉ muốn có một cảm nhận.

[^2]: Điều này hoàn toàn ngược với những ngôn ngữ như Pascal, C và C++, vốn bắt buộc hàm phải được định nghĩa, hoặc ít nhất là khai báo, trước khi dùng.

[^3]: Tôi đùa ai chứ? Tôi vẫn là một lập trình viên hợp ngữ. Có thể đưa cậu bé ra khỏi kim loại, nhưng không thể đưa kim loại ra khỏi cậu bé!
