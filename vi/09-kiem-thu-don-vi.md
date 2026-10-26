# Chương 9: Kiểm thử đơn vị

Nghề của chúng ta đã tiến một chặng đường dài trong mười năm qua. Năm 1997, chưa ai nghe nói đến Phát triển hướng kiểm thử (Test Driven Development). Với đại đa số chúng ta, kiểm thử đơn vị chỉ là những đoạn mã ngắn dùng một lần, được viết ra để bảo đảm chương trình “chạy được”. Chúng ta cặm cụi viết các lớp và phương thức, rồi chế ra vài đoạn mã tùy tiện để kiểm tra chúng. Thường thì đó là một chương trình điều khiển đơn giản cho phép chúng ta tương tác thủ công với chương trình mình vừa viết.

Tôi nhớ đã viết một chương trình C++ cho hệ thống nhúng thời gian thực vào giữa thập niên 1990. Chương trình là một bộ định giờ đơn giản với khai báo sau:

```cpp
void Timer::ScheduleCommand(Command* theCommand, int milliseconds)
```

Ý tưởng rất đơn giản: phương thức execute của Command sẽ chạy trong một luồng mới sau số mili giây đã chỉ định. Vấn đề là kiểm thử nó thế nào.

Tôi chắp vá một chương trình điều khiển đơn giản để lắng nghe bàn phím. Mỗi lần có ký tự được gõ, chương trình sẽ lên lịch để gõ lại chính ký tự đó sau năm giây. Rồi tôi gõ một giai điệu có nhịp điệu trên bàn phím và chờ giai điệu phát lại trên màn hình sau năm giây.

“Em . . . muốn . . . một-cô-gái . . . giống . . . cô-gái-đã-cưới . . . người . . . cha . . . già . . . thân-yêu.”

Tôi thực sự vừa gõ phím “.” vừa hát giai điệu đó, rồi lại hát lần nữa khi các dấu chấm hiện lên trên màn hình.

Đó là bài kiểm thử của tôi! Sau khi thấy nó chạy được và trình diễn cho đồng nghiệp, tôi vứt đoạn mã kiểm thử đi.

Như tôi đã nói, nghề của chúng ta đã tiến một chặng đường dài. Ngày nay, tôi sẽ viết một bài kiểm thử bảo đảm mọi ngóc ngách của đoạn mã hoạt động đúng như mong đợi. Tôi sẽ cô lập mã của mình khỏi hệ điều hành thay vì chỉ gọi các hàm định thời chuẩn. Tôi sẽ giả lập các hàm định thời đó để kiểm soát thời gian tuyệt đối. Tôi sẽ lên lịch các lệnh đặt những cờ boolean, rồi cho thời gian tiến lên từng bước, theo dõi các cờ và xác nhận chúng chuyển từ false sang true đúng lúc tôi đưa thời gian đến giá trị tương ứng.

Sau khi có một bộ kiểm thử chạy qua, tôi sẽ bảo đảm bất cứ ai cần làm việc với đoạn mã đều có thể chạy chúng dễ dàng. Tôi sẽ bảo đảm các bài kiểm thử và mã nguồn được đưa vào cùng một gói mã nguồn.

Đúng vậy, chúng ta đã tiến xa, nhưng vẫn còn cả chặng đường phía trước. Các phong trào Agile và TDD đã khuyến khích nhiều lập trình viên viết kiểm thử đơn vị tự động, và mỗi ngày lại có thêm người tham gia. Nhưng trong cuộc chạy đua điên cuồng để đưa kiểm thử vào quy trình làm việc, nhiều lập trình viên đã bỏ qua một số điểm tinh tế và quan trọng hơn trong việc viết kiểm thử tốt.

## Ba quy luật của TDD

Đến nay, ai cũng biết TDD yêu cầu chúng ta viết kiểm thử đơn vị trước khi viết mã sản phẩm. Nhưng quy tắc đó chỉ là phần nổi của tảng băng. Hãy xem xét ba quy luật sau:¹

**Quy luật thứ nhất** Bạn không được viết mã sản phẩm cho đến khi đã viết một kiểm thử đơn vị thất bại.

**Quy luật thứ hai** Bạn không được viết thêm kiểm thử đơn vị nào ngoài mức vừa đủ để nó thất bại, và không biên dịch được cũng được xem là thất bại.

**Quy luật thứ ba** Bạn không được viết thêm mã sản phẩm nào ngoài mức vừa đủ để kiểm thử đang thất bại hiện tại chạy qua.

¹ Professionalism and Test-Driven Development, Robert C. Martin, Object Mentor, IEEE Software, May/June 2007 (Vol. 24, No. 3) pp. 32–36
http://doi.ieeecomputersociety.org/10.1109/MS.2007.85

Ba quy luật này buộc chúng ta vào một chu kỳ có lẽ chỉ dài khoảng ba mươi giây. Kiểm thử và mã sản phẩm được viết cùng nhau, trong đó phần kiểm thử chỉ đi trước mã sản phẩm vài giây.

Nếu làm theo cách này, mỗi ngày chúng ta sẽ viết hàng chục bài kiểm thử, mỗi tháng hàng trăm bài, mỗi năm hàng nghìn bài. Khi đó, các bài kiểm thử sẽ bao phủ gần như toàn bộ mã sản phẩm. Số lượng khổng lồ của chúng, có thể sánh ngang với chính mã sản phẩm, sẽ tạo ra một vấn đề quản lý đáng ngại.

## Giữ cho kiểm thử sạch

Vài năm trước, tôi được mời hướng dẫn một nhóm đã chủ động quyết định rằng mã kiểm thử không cần được duy trì theo cùng tiêu chuẩn chất lượng như mã sản phẩm. Họ cho phép nhau phá vỡ các quy tắc trong kiểm thử đơn vị. “Nhanh và bẩn” là phương châm của họ. Họ không cần đặt tên biến cho tử tế, các hàm kiểm thử không cần ngắn gọn và mô tả rõ ràng. Mã kiểm thử không cần được thiết kế tốt hay chia tách cẩn thận. Chỉ cần mã kiểm thử chạy được và bao phủ mã sản phẩm thì thế là đủ.

Một số bạn đọc đến đây có thể đồng tình với quyết định đó. Có lẽ ngày trước bạn từng viết những bài kiểm thử giống như bài tôi viết cho lớp Timer. Từ kiểu kiểm thử dùng một lần ấy đến một bộ kiểm thử đơn vị tự động là một bước tiến rất lớn. Vì thế, giống như nhóm tôi hướng dẫn, bạn có thể nghĩ rằng kiểm thử bẩn vẫn hơn là không có kiểm thử.

Điều nhóm này không nhận ra là có kiểm thử bẩn cũng chẳng khác gì, thậm chí còn tệ hơn, không có kiểm thử. Vấn đề nằm ở chỗ kiểm thử phải thay đổi khi mã sản phẩm phát triển. Kiểm thử càng bẩn thì càng khó sửa. Mã kiểm thử càng rối rắm, bạn càng có khả năng phải mất nhiều thời gian nhồi thêm kiểm thử mới vào bộ kiểm thử hơn là viết mã sản phẩm mới. Khi bạn sửa mã sản phẩm, các bài kiểm thử cũ bắt đầu thất bại, còn mớ hỗn độn trong mã kiểm thử khiến việc làm cho chúng chạy qua trở nên khó khăn. Dần dà, người ta xem các bài kiểm thử như một gánh nặng ngày càng lớn.

Qua từng bản phát hành, chi phí bảo trì bộ kiểm thử của nhóm tôi ngày càng tăng. Cuối cùng, đó trở thành điều khiến các nhà phát triển phàn nàn nhiều nhất. Khi quản lý hỏi tại sao ước lượng của họ cứ lớn mãi, các nhà phát triển đổ lỗi cho kiểm thử. Rốt cuộc, họ buộc phải loại bỏ hoàn toàn bộ kiểm thử.

Nhưng khi không còn bộ kiểm thử, họ mất khả năng bảo đảm các thay đổi trong kho mã hoạt động đúng như mong đợi. Họ không thể bảo đảm thay đổi ở một phần của hệ thống không làm hỏng những phần khác. Vì vậy, tỷ lệ lỗi bắt đầu tăng. Khi số lỗi ngoài ý muốn ngày càng nhiều, họ bắt đầu sợ thay đổi. Họ ngừng làm sạch mã sản phẩm vì sợ thay đổi sẽ gây hại nhiều hơn lợi. Mã sản phẩm bắt đầu mục ruỗng. Cuối cùng, họ chỉ còn lại một hệ thống không có kiểm thử, mã sản phẩm rối rắm đầy lỗi, khách hàng thất vọng và cảm giác rằng nỗ lực kiểm thử đã phụ lòng họ.

Theo một nghĩa nào đó, họ nói đúng. Nỗ lực kiểm thử đã phụ lòng họ. Nhưng chính quyết định cho phép kiểm thử trở nên bừa bộn đã gieo mầm cho thất bại đó. Nếu giữ cho kiểm thử sạch, nỗ lực kiểm thử của họ đã không thất bại. Tôi có thể nói điều này khá chắc chắn vì tôi từng tham gia và hướng dẫn nhiều nhóm thành công với kiểm thử đơn vị sạch.

Bài học rất đơn giản: mã kiểm thử cũng quan trọng như mã sản phẩm. Nó không phải công dân hạng hai. Nó cần được suy nghĩ, thiết kế và chăm chút. Phải giữ cho nó sạch như mã sản phẩm.

### Kiểm thử tạo điều kiện cho mọi “-ility”

Nếu không giữ cho kiểm thử sạch, bạn sẽ đánh mất chúng. Và không có chúng, bạn sẽ mất đi chính thứ giúp mã sản phẩm linh hoạt. Đúng vậy, bạn đọc không nhầm đâu. Chính kiểm thử đơn vị giúp mã của chúng ta linh hoạt, dễ bảo trì và tái sử dụng. Lý do rất đơn giản. Khi có kiểm thử, bạn không sợ thay đổi mã! Không có kiểm thử, mọi thay đổi đều có thể gây ra lỗi. Kiến trúc của bạn linh hoạt đến đâu, thiết kế được chia tách gọn gàng đến mức nào cũng vậy, nếu không có kiểm thử, bạn sẽ ngần ngại thay đổi vì sợ đưa vào những lỗi không được phát hiện.

Nhưng khi có kiểm thử, nỗi sợ đó gần như biến mất. Độ bao phủ kiểm thử càng cao, bạn càng ít sợ. Bạn có thể gần như yên tâm thay đổi cả những đoạn mã có kiến trúc chưa xuất sắc, thiết kế rối rắm và khó hiểu. Thậm chí, bạn có thể cải thiện kiến trúc và thiết kế mà không sợ hãi!

Vì vậy, có một bộ kiểm thử đơn vị tự động bao phủ mã sản phẩm là chìa khóa để giữ thiết kế và kiến trúc sạch nhất có thể. Kiểm thử tạo điều kiện cho mọi phẩm chất kết thúc bằng “-ility”, bởi kiểm thử tạo điều kiện cho thay đổi.

Nếu kiểm thử bẩn, khả năng thay đổi mã của bạn sẽ bị cản trở, và bạn dần mất khả năng cải thiện cấu trúc mã. Kiểm thử càng bẩn, mã của bạn càng bẩn. Cuối cùng, bạn mất kiểm thử và mã của bạn mục ruỗng.

## Kiểm thử sạch

Điều gì tạo nên một bài kiểm thử sạch? Ba thứ: khả năng đọc, khả năng đọc và khả năng đọc. Khả năng đọc trong kiểm thử đơn vị có lẽ còn quan trọng hơn trong mã sản phẩm. Điều gì làm cho kiểm thử dễ đọc? Cũng chính những yếu tố làm mọi đoạn mã dễ đọc: rõ ràng, đơn giản và diễn đạt cô đọng. Trong một bài kiểm thử, bạn muốn nói được nhiều nhất với số biểu thức ít nhất.

Hãy xem đoạn mã từ FitNesse trong Đoạn mã 9-1. Ba bài kiểm thử này khó hiểu và chắc chắn có thể cải thiện. Trước hết, các lời gọi addPage và assertSubString lặp lại gây trùng lặp mã [G5] rất nhiều. Quan trọng hơn, đoạn mã chứa đầy những chi tiết làm giảm sức diễn đạt của bài kiểm thử.

**Đoạn mã 9-1**
**SerializedPageResponderTest.java**

```java
public void testGetPageHieratchyAsXml() throws Exception
{
  crawler.addPage(root, PathParser.parse("PageOne"));
  crawler.addPage(root, PathParser.parse("PageOne.ChildOne"));
  crawler.addPage(root, PathParser.parse("PageTwo"));
    request.setResource("root");
    request.addInput("type", "pages");
    Responder responder = new SerializedPageResponder();
    SimpleResponse response =
     (SimpleResponse) responder.makeResponse(
        new FitNesseContext(root), request);
    String xml = response.getContent();

    assertEquals("text/xml", response.getContentType());
    assertSubString("<name>PageOne</name>", xml);
    assertSubString("<name>PageTwo</name>", xml);
    assertSubString("<name>ChildOne</name>", xml);
}

public void testGetPageHieratchyAsXmlDoesntContainSymbolicLinks()
throws Exception
{
   WikiPage pageOne = crawler.addPage(root, PathParser.parse("PageOne"));
   crawler.addPage(root, PathParser.parse("PageOne.ChildOne"));
   crawler.addPage(root, PathParser.parse("PageTwo"));

    PageData data = pageOne.getData();
    WikiPageProperties properties = data.getProperties();
    WikiPageProperty symLinks = properties.set(SymbolicPage.PROPERTY_NAME);
    symLinks.set("SymPage", "PageTwo");
    pageOne.commit(data);

    request.setResource("root");
    request.addInput("type", "pages");
    Responder responder = new SerializedPageResponder();
    SimpleResponse response =
     (SimpleResponse) responder.makeResponse(
        new FitNesseContext(root), request);
    String xml = response.getContent();
    assertEquals("text/xml", response.getContentType());
    assertSubString("<name>PageOne</name>", xml);
    assertSubString("<name>PageTwo</name>", xml);
    assertSubString("<name>ChildOne</name>", xml);
    assertNotSubString("SymPage", xml);
}

public void testGetDataAsHtml() throws Exception
{
  crawler.addPage(root, PathParser.parse("TestPageOne"), "test page");
    request.setResource("TestPageOne");
    request.addInput("type", "data");
```

**Đoạn mã 9-1 (tiếp)**
**SerializedPageResponderTest.java**

```java
     Responder responder = new SerializedPageResponder();
     SimpleResponse response =
       (SimpleResponse) responder.makeResponse(
          new FitNesseContext(root), request);
     String xml = response.getContent();
     assertEquals("text/xml", response.getContentType());
     assertSubString("test page", xml);
     assertSubString("<Test", xml);
 }
```

Chẳng hạn, hãy xem các lời gọi PathParser. Chúng chuyển chuỗi thành các đối tượng PagePath mà crawler sử dụng. Việc chuyển đổi này hoàn toàn không liên quan đến bài kiểm thử đang xét, chỉ làm lu mờ ý định. Các chi tiết quanh việc tạo responder, lấy response và ép kiểu cũng chỉ là nhiễu. Rồi còn cách dựng URL của yêu cầu rất vụng về từ một resource và một đối số nữa. (Tôi đã góp phần viết đoạn mã này, nên cứ thoải mái phê bình thẳng tay.)

Rốt cuộc, đoạn mã này không được thiết kế để người khác đọc. Người đọc tội nghiệp bị nhấn chìm trong một loạt chi tiết phải hiểu trước khi các bài kiểm thử trở nên có ý nghĩa.

Giờ hãy xem các bài kiểm thử đã cải thiện trong Đoạn mã 9-2. Chúng làm đúng những việc như cũ, nhưng đã được tái cấu trúc thành dạng gọn gàng và dễ giải thích hơn nhiều.

**Đoạn mã 9-2**
**SerializedPageResponderTest.java (đã tái cấu trúc)**

```java
public void testGetPageHierarchyAsXml() throws Exception {
  makePages("PageOne", "PageOne.ChildOne", "PageTwo");

    submitRequest("root", "type:pages");
    assertResponseIsXML();
    assertResponseContains(
       "<name>PageOne</name>", "<name>PageTwo</name>", "<name>ChildOne</name>"
    );
}

public void testSymbolicLinksAreNotInXmlPageHierarchy() throws Exception {
  WikiPage page = makePage("PageOne");
  makePages("PageOne.ChildOne", "PageTwo");

    addLinkTo(page, "PageTwo", "SymPage");

    submitRequest("root", "type:pages");
    assertResponseIsXML();
    assertResponseContains(
       "<name>PageOne</name>", "<name>PageTwo</name>", "<name>ChildOne</name>"
    );
    assertResponseDoesNotContain("SymPage");
}
```

**Đoạn mã 9-2 (tiếp)**
**SerializedPageResponderTest.java (đã tái cấu trúc)**

```java
public void testGetDataAsXml() throws Exception {
  makePageWithContent("TestPageOne", "test page");

    submitRequest("TestPageOne", "type:data");
    assertResponseIsXML();
    assertResponseContains("test page", "<Test");
}
```

Mẫu BUILD-OPERATE-CHECK² hiện lên rõ ràng qua cấu trúc của các bài kiểm thử này. Mỗi bài được chia thành ba phần rành mạch. Phần đầu dựng dữ liệu kiểm thử, phần thứ hai thao tác trên dữ liệu đó, phần thứ ba kiểm tra thao tác có tạo ra kết quả mong đợi hay không.

Hãy để ý rằng phần lớn những chi tiết gây phiền đã được loại bỏ. Các bài kiểm thử đi thẳng vào vấn đề, chỉ dùng những kiểu dữ liệu và hàm thực sự cần thiết. Ai đọc chúng cũng có thể nhanh chóng hiểu chúng làm gì, không bị chi tiết đánh lạc hướng hay nhấn chìm.

### Ngôn ngữ kiểm thử chuyên biệt theo miền

Các bài kiểm thử trong Đoạn mã 9-2 minh họa kỹ thuật xây dựng một ngôn ngữ chuyên biệt theo miền cho kiểm thử. Thay vì dùng các API mà lập trình viên sử dụng để thao tác với hệ thống, chúng ta xây dựng một tập hợp hàm và tiện ích sử dụng những API đó, giúp viết kiểm thử thuận tiện hơn và đọc dễ hơn. Các hàm và tiện ích này trở thành một API chuyên biệt được các bài kiểm thử sử dụng. Chúng tạo thành ngôn ngữ kiểm thử để lập trình viên tự viết kiểm thử và giúp những người đọc chúng về sau.

API kiểm thử này không được thiết kế từ đầu. Nó phát triển dần qua quá trình tái cấu trúc liên tục mã kiểm thử đã bị nhiễm quá nhiều chi tiết che khuất ý định. Cũng như bạn vừa thấy tôi tái cấu trúc Đoạn mã 9-1 thành Đoạn mã 9-2, những nhà phát triển có kỷ luật cũng sẽ tái cấu trúc mã kiểm thử thành các dạng ngắn gọn và giàu sức diễn đạt hơn.

### Hai tiêu chuẩn

Theo một nghĩa nào đó, nhóm tôi nhắc đến ở đầu chương đã đúng. Mã bên trong API kiểm thử có thể áp dụng một bộ tiêu chuẩn kỹ thuật khác với mã sản phẩm. Nó vẫn phải đơn giản, ngắn gọn và giàu sức diễn đạt, nhưng không nhất thiết hiệu quả như mã sản phẩm. Dù sao thì nó chạy trong môi trường kiểm thử chứ không phải môi trường sản phẩm, mà hai môi trường ấy có những yêu cầu rất khác nhau.

² http://fitnesse.org/FitNesse.AcceptanceTestPatterns

Hãy xem bài kiểm thử trong Đoạn mã 9-3. Tôi viết nó như một phần của hệ thống điều khiển môi trường mà mình đang làm thử nghiệm nguyên mẫu. Không cần biết chi tiết, bạn vẫn có thể thấy bài kiểm thử này xác nhận rằng báo động nhiệt độ thấp, bộ sưởi và quạt gió đều bật khi nhiệt độ “quá lạnh”.

**Đoạn mã 9-3**
**EnvironmentControllerTest.java**

```java
@Test
  public void turnOnLoTempAlarmAtThreashold() throws Exception {
    hw.setTemp(WAY_TOO_COLD);
    controller.tic();
    assertTrue(hw.heaterState());
    assertTrue(hw.blowerState());
    assertFalse(hw.coolerState());
    assertFalse(hw.hiTempAlarm());
    assertTrue(hw.loTempAlarm());
  }
```

Dĩ nhiên ở đây có nhiều chi tiết. Chẳng hạn, hàm tic dùng để làm gì? Thực ra, tôi muốn bạn đừng bận tâm đến điều đó khi đọc bài kiểm thử này. Tôi chỉ muốn bạn xem trạng thái cuối cùng của hệ thống có nhất quán với mức nhiệt “quá lạnh” hay không.

Khi đọc bài kiểm thử, hãy để ý mắt bạn phải liên tục qua lại giữa tên trạng thái được kiểm tra và ý nghĩa của phép kiểm tra đó. Bạn thấy heaterState, rồi mắt lướt sang trái đến assertTrue. Bạn thấy coolerState, mắt lại phải lần sang trái đến assertFalse. Việc này vừa tẻ nhạt vừa dễ sai, khiến bài kiểm thử khó đọc.

Tôi cải thiện đáng kể khả năng đọc của bài kiểm thử này bằng cách chuyển nó thành Đoạn mã 9-4.

**Đoạn mã 9-4**
**EnvironmentControllerTest.java (đã tái cấu trúc)**

```java
@Test
  public void turnOnLoTempAlarmAtThreshold() throws Exception {
    wayTooCold();
    assertEquals("HBchL", hw.getState());
  }
```

Dĩ nhiên, tôi đã che giấu chi tiết của hàm tic bằng cách tạo ra hàm wayTooCold. Nhưng điều đáng chú ý là chuỗi kỳ lạ trong assertEquals. Chữ hoa nghĩa là “bật”, chữ thường nghĩa là “tắt”, và các chữ cái luôn theo thứ tự sau: {heater, blower, cooler, hi-temp-alarm, lo-temp-alarm}.

Dù cách này gần như vi phạm quy tắc tránh buộc người đọc tự ánh xạ trong đầu,³ nhưng trong trường hợp này có vẻ phù hợp. Khi đã biết ý nghĩa, bạn sẽ lướt mắt qua chuỗi đó và nhanh chóng hiểu kết quả. Đọc bài kiểm thử gần như trở thành niềm vui. Hãy xem Đoạn mã 9-5 để thấy các bài kiểm thử này dễ hiểu đến mức nào.

³ “Tránh ánh xạ trong đầu” ở trang 25.

**Đoạn mã 9-5**
**EnvironmentControllerTest.java (tuyển chọn lớn hơn)**

```java
@Test
  public void turnOnCoolerAndBlowerIfTooHot() throws Exception {
    tooHot();
    assertEquals("hBChl", hw.getState());
  }

  @Test
  public void turnOnHeaterAndBlowerIfTooCold() throws Exception {
    tooCold();
    assertEquals("HBchl", hw.getState());
  }

  @Test
  public void turnOnHiTempAlarmAtThreshold() throws Exception {
    wayTooHot();
    assertEquals("hBCHl", hw.getState());
  }
  @Test
  public void turnOnLoTempAlarmAtThreshold() throws Exception {
    wayTooCold();
    assertEquals("HBchL", hw.getState());
  }
```

Hàm getState được trình bày trong Đoạn mã 9-6. Hãy chú ý, đây không phải đoạn mã hiệu quả lắm. Muốn nó hiệu quả hơn, có lẽ tôi nên dùng StringBuffer.

**Đoạn mã 9-6**
**MockControlHardware.java**

```java
public String getState() {
    String state = "";
    state += heater ? "H" : "h";
    state += blower ? "B" : "b";
    state += cooler ? "C" : "c";
    state += hiTempAlarm ? "H" : "h";
    state += loTempAlarm ? "L" : "l";
    return state;
  }
```

StringBuffer hơi xấu. Ngay cả trong mã sản phẩm, nếu chi phí nhỏ, tôi cũng tránh dùng chúng; và bạn có thể lập luận rằng chi phí của đoạn mã trong Đoạn mã 9-6 rất thấp. Tuy nhiên, ứng dụng này rõ ràng là một hệ thống nhúng thời gian thực, và nhiều khả năng tài nguyên máy tính cũng như bộ nhớ rất hạn chế. Còn môi trường kiểm thử thì có lẽ chẳng bị giới hạn gì đáng kể.

Đó là bản chất của hai tiêu chuẩn. Có những điều bạn có thể chẳng bao giờ làm trong môi trường sản phẩm nhưng lại hoàn toàn ổn trong môi trường kiểm thử. Thường thì chúng liên quan đến hiệu quả sử dụng bộ nhớ hoặc CPU. Nhưng chúng không bao giờ liên quan đến độ sạch của mã.

## Mỗi bài kiểm thử một assert

Có một trường phái tư tưởng⁴ cho rằng mỗi hàm kiểm thử trong một bài kiểm thử JUnit chỉ nên có đúng một câu lệnh assert. Quy tắc này nghe có vẻ hà khắc, nhưng ưu điểm của nó thể hiện trong Đoạn mã 9-5. Mỗi bài kiểm thử đi đến một kết luận duy nhất, nhanh chóng và dễ hiểu.

Còn Đoạn mã 9-2 thì sao? Có vẻ khó mà dễ dàng gộp xác nhận đầu ra là XML với xác nhận đầu ra chứa những chuỗi con nhất định. Tuy nhiên, chúng ta có thể tách bài kiểm thử thành hai bài riêng, mỗi bài có một xác nhận cụ thể, như trong Đoạn mã 9-7.

**Đoạn mã 9-7**
**SerializedPageResponderTest.java (một assert)**

```java
public void testGetPageHierarchyAsXml() throws Exception {
    givenPages("PageOne", "PageOne.ChildOne", "PageTwo");

      whenRequestIsIssued("root", "type:pages");
      thenResponseShouldBeXML();
  }

  public void testGetPageHierarchyHasRightTags() throws Exception {
    givenPages("PageOne", "PageOne.ChildOne", "PageTwo");
      whenRequestIsIssued("root", "type:pages");

      thenResponseShouldContain(
         "<name>PageOne</name>", "<name>PageTwo</name>", "<name>ChildOne</name>"
      );
  }
```

Hãy để ý tôi đã đổi tên các hàm theo quy ước given-when-then phổ biến.⁵ Điều này giúp đọc kiểm thử dễ hơn nữa. Đáng tiếc là việc chia tách như trên tạo ra nhiều mã trùng lặp.

Chúng ta có thể loại bỏ phần trùng lặp bằng cách dùng mẫu TEMPLATE METHOD⁶, đưa các phần given/when vào lớp cơ sở và đặt phần then trong các lớp dẫn xuất khác nhau. Hoặc ta có thể tạo hẳn một lớp kiểm thử riêng, đặt phần given và when trong hàm @Before, rồi đặt phần then trong từng hàm @Test. Nhưng với một vấn đề nhỏ như vậy, cách đó có vẻ tạo ra quá nhiều cơ chế. Cuối cùng, tôi thích dùng nhiều assert trong Đoạn mã 9-2 hơn.

⁴ Xem bài đăng trên blog của Dave Astel: http://www.artima.com/weblogs/viewpost.jsp?thread=35578
⁵ [RSpec].
⁶ [GOF].

Tôi nghĩ quy tắc một assert là một nguyên tắc hữu ích.⁷ Thường thì tôi cố gắng tạo một ngôn ngữ kiểm thử chuyên biệt theo miền hỗ trợ quy tắc đó, như trong Đoạn mã 9-5. Nhưng tôi không ngại đặt nhiều hơn một assert trong một bài kiểm thử. Có lẽ cách diễn đạt tốt nhất là nên giảm thiểu số lượng assert trong mỗi bài kiểm thử.

⁷ “Bám sát mã!”

### Mỗi bài kiểm thử một khái niệm

Có lẽ quy tắc tốt hơn là mỗi hàm kiểm thử chỉ nên kiểm tra một khái niệm. Ta không muốn những hàm kiểm thử dài, lần lượt kiểm tra hết thứ linh tinh này đến thứ linh tinh khác. Đoạn mã 9-8 là ví dụ về một bài kiểm thử như vậy. Nên tách nó thành ba bài kiểm thử độc lập vì nó kiểm tra ba việc riêng biệt. Gộp tất cả vào cùng một hàm buộc người đọc phải tìm hiểu lý do từng phần có mặt và mỗi phần đang kiểm tra điều gì.

**Đoạn mã 9-8**

```java
      /**
       * Miscellaneous tests for the addMonths() method.
       */
      public void testAddMonths() {
          SerialDate d1 = SerialDate.createInstance(31, 5, 2004);

            SerialDate d2 = SerialDate.addMonths(1, d1);
            assertEquals(30, d2.getDayOfMonth());
            assertEquals(6, d2.getMonth());
            assertEquals(2004, d2.getYYYY());
            SerialDate d3 = SerialDate.addMonths(2, d1);
            assertEquals(31, d3.getDayOfMonth());
            assertEquals(7, d3.getMonth());
            assertEquals(2004, d3.getYYYY());

            SerialDate d4 = SerialDate.addMonths(1, SerialDate.addMonths(1, d1));
            assertEquals(30, d4.getDayOfMonth());
            assertEquals(7, d4.getMonth());
            assertEquals(2004, d4.getYYYY());
      }
```

Có lẽ ba hàm kiểm thử nên được viết như sau:

- Cho ngày cuối cùng của một tháng có 31 ngày, chẳng hạn tháng Năm:

  1. Khi cộng thêm một tháng, mà tháng mới kết thúc vào ngày 30, chẳng hạn tháng Sáu, ngày phải là 30 chứ không phải 31.
  2. Khi cộng thêm hai tháng vào ngày đó, để tháng cuối cùng có 31 ngày, ngày phải là 31.

- Cho ngày cuối cùng của một tháng có 30 ngày, chẳng hạn tháng Sáu:

  1. Khi cộng thêm một tháng để tháng mới có ngày cuối cùng là ngày 31, ngày phải là 30 chứ không phải 31.

Diễn đạt như vậy, bạn sẽ thấy có một quy tắc chung ẩn trong các bài kiểm thử linh tinh này. Khi tăng tháng, ngày không thể lớn hơn ngày cuối cùng của tháng đó. Điều này hàm ý rằng tăng tháng từ ngày 28 tháng Hai sẽ cho ra ngày 28 tháng Ba. Bài kiểm thử đó còn thiếu và sẽ rất hữu ích nếu được viết thêm.

Vì vậy, vấn đề không nằm ở chỗ mỗi phần của Đoạn mã 9-8 có nhiều assert. Vấn đề là có nhiều khái niệm được kiểm tra. Quy tắc tốt nhất có lẽ là giảm số assert cho mỗi khái niệm và chỉ kiểm tra một khái niệm trong mỗi hàm kiểm thử.

## F.I.R.S.T.⁸

Kiểm thử sạch tuân theo năm quy tắc khác, tạo thành từ viết tắt trên:

**Nhanh (Fast)** Kiểm thử phải nhanh. Chúng phải chạy nhanh chóng. Khi kiểm thử chạy chậm, bạn sẽ không muốn chạy thường xuyên. Nếu không chạy thường xuyên, bạn sẽ không phát hiện vấn đề đủ sớm để sửa dễ dàng. Bạn sẽ không còn thoải mái làm sạch mã. Cuối cùng, mã sẽ bắt đầu mục ruỗng.

**Độc lập (Independent)** Các bài kiểm thử không nên phụ thuộc lẫn nhau. Một bài không nên chuẩn bị điều kiện cho bài tiếp theo. Bạn phải có thể chạy từng bài độc lập và chạy theo bất cứ thứ tự nào mình muốn. Khi các bài kiểm thử phụ thuộc lẫn nhau, bài đầu tiên thất bại sẽ gây ra hàng loạt lỗi dây chuyền ở các bài sau, khiến việc chẩn đoán khó khăn và che giấu những lỗi tiếp theo.

**Có thể lặp lại (Repeatable)** Kiểm thử phải có thể lặp lại trong mọi môi trường. Bạn phải chạy được chúng trong môi trường sản phẩm, môi trường QA và trên máy tính xách tay khi đang đi tàu về nhà mà không có mạng. Nếu không thể lặp lại kiểm thử trong mọi môi trường, bạn sẽ luôn có cớ để giải thích tại sao chúng thất bại. Bạn cũng sẽ thấy mình không thể chạy kiểm thử khi môi trường không sẵn sàng.

**Tự xác nhận (Self-Validating)** Kiểm thử phải cho kết quả boolean. Hoặc đạt, hoặc thất bại. Bạn không nên phải đọc tệp log để biết kiểm thử có đạt hay không. Bạn không nên phải tự so sánh hai tệp văn bản khác nhau để biết kết quả. Nếu kiểm thử không tự xác nhận, việc thất bại có thể trở thành chuyện chủ quan và chạy kiểm thử có thể đòi hỏi một quá trình đánh giá thủ công dài dòng.

⁸ Tài liệu đào tạo của Object Mentor.

**Đúng lúc (Timely)** Kiểm thử phải được viết đúng lúc. Kiểm thử đơn vị nên được viết ngay trước mã sản phẩm giúp chúng chạy qua. Nếu viết kiểm thử sau mã sản phẩm, bạn có thể thấy mã sản phẩm khó kiểm thử. Bạn có thể quyết định rằng một số mã sản phẩm quá khó kiểm thử. Bạn có thể không thiết kế mã sản phẩm sao cho có thể kiểm thử được.

## Kết luận

Chúng ta mới chỉ chạm nhẹ vào chủ đề này. Thật vậy, tôi nghĩ có thể viết hẳn một cuốn sách về kiểm thử sạch. Kiểm thử quan trọng đối với sức khỏe của một dự án chẳng kém mã sản phẩm. Có lẽ chúng còn quan trọng hơn, vì kiểm thử gìn giữ và tăng cường tính linh hoạt, khả năng bảo trì và khả năng tái sử dụng của mã sản phẩm. Vì vậy, hãy luôn giữ cho kiểm thử sạch. Hãy làm cho chúng giàu sức diễn đạt và ngắn gọn. Hãy tạo ra các API kiểm thử đóng vai trò như ngôn ngữ chuyên biệt theo miền, giúp bạn viết kiểm thử.

Nếu để kiểm thử mục ruỗng, mã của bạn cũng sẽ mục ruỗng. Hãy giữ cho kiểm thử sạch.

## Tài liệu tham khảo

[RSpec]: RSpec: Behavior Driven Development for Ruby Programmers, Aslak Hellesøy, David Chelimsky, Pragmatic Bookshelf, 2008.

[GOF]: Design Patterns: Elements of Reusable Object Oriented Software, Gamma et al., Addison-Wesley, 1996.
