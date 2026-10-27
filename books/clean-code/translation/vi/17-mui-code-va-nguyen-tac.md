# Chương 17: Mùi code và nguyên tắc kinh nghiệm

Trong cuốn sách tuyệt vời *Refactoring*,¹ Martin Fowler đã nhận diện nhiều “mùi code”. Danh sách dưới đây gồm nhiều mùi code của Martin, đồng thời bổ sung thêm nhiều mùi do tôi tự nhận ra. Danh sách cũng có những điều đúc kết và nguyên tắc kinh nghiệm khác mà tôi dùng trong nghề.

¹. [Refactoring].

Tôi biên soạn danh sách này bằng cách xem qua một số chương trình khác nhau và tái cấu trúc chúng. Mỗi khi thực hiện một thay đổi, tôi tự hỏi vì sao mình làm thế rồi ghi lại lý do ở đây. Kết quả là một danh sách khá dài những điều khiến tôi thấy code có mùi khi đọc.

Danh sách này được sắp xếp để đọc từ trên xuống, đồng thời cũng dùng làm tài liệu tra cứu. Mỗi nguyên tắc kinh nghiệm đều có dẫn chiếu chéo, cho biết nó được nhắc đến ở đâu trong phần còn lại của sách, tại “Phụ lục C” ở trang 409.

## Chú thích

### C1: Thông tin không phù hợp

Chú thích không nên chứa những thông tin phù hợp hơn với một hệ thống khác, chẳng hạn hệ thống quản lý mã nguồn, hệ thống theo dõi vấn đề hay bất kỳ hệ thống lưu trữ hồ sơ nào khác. Ví dụ, lịch sử thay đổi chỉ khiến tệp mã nguồn rối thêm bởi những khối văn bản dài dòng, chẳng mấy thú vị. Nói chung, siêu dữ liệu như tác giả, ngày sửa đổi gần nhất, mã SPR, v.v. không nên xuất hiện trong chú thích. Chú thích nên dành cho các ghi chú kỹ thuật về mã và thiết kế.

### C2: Chú thích lỗi thời

Một chú thích đã cũ, không còn liên quan và sai lệch là chú thích lỗi thời. Chú thích nhanh chóng trở nên cũ. Tốt nhất đừng viết chú thích sẽ lỗi thời. Nếu phát hiện chú thích lỗi thời, hãy cập nhật hoặc xóa nó càng sớm càng tốt. Chú thích lỗi thời thường tách rời khỏi đoạn mã mà ban đầu nó mô tả, rồi biến thành những hòn đảo lơ lửng, chẳng còn liên quan và chỉ dẫn sai trong mã.

### C3: Chú thích thừa

Một chú thích là thừa nếu nó mô tả điều vốn đã tự nói lên đầy đủ. Ví dụ:

```java
i++; // tăng i
```

Một ví dụ khác là Javadoc không nói gì hơn (thậm chí còn ít hơn) chữ ký hàm:

```java
/**
 * @param sellRequest
 * @return
 * @throws ManagedComponentException
 */
public SellResponse beginSellItem(SellRequest sellRequest)
  throws ManagedComponentException
```

Chú thích nên nói những điều mà bản thân mã không thể nói.

### C4: Chú thích viết kém

Chú thích đáng để viết thì cũng đáng được viết cho tốt. Nếu định viết chú thích, hãy dành thời gian để viết câu tốt nhất có thể. Chọn từ cẩn thận. Dùng ngữ pháp và dấu câu chính xác. Đừng lan man. Đừng nói điều hiển nhiên. Hãy ngắn gọn.

### C5: Mã bị chú thích vô hiệu hóa

Tôi phát điên khi thấy những đoạn mã bị chú thích vô hiệu hóa. Ai biết chúng đã cũ đến mức nào? Ai biết chúng còn ý nghĩa hay không? Vậy mà chẳng ai xóa, vì ai cũng cho rằng người khác cần đến chúng hoặc đang có kế hoạch dùng chúng.

Đoạn mã ấy cứ nằm đó mục ruỗng, ngày qua ngày càng ít liên quan hơn. Nó gọi những hàm không còn tồn tại. Nó dùng những biến đã đổi tên. Nó tuân theo những quy ước lỗi thời từ lâu. Nó làm ô nhiễm các mô-đun chứa nó và khiến người đọc mất tập trung. Mã bị chú thích vô hiệu hóa là một tai họa.

Thấy mã bị chú thích vô hiệu hóa thì xóa đi! Đừng lo, hệ thống quản lý mã nguồn vẫn lưu nó. Nếu ai đó thật sự cần, họ có thể quay lại lấy phiên bản cũ. Đừng để mã bị chú thích vô hiệu hóa sống sót.

## Môi trường

### E1: Build cần nhiều hơn một bước

Build một dự án phải là thao tác đơn giản, chỉ cần một bước. Bạn không nên phải lấy nhiều mảnh nhỏ từ hệ thống quản lý mã nguồn. Bạn cũng không nên cần một chuỗi lệnh bí hiểm hay các script phụ thuộc vào ngữ cảnh để build từng thành phần. Bạn không nên phải tìm khắp nơi những JAR, tệp XML và tạo tác phụ nhỏ mà hệ thống cần. Bạn cần có thể lấy mã hệ thống bằng một lệnh đơn giản, rồi chạy một lệnh đơn giản khác để build nó.

```sh
svn get mySystem
cd mySystem
ant all
```

### E2: Kiểm thử cần nhiều hơn một bước

Bạn cần có thể chạy toàn bộ kiểm thử đơn vị chỉ bằng một lệnh. Tốt nhất là chạy tất cả kiểm thử bằng cách bấm một nút trong IDE. Tệ nhất thì bạn cũng phải chạy được chúng bằng một lệnh đơn giản trong shell. Chạy được toàn bộ kiểm thử là điều cơ bản và quan trọng đến mức thao tác này phải nhanh, dễ và hiển nhiên.

## Hàm

### F1: Quá nhiều đối số

Hàm nên có ít đối số. Tốt nhất là không có đối số, kế đến là một, hai rồi ba. Nhiều hơn ba là rất đáng ngờ và nên kiên quyết tránh. (Xem “Đối số của hàm” ở trang 40.)

### F2: Đối số đầu ra

Đối số đầu ra trái với trực giác. Người đọc mong đợi đối số là đầu vào, không phải đầu ra. Nếu hàm phải thay đổi trạng thái của thứ gì đó, hãy để nó thay đổi trạng thái của đối tượng mà nó được gọi trên đó. (Xem “Đối số đầu ra” ở trang 45.)

### F3: Đối số cờ

Đối số Boolean nói rõ rằng hàm làm nhiều hơn một việc. Chúng gây khó hiểu và nên bị loại bỏ. (Xem “Đối số cờ” ở trang 41.)

### F4: Hàm chết

Các phương thức không bao giờ được gọi nên bị loại bỏ. Giữ mã chết chỉ gây lãng phí. Đừng ngại xóa hàm. Hãy nhớ hệ thống quản lý mã nguồn vẫn lưu nó.

## Tổng quát

### G1: Nhiều ngôn ngữ trong cùng một tệp mã nguồn

Các môi trường lập trình hiện đại ngày nay cho phép đặt nhiều ngôn ngữ khác nhau vào cùng một tệp mã nguồn. Chẳng hạn, một tệp Java có thể chứa các đoạn XML, HTML, YAML, JavaDoc, tiếng Anh, JavaScript, v.v. Một ví dụ khác, ngoài HTML, tệp JSP có thể chứa Java, cú pháp thư viện thẻ, chú thích tiếng Anh, Javadoc, XML, JavaScript, v.v. Trường hợp tốt nhất thì việc này gây khó hiểu, tệ nhất là cẩu thả.

Lý tưởng nhất là một tệp mã nguồn chỉ chứa đúng một ngôn ngữ. Trên thực tế, có lẽ ta sẽ phải dùng nhiều hơn một. Nhưng nên cố gắng giảm cả số lượng lẫn phạm vi của các ngôn ngữ bổ sung trong tệp mã nguồn.

### G2: Hành vi hiển nhiên chưa được triển khai

Theo “Nguyên tắc ít gây ngạc nhiên nhất”,² mọi hàm hay lớp nên triển khai những hành vi mà một lập trình viên khác có thể hợp lý mong đợi. Ví dụ, hãy xét một hàm chuyển tên ngày trong tuần thành enum biểu diễn ngày đó.

```java
Day day = DayDate.StringToDay(String dayName);
```

Ta mong chuỗi `"Monday"` được chuyển thành `Day.MONDAY`. Ta cũng mong các dạng viết tắt thông dụng được chuyển đổi và hàm không phân biệt chữ hoa chữ thường.

Khi một hành vi hiển nhiên không được triển khai, người đọc và người dùng mã không còn có thể dựa vào trực giác về tên hàm. Họ mất lòng tin vào tác giả ban đầu và phải quay lại đọc chi tiết mã.

². Còn gọi là “Nguyên tắc ít gây kinh ngạc nhất”: http://en.wikipedia.org/wiki/Principle_of_least_astonishment

### G3: Hành vi sai ở các ranh giới

Nói rằng mã phải hoạt động chính xác nghe có vẻ hiển nhiên. Vấn đề là chúng ta hiếm khi nhận ra hành vi chính xác phức tạp đến mức nào. Lập trình viên thường viết hàm mà họ nghĩ sẽ chạy đúng, rồi tin vào trực giác thay vì bỏ công chứng minh mã hoạt động trong mọi trường hợp góc và ranh giới.

Không gì thay thế được sự cẩn trọng cần thiết. Mỗi điều kiện biên, mỗi trường hợp góc, mỗi tình huống bất thường và ngoại lệ đều có thể phá hỏng một thuật toán tưởng như tao nhã, hợp lý. Đừng dựa vào trực giác. Hãy tìm từng điều kiện biên và viết kiểm thử cho nó.

### G4: Vô hiệu hóa các cơ chế an toàn

Thảm họa Chernobyl xảy ra vì người quản lý nhà máy lần lượt vô hiệu hóa từng cơ chế an toàn. Các cơ chế đó gây bất tiện khi tiến hành một thí nghiệm. Kết quả là thí nghiệm không được thực hiện, và thế giới chứng kiến thảm họa hạt nhân dân sự lớn đầu tiên.

Vô hiệu hóa cơ chế an toàn rất rủi ro. Có thể cần kiểm soát thủ công `serialVersionUID`, nhưng việc đó luôn nguy hiểm. Tắt một số cảnh báo của trình biên dịch (hoặc tắt hết!) có thể giúp build thành công, nhưng đổi lại là nguy cơ phải ngồi gỡ lỗi triền miên. Tắt các kiểm thử đang thất bại rồi tự nhủ sẽ làm chúng chạy qua sau cũng tệ như nghĩ thẻ tín dụng là tiền miễn phí.

### G5: Trùng lặp

Đây là một trong những quy tắc quan trọng nhất trong sách, bạn nên xem nó thật nghiêm túc. Hầu như tác giả nào viết về thiết kế phần mềm cũng nhắc đến quy tắc này. Dave Thomas và Andy Hunt gọi đó là nguyên tắc DRY³ (Đừng lặp lại chính mình). Kent Beck đưa nó thành một trong những nguyên tắc cốt lõi của Extreme Programming và gọi là: “Một lần, và chỉ một lần.” Ron Jeffries xếp quy tắc này ở vị trí thứ hai, chỉ sau việc làm cho mọi kiểm thử đều chạy qua.

Mỗi lần thấy mã bị trùng lặp, đó là cơ hội trừu tượng hóa đã bị bỏ lỡ. Phần mã lặp có lẽ có thể trở thành một hàm con hoặc thậm chí một lớp riêng. Gom phần trùng lặp vào một cấu trúc trừu tượng như vậy sẽ làm giàu vốn từ vựng trong thiết kế của bạn. Các lập trình viên khác có thể dùng những cấu trúc trừu tượng bạn tạo ra. Việc viết mã sẽ nhanh hơn và ít lỗi hơn vì bạn đã nâng mức trừu tượng.

Dạng trùng lặp dễ thấy nhất là những khối mã giống hệt nhau, trông như thể ai đó rê chuột rồi dán cùng một đoạn mã hết lần này đến lần khác. Nên thay chúng bằng các phương thức đơn giản.

Dạng kín đáo hơn là chuỗi switch/case hoặc if/else xuất hiện lặp đi lặp lại ở nhiều mô-đun, lần nào cũng kiểm tra cùng một tập điều kiện. Nên thay chúng bằng đa hình.

Kín đáo hơn nữa là những mô-đun có thuật toán tương tự nhau nhưng không dùng chung các dòng mã giống nhau. Đó vẫn là trùng lặp và cần được xử lý bằng mẫu TEMPLATE METHOD⁴ hoặc STRATEGY.⁵

Thật vậy, hầu hết mẫu thiết kế xuất hiện trong mười lăm năm qua chỉ là những cách quen thuộc để loại bỏ trùng lặp. Các dạng chuẩn Codd cũng là một chiến lược loại bỏ trùng lặp trong lược đồ cơ sở dữ liệu. Bản thân lập trình hướng đối tượng cũng là một chiến lược tổ chức mô-đun và loại bỏ trùng lặp. Lập trình cấu trúc cũng vậy, chẳng có gì đáng ngạc nhiên.

Tôi nghĩ đã nói đủ. Hãy tìm và loại bỏ trùng lặp ở bất cứ đâu có thể.

³. [PRAG].
⁴. [GOF].
⁵. [GOF].

### G6: Mã ở sai mức trừu tượng

Điều quan trọng là tạo ra các cấu trúc trừu tượng để tách những khái niệm tổng quát ở mức cao khỏi các chi tiết ở mức thấp. Đôi khi ta làm vậy bằng cách tạo lớp trừu tượng chứa các khái niệm mức cao và các lớp dẫn xuất chứa khái niệm mức thấp. Khi đó, cần bảo đảm sự phân tách hoàn chỉnh: mọi khái niệm mức thấp nằm trong các lớp dẫn xuất, còn mọi khái niệm mức cao nằm trong lớp cơ sở.

Chẳng hạn, các hằng, biến hay hàm tiện ích chỉ liên quan đến phần triển khai chi tiết không nên có mặt trong lớp cơ sở. Lớp cơ sở không nên biết gì về chúng.

Quy tắc này cũng áp dụng cho tệp mã nguồn, thành phần và mô-đun. Thiết kế phần mềm tốt đòi hỏi ta tách các khái niệm ở những mức khác nhau và đặt chúng vào những nơi chứa khác nhau. Những nơi chứa đó đôi khi là lớp cơ sở hay lớp dẫn xuất, đôi khi là tệp mã nguồn, mô-đun hoặc thành phần. Dù dùng loại nào, sự phân tách phải hoàn chỉnh. Ta không muốn trộn lẫn khái niệm mức thấp với mức cao.

Hãy xem đoạn mã sau:

```java
public interface Stack {
  Object pop() throws EmptyException;
  void push(Object o) throws FullException;
  double percentFull();

  class EmptyException extends Exception {}
  class FullException extends Exception {}
}
```

Hàm `percentFull` nằm sai mức trừu tượng. Nhiều cách triển khai Stack có thể xem khái niệm độ đầy là hợp lý, nhưng cũng có những cách triển khai không thể biết mình đầy đến đâu. Vì vậy, nên đặt hàm này trong một giao diện dẫn xuất như `BoundedStack`.

Có thể bạn nghĩ rằng khi ngăn xếp không giới hạn, cách triển khai chỉ cần trả về 0. Vấn đề là không có ngăn xếp nào thực sự không giới hạn. Kiểm tra

```java
stack.percentFull() < 50.0
```

cũng chẳng thể ngăn được `OutOfMemoryException`. Cài đặt hàm để nó trả về 0 tức là nói dối.

Bạn không thể nói dối hay giả vờ để chữa một cấu trúc trừu tượng đặt sai chỗ. Tách biệt các cấu trúc trừu tượng là một trong những việc khó nhất mà nhà phát triển phần mềm phải làm, và khi làm sai thì chẳng có cách sửa nhanh nào.

### G7: Lớp cơ sở phụ thuộc vào lớp dẫn xuất

Lý do phổ biến nhất để chia các khái niệm thành lớp cơ sở và lớp dẫn xuất là giúp các khái niệm mức cao trong lớp cơ sở độc lập với các khái niệm mức thấp trong lớp dẫn xuất. Vì thế, khi thấy lớp cơ sở nhắc đến tên các lớp dẫn xuất, ta nên nghi ngờ có vấn đề. Nói chung, lớp cơ sở không nên biết gì về các lớp dẫn xuất.

Dĩ nhiên, quy tắc này có ngoại lệ. Đôi khi số lớp dẫn xuất được cố định chặt chẽ, và lớp cơ sở có mã để chọn giữa chúng. Ta thường thấy điều này trong các cách triển khai máy trạng thái hữu hạn. Tuy nhiên, trong trường hợp ấy, lớp dẫn xuất và lớp cơ sở phụ thuộc chặt chẽ vào nhau, đồng thời luôn được triển khai cùng nhau trong một tệp JAR. Nói chung, ta muốn có thể triển khai lớp dẫn xuất và lớp cơ sở trong các tệp JAR riêng.

Việc triển khai lớp dẫn xuất và lớp cơ sở trong các tệp JAR riêng, đồng thời bảo đảm các tệp JAR chứa lớp cơ sở không biết gì về nội dung của các tệp JAR chứa lớp dẫn xuất, cho phép ta triển khai hệ thống thành những thành phần riêng biệt, độc lập. Khi sửa đổi các thành phần đó, ta có thể triển khai lại chúng mà không phải triển khai lại các thành phần cơ sở. Nhờ vậy, tác động của thay đổi giảm đáng kể và việc bảo trì hệ thống đang vận hành cũng đơn giản hơn nhiều.

### G8: Quá nhiều thông tin

Mô-đun được định nghĩa tốt có giao diện rất nhỏ, cho phép làm được nhiều việc với ít thao tác. Mô-đun được định nghĩa kém có giao diện rộng và phức tạp, buộc bạn phải dùng nhiều thao tác khác nhau để làm những việc đơn giản. Giao diện được định nghĩa tốt không cung cấp nhiều hàm để phụ thuộc vào, nên sự phụ thuộc thấp. Giao diện được định nghĩa kém có nhiều hàm bạn phải gọi, nên sự phụ thuộc cao.

Nhà phát triển phần mềm giỏi học cách giới hạn những gì họ để lộ qua giao diện của lớp và mô-đun. Một lớp càng có ít phương thức càng tốt. Một hàm càng biết ít biến càng tốt. Một lớp càng có ít biến thực thể càng tốt.

Hãy ẩn dữ liệu. Ẩn các hàm tiện ích. Ẩn các hằng và biến tạm. Đừng tạo lớp có quá nhiều phương thức hay biến thực thể. Đừng tạo nhiều biến và hàm `protected` cho các lớp con. Hãy tập trung giữ giao diện thật gọn và nhỏ. Giới hạn thông tin để giúp giảm sự phụ thuộc.

### G9: Mã chết

Mã chết là mã không được thực thi. Bạn có thể thấy nó trong thân một câu lệnh if kiểm tra điều kiện không thể xảy ra. Bạn cũng có thể thấy nó trong khối catch của một try không bao giờ ném ngoại lệ, trong những hàm tiện ích nhỏ không bao giờ được gọi, hoặc trong các nhánh switch/case không bao giờ xảy ra.

Vấn đề là mã chết bắt đầu có mùi sau một thời gian. Càng cũ, mùi càng nồng và chua. Đó là vì khi thiết kế thay đổi, mã chết không được cập nhật đầy đủ. Nó vẫn biên dịch được nhưng không theo những quy ước hay quy tắc mới hơn. Nó được viết khi hệ thống còn khác. Khi tìm thấy mã chết, hãy làm điều đúng đắn: chôn cất tử tế. Xóa nó khỏi hệ thống.

### G10: Tách biệt theo chiều dọc

Biến và hàm nên được định nghĩa gần nơi chúng được dùng. Biến cục bộ nên được khai báo ngay trước lần sử dụng đầu tiên và có phạm vi theo chiều dọc ngắn. Ta không muốn biến cục bộ được khai báo cách chỗ sử dụng hàng trăm dòng.

Hàm riêng nên được định nghĩa ngay dưới chỗ sử dụng đầu tiên. Hàm riêng thuộc phạm vi của cả lớp, nhưng ta vẫn muốn giới hạn khoảng cách theo chiều dọc giữa chỗ gọi và chỗ định nghĩa. Tìm một hàm riêng chỉ nên cần rà xuống dưới từ lần sử dụng đầu tiên.

### G11: Không nhất quán

Nếu làm một việc theo cách nào đó, hãy làm mọi việc tương tự theo cùng cách. Điều này bắt nguồn từ nguyên tắc ít gây ngạc nhiên nhất. Hãy cẩn thận khi chọn quy ước và một khi đã chọn thì cần tiếp tục tuân theo.

Nếu trong một hàm bạn dùng biến tên `response` để chứa một `HttpServletResponse`, hãy dùng nhất quán cùng tên biến trong những hàm khác có dùng đối tượng `HttpServletResponse`. Nếu bạn đặt tên phương thức là `processVerificationRequest`, hãy dùng tên tương tự như `processDeletionRequest` cho các phương thức xử lý những loại yêu cầu khác.

Sự nhất quán đơn giản như vậy, nếu được áp dụng đều đặn, có thể giúp mã dễ đọc và sửa đổi hơn nhiều.

### G12: Rác

Một hàm khởi tạo mặc định không có phần triển khai thì có ích gì? Nó chỉ khiến mã thêm lộn xộn với những thứ vô nghĩa. Biến không được dùng, hàm không bao giờ được gọi, chú thích không cung cấp thông tin, v.v. Tất cả đều là rác và nên bị loại bỏ. Hãy giữ tệp mã nguồn sạch sẽ, ngăn nắp, không có rác.

### G13: Tạo sự phụ thuộc nhân tạo

Những thứ không phụ thuộc vào nhau thì không nên bị buộc phụ thuộc một cách nhân tạo. Chẳng hạn, không nên đặt enum tổng quát bên trong các lớp cụ thể hơn, vì như thế cả ứng dụng phải biết đến những lớp cụ thể ấy. Điều tương tự cũng đúng với các hàm tĩnh đa dụng được khai báo trong lớp chuyên biệt.

Nói chung, sự phụ thuộc nhân tạo là sự phụ thuộc giữa hai mô-đun không phục vụ mục đích trực tiếp nào. Nó xuất hiện khi ta đặt biến, hằng hay hàm vào một vị trí tạm thời tiện lợi nhưng không phù hợp. Đó là lười biếng và cẩu thả.

Hãy dành thời gian xác định nên khai báo hàm, hằng và biến ở đâu. Đừng tiện tay ném chúng vào chỗ thuận tiện nhất rồi để nguyên ở đó.

### G14: Hàm mê dữ liệu của lớp khác

Đây là một trong những mùi code của Martin Fowler.⁶ Các phương thức của một lớp nên quan tâm đến biến và hàm của chính lớp đó, chứ không phải biến và hàm của lớp khác. Khi một phương thức dùng các hàm truy cập và hàm sửa đổi của một đối tượng khác để thao tác dữ liệu bên trong đối tượng đó, nó đang thèm muốn phạm vi của lớp chứa đối tượng kia. Nó ước mình nằm trong lớp kia để có thể truy cập trực tiếp các biến mà nó đang thao tác. Ví dụ:

```java
public class HourlyPayCalculator {
  public Money calculateWeeklyPay(HourlyEmployee e) {
    int tenthRate = e.getTenthRate().getPennies();
    int tenthsWorked = e.getTenthsWorked();
    int straightTime = Math.min(400, tenthsWorked);
    int overTime = Math.max(0, tenthsWorked - straightTime);
    int straightPay = straightTime * tenthRate;
    int overtimePay = (int)Math.round(overTime*tenthRate*1.5);
    return new Money(straightPay + overtimePay);
  }
}
```

Phương thức `calculateWeeklyPay` truy cập sâu vào đối tượng `HourlyEmployee` để lấy dữ liệu mà nó xử lý. Phương thức này thèm muốn phạm vi của `HourlyEmployee`. Nó “ước” mình có thể nằm bên trong `HourlyEmployee`.

⁶. [Refactoring].

Nếu mọi yếu tố khác như nhau, ta muốn loại bỏ kiểu mê dữ liệu này vì nó để lộ phần bên trong của một lớp cho lớp khác. Tuy vậy, đôi khi đây là điều bất đắc dĩ. Hãy xét ví dụ sau:

```java
public class HourlyEmployeeReport {
  private HourlyEmployee employee;

  public HourlyEmployeeReport(HourlyEmployee e) {
    this.employee = e;
  }

  String reportHours() {
    return String.format(
      "Name: %s\tHours:%d.%1d\n",
      employee.getName(),
      employee.getTenthsWorked()/10,
      employee.getTenthsWorked()%10);
  }
}
```

Rõ ràng phương thức `reportHours` thèm muốn lớp `HourlyEmployee`. Mặt khác, ta không muốn `HourlyEmployee` phải biết định dạng báo cáo. Chuyển chuỗi định dạng vào lớp `HourlyEmployee` sẽ vi phạm một số nguyên tắc thiết kế hướng đối tượng.⁷ Làm vậy sẽ khiến `HourlyEmployee` phụ thuộc vào định dạng báo cáo, làm lớp này chịu ảnh hưởng mỗi khi định dạng thay đổi.

⁷. Cụ thể là Nguyên tắc Trách nhiệm Đơn nhất, Nguyên tắc đóng mở và Nguyên tắc đóng chung. Xem [PPP].

### G15: Đối số chọn hành vi

Hầu như chẳng có gì tệ hơn một đối số `false` lủng lẳng ở cuối lời gọi hàm. Nó có nghĩa gì? Nếu là `true` thì điều gì sẽ thay đổi? Mục đích của đối số chọn hành vi vốn đã khó nhớ, và mỗi đối số như vậy lại gộp nhiều hàm thành một. Đây chỉ là cách lười biếng để khỏi chia một hàm lớn thành vài hàm nhỏ. Hãy xem:

```java
public int calculateWeeklyPay(boolean overtime) {
  int tenthRate = getTenthRate();
  int tenthsWorked = getTenthsWorked();
  int straightTime = Math.min(400, tenthsWorked);
  int overTime = Math.max(0, tenthsWorked - straightTime);
  int straightPay = straightTime * tenthRate;
  double overtimeRate = overtime ? 1.5 : 1.0 * tenthRate;
  int overtimePay = (int)Math.round(overTime*overtimeRate);
  return straightPay + overtimePay;
}
```

Bạn gọi hàm này với `true` nếu giờ làm thêm được trả gấp rưỡi, và với `false` nếu giờ làm thêm được trả theo mức thông thường. Mỗi khi tình cờ gặp `calculateWeeklyPay(false)`, bạn đã phải nhớ xem lời gọi ấy có nghĩa gì. Nhưng điều đáng tiếc thật sự ở một hàm như thế này là tác giả đã bỏ lỡ cơ hội viết:

```java
public int straightPay() {
  return getTenthsWorked() * getTenthRate();
}

public int overTimePay() {
  int overTimeTenths = Math.max(0, getTenthsWorked() - 400);
  int overTimePay = overTimeBonus(overTimeTenths);
  return straightPay() + overTimePay;
}

private int overTimeBonus(int overTimeTenths) {
  double bonus = 0.5 * getTenthRate() * overTimeTenths;
  return (int) Math.round(bonus);
}
```

Đối số chọn hành vi không nhất thiết phải là Boolean. Nó có thể là enum, số nguyên hoặc bất kỳ kiểu đối số nào dùng để chọn hành vi của hàm. Nói chung, có nhiều hàm vẫn tốt hơn là truyền một thứ gì đó vào hàm để chọn hành vi.

### G16: Ý định bị che khuất

Ta muốn mã biểu đạt rõ nhất có thể. Biểu thức nối dài, ký pháp Hungary và số ma thuật đều che khuất ý định của tác giả. Ví dụ, hàm `overTimePay` có thể được viết như sau:

```java
public int m_otCalc() {
  return iThsWkd * iThsRte +
    (int) Math.round(0.5 * iThsRte *
      Math.max(0, iThsWkd - 400)
    );
}
```

Đoạn mã có vẻ ngắn gọn, nhưng gần như không thể hiểu nổi. Hãy dành thời gian để làm rõ ý định trong mã cho người đọc.

### G17: Trách nhiệm đặt sai chỗ

Một trong những quyết định quan trọng nhất mà nhà phát triển phần mềm phải đưa ra là đặt mã ở đâu. Chẳng hạn, hằng PI nên nằm ở đâu? Trong lớp `Math` chăng? Có lẽ nó thuộc lớp `Trigonometry`? Hay có thể là lớp `Circle`?

Ở đây cần áp dụng nguyên tắc ít gây ngạc nhiên nhất. Mã nên được đặt ở nơi người đọc tự nhiên mong đợi. Hằng PI nên nằm ở nơi khai báo các hàm lượng giác. Hằng `OVERTIME_RATE` nên được khai báo trong lớp `HourlyPayCalculator`.

Đôi khi ta tỏ ra “khôn lỏi” khi quyết định đặt một chức năng ở đâu. Ta đặt nó vào một hàm tiện cho mình nhưng chưa chắc hợp với trực giác của người đọc. Ví dụ, có thể ta cần in báo cáo tổng số giờ một nhân viên đã làm. Ta có thể cộng số giờ trong đoạn mã in báo cáo, hoặc duy trì một tổng lũy kế trong phần mã tiếp nhận thẻ chấm công.

Một cách đưa ra quyết định này là xem tên hàm. Giả sử mô-đun báo cáo có hàm tên `getTotalHours`. Giả sử mô-đun tiếp nhận thẻ chấm công có hàm `saveTimeCard`. Nhìn vào tên, hàm nào ngụ ý rằng nó tính tổng số giờ? Câu trả lời hẳn rất rõ.

Dĩ nhiên, đôi khi có lý do về hiệu năng để tính tổng số giờ khi tiếp nhận thẻ chấm công thay vì lúc in báo cáo. Không sao, nhưng tên hàm cần thể hiện điều đó. Ví dụ, trong mô-đun thẻ chấm công nên có hàm `computeRunningTotalOfHours`.

### G18: Dùng static không phù hợp

`Math.max(double a, double b)` là một phương thức tĩnh tốt. Nó không thao tác trên một thực thể cụ thể nào; quả thật, sẽ thật ngớ ngẩn nếu phải viết `new Math().max(a,b)` hay thậm chí `a.max(b)`. Toàn bộ dữ liệu `max` sử dụng đều đến từ hai đối số, không phải từ một đối tượng “sở hữu” nào. Quan trọng hơn, gần như không có khả năng ta muốn `Math.max` hỗ trợ đa hình.

Tuy nhiên, đôi khi ta viết những hàm tĩnh lẽ ra không nên là hàm tĩnh. Ví dụ, hãy xét:

```java
HourlyPayCalculator.calculatePay(employee, overtimeRate).
```

Hàm tĩnh này có vẻ hợp lý. Nó không hoạt động trên một đối tượng cụ thể nào và nhận toàn bộ dữ liệu từ các đối số. Tuy vậy, khả năng ta muốn hàm này hỗ trợ đa hình là có thật. Chẳng hạn, ta có thể muốn triển khai nhiều thuật toán tính lương theo giờ, như `OvertimeHourlyPayCalculator` và `StraightTimeHourlyPayCalculator`. Trong trường hợp này, hàm không nên là hàm tĩnh mà nên là một phương thức thành viên không tĩnh của `Employee`.

Nói chung, nên ưu tiên phương thức không tĩnh hơn phương thức tĩnh. Khi chưa chắc, hãy để hàm là phương thức không tĩnh. Nếu thật sự muốn hàm tĩnh, hãy chắc chắn rằng không có khả năng bạn sẽ muốn nó hoạt động đa hình.

### G19: Dùng biến diễn giải

Kent Beck đã viết về điều này trong cuốn sách tuyệt vời *Smalltalk Best Practice Patterns*⁸ và gần đây hơn trong cuốn cũng tuyệt vời không kém *Implementation Patterns*.⁹ Một trong những cách hiệu quả để làm chương trình dễ đọc là chia phép tính thành các giá trị trung gian, lưu trong những biến có tên rõ nghĩa.

⁸. [Beck97], trang 108.
⁹. [Beck07].

Hãy xem ví dụ sau từ FitNesse:

```java
Matcher match = headerPattern.matcher(line);
if(match.find())
{
  String key = match.group(1);
  String value = match.group(2);
  headers.put(key.toLowerCase(), value);
}
```

Chỉ cần dùng các biến diễn giải đơn giản, ta đã thấy rõ nhóm khớp thứ nhất là khóa, nhóm thứ hai là giá trị.

Rất khó dùng quá tay cách này. Thường thì có nhiều biến diễn giải vẫn tốt hơn ít biến. Thật đáng kinh ngạc khi một mô-đun khó hiểu bỗng trở nên trong sáng chỉ bằng cách chia phép tính thành những giá trị trung gian có tên rõ ràng.

### G20: Tên hàm phải nói rõ hàm làm gì

Hãy xem đoạn mã này:

```java
Date newDate = date.add(5);
```

Bạn nghĩ hàm này cộng năm ngày vào ngày đó chăng? Hay là tuần, hay giờ? Đối tượng ngày có bị thay đổi không, hay hàm chỉ trả về một `Date` mới mà không đổi đối tượng cũ? Chỉ nhìn lời gọi thì không thể biết hàm làm gì.

Nếu hàm cộng năm ngày vào ngày và làm thay đổi ngày đó, hãy đặt tên là `addDaysTo` hoặc `increaseByDays`. Còn nếu hàm trả về một ngày mới, muộn hơn năm ngày nhưng không thay đổi thực thể ngày, hãy đặt tên là `daysLater` hoặc `daysSince`.

Nếu phải xem phần triển khai (hoặc tài liệu) của hàm mới biết nó làm gì, bạn nên tìm tên tốt hơn hoặc sắp xếp lại chức năng để có thể đặt nó vào những hàm mang tên rõ ràng hơn.

### G21: Hiểu thuật toán

Nhiều đoạn mã rất buồn cười được viết ra vì người ta không dành thời gian hiểu thuật toán. Họ khiến thứ gì đó chạy được bằng cách chèn đủ câu lệnh if và cờ, mà không thật sự dừng lại suy nghĩ xem chuyện gì đang diễn ra.

Lập trình thường là một quá trình khám phá. Bạn nghĩ mình biết thuật toán phù hợp cho một việc, nhưng rồi phải vọc vạch, thăm dò, thử tới thử lui cho đến khi khiến nó “chạy được”. Làm sao biết nó “chạy được”? Vì nó vượt qua những ca kiểm thử mà bạn nghĩ ra.

Cách tiếp cận này chẳng có gì sai. Quả thật, thường đó là cách duy nhất để khiến hàm làm được điều bạn mong muốn. Tuy nhiên, không thể cứ giữ mãi dấu ngoặc kép quanh chữ “chạy được”.

Trước khi cho rằng mình đã hoàn thành một hàm, hãy chắc rằng bạn hiểu nó hoạt động ra sao. Việc mọi kiểm thử đều chạy qua chưa đủ. Bạn phải biết¹⁰ lời giải là đúng.

Thường thì cách tốt nhất để có được hiểu biết ấy là tái cấu trúc hàm thành thứ sạch sẽ, biểu đạt rõ đến mức cách nó hoạt động trở nên hiển nhiên.

¹⁰. Biết cách mã hoạt động khác với biết liệu thuật toán có thực hiện được công việc cần thiết hay không. Không chắc thuật toán có phù hợp hay không thường là chuyện bình thường. Không biết mã của mình làm gì thì chỉ là lười biếng.

### G22: Biến sự phụ thuộc logic thành phụ thuộc cụ thể

Nếu một mô-đun phụ thuộc vào mô-đun khác, sự phụ thuộc đó phải được thể hiện cụ thể chứ không chỉ tồn tại về mặt logic. Mô-đun phụ thuộc không nên tự giả định (nói cách khác, tạo ra sự phụ thuộc logic) về mô-đun mà nó dựa vào. Thay vào đó, nó phải hỏi tường minh mô-đun ấy mọi thông tin mà nó cần.

Ví dụ, hãy tưởng tượng bạn đang viết một hàm in báo cáo văn bản thuần về số giờ nhân viên đã làm. Một lớp tên `HourlyReporter` thu thập toàn bộ dữ liệu thành dạng tiện dụng rồi chuyển cho `HourlyReportFormatter` để in. (Xem Đoạn mã 17-1.)

**Đoạn mã 17-1**  
**HourlyReporter.java**

```java
public class HourlyReporter {
  private HourlyReportFormatter formatter;
  private List<LineItem> page;
  private final int PAGE_SIZE = 55;

  public HourlyReporter(HourlyReportFormatter formatter) {
    this.formatter = formatter;
    page = new ArrayList<LineItem>();
  }

  public void generateReport(List<HourlyEmployee> employees) {
    for (HourlyEmployee e : employees) {
      addLineItemToPage(e);
      if (page.size() == PAGE_SIZE)
        printAndClearItemList();
    }
    if (page.size() > 0)
      printAndClearItemList();
  }

  private void printAndClearItemList() {
    formatter.format(page);
    page.clear();
  }

  private void addLineItemToPage(HourlyEmployee e) {
    LineItem item = new LineItem();
    item.name = e.getName();
    item.hours = e.getTenthsWorked() / 10;
```

**Đoạn mã 17-1 (tiếp theo)**  
**HourlyReporter.java**

```java
    item.tenths = e.getTenthsWorked() % 10;
    page.add(item);
  }

  public class LineItem {
    public String name;
    public int hours;
    public int tenths;
  }
}
```

Trong mã này có một sự phụ thuộc logic chưa được thể hiện cụ thể. Bạn thấy đó là gì không? Đó là hằng `PAGE_SIZE`. Vì sao `HourlyReporter` phải biết kích thước trang? Kích thước trang nên thuộc trách nhiệm của `HourlyReportFormatter`.

Việc khai báo `PAGE_SIZE` trong `HourlyReporter` thể hiện trách nhiệm đặt sai chỗ [G17], khiến `HourlyReporter` cho rằng nó biết kích thước trang nên là bao nhiêu. Giả định ấy tạo ra sự phụ thuộc logic. `HourlyReporter` phụ thuộc vào việc `HourlyReportFormatter` có thể xử lý các trang cỡ 55. Nếu một cách triển khai nào đó của `HourlyReportFormatter` không xử lý được kích thước như vậy, lỗi sẽ xảy ra.

Ta có thể thể hiện cụ thể sự phụ thuộc này bằng cách tạo một phương thức mới tên `getMaxPageSize()` trong `HourlyReportFormatter`. Sau đó, `HourlyReporter` sẽ gọi hàm này thay vì dùng hằng `PAGE_SIZE`.

### G23: Ưu tiên đa hình thay cho if/else hoặc switch/case

Gợi ý này có thể nghe lạ nếu xét chủ đề của Chương 6. Dù sao, trong chương đó tôi lập luận rằng câu lệnh switch có lẽ phù hợp ở những phần của hệ thống có khả năng cần thêm hàm cao hơn khả năng cần thêm kiểu mới.

Thứ nhất, đa số mọi người dùng câu lệnh switch vì đó là giải pháp vét cạn hiển nhiên, chứ không phải vì nó phù hợp với tình huống. Vì thế, nguyên tắc kinh nghiệm này nhắc ta cân nhắc đa hình trước khi dùng switch.

Thứ hai, những trường hợp hàm thay đổi thường xuyên hơn kiểu dữ liệu tương đối hiếm. Vì vậy, mọi câu lệnh switch đều đáng ngờ.

Tôi dùng quy tắc “MỘT SWITCH” như sau: Với mỗi kiểu lựa chọn, không được có quá một câu lệnh switch. Các nhánh trong câu lệnh switch ấy phải tạo ra những đối tượng đa hình thay thế cho các câu lệnh switch khác trong phần còn lại của hệ thống.

### G24: Tuân theo quy ước chuẩn

Mỗi nhóm nên tuân theo một chuẩn viết mã dựa trên những thông lệ chung của ngành. Chuẩn này cần quy định những điều như khai báo biến thực thể ở đâu, đặt tên lớp, phương thức và biến thế nào, đặt dấu ngoặc nhọn ở đâu, v.v. Nhóm không cần tài liệu mô tả những quy ước ấy, vì chính mã của họ đã nêu ví dụ.

Mọi người trong nhóm đều nên tuân theo các quy ước này. Điều đó có nghĩa mỗi thành viên phải đủ chín chắn để hiểu rằng đặt dấu ngoặc nhọn ở đâu chẳng quan trọng chút nào, miễn là cả nhóm thống nhất vị trí đặt chúng.

Nếu muốn biết tôi tuân theo quy ước nào, bạn có thể xem mã đã tái cấu trúc trong Đoạn mã B-7 ở trang 394 đến Đoạn mã B-14.

### G25: Thay số ma thuật bằng hằng có tên

Đây có lẽ là một trong những quy tắc lâu đời nhất trong phát triển phần mềm. Tôi nhớ đã đọc về nó từ cuối thập niên sáu mươi trong các tài liệu nhập môn COBOL, FORTRAN và PL/1. Nói chung, để số trần trong mã là một ý tưởng tồi. Bạn nên giấu chúng sau các hằng có tên rõ nghĩa.

Ví dụ, số 86.400 nên được giấu sau hằng `SECONDS_PER_DAY`. Nếu mỗi trang in 55 dòng, hằng 55 nên được giấu sau hằng `LINES_PER_PAGE`.

Một số hằng dễ nhận ra đến mức không phải lúc nào cũng cần đặt sau một hằng có tên, miễn là chúng được dùng cùng đoạn mã tự giải thích rõ nghĩa. Ví dụ:

```java
double milesWalked = feetWalked/5280.0;
int dailyPay = hourlyRate * 8;
double circumference = radius * Math.PI * 2;
```

Trong các ví dụ trên, ta có thật sự cần các hằng `FEET_PER_MILE`, `WORK_HOURS_PER_DAY` và `TWO` không? Rõ ràng, trường hợp cuối thật vô lý. Có những công thức viết hằng trực tiếp thành số sẽ tốt hơn. Bạn có thể tranh luận về trường hợp `WORK_HOURS_PER_DAY` vì luật lệ hay quy ước có thể thay đổi. Mặt khác, công thức có số 8 đọc rất tự nhiên, nên tôi ngần ngại bắt người đọc gánh thêm 17 ký tự. Còn trong trường hợp `FEET_PER_MILE`, số 5280 nổi tiếng và đặc thù đến mức người đọc vẫn nhận ra nó ngay cả khi đứng một mình trên trang giấy, không có ngữ cảnh nào xung quanh.

Những hằng như 3.141592653589793 cũng rất nổi tiếng và dễ nhận ra. Tuy nhiên, khả năng mắc lỗi quá cao, không nên để chúng ở dạng số trần. Mỗi khi thấy 3.1415927535890793, người ta biết đó là π nên không xem xét kỹ. (Bạn có phát hiện lỗi một chữ số không?) Ta cũng không muốn mọi người dùng 3.14, 3.14159, 3.142, v.v. Vì thế, thật tốt khi `Math.PI` đã được định nghĩa sẵn.

Thuật ngữ “số ma thuật” không chỉ nói về số. Nó áp dụng cho mọi token có giá trị không tự nói rõ ý nghĩa. Ví dụ:

```java
assertEquals(7777, Employee.find("John Doe").employeeNumber());
```

Trong câu khẳng định này có hai số ma thuật. Số đầu tiên hiển nhiên là 7777, dù ý nghĩa của nó không rõ. Số ma thuật thứ hai là `"John Doe"`, và ý định ở đây cũng không rõ.

Hóa ra `"John Doe"` là tên của nhân viên mã số 7777 trong cơ sở dữ liệu kiểm thử nổi tiếng do nhóm chúng tôi tạo. Mọi người trong nhóm đều biết khi kết nối với cơ sở dữ liệu này, sẽ có sẵn một số nhân viên cùng các giá trị và thuộc tính quen thuộc. Hóa ra `"John Doe"` là nhân viên hưởng lương theo giờ duy nhất trong cơ sở dữ liệu kiểm thử đó. Vì vậy, kiểm thử này thực ra nên viết như sau:

```java
assertEquals(
  HOURLY_EMPLOYEE_ID,
  Employee.find(HOURLY_EMPLOYEE_NAME).employeeNumber());
```

### G26: Chính xác

Cho rằng kết quả đầu tiên khớp truy vấn cũng là kết quả duy nhất có lẽ là ngây thơ. Dùng số thực dấu phẩy động để biểu diễn tiền tệ gần như là tội ác. Tránh khóa hoặc quản lý giao dịch vì nghĩ rằng cập nhật đồng thời ít có khả năng xảy ra, cùng lắm cũng là lười biếng. Khai báo biến kiểu `ArrayList` trong khi `List` đã đủ dùng là tự giới hạn quá mức. Mặc định đặt tất cả biến ở mức `protected` lại là giới hạn chưa đủ.

Khi đưa ra quyết định trong mã, hãy xác định thật chính xác. Hãy biết vì sao bạn quyết định như vậy và sẽ xử lý ngoại lệ ra sao. Đừng lười trong việc xác định độ chính xác cho các quyết định. Nếu quyết định gọi một hàm có thể trả về `null`, hãy kiểm tra `null`. Nếu truy vấn thứ bạn nghĩ là bản ghi duy nhất trong cơ sở dữ liệu, hãy bảo đảm mã kiểm tra xem còn bản ghi nào khác không. Nếu phải xử lý tiền tệ, hãy dùng số nguyên¹¹ và xử lý việc làm tròn cho phù hợp. Nếu có khả năng cập nhật đồng thời, hãy triển khai một cơ chế khóa nào đó.

Sự mơ hồ và thiếu chính xác trong mã xuất phát từ bất đồng hoặc lười biếng. Dù lý do nào, cũng cần loại bỏ chúng.

¹¹. Hoặc tốt hơn nữa, dùng một lớp `Money` lưu giá trị bằng số nguyên.

### G27: Cấu trúc thay cho quy ước

Hãy áp đặt các quyết định thiết kế bằng cấu trúc thay vì quy ước. Quy ước đặt tên rất tốt, nhưng không bằng những cấu trúc buộc mọi người phải tuân thủ. Ví dụ, switch/case với enum được đặt tên rõ ràng vẫn kém hơn lớp cơ sở có các phương thức trừu tượng. Không ai bị buộc phải viết câu lệnh switch/case theo cùng một cách mỗi lần, còn lớp cơ sở thì buộc các lớp cụ thể phải triển khai mọi phương thức trừu tượng.

### G28: Đóng gói điều kiện

Logic Boolean vốn đã khó hiểu, càng khó hơn khi phải đọc trong ngữ cảnh câu lệnh if hay while. Hãy tách thành các hàm giải thích ý định của điều kiện.

Ví dụ:

```java
if (shouldBeDeleted(timer))
```

tốt hơn:

```java
if (timer.hasExpired() && !timer.isRecurrent())
```

### G29: Tránh điều kiện phủ định

Điều kiện phủ định khó hiểu hơn một chút so với điều kiện khẳng định. Vì vậy, khi có thể, hãy viết điều kiện theo hướng khẳng định. Ví dụ:

```java
if (buffer.shouldCompact())
```

tốt hơn:

```java
if (!buffer.shouldNotCompact())
```

### G30: Mỗi hàm chỉ nên làm một việc

Ta thường dễ bị cám dỗ viết những hàm gồm nhiều phần, mỗi phần thực hiện một loạt thao tác. Loại hàm này làm nhiều việc, nên cần được chuyển thành nhiều hàm nhỏ hơn, mỗi hàm chỉ làm một việc.

Ví dụ:

```java
public void pay() {
  for (Employee e : employees) {
    if (e.isPayday()) {
      Money pay = e.calculatePay();
      e.deliverPay(pay);
    }
  }
}
```

Đoạn mã này làm ba việc. Nó lặp qua mọi nhân viên, kiểm tra xem từng người có đến ngày nhận lương không, rồi trả lương cho nhân viên ấy. Nên viết lại như sau:

```java
public void pay() {
  for (Employee e : employees)
    payIfNecessary(e);
}

private void payIfNecessary(Employee e) {
  if (e.isPayday())
    calculateAndDeliverPay(e);
}

private void calculateAndDeliverPay(Employee e) {
  Money pay = e.calculatePay();
  e.deliverPay(pay);
}
```

Mỗi hàm trong số này chỉ làm một việc. (Xem “Làm một việc” ở trang 35.)

### G31: Sự phụ thuộc vào thời điểm bị che giấu

Sự phụ thuộc vào thời điểm thường là cần thiết, nhưng đừng che giấu nó. Hãy sắp xếp các đối số của hàm sao cho thứ tự cần gọi các hàm trở nên hiển nhiên. Xét đoạn mã sau:

```java
public class MoogDiver {
  Gradient gradient;
  List<Spline> splines;

  public void dive(String reason) {
    saturateGradient();
    reticulateSplines();
    diveForMoog(reason);
  }
  ...
}
```

Thứ tự của ba hàm rất quan trọng. Phải làm bão hòa gradient trước rồi mới có thể nối các spline, sau đó mới được lặn tìm moog. Đáng tiếc là mã không bảo đảm được thứ tự thực thi này. Một lập trình viên khác có thể gọi `reticulateSplines` trước khi gọi `saturateGradient`, dẫn đến `UnsaturatedGradientException`. Cách tốt hơn là:

```java
public class MoogDiver {
  Gradient gradient;
  List<Spline> splines;

  public void dive(String reason) {
    Gradient gradient = saturateGradient();
    List<Spline> splines = reticulateSplines(gradient);
    diveForMoog(splines, reason);
  }
  ...
}
```

Cách này làm lộ sự phụ thuộc vào thời điểm bằng cách tạo thành một dây chuyền. Mỗi hàm tạo ra kết quả mà hàm tiếp theo cần, vì thế không có cách hợp lý nào để gọi chúng sai thứ tự.

Có thể bạn sẽ phàn nàn rằng cách này làm các hàm phức tạp hơn, và bạn nói đúng. Nhưng phần phức tạp cú pháp thêm vào phơi bày độ phức tạp thực sự về thời điểm của tình huống.

Lưu ý rằng tôi vẫn giữ nguyên các biến thực thể. Tôi cho rằng các phương thức riêng trong lớp cần chúng. Dù vậy, tôi vẫn muốn để các đối số ở đó để thể hiện rõ sự phụ thuộc vào thời điểm.

### G32: Đừng tùy tiện

Hãy có lý do cho cách cấu trúc mã và bảo đảm cấu trúc thể hiện được lý do đó. Nếu cấu trúc trông tùy tiện, người khác sẽ thấy mình có thể thay đổi nó. Nếu cấu trúc nhất quán trong toàn hệ thống, người khác sẽ dùng và giữ theo quy ước. Chẳng hạn, gần đây khi gộp các thay đổi vào FitNesse, tôi phát hiện một người đóng góp đã viết như sau:

```java
public class AliasLinkWidget extends ParentWidget
{
  public static class VariableExpandingWidgetRoot {
    ...
    ...
  }
}
```

Vấn đề là `VariableExpandingWidgetRoot` không cần nằm trong phạm vi của `AliasLinkWidget`. Hơn nữa, một số lớp không liên quan khác lại dùng `AliasLinkWidget.VariableExpandingWidgetRoot`. Những lớp đó không cần biết đến `AliasLinkWidget`.

Có lẽ lập trình viên đưa `VariableExpandingWidgetRoot` vào `AliasWidget` cho tiện, hoặc nghĩ rằng nó thật sự cần được đặt trong phạm vi của `AliasWidget`. Dù lý do là gì, kết quả vẫn tùy tiện. Các lớp công khai không phải tiện ích của một lớp khác thì không nên được đặt trong lớp đó. Theo quy ước, chúng nên được khai báo công khai ở cấp cao nhất của gói.

### G33: Đóng gói điều kiện biên

Điều kiện biên rất khó theo dõi. Hãy đặt phần xử lý chúng ở một nơi. Đừng để chúng rò rỉ khắp mã. Ta không muốn các phép cộng trừ 1 rải rác lung tung. Hãy xem ví dụ đơn giản sau trong FIT:

```java
if(level + 1 < tags.length)
{
  parts = new Parse(body, tags, level + 1, offset + endTag);
  body = null;
}
```

Bạn thấy `level+1` xuất hiện hai lần. Đây là một điều kiện biên nên được đóng gói trong biến tên chẳng hạn `nextLevel`.

```java
int nextLevel = level + 1;
if(nextLevel < tags.length)
{
  parts = new Parse(body, tags, nextLevel, offset + endTag);
  body = null;
}
```

### G34: Hàm chỉ nên đi xuống một mức trừu tượng

Các câu lệnh bên trong một hàm nên được viết ở cùng một mức trừu tượng, thấp hơn một mức so với thao tác được mô tả bởi tên hàm. Đây có thể là nguyên tắc kinh nghiệm khó diễn giải và tuân theo nhất. Ý tưởng nghe có vẻ đơn giản, nhưng con người quá giỏi trong việc trộn lẫn các mức trừu tượng một cách trơn tru. Chẳng hạn, hãy xem đoạn mã sau lấy từ FitNesse:

```java
public String render() throws Exception
{
  StringBuffer html = new StringBuffer("<hr");
  if(size > 0)
    html.append(" size=\"").append(size + 1).append("\"");
  html.append(">");

  return html.toString();
}
```

Chỉ cần xem qua một lúc là bạn hiểu chuyện gì xảy ra. Hàm này dựng thẻ HTML để vẽ một đường kẻ ngang trên trang. Chiều cao của đường kẻ được quy định trong biến `size`.

Giờ hãy xem lại. Phương thức này trộn ít nhất hai mức trừu tượng. Mức thứ nhất là khái niệm đường kẻ ngang có kích thước. Mức thứ hai là cú pháp của thẻ HR. Đoạn mã này thuộc mô-đun `HruleWidget` trong FitNesse. Mô-đun này phát hiện một dãy gồm bốn dấu gạch ngang trở lên rồi chuyển nó thành thẻ HR tương ứng. Càng nhiều dấu gạch ngang, kích thước càng lớn.

Tôi tái cấu trúc đoạn mã như sau. Lưu ý rằng tôi đổi tên trường `size` để phản ánh mục đích thực sự của nó. Trường này lưu số dấu gạch ngang thừa.

```java
public String render() throws Exception
{
  HtmlTag hr = new HtmlTag("hr");
  if (extraDashes > 0)
    hr.addAttribute("size", hrSize(extraDashes));
  return hr.html();
}

private String hrSize(int height)
{
  int hrSize = height + 1;
  return String.format("%d", hrSize);
}
```

Thay đổi này tách riêng hai mức trừu tượng một cách gọn gàng. Hàm `render` chỉ dựng thẻ HR mà không cần biết gì về cú pháp HTML của thẻ đó. Mô-đun `HtmlTag` đảm nhiệm những chi tiết cú pháp rắc rối.

Thật ra, nhờ thay đổi này tôi đã phát hiện một lỗi khó thấy. Mã ban đầu không đặt dấu gạch chéo đóng vào thẻ HR theo yêu cầu của chuẩn XHTML. (Nói cách khác, nó xuất `<hr>` thay vì `<hr/>`.) Mô-đun `HtmlTag` đã được thay đổi để tuân theo XHTML từ lâu.

Tách các mức trừu tượng là một trong những chức năng quan trọng nhất của tái cấu trúc, đồng thời cũng là một trong những việc khó làm tốt nhất. Ví dụ, hãy xem đoạn mã dưới đây. Đây là lần đầu tôi thử tách các mức trừu tượng trong phương thức `HruleWidget.render`.

```java
public String render() throws Exception
{
  HtmlTag hr = new HtmlTag("hr");
  if (size > 0) {
    hr.addAttribute("size", ""+(size+1));
  }
  return hr.html();
}
```

Lúc đó, mục tiêu của tôi là tạo sự phân tách cần thiết và làm cho các kiểm thử chạy qua. Tôi dễ dàng đạt mục tiêu, nhưng kết quả vẫn là một hàm trộn lẫn các mức trừu tượng. Trong trường hợp này, những mức trừu tượng bị trộn là việc dựng thẻ HR và diễn giải, định dạng biến `size`. Điều đó cho thấy khi chia một hàm theo các mức trừu tượng, ta thường phát hiện thêm những ranh giới trừu tượng mới vốn bị cấu trúc trước đó che khuất.

### G35: Giữ dữ liệu cấu hình ở mức cao

Nếu có một hằng như giá trị mặc định hay cấu hình vốn được biết đến và được mong đợi ở mức trừu tượng cao, đừng chôn nó trong một hàm mức thấp. Hãy đưa nó ra làm đối số cho hàm mức thấp được gọi từ hàm mức cao. Hãy xem đoạn mã sau trong FitNesse:

```java
public static void main(String[] args) throws Exception
{
  Arguments arguments = parseCommandLine(args);
  ...
}

public class Arguments
{
  public static final String DEFAULT_PATH = ".";
  public static final String DEFAULT_ROOT = "FitNesseRoot";
  public static final int DEFAULT_PORT = 80;
  public static final int DEFAULT_VERSION_DAYS = 14;
  ...
}
```

Các đối số dòng lệnh được phân tích ngay dòng lệnh thực thi đầu tiên của FitNesse. Các giá trị mặc định của chúng được quy định ở đầu lớp `Arguments`. Bạn không phải mò xuống các mức thấp của hệ thống để tìm những câu lệnh như sau:

```java
if (arguments.port == 0) // mặc định dùng cổng 80
```

Các hằng cấu hình nằm ở mức rất cao và dễ thay đổi. Chúng được truyền xuống phần còn lại của ứng dụng. Các mức thấp hơn của ứng dụng không sở hữu giá trị của những hằng này.

### G36: Tránh điều hướng bắc cầu

Nói chung, ta không muốn một mô-đun biết quá nhiều về các đối tác của nó. Cụ thể hơn, nếu A cộng tác với B, còn B cộng tác với C, ta không muốn các mô-đun dùng A biết về C. (Chẳng hạn, ta không muốn `a.getB().getC().doSomething()`.)

Cách làm này đôi khi được gọi là Luật Demeter. Các Pragmatic Programmers gọi nó là “Viết mã kín đáo”.¹² Dù gọi thế nào, ý chính là bảo đảm các mô-đun chỉ biết những đối tác trực tiếp của mình, chứ không biết sơ đồ điều hướng của toàn hệ thống.

¹². [PRAG], tr. 138.

Nếu nhiều mô-đun dùng dạng câu lệnh `a.getB().getC()`, ta sẽ khó thay đổi thiết kế và kiến trúc để chèn Q vào giữa B và C. Khi đó, ta phải tìm từng chỗ dùng `a.getB().getC()` và đổi thành `a.getB().getQ().getC()`. Đó là cách kiến trúc trở nên cứng nhắc. Quá nhiều mô-đun biết quá nhiều về kiến trúc.

Thay vào đó, ta muốn các đối tác trực tiếp cung cấp mọi dịch vụ cần thiết. Ta không nên phải lần theo đồ thị đối tượng của hệ thống để tìm phương thức cần gọi. Ta chỉ cần viết:

```java
myCollaborator.doSomething().
```

*Chú thích*

12. [PRAG], trang 138.

## Java

### J1: Tránh danh sách import dài bằng cách dùng ký tự đại diện

Nếu dùng từ hai lớp trở lên trong một gói, hãy import cả gói:

```java
import package.*;
```

Danh sách import dài khiến người đọc nản lòng. Ta không muốn làm đầu mô-đun thêm lộn xộn với 80 dòng import. Thay vào đó, muốn các import nói gọn gàng những gói mà mô-đun cộng tác.

Import cụ thể tạo ra phụ thuộc cứng, còn import ký tự đại diện thì không. Nếu import một lớp cụ thể, lớp đó phải tồn tại. Nhưng nếu import cả gói bằng ký tự đại diện, không cần lớp cụ thể nào phải tồn tại. Câu lệnh import chỉ thêm gói vào đường dẫn tìm kiếm khi tra tên. Vì thế, các import này không tạo ra phụ thuộc thật sự và giúp mô-đun ít phụ thuộc lẫn nhau hơn.

Đôi khi danh sách dài các import cụ thể có ích. Chẳng hạn, nếu đang xử lý mã cũ và muốn biết cần tạo mock, stub cho những lớp nào, bạn có thể xem danh sách import cụ thể để tìm tên đầy đủ của tất cả các lớp, rồi tạo những stub phù hợp. Tuy nhiên, trường hợp cần import cụ thể như vậy rất hiếm. Hơn nữa, hầu hết IDE hiện đại cho phép chuyển import ký tự đại diện thành danh sách import cụ thể chỉ bằng một lệnh. Vì vậy, kể cả với mã cũ, import ký tự đại diện vẫn tốt hơn.

Import ký tự đại diện đôi khi có thể gây xung đột và mơ hồ về tên. Hai lớp cùng tên nhưng thuộc các gói khác nhau cần được import riêng, hoặc ít nhất phải ghi rõ đầy đủ tên gói khi dùng. Điều đó có thể gây phiền, nhưng hiếm khi xảy ra, nên nhìn chung import ký tự đại diện vẫn tốt hơn import cụ thể.

### J2: Đừng kế thừa hằng

Tôi đã thấy cách làm này nhiều lần và lần nào cũng nhăn mặt. Lập trình viên đặt một số hằng trong giao diện rồi lấy chúng bằng cách kế thừa giao diện ấy. Hãy xem đoạn mã sau:

```java
public class HourlyEmployee extends Employee {
  private int tenthsWorked;
  private double hourlyRate;

  public Money calculatePay() {
    int straightTime = Math.min(tenthsWorked, TENTHS_PER_WEEK);
    int overTime = tenthsWorked - straightTime;
    return new Money(
      hourlyRate * (tenthsWorked + OVERTIME_RATE * overTime)
    );
  }
  ...
}
```

Các hằng `TENTHS_PER_WEEK` và `OVERTIME_RATE` từ đâu ra? Có thể chúng đến từ lớp `Employee`, hãy xem thử:

```java
public abstract class Employee implements PayrollConstants {
  public abstract boolean isPayday();
  public abstract Money calculatePay();
  public abstract void deliverPay(Money pay);
}
```

Không phải ở đó. Vậy chúng ở đâu? Hãy nhìn kỹ lớp `Employee`. Nó cài đặt `PayrollConstants`.

```java
public interface PayrollConstants {
  public static final int TENTHS_PER_WEEK = 400;
  public static final double OVERTIME_RATE = 1.5;
}
```

Đây là cách làm thật xấu xí! Các hằng bị giấu ở đầu hệ thống phân cấp kế thừa. Eo ôi! Đừng dùng kế thừa để lách quy tắc phạm vi của ngôn ngữ. Thay vào đó, hãy dùng import static.

```java
import static PayrollConstants.*;

public class HourlyEmployee extends Employee {
  private int tenthsWorked;
  private double hourlyRate;

  public Money calculatePay() {
    int straightTime = Math.min(tenthsWorked, TENTHS_PER_WEEK);
    int overTime = tenthsWorked - straightTime;
    return new Money(
      hourlyRate * (tenthsWorked + OVERTIME_RATE * overTime)
    );
  }
  ...
}
```

### J3: Hằng hay enum

Giờ enum đã được thêm vào ngôn ngữ (Java 5), hãy dùng chúng! Đừng tiếp tục dùng mẹo cũ với các số nguyên `public static final`. Ý nghĩa của số nguyên có thể bị quên mất. Ý nghĩa của enum thì không, vì chúng thuộc về một kiểu liệt kê có tên.

Hơn nữa, hãy nghiên cứu kỹ cú pháp enum. Chúng có thể có phương thức và trường. Nhờ vậy, enum là công cụ rất mạnh, biểu đạt linh hoạt hơn nhiều so với số nguyên. Xét biến thể sau của mã tính lương:

```java
public class HourlyEmployee extends Employee {
  private int tenthsWorked;
  HourlyPayGrade grade;

  public Money calculatePay() {
    int straightTime = Math.min(tenthsWorked, TENTHS_PER_WEEK);
    int overTime = tenthsWorked - straightTime;
    return new Money(
      grade.rate() * (tenthsWorked + OVERTIME_RATE * overTime)
    );
  }
  ...
}

public enum HourlyPayGrade {
  APPRENTICE {
    public double rate() {
      return 1.0;
    }
  },
  LEUTENANT_JOURNEYMAN {
    public double rate() {
      return 1.2;
    }
  },
  JOURNEYMAN {
    public double rate() {
      return 1.5;
    }
  },
  MASTER {
    public double rate() {
      return 2.0;
    }
  };
  public abstract double rate();
}
```

## Tên

### N1: Chọn tên có tính mô tả

Đừng vội chọn tên. Hãy bảo đảm tên có tính mô tả. Ý nghĩa thường thay đổi khi phần mềm phát triển, vì thế hãy thường xuyên đánh giá lại xem những tên bạn chọn còn phù hợp hay không.

Đây không chỉ là lời khuyên để nghe cho vui. Tên trong phần mềm quyết định 90 phần trăm khả năng đọc của mã. Bạn cần dành thời gian chọn tên cho khôn ngoan và giữ chúng phù hợp. Tên quan trọng đến mức không thể xem nhẹ.

Xét đoạn mã dưới đây. Nó làm gì? Nếu tôi cho bạn xem mã với những cái tên được chọn kỹ, bạn sẽ hiểu ngay. Còn như thế này, nó chỉ là một mớ ký hiệu và số ma thuật.

```java
public int x() {
  int q = 0;
  int z = 0;
  for (int kk = 0; kk < 10; kk++) {
    if (l[z] == 10)
    {
      q += 10 + (l[z + 1] + l[z + 2]);
      z += 1;
    }
    else if (l[z] + l[z + 1] == 10)
    {
      q += 10 + l[z + 2];
      z += 2;
    } else {
      q += l[z] + l[z + 1];
      z += 2;
    }
  }
  return q;
}
```

Đây là đoạn mã nên được viết. Thực ra, đoạn này còn ít hoàn chỉnh hơn đoạn trên. Dù vậy, bạn có thể hiểu ngay nó đang cố làm gì và rất có thể tự viết được các hàm còn thiếu dựa trên ý nghĩa suy ra. Các số ma thuật không còn là ma thuật, còn cấu trúc thuật toán mô tả rõ ràng điều nó làm.

```java
public int score() {
  int score = 0;
  int frame = 0;
  for (int frameNumber = 0; frameNumber < 10; frameNumber++) {
    if (isStrike(frame)) {
      score += 10 + nextTwoBallsForStrike(frame);
      frame += 1;
    } else if (isSpare(frame)) {
      score += 10 + nextBallForSpare(frame);
      frame += 2;
    } else {
      score += twoBallsInFrame(frame);
      frame += 2;
    }
  }
  return score;
}
```

Tên được chọn cẩn thận có sức mạnh làm cho cấu trúc mã đồng thời truyền tải mô tả. Mô tả đó định hình kỳ vọng của người đọc về chức năng của các hàm khác trong mô-đun. Nhìn đoạn mã trên, bạn có thể suy ra phần cài đặt của `isStrike()`. Khi đọc phương thức `isStrike`, bạn sẽ thấy nó “gần như đúng những gì mình mong đợi”.¹³

¹³. Xem lời trích dẫn của Ward Cunningham ở trang 11.

```java
private boolean isStrike(int frame) {
  return rolls[frame] == 10;
}
```

### N2: Chọn tên phù hợp với mức trừu tượng

Đừng chọn tên mô tả phần cài đặt; hãy chọn tên thể hiện mức trừu tượng của lớp hoặc hàm bạn đang làm việc. Việc này không dễ. Một lần nữa, con người quá giỏi trộn lẫn các mức trừu tượng. Mỗi lần xem lại mã, có lẽ bạn sẽ tìm thấy một biến được đặt tên ở mức quá thấp. Hãy đổi tên ngay khi phát hiện. Làm cho mã dễ đọc đòi hỏi sự kiên trì cải thiện liên tục. Xét giao diện `Modem` sau:

```java
public interface Modem {
  boolean dial(String phoneNumber);
  boolean disconnect();
  boolean send(char c);
  char recv();
  String getConnectedPhoneNumber();
}
```

Thoạt nhìn, giao diện này có vẻ ổn. Các hàm đều hợp lý. Quả thật, chúng phù hợp với nhiều ứng dụng. Nhưng hãy xét ứng dụng dùng một số modem không kết nối bằng cách quay số. Thay vào đó, chúng được nối cố định với nhau bằng dây, chẳng hạn modem cáp cung cấp kết nối Internet cho phần lớn hộ gia đình ngày nay. Có lẽ một số modem kết nối bằng cách gửi số cổng đến bộ chuyển mạch qua USB. Rõ ràng, khái niệm số điện thoại nằm ở sai mức trừu tượng. Cách đặt tên tốt hơn cho tình huống này có thể là:

```java
public interface Modem {
  boolean connect(String connectionLocator);
  boolean disconnect();
  boolean send(char c);
  char recv();
  String getConnectedLocator();
}
```

Những tên này không giả định kết nối phải dùng số điện thoại. Chúng vẫn dùng được với số điện thoại, hoặc bất kỳ chiến lược kết nối nào khác.

### N3: Dùng thuật ngữ chuẩn khi có thể

Tên dễ hiểu hơn nếu dựa trên quy ước hoặc cách dùng sẵn có. Chẳng hạn, nếu dùng mẫu DECORATOR, bạn nên đưa từ Decorator vào tên các lớp trang trí. Ví dụ, `AutoHangupModemDecorator` có thể là tên lớp bổ sung khả năng tự ngắt modem khi phiên kết nối kết thúc.

Mẫu thiết kế chỉ là một loại quy ước. Chẳng hạn, trong Java, các hàm chuyển đối tượng thành dạng biểu diễn chuỗi thường được đặt tên là `toString`. Làm theo những quy ước như vậy tốt hơn là tự nghĩ ra tên riêng.

Các nhóm thường tự tạo một hệ thống tên chuẩn cho dự án. Eric Evans gọi đó là ngôn ngữ phổ quát của dự án.¹⁴ Mã của bạn nên dùng rộng rãi các thuật ngữ trong ngôn ngữ đó. Tóm lại, càng dùng được nhiều tên mang những ý nghĩa đặc thù phù hợp với dự án, người đọc càng dễ hiểu mã đang nói về điều gì.

¹⁴. [DDD].

### N4: Tên không mơ hồ

Hãy chọn tên giúp người đọc hiểu rõ hàm hoặc biến hoạt động ra sao. Xét ví dụ sau từ FitNesse:

```java
private String doRename() throws Exception
{
  if(refactorReferences)
    renameReferences();
  renamePage();

  pathToRename.removeNameFromEnd();
  pathToRename.addNameToEnd(newName);
  return PathParser.render(pathToRename);
}
```

Tên hàm này chỉ nói rất chung chung và mơ hồ về việc hàm làm gì. Điều đó càng rõ khi bên trong hàm tên `doRename` lại có một hàm tên `renamePage`! Tên gọi cho ta biết gì về sự khác nhau giữa hai hàm? Chẳng biết gì cả.

Tên tốt hơn cho hàm đó là `renamePageAndOptionallyAllReferences`. Tên này có vẻ dài, đúng là dài, nhưng hàm chỉ được gọi ở một nơi trong mô-đun, nên giá trị giải thích của nó quan trọng hơn độ dài.

### N5: Dùng tên dài cho phạm vi dài

Độ dài tên nên tương ứng với độ dài phạm vi. Trong phạm vi rất nhỏ, bạn có thể dùng tên biến ngắn; trong phạm vi lớn, nên dùng tên dài hơn.

Tên biến như `i` và `j` hoàn toàn ổn nếu phạm vi của chúng chỉ dài năm dòng. Xét đoạn mã từ ví dụ “Bowling Game” kinh điển cũ:

```java
private void rollMany(int n, int pins)
{
  for (int i=0; i<n; i++)
    g.roll(pins);
}
```

Đoạn này hoàn toàn rõ ràng. Nếu thay `i` bằng cái tên phiền phức như `rollCount`, mã sẽ khó hiểu hơn. Ngược lại, biến và hàm có tên ngắn sẽ mất ý nghĩa khi phạm vi trải dài. Phạm vi tên càng rộng, tên càng cần dài và chính xác.

### N6: Tránh mã hóa tên

Không nên mã hóa thông tin về kiểu hay phạm vi vào tên. Các tiền tố như `m_` hoặc `f` chẳng có ích trong môi trường ngày nay. Tương tự, các tiền tố mã hóa dự án và/hoặc hệ thống con như `vis_` (viết tắt của visual imaging system, hệ thống tạo ảnh trực quan) gây rối và thừa. Một lần nữa, môi trường hiện đại đã cung cấp mọi thông tin đó, không cần làm biến dạng tên. Hãy giữ tên trong sạch, tránh nhiễm ký pháp Hungary.

### N7: Tên nên mô tả tác dụng phụ

Tên nên mô tả mọi điều mà hàm, biến hoặc lớp là hoặc làm. Đừng che giấu tác dụng phụ trong tên. Đừng dùng một động từ đơn giản để mô tả hàm làm nhiều hơn hành động đơn giản đó. Chẳng hạn, hãy xét đoạn mã sau từ TestNG:

```java
public ObjectOutputStream getOos() throws IOException {
  if (m_oos == null) {
    m_oos = new ObjectOutputStream(m_socket.getOutputStream());
  }
  return m_oos;
}
```

Hàm này làm nhiều hơn là lấy một `oos`: nó tạo `oos` nếu chưa được tạo. Vì vậy, tên tốt hơn có thể là `createOrReturnOos`.

## Kiểm thử

### T1: Kiểm thử chưa đầy đủ

Bộ kiểm thử nên có bao nhiêu ca? Đáng tiếc, thước đo nhiều lập trình viên dùng là “Có vẻ đủ rồi”. Bộ kiểm thử nên kiểm tra mọi thứ có thể bị hỏng. Chừng nào còn điều kiện chưa được kiểm tra hoặc phép tính chưa được xác thực, kiểm thử vẫn chưa đầy đủ.

### T2: Dùng công cụ đo độ bao phủ!

Công cụ đo độ bao phủ chỉ ra những lỗ hổng trong chiến lược kiểm thử. Chúng giúp dễ dàng tìm ra các mô-đun, lớp và hàm chưa được kiểm thử đầy đủ. Hầu hết IDE đều biểu thị trực quan: những dòng đã được thực thi có màu xanh lá, còn dòng chưa được thực thi có màu đỏ. Nhờ vậy, có thể nhanh chóng tìm ra các câu lệnh if hoặc catch mà phần thân chưa được kiểm tra.

### T3: Đừng bỏ qua kiểm thử đơn giản

Chúng dễ viết, còn giá trị tài liệu của chúng lớn hơn chi phí tạo ra.

### T4: Kiểm thử bị bỏ qua là câu hỏi về một điểm mơ hồ

Đôi khi ta không chắc một chi tiết hành vi vì yêu cầu chưa rõ. Ta có thể diễn đạt câu hỏi về yêu cầu bằng một kiểm thử được chú thích để vô hiệu hóa, hoặc một kiểm thử được gắn `@Ignore`. Chọn cách nào tùy thuộc vào việc điểm mơ hồ có liên quan đến thứ khiến mã biên dịch được hay không.

### T5: Kiểm thử điều kiện ranh giới

Hãy đặc biệt cẩn thận khi kiểm thử điều kiện ranh giới. Ta thường xử lý đúng phần giữa của thuật toán nhưng đánh giá sai các ranh giới.

### T6: Kiểm thử kỹ quanh lỗi

Lỗi thường tụ lại với nhau. Khi phát hiện lỗi trong một hàm, nên kiểm thử hàm đó thật kỹ. Có lẽ lỗi ấy không đứng một mình.

### T7: Mẫu lỗi tiết lộ nhiều điều

Đôi khi có thể chẩn đoán vấn đề bằng cách tìm mẫu trong cách các ca kiểm thử thất bại. Đây là thêm một lý do để viết các ca kiểm thử đầy đủ nhất có thể. Các ca kiểm thử đầy đủ, được sắp xếp hợp lý, sẽ làm lộ ra các mẫu.

Ví dụ đơn giản: giả sử bạn nhận thấy mọi kiểm thử có đầu vào dài hơn năm ký tự đều thất bại. Hoặc mọi kiểm thử truyền số âm vào đối số thứ hai của một hàm đều thất bại thì sao? Đôi khi chỉ nhìn mẫu đỏ xanh trong báo cáo kiểm thử cũng đủ gợi ra tiếng “À!” dẫn đến lời giải. Xem lại trang 267 để thấy một ví dụ thú vị về điều này trong ví dụ SerialDate.

### T8: Mẫu độ bao phủ kiểm thử có thể tiết lộ nhiều điều

Xem những đoạn mã nào được hoặc không được thực thi bởi các kiểm thử đạt có thể giúp tìm ra lý do những kiểm thử thất bại.

### T9: Kiểm thử phải nhanh

Kiểm thử chậm là kiểm thử không được chạy. Khi tiến độ căng, những kiểm thử chậm sẽ bị bỏ khỏi bộ kiểm thử. Vì vậy, hãy làm mọi việc cần thiết để giữ cho kiểm thử chạy nhanh.

## Kết luận

Khó có thể nói danh sách các nguyên tắc kinh nghiệm và mùi code này đã đầy đủ. Thật ra, tôi không chắc một danh sách như vậy có bao giờ đầy đủ được không. Nhưng có lẽ đầy đủ không phải là mục tiêu, vì danh sách này thể hiện một hệ giá trị.

Quả thật, hệ giá trị ấy là mục tiêu và chủ đề của cuốn sách này. Mã sạch không được viết bằng cách tuân theo một bộ quy tắc. Học thuộc một danh sách các nguyên tắc kinh nghiệm không biến bạn thành người thợ phần mềm lành nghề. Tính chuyên nghiệp và tay nghề đến từ những giá trị dẫn dắt kỷ luật.

## Tài liệu tham khảo

[Refactoring]: *Refactoring: Improving the Design of Existing Code*, Martin Fowler và cộng sự, Addison-Wesley, 1999.

[PRAG]: *The Pragmatic Programmer*, Andrew Hunt, Dave Thomas, Addison-Wesley, 2000.

[GOF]: *Design Patterns: Elements of Reusable Object Oriented Software*, Gamma và cộng sự, Addison-Wesley, 1996.

[Beck97]: *Smalltalk Best Practice Patterns*, Kent Beck, Prentice Hall, 1997.

[Beck07]: *Implementation Patterns*, Kent Beck, Addison-Wesley, 2008.

[PPP]: *Agile Software Development: Principles, Patterns, and Practices*, Robert C. Martin, Prentice Hall, 2002.

[DDD]: *Domain Driven Design*, Eric Evans, Addison-Wesley, 2003.
