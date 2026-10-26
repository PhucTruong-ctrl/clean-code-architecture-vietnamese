# Chương 3: Hàm

Thuở sơ khai của lập trình, chúng ta dựng hệ thống từ các routine và subroutine. Rồi đến thời Fortran và PL/1, chúng ta dựng hệ thống từ program, subprogram và function. Ngày nay, trong những thứ thuở ấy chỉ còn function sống sót. Hàm là cấp tổ chức đầu tiên trong mọi chương trình. Viết hàm cho tốt là chủ đề của chương này.

Hãy xem đoạn mã trong Đoạn mã 3-1. Rất khó tìm một hàm dài trong FitNesse[^1], nhưng sau một hồi lục lọi tôi cũng vấp phải hàm này. Nó không chỉ dài mà còn có mã trùng lặp, đầy những chuỗi kỳ quặc, cùng nhiều kiểu dữ liệu và API lạ lùng, khó đoán. Bạn thử xem trong ba phút tới mình hiểu được bao nhiêu.

**Đoạn mã 3-1**
**HtmlUtil.java (FitNesse 20070619)**

```java
public static String testableHtml(
  PageData pageData,
  boolean includeSuiteSetup
) throws Exception {
  WikiPage wikiPage = pageData.getWikiPage();
  StringBuffer buffer = new StringBuffer();
  if (pageData.hasAttribute("Test")) {
    if (includeSuiteSetup) {
      WikiPage suiteSetup =
        PageCrawlerImpl.getInheritedPage(
                SuiteResponder.SUITE_SETUP_NAME, wikiPage
        );
      if (suiteSetup != null) {
        WikiPagePath pagePath =
          suiteSetup.getPageCrawler().getFullPath(suiteSetup);
        String pagePathName = PathParser.render(pagePath);
        buffer.append("!include -setup .")
              .append(pagePathName)
              .append("\n");
      }
    }
    WikiPage setup =
      PageCrawlerImpl.getInheritedPage("SetUp", wikiPage);
    if (setup != null) {
      WikiPagePath setupPath =
        wikiPage.getPageCrawler().getFullPath(setup);
      String setupPathName = PathParser.render(setupPath);
      buffer.append("!include -setup .")
            .append(setupPathName)
            .append("\n");
    }
  }
  buffer.append(pageData.getContent());
  if (pageData.hasAttribute("Test")) {
    WikiPage teardown =
      PageCrawlerImpl.getInheritedPage("TearDown", wikiPage);
    if (teardown != null) {
      WikiPagePath tearDownPath =
        wikiPage.getPageCrawler().getFullPath(teardown);
      String tearDownPathName = PathParser.render(tearDownPath);
      buffer.append("\n")
            .append("!include -teardown .")
            .append(tearDownPathName)
            .append("\n");
    }
```

**Đoạn mã 3-1 (tiếp theo)**
**HtmlUtil.java (FitNesse 20070619)**

```java
    if (includeSuiteSetup) {
      WikiPage suiteTeardown =
        PageCrawlerImpl.getInheritedPage(
                SuiteResponder.SUITE_TEARDOWN_NAME,
                wikiPage
        );
      if (suiteTeardown != null) {
        WikiPagePath pagePath =
          suiteTeardown.getPageCrawler().getFullPath (suiteTeardown);
        String pagePathName = PathParser.render(pagePath);
        buffer.append("!include -teardown .")
              .append(pagePathName)
              .append("\n");
      }
    }
  }
  pageData.setContent(buffer.toString());
  return pageData.getHtml();
}
```

Ba phút nghiên cứu xong, bạn đã hiểu hàm này chưa? Chắc là chưa. Trong đó có quá nhiều thứ đang diễn ra, ở quá nhiều mức trừu tượng khác nhau. Có những chuỗi kỳ quặc và những lời gọi hàm lạ lùng chen giữa các câu lệnh if lồng đôi được điều khiển bằng cờ.

Ấy vậy mà chỉ với vài phép tách phương thức đơn giản, vài lần đổi tên và một chút sắp xếp lại, tôi đã nắm được ý định của hàm trong chín dòng của Đoạn mã 3-2. Bạn xem trong ba phút tới mình có hiểu được đoạn này không.

**Đoạn mã 3-2**
**HtmlUtil.java (đã tái cấu trúc)**

```java
public static String renderPageWithSetupsAndTeardowns(
  PageData pageData, boolean isSuite
) throws Exception {
  boolean isTestPage = pageData.hasAttribute("Test");
  if (isTestPage) {
    WikiPage testPage = pageData.getWikiPage();
    StringBuffer newPageContent = new StringBuffer();
    includeSetupPages(testPage, newPageContent, isSuite);
    newPageContent.append(pageData.getContent());
    includeTeardownPages(testPage, newPageContent, isSuite);
    pageData.setContent(newPageContent.toString());
  }

  return pageData.getHtml();
}
```

Nếu không phải dân trong nghề FitNesse, bạn có lẽ không hiểu hết mọi chi tiết. Nhưng chắc bạn hiểu được rằng hàm này chèn một số trang thiết lập và dọn dẹp vào một trang kiểm thử rồi kết xuất trang đó ra HTML. Nếu đã quen với JUnit[^2], bạn có lẽ nhận ra hàm này thuộc về một kiểu framework kiểm thử chạy trên Web nào đó. Và dĩ nhiên, đúng là như vậy. Đoán ra thông tin ấy từ Đoạn mã 3-2 khá dễ, nhưng Đoạn mã 3-1 thì che nó đi khá kỹ.

Vậy điều gì khiến một hàm như trong Đoạn mã 3-2 trở nên dễ đọc, dễ hiểu? Làm sao để một hàm truyền đạt được ý định của mình? Ta có thể trao cho hàm những phẩm chất gì để người đọc thông thường cũng linh cảm được kiểu chương trình mà hàm ấy đang sống trong đó?

## Nhỏ!

Quy tắc đầu tiên của hàm là chúng phải nhỏ. Quy tắc thứ hai của hàm là chúng phải nhỏ hơn thế. Đây không phải điều tôi có thể chứng minh. Tôi không có nghiên cứu nào cho thấy hàm rất nhỏ thì tốt hơn. Điều tôi có thể nói là gần bốn thập kỷ qua tôi đã viết hàm đủ mọi cỡ. Tôi đã viết vài con quái vật 3.000 dòng kinh khủng. Tôi đã viết hàng đống hàm dài 100 đến 300 dòng. Và tôi cũng đã viết những hàm chỉ 20 đến 30 dòng. Kinh nghiệm ấy, qua bao lần thử sai, dạy tôi rằng hàm nên rất nhỏ.

Thập niên tám mươi, chúng ta thường nói rằng một hàm không nên lớn hơn một màn hình. Dĩ nhiên, chúng ta nói vậy vào thời màn hình VT100 chỉ có 24 dòng 80 cột, và trình soạn thảo chiếm mất 4 dòng để hiển thị thông tin quản lý. Ngày nay, với cỡ chữ thu nhỏ và một màn hình to đẹp, bạn có thể nhét 150 ký tự vào một dòng và hơn 100 dòng vào một màn hình. Dòng thì không nên dài 150 ký tự. Hàm thì không nên dài 100 dòng. Hàm gần như không bao giờ nên dài 20 dòng.

Vậy hàm nên ngắn đến mức nào? Năm 1999, tôi đến thăm Kent Beck tại nhà anh ở Oregon. Chúng tôi ngồi xuống cùng lập trình. Có lúc anh cho tôi xem một chương trình Java/Swing nhỏ xinh mà anh gọi là Sparkle. Nó tạo ra hiệu ứng hình ảnh trên màn hình rất giống cây đũa thần của bà tiên đỡ đầu trong phim Cinderella. Khi bạn di chuột, những tia sáng lấp lánh sẽ nhỏ giọt từ con trỏ với một thứ ánh sáng đã mắt, rồi rơi xuống đáy cửa sổ qua một trường hấp dẫn mô phỏng. Khi Kent cho tôi xem mã, tôi sững người vì mọi hàm đều nhỏ đến thế. Tôi vốn quen với những hàm trong chương trình Swing chiếm hàng dặm chiều dọc. Ở chương trình này, mỗi hàm chỉ dài hai, ba hoặc bốn dòng. Hàm nào cũng trong suốt, hiển nhiên. Hàm nào cũng kể một câu chuyện. Và mỗi hàm dẫn bạn sang hàm tiếp theo trong một trình tự cuốn hút. Hàm của bạn nên ngắn đến mức ấy![^3]

Hàm của bạn nên ngắn đến mức nào? Thường thì nên ngắn hơn Đoạn mã 3-2! Thật vậy, Đoạn mã 3-2 nên được rút gọn thành Đoạn mã 3-3.

**Đoạn mã 3-3**
**HtmlUtil.java (tái cấu trúc lần nữa)**

```java
public static String renderPageWithSetupsAndTeardowns(
  PageData pageData, boolean isSuite) throws Exception {
  if (isTestPage(pageData))
    includeSetupAndTeardownPages(pageData, isSuite);
  return pageData.getHtml();
}
```

### Khối lệnh và thụt lề

Điều này ngụ ý rằng khối lệnh bên trong các câu lệnh if, else, while và tương tự nên chỉ dài một dòng. Có lẽ dòng đó nên là một lời gọi hàm. Như vậy không những giữ cho hàm bao quanh nhỏ, mà còn thêm giá trị tài liệu, bởi hàm được gọi trong khối có thể mang một cái tên mô tả đẹp đẽ.

Điều này cũng ngụ ý rằng hàm không nên lớn đến mức chứa được các cấu trúc lồng nhau. Vì thế, mức thụt lề trong một hàm không nên vượt quá một hoặc hai. Dĩ nhiên, điều đó khiến hàm dễ đọc và dễ hiểu hơn.

## Làm một việc

![Làm một việc](assets/illustrations/03-do-one-thing.png){w=127}

Phải thấy rõ rằng Đoạn mã 3-1 đang làm nhiều hơn một việc. Nó tạo bộ đệm, lấy trang, tìm các trang kế thừa, kết xuất đường dẫn, nối những chuỗi bí hiểm và sinh HTML, cùng nhiều việc khác. Đoạn mã 3-1 rất bận rộn với hàng loạt việc khác nhau. Ngược lại, Đoạn mã 3-3 chỉ làm một việc đơn giản. Nó chèn phần thiết lập và dọn dẹp vào các trang kiểm thử.

Lời khuyên sau đây đã xuất hiện dưới hình thức này hay hình thức khác suốt 30 năm hoặc hơn.

> HÀM NÊN LÀM MỘT VIỆC. VÀ LÀM THẬT TỐT.
> CHỈ VIỆC ĐÓ MÀ THÔI.

Vấn đề với câu nói ấy là rất khó biết “một việc” nghĩa là gì. Đoạn mã 3-3 có làm một việc không? Dễ lập luận rằng nó đang làm ba việc:

1. Xác định xem trang có phải trang kiểm thử không.
2. Nếu phải, chèn phần thiết lập và dọn dẹp.
3. Kết xuất trang ra HTML.

Vậy rốt cuộc là sao? Hàm làm một việc hay ba việc? Hãy để ý rằng ba bước của hàm nằm ở mức trừu tượng thấp hơn một bậc so với cái tên đã đặt cho hàm. Ta có thể mô tả hàm bằng một đoạn TO[^4] ngắn gọn:

> TO RenderPageWithSetupsAndTeardowns, chúng ta kiểm tra xem trang có phải trang kiểm thử không; nếu phải, chúng ta chèn phần thiết lập và dọn dẹp. Dù thế nào, chúng ta cũng kết xuất trang ra HTML.

Nếu một hàm chỉ làm những bước nằm dưới tên của nó đúng một mức, thì hàm ấy đang làm một việc. Suy cho cùng, lý do ta viết hàm là để phân rã một khái niệm lớn hơn (nói cách khác, tên của hàm) thành một tập bước ở mức trừu tượng kế tiếp.

Phải thấy rõ rằng Đoạn mã 3-1 chứa các bước ở rất nhiều mức trừu tượng khác nhau. Vậy nên rõ ràng nó làm nhiều hơn một việc. Ngay cả Đoạn mã 3-2 cũng có hai mức trừu tượng, bằng chứng là ta có thể thu nhỏ nó lại. Nhưng sẽ rất khó thu nhỏ Đoạn mã 3-3 một cách có ý nghĩa. Ta có thể tách câu lệnh if thành một hàm tên là includeSetupsAndTeardownsIfTestPage, nhưng làm vậy chỉ diễn đạt lại đoạn mã mà không đổi mức trừu tượng.

Vậy một cách khác để biết hàm đang làm nhiều hơn “một việc” là xem bạn có tách được khỏi nó một hàm khác với cái tên không chỉ là diễn đạt lại phần hiện thực hay không [G34].

### Các mục trong hàm

Xem Đoạn mã 4-7 ở trang 71. Bạn sẽ thấy hàm generatePrimes được chia thành các mục như khai báo, khởi tạo và sàng. Đây là triệu chứng rõ ràng của việc làm nhiều hơn một việc. Những hàm chỉ làm một việc không thể bị chia thành các mục một cách hợp lý.

## Mỗi hàm một mức trừu tượng

Để chắc chắn các hàm của mình đang làm “một việc”, ta cần bảo đảm mọi câu lệnh trong hàm đều nằm ở cùng một mức trừu tượng. Dễ thấy Đoạn mã 3-1 vi phạm quy tắc này. Trong đó có những khái niệm ở mức trừu tượng rất cao, như getHtml(); có những khái niệm ở mức trung gian, như: `String pagePathName = PathParser.render(pagePath);` và lại có những thứ ở mức thấp đáng kinh ngạc, như: `.append("\n")`.

Trộn lẫn các mức trừu tượng trong một hàm thì luôn gây bối rối. Người đọc có thể không phân biệt nổi một biểu thức cụ thể là khái niệm thiết yếu hay chỉ là chi tiết. Tệ hơn, giống như những ô cửa sổ vỡ, một khi chi tiết đã trộn vào khái niệm thiết yếu thì trong hàm sẽ ngày càng tích tụ thêm chi tiết.

### Đọc mã từ trên xuống: Quy tắc bậc thang

Ta muốn mã đọc như một câu chuyện kể từ trên xuống[^5]. Ta muốn mỗi hàm được theo sau bởi những hàm ở mức trừu tượng kế tiếp, để có thể đọc chương trình, mỗi lúc hạ xuống một mức trừu tượng khi đọc dần danh sách hàm. Tôi gọi đó là Quy tắc bậc thang.

Nói cách khác, ta muốn có thể đọc chương trình như thể nó là một tập các đoạn TO, mỗi đoạn mô tả mức trừu tượng hiện tại và tham chiếu tới những đoạn TO tiếp theo ở mức thấp hơn.

> Để chèn phần thiết lập và dọn dẹp, chúng ta chèn phần thiết lập, rồi chèn nội dung trang kiểm thử, rồi chèn phần dọn dẹp.
>
> Để chèn phần thiết lập, chúng ta chèn thiết lập của suite nếu đây là một suite, rồi chèn thiết lập thường.
>
> Để chèn thiết lập của suite, chúng ta tìm trang “SuiteSetUp” trong hệ thống phân cấp cha và thêm một câu lệnh include kèm đường dẫn của trang đó.
>
> Để tìm trang cha. . .

Suy cho cùng, việc học theo quy tắc này và viết được những hàm chỉ giữ một mức trừu tượng là rất khó đối với lập trình viên. Nhưng học được mẹo này cũng rất quan trọng. Đó là chìa khóa để giữ hàm ngắn và bảo đảm chúng làm “một việc”. Làm cho mã đọc như một tập đoạn TO từ trên xuống là kỹ thuật hiệu quả để giữ mức trừu tượng nhất quán.

Hãy xem Đoạn mã 3-7 ở cuối chương này. Nó cho thấy toàn bộ hàm testableHtml đã được tái cấu trúc theo những nguyên tắc mô tả ở đây. Hãy để ý mỗi hàm giới thiệu hàm kế tiếp, và hàm nào cũng giữ một mức trừu tượng nhất quán.

## Câu lệnh switch

Rất khó làm một câu lệnh switch nhỏ[^6]. Ngay cả một câu lệnh switch chỉ có hai nhánh cũng lớn hơn mức tôi muốn ở một khối hay một hàm. Cũng rất khó làm một câu lệnh switch chỉ làm một việc. Bản chất của chúng là luôn làm N việc. Đáng tiếc, không phải lúc nào ta cũng tránh được switch, nhưng ta có thể bảo đảm mỗi câu lệnh switch được chôn trong một lớp mức thấp và không bao giờ bị lặp lại. Dĩ nhiên, ta làm điều đó bằng đa hình.

Xét Đoạn mã 3-4. Nó chỉ cho thấy một trong những thao tác có thể phụ thuộc vào loại nhân viên.

**Đoạn mã 3-4**
**Payroll.java**

```java
public Money calculatePay(Employee e)
throws InvalidEmployeeType {
  switch (e.type) {
    case COMMISSIONED:
      return calculateCommissionedPay(e);
    case HOURLY:
      return calculateHourlyPay(e);
    case SALARIED:
      return calculateSalariedPay(e);
    default:
      throw new InvalidEmployeeType(e.type);
  }
}
```

Hàm này có vài vấn đề. Thứ nhất, nó lớn, và khi có thêm loại nhân viên mới, nó sẽ phình ra. Thứ hai, rõ ràng nó làm nhiều hơn một việc. Thứ ba, nó vi phạm Nguyên lý Trách nhiệm Đơn (SRP)[^7] vì có nhiều hơn một lý do để nó thay đổi. Thứ tư, nó vi phạm Nguyên lý Mở/Đóng (OCP)[^8] vì nó buộc phải thay đổi mỗi khi thêm loại mới. Nhưng có lẽ vấn đề tệ nhất của hàm này là có vô số hàm khác sẽ có cùng cấu trúc. Chẳng hạn, ta có thể có `isPayday(Employee e, Date date)`, hoặc `deliverPay(Employee e, Money pay)`, hoặc cả một loạt hàm khác. Tất cả đều sẽ có cùng cấu trúc tai hại ấy.

Giải pháp cho vấn đề này (xem Đoạn mã 3-5) là chôn câu lệnh switch dưới tầng hầm của một ABSTRACT FACTORY[^9], và không để ai nhìn thấy nó nữa. Nhà máy sẽ dùng câu lệnh switch để tạo các thực thể phù hợp của những lớp dẫn xuất từ Employee, còn các hàm khác nhau như calculatePay, isPayday và deliverPay sẽ được điều phối đa hình qua giao diện Employee.

Quy tắc chung của tôi với câu lệnh switch là có thể chấp nhận chúng nếu chúng chỉ xuất hiện một lần, được dùng để tạo các đối tượng đa hình, và được giấu sau một quan hệ kế thừa để phần còn lại của hệ thống không nhìn thấy chúng [G23]. Dĩ nhiên, mỗi hoàn cảnh đều riêng biệt, và có những lúc tôi vi phạm một hoặc vài phần của quy tắc ấy.

**Đoạn mã 3-5**
**Employee and Factory**

```java
public abstract class Employee {
  public abstract boolean isPayday();
  public abstract Money calculatePay();
  public abstract void deliverPay(Money pay);
}
-----------------
public interface EmployeeFactory {
  public Employee makeEmployee(EmployeeRecord r) throws InvalidEmployeeType;
}
-----------------
public class EmployeeFactoryImpl implements EmployeeFactory {
  public Employee makeEmployee(EmployeeRecord r) throws InvalidEmployeeType {
    switch (r.type) {
      case COMMISSIONED:
        return new CommissionedEmployee(r) ;
      case HOURLY:
        return new HourlyEmployee(r);
      case SALARIED:
        return new SalariedEmploye(r);
      default:
        throw new InvalidEmployeeType(r.type);
    }
  }
}
```

## Dùng tên mô tả

Trong Đoạn mã 3-7, tôi đổi tên hàm ví dụ từ testableHtml thành SetupTeardownIncluder.render. Đây là cái tên tốt hơn nhiều vì nó mô tả đúng hơn việc hàm làm. Tôi cũng đặt cho mỗi phương thức riêng một cái tên mô tả tương xứng, chẳng hạn isTestable hoặc includeSetupAndTeardownPages. Thật khó mà đánh giá quá cao giá trị của những cái tên hay. Hãy nhớ nguyên lý của Ward: “Bạn biết mình đang làm việc với mã sạch khi mỗi thủ tục hóa ra đúng như bạn mong đợi.” Một nửa trận chiến để đạt được nguyên lý ấy là chọn tên hay cho những hàm nhỏ chỉ làm một việc. Hàm càng nhỏ và càng tập trung bao nhiêu, càng dễ chọn cho nó một cái tên mô tả bấy nhiêu.

Đừng ngại đặt tên dài. Một cái tên dài mà mô tả vẫn hơn một cái tên ngắn mà bí hiểm. Một cái tên dài mà mô tả cũng hơn một chú thích dài mà mô tả. Hãy dùng một quy ước đặt tên cho phép đọc dễ dàng nhiều từ trong tên hàm, rồi tận dụng những từ ấy để đặt cho hàm một cái tên nói đúng việc nó làm.

Đừng ngại dành thời gian chọn tên. Thật vậy, bạn nên thử vài cái tên khác nhau và đọc đoạn mã với từng cái. Những IDE hiện đại như Eclipse hay IntelliJ khiến việc đổi tên trở nên dễ như trở bàn tay. Hãy dùng một trong những IDE ấy và thử nghiệm các tên khác nhau cho tới khi tìm được cái tên mô tả nhất mà bạn có thể nghĩ ra.

Chọn những cái tên mô tả sẽ làm thiết kế của module rõ ràng hơn trong đầu bạn và giúp bạn cải thiện nó. Không hiếm chuyện săn tìm một cái tên hay lại dẫn đến một lần tái cấu trúc có lợi cho mã.

Hãy nhất quán trong cách đặt tên. Dùng cùng những cụm từ, danh từ và động từ trong tên các hàm bạn chọn cho module của mình. Chẳng hạn, hãy xét các tên includeSetupAndTeardownPages, includeSetupPages, includeSuiteSetupPage và includeSetupPage. Cách dùng từ tương tự trong những cái tên ấy cho phép cả chuỗi ấy kể nên một câu chuyện. Thật vậy, nếu tôi chỉ đưa bạn xem chuỗi trên, bạn sẽ tự hỏi: “Thế includeTeardownPages, includeSuiteTeardownPage và includeTeardownPage đâu rồi?” Thấy chưa, đúng là “. . . hóa ra đúng như bạn mong đợi.”

![Dùng tên mô tả](assets/illustrations/03-use-descriptive-names.png){w=141}

## Đối số của hàm

Số đối số lý tưởng của một hàm là không (niladic). Tiếp đến là một (monadic), rồi sát ngay sau là hai (dyadic). Ba đối số (triadic) nên tránh khi có thể. Nhiều hơn ba (polyadic) đòi hỏi lý do rất đặc biệt, và dù có lý do thì cũng không nên dùng.

Đối số là thứ khó chơi. Chúng ngốn rất nhiều sức khái quát. Đó là lý do tôi loại bỏ gần như toàn bộ đối số khỏi ví dụ. Chẳng hạn, hãy xét StringBuffer trong ví dụ. Đáng lẽ ta có thể truyền nó qua lại như một đối số thay vì biến nó thành biến thực thể, nhưng khi ấy người đọc sẽ phải diễn giải nó mỗi lần nhìn thấy. Khi bạn đọc câu chuyện mà module kể, includeSetupPage() dễ hiểu hơn includeSetupPageInto(newPageContent). Đối số nằm ở mức trừu tượng khác với tên hàm và buộc bạn phải biết một chi tiết (nói cách khác, StringBuffer) không quan trọng lắm ở điểm đó.

Đối số còn khó hơn nữa dưới góc nhìn kiểm thử. Thử tưởng tượng nỗi vất vả khi phải viết mọi ca kiểm thử để bảo đảm mọi tổ hợp đối số khác nhau đều chạy đúng. Không có đối số thì chuyện này tầm thường. Có một đối số thì không khó lắm. Với hai đối số, vấn đề bắt đầu thử thách hơn một chút. Với hơn hai đối số, kiểm thử mọi tổ hợp giá trị phù hợp có thể là một cơn ác mộng.

Đối số đầu ra khó hiểu hơn đối số đầu vào. Khi đọc một hàm, ta quen với ý tưởng thông tin đi vào hàm qua đối số và đi ra qua giá trị trả về. Ta thường không chờ đợi thông tin đi ra qua đối số. Vì thế đối số đầu ra hay khiến ta phải nhìn lại lần hai.

Một đối số đầu vào là lựa chọn tốt nhất ngay sau không có đối số nào. SetupTeardownIncluder.render(pageData) khá dễ hiểu. Rõ ràng ta sắp kết xuất dữ liệu trong đối tượng pageData.

### Các dạng một đối số phổ biến

Có hai lý do rất phổ biến để truyền một đối số vào hàm. Có thể bạn đang hỏi một câu về đối số đó, như trong `boolean fileExists("MyFile")`. Hoặc bạn đang thao tác trên đối số đó, biến nó thành thứ khác rồi trả về. Chẳng hạn, `InputStream fileOpen("MyFile")` biến một chuỗi tên tệp thành giá trị trả về InputStream. Hai cách dùng này là điều người đọc trông đợi khi thấy một hàm. Bạn nên chọn những cái tên làm nổi bật sự phân biệt ấy, và luôn dùng hai dạng này trong một bối cảnh nhất quán. (Xem phần Tách lệnh khỏi truy vấn bên dưới.)

Một dạng ít phổ biến hơn nhưng vẫn rất hữu ích của hàm một đối số là sự kiện. Ở dạng này có một đối số đầu vào nhưng không có đối số đầu ra. Toàn bộ chương trình được hiểu là hãy diễn giải lời gọi hàm như một sự kiện và dùng đối số để thay đổi trạng thái của hệ thống, chẳng hạn `void passwordAttemptFailedNtimes(int attempts)`. Hãy dùng dạng này cẩn thận. Phải để người đọc thấy rõ đây là một sự kiện. Chọn tên và bối cảnh cho cẩn thận.

Hãy cố tránh mọi hàm một đối số không theo các dạng ấy, chẳng hạn `void includeSetupPageInto(StringBuffer pageText)`. Dùng đối số đầu ra thay cho giá trị trả về trong một phép biến đổi là chuyện gây bối rối. Nếu hàm sắp biến đổi đối số đầu vào của nó, phép biến đổi nên xuất hiện dưới dạng giá trị trả về. Thật vậy, `StringBuffer transform(StringBuffer in)` tốt hơn `void transform(StringBuffer out)`, kể cả khi phần hiện thực của trường hợp đầu chỉ đơn giản trả về đối số đầu vào. Ít nhất nó vẫn tuân theo dạng của một phép biến đổi.

### Đối số cờ

Đối số cờ thật xấu xí. Truyền một boolean vào hàm là một thói quen thật sự tệ hại. Nó lập tức làm phức tạp chữ ký của phương thức, và lớn tiếng tuyên bố rằng hàm này làm nhiều hơn một việc. Nó làm một việc nếu cờ là true và làm việc khác nếu cờ là false!

Trong Đoạn mã 3-7, chúng tôi không có lựa chọn nào khác vì những nơi gọi đã truyền cờ ấy vào từ trước, và tôi muốn giới hạn phạm vi tái cấu trúc trong hàm và những thứ bên dưới nó. Dẫu vậy, lời gọi render(true) vẫn cứ gây bối rối cho một người đọc tội nghiệp. Rà chuột lên lời gọi và thấy render(boolean isSuite) cũng đỡ được chút ít, nhưng không đáng kể. Đáng lẽ chúng tôi nên tách hàm thành hai: renderForSuite() và renderForSingleTest().

### Hàm hai đối số

Hàm hai đối số khó hiểu hơn hàm một đối số. Chẳng hạn, writeField(name) dễ hiểu hơn `writeField(outputStream, name)`[^10]. Dù ý nghĩa của cả hai đều rõ, cái đầu trôi qua mắt và dễ dàng đọng lại ý nghĩa. Cái thứ hai đòi một khoảng dừng ngắn cho tới khi ta học cách phớt lờ tham số đầu tiên. Và dĩ nhiên, điều đó cuối cùng dẫn đến rắc rối, vì ta không bao giờ nên phớt lờ bất kỳ phần nào của mã. Những phần ta phớt lờ chính là nơi lũ bug trú ngụ.

Có những lúc, dĩ nhiên, hai đối số là hợp lý. Chẳng hạn, `Point p = new Point(0,0);` hoàn toàn hợp lý. Điểm Descartes vốn dĩ nhận hai đối số. Thật vậy, ta sẽ rất ngạc nhiên nếu thấy `new Point(0)`. Tuy nhiên, hai đối số trong trường hợp này là các thành phần có thứ tự của một giá trị duy nhất! Trong khi đó, outputStream và name không có sự gắn kết tự nhiên, cũng chẳng có thứ tự tự nhiên.

Ngay cả những hàm hai đối số hiển nhiên như `assertEquals(expected, actual)` cũng có vấn đề. Bao nhiêu lần bạn đã đặt actual vào chỗ đáng lẽ là expected? Hai đối số không có thứ tự tự nhiên. Thứ tự expected, actual là một quy ước cần luyện tập mới nhớ.

Hàm hai đối số không phải thứ xấu xa, và chắc chắn bạn sẽ phải viết chúng. Nhưng bạn nên biết rằng chúng phải trả giá, và nên tận dụng mọi cơ chế sẵn có để chuyển chúng thành hàm một đối số. Chẳng hạn, bạn có thể đưa phương thức writeField vào outputStream như một thành viên, để có thể viết outputStream.writeField(name). Hoặc biến outputStream thành biến thành viên của lớp hiện tại để khỏi phải truyền nó. Hoặc tách ra một lớp mới như FieldWriter, nhận outputStream trong hàm dựng và có một phương thức write.

### Hàm ba đối số

Hàm nhận ba đối số khó hiểu hơn hẳn hàm hai đối số. Các vấn đề về thứ tự, khoảng dừng và sự phớt lờ tăng lên hơn gấp đôi. Tôi khuyên bạn nghĩ thật kỹ trước khi tạo một hàm ba đối số.

Chẳng hạn, hãy xét bản nạp chồng phổ biến của assertEquals nhận ba đối số: `assertEquals(message, expected, actual)`. Bao nhiêu lần bạn đọc message rồi tưởng đó là expected? Tôi đã vấp và dừng lại vì cái bộ ba ấy không biết bao nhiêu lần. Thật vậy, mỗi lần thấy nó, tôi đều phải nhìn lại lần hai, rồi sau đó học cách phớt lờ message.

Mặt khác, đây là một bộ ba không quá hiểm: `assertEquals(1.0, amount, .001)`. Dù vẫn phải nhìn lại lần hai, lần nhìn lại này đáng giá. Luôn tốt khi được nhắc rằng sự bằng nhau của các giá trị số thực dấu phẩy động là chuyện tương đối.

### Đối tượng đối số

Khi một hàm có vẻ cần nhiều hơn hai hoặc ba đối số, rất có thể một số đối số ấy nên được gói vào một lớp riêng. Chẳng hạn, hãy xét sự khác biệt giữa hai khai báo sau:

```java
Circle makeCircle(double x, double y, double radius);
Circle makeCircle(Point center, double radius);
```

Giảm số đối số bằng cách tạo đối tượng từ chúng có vẻ như ăn gian, nhưng không phải vậy. Khi những nhóm biến được truyền cùng nhau, theo cách x và y được truyền trong ví dụ trên, chúng rất có thể là một phần của một khái niệm xứng đáng có tên riêng.

### Danh sách đối số

Đôi khi ta muốn truyền một số lượng đối số thay đổi vào hàm. Chẳng hạn, hãy xét phương thức String.format:

```java
String.format("%s worked %.2f hours.", name, hours);
```

Nếu mọi đối số thay đổi đều được đối xử như nhau, như trong ví dụ trên, thì chúng tương đương với một đối số duy nhất kiểu List. Lập luận như vậy thì String.format thực ra là hàm hai đối số. Thật vậy, khai báo của String.format như dưới đây rõ ràng là hai đối số.

```java
public String format(String format, Object... args)
```

Vậy mọi quy tắc cũ vẫn áp dụng. Hàm nhận đối số thay đổi có thể là một đối số, hai đối số, thậm chí ba đối số. Nhưng cho chúng nhiều đối số hơn thế sẽ là sai lầm.

```java
void monad(Integer... args);
void dyad(String name, Integer... args);
void triad(String name, int count, Integer... args);
```

### Động từ và từ khóa

Chọn tên hay cho hàm có thể đi được một quãng dài trên đường giải thích ý định của hàm cùng thứ tự và ý định của các đối số. Với hàm một đối số, hàm và đối số nên tạo thành một cặp động từ/danh từ thật đẹp. Chẳng hạn, write(name) gợi ra rất nhiều điều. Thứ “name” này, dù nó là gì, đang được “write”. Một cái tên còn hay hơn có lẽ là writeField(name), cho ta biết thứ “name” là một “field”.

Cái sau là ví dụ về dạng từ khóa của tên hàm. Dùng dạng này, ta mã hóa tên của các đối số vào tên hàm. Chẳng hạn, assertEquals có lẽ nên được viết là assertExpectedEqualsActual(expected, actual). Cách này giảm mạnh vấn đề phải nhớ thứ tự của các đối số.

## Đừng gây tác dụng phụ

Tác dụng phụ là những lời dối trá. Hàm của bạn hứa làm một việc, nhưng nó còn làm những việc ẩn giấu khác. Đôi khi nó tạo ra những thay đổi bất ngờ đối với các biến của chính lớp chứa nó. Đôi khi nó tạo ra những thay đổi ấy đối với các tham số được truyền vào hàm hoặc đối với biến toàn cục của hệ thống. Trong cả hai trường hợp, chúng đều là những lời dối trá xảo quyệt và tai hại, thường dẫn đến những mối ghép thời gian và những phụ thuộc thứ tự kỳ quặc.

Chẳng hạn, hãy xét hàm có vẻ vô hại trong Đoạn mã 3-6. Hàm này dùng một thuật toán chuẩn để ghép userName với mật khẩu. Nó trả về true nếu hai thứ khớp nhau và false nếu có gì sai. Nhưng nó còn có một tác dụng phụ. Bạn có nhận ra không?

**Đoạn mã 3-6**
**UserValidator.java**

```java
public class UserValidator {
  private Cryptographer cryptographer;

  public boolean checkPassword(String userName, String password) {
    User user = UserGateway.findByName(userName);
    if (user != User.NULL) {
      String codedPhrase = user.getPhraseEncodedByPassword();
      String phrase = cryptographer.decrypt(codedPhrase, password);
      if ("Valid Password".equals(phrase)) {
        Session.initialize();
        return true;
      }
    }
    return false;
  }
}
```

Tác dụng phụ ấy là lời gọi Session.initialize(), dĩ nhiên rồi. Hàm checkPassword, qua cái tên của mình, nói rằng nó kiểm tra mật khẩu. Cái tên không hề ngụ ý rằng nó khởi tạo phiên làm việc. Vì thế, một người gọi tin vào điều tên hàm nói sẽ có nguy cơ xóa sạch dữ liệu phiên hiện có khi quyết định kiểm tra tính hợp lệ của người dùng.

Tác dụng phụ này tạo ra một mối ghép thời gian. Nghĩa là checkPassword chỉ có thể được gọi vào những thời điểm nhất định (nói cách khác, khi khởi tạo phiên là an toàn). Nếu nó bị gọi sai thứ tự, dữ liệu phiên có thể bị mất ngoài ý muốn. Những mối ghép thời gian gây bối rối, nhất là khi bị giấu dưới dạng tác dụng phụ. Nếu buộc phải có một mối ghép thời gian, bạn nên làm rõ nó trong tên của hàm. Trong trường hợp này, có lẽ ta đổi tên hàm thành checkPasswordAndInitializeSession, dù làm vậy chắc chắn vi phạm “Làm một việc”.

### Đối số đầu ra

Đối số tự nhiên được hiểu là đầu vào của hàm. Nếu bạn đã lập trình hơn vài năm, tôi chắc bạn đã từng phải nhìn lại lần hai trước một đối số hóa ra là đầu ra chứ không phải đầu vào. Chẳng hạn:

```java
appendFooter(s);
```

Hàm này nối s vào làm chân trang cho một thứ gì đó ư? Hay nó nối một chân trang nào đó vào s? s là đầu vào hay đầu ra? Không mất nhiều thời gian để nhìn chữ ký hàm và thấy:

```java
public void appendFooter(StringBuffer report)
```

Điều này làm rõ vấn đề, nhưng chỉ với cái giá là phải kiểm tra khai báo của hàm. Bất cứ thứ gì buộc bạn phải kiểm tra chữ ký hàm đều tương đương với việc nhìn lại lần hai. Đó là một sự gián đoạn nhận thức và nên tránh.

Vào thời trước lập trình hướng đối tượng, đôi khi người ta buộc phải có đối số đầu ra. Tuy nhiên, phần lớn nhu cầu về đối số đầu ra biến mất trong các ngôn ngữ hướng đối tượng, vì `this` được dùng như một đối số đầu ra. Nói cách khác, sẽ tốt hơn nếu appendFooter được gọi như sau:

```java
report.appendFooter();
```

Nhìn chung, nên tránh đối số đầu ra. Nếu hàm của bạn buộc phải thay đổi trạng thái của một thứ gì đó, hãy để nó thay đổi trạng thái của đối tượng sở hữu nó.

## Tách lệnh khỏi truy vấn

Hàm nên hoặc làm việc gì đó, hoặc trả lời việc gì đó, chứ không nên làm cả hai. Hoặc hàm của bạn nên thay đổi trạng thái của một đối tượng, hoặc nó nên trả về một thông tin nào đó về đối tượng ấy. Làm cả hai thường dẫn đến bối rối. Chẳng hạn, hãy xét hàm sau:

```java
public boolean set(String attribute, String value);
```

Hàm này đặt giá trị cho một thuộc tính có tên và trả về true nếu thành công, false nếu không có thuộc tính ấy. Điều này dẫn đến những câu lệnh kỳ quặc như:

```java
if (set("username", "unclebob"))...
```

Hãy tưởng tượng điều này từ góc nhìn người đọc. Nó nghĩa là gì? Nó đang hỏi xem thuộc tính “username” trước đó có được đặt thành “unclebob” không? Hay nó đang hỏi xem thuộc tính “username” có được đặt thành công thành “unclebob” không? Thật khó suy ra ý nghĩa từ lời gọi, vì không rõ từ “set” là động từ hay tính từ.

Tác giả định dùng set như một động từ, nhưng trong bối cảnh câu lệnh if, nó có cảm giác như một tính từ. Vậy nên câu lệnh đọc thành “Nếu thuộc tính username trước đó đã được đặt thành unclebob”, chứ không phải “đặt thuộc tính username thành unclebob và nếu việc đó thành công thì . . .”. Ta có thể thử giải quyết bằng cách đổi tên hàm set thành setAndCheckIfExists, nhưng cách ấy không giúp ích mấy cho khả năng đọc của câu lệnh if. Giải pháp thật sự là tách lệnh khỏi truy vấn để sự mơ hồ không thể xảy ra.

```java
if (attributeExists("username")) {
  setAttribute("username", "unclebob");
  ...
}
```

## Ưu tiên ngoại lệ hơn mã lỗi

Trả về mã lỗi từ các hàm lệnh là một sự vi phạm tinh vi đối với nguyên tắc tách lệnh khỏi truy vấn. Nó khuyến khích việc dùng lệnh làm biểu thức trong các vị từ của câu lệnh if.

```java
if (deletePage(page) == E_OK)
```

Cách này không mắc chứng nhầm lẫn động từ/tính từ nhưng lại dẫn đến những cấu trúc lồng rất sâu. Khi trả về một mã lỗi, bạn tạo ra vấn đề là người gọi buộc phải xử lý lỗi ngay lập tức.

```java
if (deletePage(page) == E_OK) {
  if (registry.deleteReference(page.name) == E_OK) {
     if (configKeys.deleteKey(page.name.makeKey()) == E_OK){
       logger.log("page deleted");
     } else {
       logger.log("configKey not deleted");
     }
  } else {
     logger.log("deleteReference from registry failed");
  }
} else {
  logger.log("delete failed");
  return E_ERROR;
}
```

Mặt khác, nếu dùng ngoại lệ thay cho mã lỗi trả về, thì phần mã xử lý lỗi có thể được tách khỏi phần mã của luồng thuận lợi và có thể được đơn giản hóa:

```java
try {
  deletePage(page);
  registry.deleteReference(page.name);
  configKeys.deleteKey(page.name.makeKey());
}
catch (Exception e) {
  logger.log(e.getMessage());
}
```

### Tách khối try/catch

Bản thân các khối try/catch đã xấu xí. Chúng làm rối cấu trúc của mã và trộn việc xử lý lỗi với việc xử lý bình thường. Vì thế, tốt hơn là tách phần thân của khối try và khối catch ra thành những hàm riêng.

```java
public void delete(Page page) {
  try {
    deletePageAndAllReferences(page);
  }
  catch (Exception e) {
    logError(e);
  }
}

private void deletePageAndAllReferences(Page page) throws Exception {
  deletePage(page);
  registry.deleteReference(page.name);
  configKeys.deleteKey(page.name.makeKey());
}
private void logError(Exception e) {
  logger.log(e.getMessage());
}
```

Ở đoạn trên, hàm delete chỉ toàn là chuyện xử lý lỗi. Nó dễ hiểu và dễ bỏ qua. Hàm deletePageAndAllReferences chỉ toàn là chuyện xóa hoàn toàn một trang. Phần xử lý lỗi có thể bỏ qua. Điều này tạo ra một sự tách bạch đẹp đẽ, khiến mã dễ hiểu và dễ sửa hơn.

### Xử lý lỗi là một việc

Hàm nên làm một việc. Xử lý lỗi là một việc. Vì thế, một hàm xử lý lỗi không nên làm gì khác. Điều này ngụ ý (như trong ví dụ trên) rằng nếu từ khóa try xuất hiện trong một hàm, nó phải là từ đầu tiên trong hàm và không được có gì sau các khối catch/finally.

### Error.java, nam châm hút phụ thuộc

Trả về mã lỗi thường ngụ ý có một lớp hay enum nào đó định nghĩa mọi mã lỗi.

```java
public enum Error {
  OK,
  INVALID,
  NO_SUCH,
  LOCKED,
  OUT_OF_RESOURCES,
  WAITING_FOR_EVENT;
}
```

Những lớp như thế là một nam châm hút phụ thuộc; rất nhiều lớp khác buộc phải import và dùng chúng. Vì vậy, khi enum Error thay đổi, tất cả những lớp kia đều phải biên dịch lại và triển khai lại[^11]. Điều này tạo áp lực tiêu cực lên lớp Error. Lập trình viên không muốn thêm lỗi mới vì khi ấy họ phải build lại và triển khai lại mọi thứ. Thế là họ tái sử dụng những mã lỗi cũ thay vì thêm mã mới.

Khi dùng ngoại lệ thay cho mã lỗi, những ngoại lệ mới là lớp dẫn xuất của lớp ngoại lệ. Có thể thêm chúng mà không buộc phải biên dịch lại hay triển khai lại bất cứ thứ gì[^12].

![Error.java](assets/illustrations/03-error-java.png){w=173}

## Đừng lặp lại chính mình

Hãy nhìn lại Đoạn mã 3-1 thật kỹ[^13], bạn sẽ thấy có một thuật toán bị lặp lại bốn lần, mỗi lần ứng với một trong các trường hợp SetUp, SuiteSetUp, TearDown và SuiteTearDown. Không dễ phát hiện sự trùng lặp này vì bốn thực thể ấy chen lẫn với mã khác và không được lặp lại một cách đồng nhất. Dẫu vậy, trùng lặp vẫn là vấn đề vì nó làm mã phình ra và sẽ đòi hỏi phải sửa bốn chỗ nếu thuật toán ấy có ngày phải thay đổi. Đó cũng là bốn cơ hội để mắc lỗi bỏ sót.

Sự trùng lặp này đã được khắc phục bằng phương thức include trong Đoạn mã 3-7. Hãy đọc lại đoạn mã ấy và để ý khả năng đọc của cả module được nâng lên thế nào nhờ giảm bớt sự trùng lặp.

Trùng lặp có thể là gốc rễ của mọi điều xấu trong phần mềm. Nhiều nguyên lý và thực hành đã ra đời nhằm mục đích kiểm soát hoặc loại bỏ nó. Chẳng hạn, hãy xét việc mọi dạng chuẩn hóa cơ sở dữ liệu của Codd đều nhằm loại bỏ trùng lặp trong dữ liệu. Cũng hãy xét việc lập trình hướng đối tượng nhằm dồn mã vào các lớp cơ sở, những thứ nếu không thì sẽ dư thừa. Lập trình có cấu trúc, Lập trình Hướng khía cạnh, Lập trình Hướng thành phần, tất cả đều, ở một phần nào đó, là những chiến lược loại bỏ trùng lặp. Có vẻ như kể từ khi phát minh ra subroutine, những đổi mới trong phát triển phần mềm đã là một nỗ lực không ngừng nhằm loại bỏ trùng lặp khỏi mã nguồn của chúng ta.

## Lập trình có cấu trúc

Một số lập trình viên theo các quy tắc lập trình có cấu trúc[^14] của Edsger Dijkstra. Dijkstra nói rằng mọi hàm, và mọi khối trong một hàm, nên có một điểm vào và một điểm ra. Theo những quy tắc này, trong một hàm chỉ nên có một câu lệnh return, không có câu lệnh break hay continue trong vòng lặp, và tuyệt đối không bao giờ có câu lệnh goto.

Dù chúng tôi đồng cảm với mục tiêu và kỷ luật của lập trình có cấu trúc, những quy tắc ấy chẳng mang lại bao nhiêu lợi ích khi hàm rất nhỏ. Chỉ trong những hàm lớn hơn, các quy tắc như vậy mới mang lại lợi ích đáng kể.

Vậy nên nếu bạn giữ hàm của mình nhỏ, thì việc thỉnh thoảng có nhiều câu lệnh return, break hay continue không gây hại, và đôi khi còn có thể biểu cảm hơn quy tắc một điểm vào, một điểm ra. Ngược lại, goto chỉ có ý nghĩa trong những hàm lớn, nên cần tránh.

## Làm thế nào để viết được những hàm như thế này?

Viết phần mềm cũng giống như bất kỳ kiểu viết nào khác. Khi viết một bài báo hay một bài viết, bạn ghi ý tưởng ra trước, rồi nhào nặn nó cho tới khi đọc xuôi. Bản nháp đầu có thể vụng về và lộn xộn, nên bạn trau chuốt từng chữ, sắp xếp lại, tinh chỉnh cho tới khi nó đọc đúng như bạn muốn.

Khi tôi viết hàm, chúng thường ra đời dài và phức tạp. Chúng có nhiều thụt lề và vòng lặp lồng nhau. Chúng có những danh sách đối số dài. Tên gọi thì tùy tiện, và mã thì trùng lặp. Nhưng tôi cũng có một bộ kiểm thử đơn vị bao phủ từng dòng mã vụng về ấy.

Rồi tôi nhào nặn và tinh chỉnh đoạn mã đó, tách hàm ra, đổi tên, loại bỏ trùng lặp. Tôi thu nhỏ các phương thức và sắp xếp lại chúng. Có khi tôi tách hẳn những lớp ra, và trong suốt quá trình ấy vẫn giữ cho các bài kiểm thử chạy qua.

Cuối cùng, tôi có được những hàm tuân theo các quy tắc tôi đã trình bày trong chương này. Tôi không viết chúng theo cách ấy ngay từ đầu. Tôi không nghĩ có ai làm được.

## Kết luận

Mọi hệ thống đều được dựng nên từ một ngôn ngữ chuyên miền (domain-specific language) do chính các lập trình viên thiết kế để mô tả hệ thống ấy. Hàm là động từ của ngôn ngữ đó, còn lớp là danh từ. Đây không phải sự quay lại với quan niệm cũ kỹ ghê sợ rằng những danh từ và động từ trong một tài liệu yêu cầu chính là phỏng đoán đầu tiên về các lớp và hàm của một hệ thống. Đúng hơn, đây là một chân lý cổ xưa hơn nhiều. Nghệ thuật lập trình là, và luôn luôn là, nghệ thuật thiết kế ngôn ngữ.

Những lập trình viên bậc thầy nghĩ về hệ thống như những câu chuyện cần được kể, chứ không phải những chương trình cần được viết. Họ dùng các phương tiện của ngôn ngữ lập trình mình chọn để dựng nên một ngôn ngữ phong phú và biểu cảm hơn nhiều, có thể dùng để kể câu chuyện ấy. Một phần của ngôn ngữ chuyên miền đó là hệ thống phân cấp các hàm mô tả mọi hành động diễn ra bên trong hệ thống. Trong một hành vi đệ quy đầy nghệ thuật, những hành động ấy được viết bằng chính ngôn ngữ chuyên miền mà chúng định nghĩa, để kể phần câu chuyện nhỏ bé của riêng chúng.

Chương này nói về cơ chế viết hàm cho tốt. Nếu bạn theo các quy tắc trong đây, hàm của bạn sẽ ngắn, được đặt tên hay và được tổ chức gọn gàng. Nhưng đừng bao giờ quên rằng mục tiêu thật sự của bạn là kể câu chuyện của hệ thống, và những hàm bạn viết cần khớp vào nhau một cách sạch sẽ để tạo thành một ngôn ngữ rõ ràng, chính xác, giúp bạn kể câu chuyện đó.

## SetupTeardownIncluder

**Đoạn mã 3-7**
**SetupTeardownIncluder.java**

```java
package fitnesse.html;

import fitnesse.responders.run.SuiteResponder;
import fitnesse.wiki.*;
public class SetupTeardownIncluder {
  private PageData pageData;
  private boolean isSuite;
  private WikiPage testPage;
  private StringBuffer newPageContent;
  private PageCrawler pageCrawler;

  public static String render(PageData pageData) throws Exception {
    return render(pageData, false);
  }

  public static String render(PageData pageData, boolean isSuite)
    throws Exception {
    return new SetupTeardownIncluder(pageData).render(isSuite);
  }

  private SetupTeardownIncluder(PageData pageData) {
    this.pageData = pageData;
    testPage = pageData.getWikiPage();
    pageCrawler = testPage.getPageCrawler();
    newPageContent = new StringBuffer();
  }
  private String render(boolean isSuite) throws Exception {
    this.isSuite = isSuite;
    if (isTestPage())
      includeSetupAndTeardownPages();
    return pageData.getHtml();
  }

  private boolean isTestPage() throws Exception {
    return pageData.hasAttribute("Test");
  }

  private void includeSetupAndTeardownPages() throws Exception {
    includeSetupPages();
    includePageContent();
    includeTeardownPages();
    updatePageContent();
  }
```

**Đoạn mã 3-7 (tiếp theo)**
**SetupTeardownIncluder.java**

```java
  private void includeSetupPages() throws Exception {
    if (isSuite)
      includeSuiteSetupPage();
    includeSetupPage();
  }
  private void includeSuiteSetupPage() throws Exception {
    include(SuiteResponder.SUITE_SETUP_NAME, "-setup");
  }
  private void includeSetupPage() throws Exception {
    include("SetUp", "-setup");
  }

  private void includePageContent() throws Exception {
    newPageContent.append(pageData.getContent());
  }
  private void includeTeardownPages() throws Exception {
    includeTeardownPage();
    if (isSuite)
      includeSuiteTeardownPage();
  }

  private void includeTeardownPage() throws Exception {
    include("TearDown", "-teardown");
  }

  private void includeSuiteTeardownPage() throws Exception {
    include(SuiteResponder.SUITE_TEARDOWN_NAME, "-teardown");
  }

  private void updatePageContent() throws Exception {
    pageData.setContent(newPageContent.toString());
  }
  private void include(String pageName, String arg) throws Exception {
    WikiPage inheritedPage = findInheritedPage(pageName);
    if (inheritedPage != null) {
      String pagePathName = getPathNameForPage(inheritedPage);
      buildIncludeDirective(pagePathName, arg);
    }
  }

  private WikiPage findInheritedPage(String pageName) throws Exception {
    return PageCrawlerImpl.getInheritedPage(pageName, testPage);
  }

  private String getPathNameForPage(WikiPage page) throws Exception {
    WikiPagePath pagePath = pageCrawler.getFullPath(page);
    return PathParser.render(pagePath);
  }

  private void buildIncludeDirective(String pagePathName, String arg) {
    newPageContent
      .append("\n!include ")
```

**Đoạn mã 3-7 (tiếp theo)**
**SetupTeardownIncluder.java**

```java
      .append(arg)
      .append(" .")
      .append(pagePathName)
      .append("\n");
  }
}
```

## Tài liệu tham khảo

[KP78]: Kernighan and Plaugher, *The Elements of Programming Style*, 2d. ed., McGraw-Hill, 1978.

[PPP02]: Robert C. Martin, *Agile Software Development: Principles, Patterns, and Practices*, Prentice Hall, 2002.

[GOF]: *Design Patterns: Elements of Reusable Object Oriented Software*, Gamma et al., Addison-Wesley, 1996.

[PRAG]: *The Pragmatic Programmer*, Andrew Hunt, Dave Thomas, Addison-Wesley, 2000.

[SP72]: *Structured Programming*, O.-J. Dahl, E. W. Dijkstra, C. A. R. Hoare, Academic Press, London, 1972.

[^1]: Một công cụ kiểm thử mã nguồn mở. www.fitnese.org

[^2]: Một công cụ kiểm thử đơn vị mã nguồn mở cho Java. www.junit.org

[^3]: Tôi hỏi Kent xem anh còn giữ một bản không, nhưng anh không tìm được. Tôi cũng lục tung các máy tính cũ của mình, vô ích. Giờ chỉ còn ký ức của tôi về chương trình đó.

[^4]: Ngôn ngữ LOGO dùng từ khóa “TO” theo đúng cách Ruby và Python dùng “def”. Vì thế mọi hàm đều bắt đầu bằng chữ “TO”. Điều này có ảnh hưởng thú vị đến cách các hàm được thiết kế.

[^5]: [KP78], tr. 37.

[^6]: Và dĩ nhiên, tôi gộp cả những chuỗi if/else vào đây.

[^7]: a. http://en.wikipedia.org/wiki/Single_responsibility_principle
    b. http://www.objectmentor.com/resources/articles/srp.pdf

[^8]: a. http://en.wikipedia.org/wiki/Open/closed_principle
    b. http://www.objectmentor.com/resources/articles/ocp.pdf

[^9]: [GOF].

[^10]: Tôi vừa tái cấu trúc xong một module dùng dạng hai đối số. Tôi đã biến được outputStream thành trường của lớp và chuyển mọi lời gọi writeField sang dạng một đối số. Kết quả sạch hơn nhiều.

[^11]: Những người tưởng có thể thoát khỏi việc biên dịch lại và triển khai lại đều đã bị tìm ra và xử lý.

[^12]: Đây là một ví dụ của Nguyên lý Mở/Đóng (OCP) [PPP02].

[^13]: Nguyên lý DRY. [PRAG].

[^14]: [SP72].
