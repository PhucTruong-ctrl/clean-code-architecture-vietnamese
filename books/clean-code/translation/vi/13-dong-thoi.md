# Chương 13: Xử lý đồng thời

> Tác giả: Brett L. Schuchert

> “Objects are abstractions of processing. Threads are abstractions of schedule.”
> James O. Coplien¹

¹ Trao đổi riêng.

Viết chương trình xử lý đồng thời sạch rất khó, cực kỳ khó. Viết mã chạy trên một luồng dễ hơn nhiều. Cũng rất dễ viết mã đa luồng trông có vẻ ổn trên bề mặt nhưng lại sai ở tầng sâu hơn. Mã như vậy vẫn chạy tốt cho đến khi hệ thống chịu tải.

Trong chương này, chúng ta bàn về nhu cầu xử lý đồng thời và những khó khăn mà nó đặt ra. Sau đó, chúng ta đưa ra một số khuyến nghị để giải quyết các khó khăn ấy và viết mã đồng thời sạch. Cuối cùng, chúng ta kết luận bằng những vấn đề liên quan đến kiểm thử mã đồng thời.

Xử lý đồng thời sạch là một chủ đề phức tạp, xứng đáng có riêng một cuốn sách. Trong cuốn sách này, chúng tôi sẽ trình bày tổng quan ở đây và cung cấp hướng dẫn chi tiết hơn trong “Concurrency II” ở trang 317. Nếu bạn chỉ tò mò về xử lý đồng thời, chương này hiện tại là đủ. Nếu cần hiểu sâu hơn, bạn cũng nên đọc phần hướng dẫn đó.

## Vì sao cần xử lý đồng thời?

Xử lý đồng thời là một chiến lược tách biệt việc gì được làm khỏi thời điểm nó được làm. Trong các ứng dụng đơn luồng, việc gì và khi nào được thực hiện gắn kết chặt đến mức ta thường có thể xác định trạng thái của toàn bộ ứng dụng bằng cách xem dấu vết ngăn xếp. Lập trình viên gỡ lỗi một hệ thống như vậy có thể đặt một điểm dừng hoặc một chuỗi điểm dừng, rồi biết trạng thái hệ thống dựa vào những điểm dừng nào được chạm tới.

Tách việc gì khỏi thời điểm thực hiện có thể cải thiện đáng kể cả thông lượng lẫn cấu trúc của ứng dụng. Xét về cấu trúc, ứng dụng trông giống nhiều máy tính nhỏ phối hợp với nhau hơn là một vòng lặp chính khổng lồ. Nhờ đó hệ thống dễ hiểu hơn và ta có một số cách mạnh mẽ để tách biệt các mối quan tâm.

Chẳng hạn, hãy xem mô hình “Servlet” tiêu chuẩn của các ứng dụng Web. Những hệ thống này chạy trong một bộ chứa Web hoặc EJB, bộ chứa đó quản lý một phần việc xử lý đồng thời thay bạn. Các servlet được thực thi bất đồng bộ mỗi khi có yêu cầu Web đến. Lập trình viên servlet không phải quản lý tất cả yêu cầu đến. Về nguyên tắc, mỗi lần thực thi servlet sống trong thế giới nhỏ riêng của nó và tách biệt với mọi lần thực thi servlet khác.

Dĩ nhiên, nếu mọi chuyện dễ dàng đến thế thì chương này đã không cần thiết. Trên thực tế, mức độ tách biệt mà các bộ chứa Web cung cấp còn lâu mới hoàn hảo. Lập trình viên servlet phải hiểu rõ và hết sức cẩn thận để bảo đảm chương trình đồng thời của mình đúng. Dù vậy, lợi ích về cấu trúc của mô hình servlet vẫn đáng kể.

Nhưng cấu trúc không phải động lực duy nhất để áp dụng xử lý đồng thời. Một số hệ thống có yêu cầu về thời gian phản hồi và thông lượng, buộc ta phải tự viết giải pháp đồng thời. Ví dụ, hãy xét một bộ tổng hợp thông tin đơn luồng lấy thông tin từ nhiều trang Web khác nhau rồi gộp lại thành bản tóm tắt hằng ngày. Vì hệ thống này chỉ có một luồng, nó lần lượt truy cập từng trang Web, luôn hoàn thành trang này trước khi bắt đầu trang tiếp theo. Lượt chạy hằng ngày phải hoàn tất trong chưa đầy 24 giờ. Tuy nhiên, khi ngày càng có nhiều trang Web được bổ sung, thời gian chạy tăng lên đến mức cần hơn 24 giờ mới thu thập hết dữ liệu. Luồng đơn phải chờ rất nhiều ở các socket Web cho đến khi thao tác I/O hoàn tất. Ta có thể cải thiện hiệu năng bằng thuật toán đa luồng, truy cập nhiều trang Web cùng lúc.

Hoặc hãy xét một hệ thống chỉ xử lý mỗi lần một người dùng và cần đúng một giây cho mỗi người. Hệ thống phản hồi khá nhanh khi chỉ có vài người dùng, nhưng khi số người dùng tăng, thời gian phản hồi cũng tăng. Không ai muốn xếp hàng sau 150 người khác! Ta có thể cải thiện thời gian phản hồi của hệ thống bằng cách xử lý đồng thời nhiều người dùng.

Hoặc xét hệ thống diễn giải các tập dữ liệu lớn nhưng chỉ đưa ra được lời giải hoàn chỉnh sau khi xử lý tất cả. Có thể xử lý mỗi tập dữ liệu trên một máy tính riêng, để nhiều tập được xử lý song song.

### Những lầm tưởng và quan niệm sai

Vậy là có những lý do thuyết phục để áp dụng xử lý đồng thời. Tuy nhiên, như đã nói, xử lý đồng thời rất khó. Nếu không cẩn thận, bạn có thể tạo ra những tình huống hết sức tai hại. Hãy xem những lầm tưởng và quan niệm sai thường gặp sau:

- Xử lý đồng thời luôn cải thiện hiệu năng.

  Đôi khi xử lý đồng thời có thể cải thiện hiệu năng, nhưng chỉ khi có nhiều thời gian chờ để chia sẻ giữa nhiều luồng hoặc nhiều bộ xử lý. Cả hai tình huống này đều không đơn giản.

- Thiết kế không thay đổi khi viết chương trình đồng thời.

  Trên thực tế, thiết kế thuật toán đồng thời có thể khác đáng kể với thiết kế hệ thống đơn luồng. Việc tách biệt điều gì được làm khỏi thời điểm thực hiện thường ảnh hưởng rất lớn đến cấu trúc hệ thống.

- Khi làm việc với bộ chứa như Web hoặc EJB, không cần hiểu các vấn đề về xử lý đồng thời.

  Thực ra, bạn cần biết chính xác bộ chứa đang làm gì và cách bảo vệ chương trình trước các vấn đề cập nhật đồng thời và bế tắc được mô tả ở phần sau của chương này.

Sau đây là một số nhận định cân bằng hơn về việc viết phần mềm đồng thời:

- Xử lý đồng thời phát sinh chi phí phụ, cả về hiệu năng lẫn lượng mã phải viết thêm.
- Xử lý đồng thời đúng rất phức tạp, kể cả với những vấn đề đơn giản.
- Lỗi đồng thời thường không tái hiện được, vì thế người ta hay xem chúng như sự cố nhất thời² thay vì lỗi thực sự.
- Xử lý đồng thời thường đòi hỏi thay đổi căn bản trong chiến lược thiết kế.

² Tia vũ trụ, trục trặc và những thứ tương tự.

## Thách thức

Điều gì khiến lập trình đồng thời khó đến vậy? Hãy xem lớp đơn giản sau:

```java
public class X {
   private int lastIdUsed;

    public int getNextId() {
         return ++lastIdUsed;
     }
}
```

Giả sử ta tạo một thể hiện của `X`, đặt trường `lastIdUsed` thành 42 rồi chia sẻ thể hiện đó cho hai luồng. Bây giờ, giả sử cả hai luồng đều gọi phương thức `getNextId()`. Có ba kết quả có thể xảy ra:

- Luồng một nhận giá trị 43, luồng hai nhận giá trị 44, `lastIdUsed` là 44.
- Luồng một nhận giá trị 44, luồng hai nhận giá trị 43, `lastIdUsed` là 44.
- Luồng một nhận giá trị 43, luồng hai nhận giá trị 43, `lastIdUsed` là 43.

Kết quả thứ ba đáng ngạc nhiên³ xảy ra khi hai luồng giẫm chân lên nhau. Điều này xảy ra vì có nhiều đường thực thi khả dĩ mà hai luồng có thể đi qua dòng mã Java duy nhất đó, và một số đường dẫn đến kết quả sai. Có bao nhiêu đường khác nhau? Để trả lời chính xác, ta cần hiểu trình biên dịch Just-In-Time làm gì với mã byte được sinh ra, cũng như mô hình bộ nhớ Java xem thao tác nào là nguyên tử.

Câu trả lời nhanh, chỉ xét mã byte đã sinh, là có 12.870 đường thực thi khả dĩ⁴ cho hai luồng cùng thực thi trong phương thức `getNextId`. Nếu đổi kiểu của `lastIdUsed` từ `int` sang `long`, số đường khả dĩ tăng lên 2.704.156. Dĩ nhiên, phần lớn các đường đó cho kết quả hợp lệ. Vấn đề là một số đường thì không.

³ Xem “Digging Deeper” ở trang 323.
⁴ Xem “Possible Paths of Execution” ở trang 321.

## Các nguyên tắc phòng vệ khi xử lý đồng thời

Sau đây là một loạt nguyên tắc và kỹ thuật giúp bảo vệ hệ thống khỏi các vấn đề do mã đồng thời gây ra.

### Nguyên tắc trách nhiệm đơn nhất

SRP⁵ quy định rằng một phương thức, lớp hoặc thành phần nhất định chỉ nên có một lý do để thay đổi. Thiết kế xử lý đồng thời đủ phức tạp để tự nó trở thành một lý do thay đổi, vì vậy cần được tách khỏi phần còn lại của mã. Đáng tiếc, chi tiết triển khai xử lý đồng thời thường bị nhúng thẳng vào mã sản phẩm. Hãy cân nhắc một số điều sau:

- Mã liên quan đến xử lý đồng thời có vòng đời phát triển, thay đổi và tinh chỉnh riêng.
- Mã liên quan đến xử lý đồng thời có những thách thức riêng, khác với mã không liên quan, và thường khó hơn.
- Số cách mã đồng thời viết sai có thể thất bại đã đủ gây khó khăn, chưa kể gánh nặng từ mã ứng dụng xung quanh.

Khuyến nghị: Hãy tách mã xử lý đồng thời khỏi phần mã còn lại.⁶

⁵ [PPP]
⁶ Xem “Client/Server Example” ở trang 317.

### Hệ quả: Giới hạn phạm vi dữ liệu

Như đã thấy, hai luồng cùng sửa một trường trong đối tượng dùng chung có thể cản trở lẫn nhau và gây ra hành vi bất ngờ. Một giải pháp là dùng từ khóa `synchronized` để bảo vệ vùng tới hạn trong mã sử dụng đối tượng dùng chung. Điều quan trọng là hạn chế số lượng vùng tới hạn như vậy. Càng có nhiều nơi có thể cập nhật dữ liệu dùng chung thì càng có khả năng:

- Bạn quên bảo vệ một hoặc nhiều nơi, khiến toàn bộ mã sửa dữ liệu dùng chung đó mất an toàn.
- Phải lặp lại công sức để bảo đảm mọi nơi đều được bảo vệ hiệu quả, vi phạm DRY⁷.
- Khó xác định nguồn gốc lỗi, vốn đã đủ khó tìm.

Khuyến nghị: Hãy coi trọng việc đóng gói dữ liệu; hạn chế nghiêm ngặt quyền truy cập vào mọi dữ liệu có thể được chia sẻ.

⁷ [PRAG].

### Hệ quả: Dùng bản sao dữ liệu

Một cách hay để tránh dữ liệu dùng chung là ngay từ đầu đừng chia sẻ dữ liệu. Trong một số tình huống, ta có thể sao chép đối tượng rồi coi chúng là chỉ đọc. Trường hợp khác, ta có thể sao chép đối tượng, thu thập kết quả từ nhiều luồng trong các bản sao này, rồi gộp kết quả bằng một luồng duy nhất.

Nếu có cách dễ dàng để tránh chia sẻ đối tượng, mã tạo ra sẽ ít có khả năng phát sinh vấn đề hơn nhiều. Có thể bạn lo ngại chi phí tạo thêm đối tượng. Hãy thử nghiệm để xem liệu đây có thực sự là vấn đề hay không. Tuy nhiên, nếu dùng bản sao đối tượng giúp mã tránh phải đồng bộ hóa, phần tiết kiệm được nhờ không phải dùng khóa nội tại có thể bù cho chi phí tạo đối tượng và thu gom rác bổ sung.

### Hệ quả: Các luồng nên độc lập tối đa

Hãy viết mã đa luồng sao cho mỗi luồng tồn tại trong thế giới riêng, không chia sẻ dữ liệu với luồng nào khác. Mỗi luồng xử lý một yêu cầu của máy khách, nhận toàn bộ dữ liệu cần thiết từ nguồn không dùng chung và lưu vào biến cục bộ. Như vậy, mỗi luồng hoạt động như thể nó là luồng duy nhất trên đời và không có yêu cầu đồng bộ hóa nào.

Ví dụ, các lớp kế thừa `HttpServlet` nhận toàn bộ thông tin dưới dạng tham số truyền vào các phương thức `doGet` và `doPost`. Điều này khiến mỗi Servlet hoạt động như thể nó có máy riêng. Chừng nào mã trong Servlet chỉ dùng biến cục bộ, Servlet sẽ không thể gây ra vấn đề đồng bộ hóa. Dĩ nhiên, phần lớn ứng dụng dùng Servlet rồi cũng phải làm việc với tài nguyên dùng chung như kết nối cơ sở dữ liệu.

Khuyến nghị: Hãy thử phân vùng dữ liệu thành các tập con độc lập để các luồng độc lập, có thể chạy trên những bộ xử lý khác nhau, xử lý chúng.

## Hiểu rõ thư viện của bạn

Java 5 có nhiều cải tiến hỗ trợ phát triển đồng thời so với các phiên bản trước. Khi viết mã đa luồng trong Java 5, cần cân nhắc một số điều:

- Dùng các collection an toàn luồng được cung cấp sẵn.
- Dùng framework executor để thực thi các tác vụ không liên quan với nhau.
- Khi có thể, hãy dùng giải pháp không chặn.
- Một số lớp thư viện không an toàn luồng.

### Collection an toàn luồng

Khi Java còn non trẻ, Doug Lea đã viết cuốn sách có ảnh hưởng lớn⁸ *Concurrent Programming in Java*. Cùng với cuốn sách, ông phát triển một số collection an toàn luồng; sau này chúng trở thành một phần của JDK trong gói `java.util.concurrent`. Các collection trong gói này an toàn trong môi trường đa luồng và hoạt động hiệu quả. Trên thực tế, cách triển khai `ConcurrentHashMap` hoạt động tốt hơn `HashMap` trong gần như mọi tình huống. Nó cũng cho phép đọc và ghi đồng thời cùng lúc, đồng thời có các phương thức hỗ trợ những thao tác kết hợp phổ biến vốn không an toàn luồng. Nếu môi trường triển khai là Java 5, hãy bắt đầu với `ConcurrentHashMap`.

⁸ [Lea99].

Một số lớp khác cũng được bổ sung để hỗ trợ thiết kế xử lý đồng thời nâng cao. Sau đây là vài ví dụ:

| Lớp | Mô tả |
|---|---|
| `ReentrantLock` | Một khóa có thể được lấy trong phương thức này và giải phóng trong phương thức khác. |
| `Semaphore` | Cách triển khai semaphore kinh điển, một khóa có bộ đếm. |
| `CountDownLatch` | Một khóa chờ một số sự kiện xảy ra rồi mới giải phóng tất cả các luồng đang chờ. Nhờ vậy mọi luồng đều có cơ hội công bằng để bắt đầu gần như cùng lúc. |

Khuyến nghị: Hãy xem lại các lớp hiện có. Với Java, hãy làm quen với `java.util.concurrent`, `java.util.concurrent.atomic`, `java.util.concurrent.locks`.

## Hiểu rõ các mô hình thực thi

Có nhiều cách khác nhau để phân chia hành vi trong ứng dụng đồng thời. Để bàn về chúng, ta cần hiểu một số định nghĩa cơ bản.

| Thuật ngữ | Định nghĩa |
|---|---|
| Tài nguyên có giới hạn | Tài nguyên có kích thước hoặc số lượng cố định được dùng trong môi trường đồng thời. Ví dụ gồm kết nối cơ sở dữ liệu và bộ đệm đọc/ghi kích thước cố định. |
| Loại trừ tương hỗ | Tại một thời điểm, chỉ một luồng có thể truy cập dữ liệu hoặc tài nguyên dùng chung. |
| Bỏ đói luồng | Một luồng hoặc một nhóm luồng không thể tiếp tục trong thời gian quá lâu hoặc mãi mãi. Ví dụ, nếu luôn cho các luồng chạy nhanh đi trước mà chúng không bao giờ hết, các luồng chạy chậm hơn có thể bị bỏ đói. |
| Bế tắc (deadlock) | Hai hoặc nhiều luồng chờ nhau hoàn tất. Mỗi luồng giữ một tài nguyên mà luồng kia cần, và không luồng nào có thể hoàn tất cho đến khi nhận được tài nguyên kia. |
| Bế tắc sống (livelock) | Các luồng đi cùng nhịp, mỗi luồng cố làm việc nhưng lại gặp luồng khác “cản đường”. Do cộng hưởng, các luồng tiếp tục cố tiến lên nhưng không thể tiến triển trong thời gian quá lâu, hoặc mãi mãi. |

Dựa trên các định nghĩa này, giờ ta có thể bàn về những mô hình thực thi khác nhau được dùng trong lập trình đồng thời.

### Nhà sản xuất-Người tiêu thụ⁹

Một hoặc nhiều luồng nhà sản xuất tạo ra công việc rồi đặt vào bộ đệm hoặc hàng đợi. Một hoặc nhiều luồng người tiêu thụ lấy công việc khỏi hàng đợi và hoàn thành nó. Hàng đợi giữa nhà sản xuất và người tiêu thụ là tài nguyên có giới hạn. Điều này có nghĩa nhà sản xuất phải chờ hàng đợi có chỗ trống trước khi ghi, còn người tiêu thụ phải chờ đến khi có thứ để tiêu thụ. Việc phối hợp thông qua hàng đợi đòi hỏi nhà sản xuất và người tiêu thụ báo hiệu cho nhau. Nhà sản xuất ghi vào hàng đợi rồi báo rằng hàng đợi không còn trống. Người tiêu thụ đọc khỏi hàng đợi rồi báo rằng hàng đợi không còn đầy. Cả hai phía có thể phải chờ được thông báo mới tiếp tục được.

⁹ http://en.wikipedia.org/wiki/Producer-consumer

### Người đọc-Người ghi¹⁰

Khi có một tài nguyên dùng chung chủ yếu cung cấp thông tin cho người đọc nhưng đôi lúc được người ghi cập nhật, thông lượng là vấn đề cần quan tâm. Ưu tiên thông lượng có thể gây nghẽn tài nguyên và tích tụ thông tin cũ. Cho phép cập nhật có thể ảnh hưởng đến thông lượng. Việc điều phối người đọc để họ không đọc khi người ghi đang cập nhật, và ngược lại, là một bài toán cân bằng khó. Người ghi thường chặn nhiều người đọc trong thời gian dài, gây vấn đề về thông lượng.

Thách thức là cân bằng nhu cầu của cả người đọc lẫn người ghi để bảo đảm hoạt động đúng, đạt thông lượng hợp lý và tránh nghẽn tài nguyên. Một chiến lược đơn giản buộc người ghi chờ đến khi không còn người đọc nào rồi mới cho phép cập nhật. Tuy nhiên, nếu người đọc liên tục xuất hiện, người ghi sẽ bị bỏ đói. Ngược lại, nếu người ghi thường xuyên xuất hiện và được ưu tiên, thông lượng sẽ giảm. Bài toán này nhằm tìm sự cân bằng đó và tránh các vấn đề cập nhật đồng thời.

¹⁰ http://en.wikipedia.org/wiki/Readers-writers_problem

### Các triết gia ăn tối¹¹

Hãy tưởng tượng một số triết gia ngồi quanh một chiếc bàn tròn. Bên trái mỗi người có một chiếc nĩa. Giữa bàn là một tô mì spaghetti lớn. Các triết gia dành thời gian suy nghĩ, trừ khi họ đói. Khi đói, họ nhặt chiếc nĩa ở hai bên mình lên để ăn. Một triết gia không thể ăn nếu không cầm cả hai chiếc nĩa. Nếu triết gia bên phải hoặc bên trái đang dùng một chiếc nĩa mà người đó cần, họ phải chờ đến khi triết gia kia ăn xong và đặt nĩa xuống. Ăn xong, mỗi triết gia đặt cả hai chiếc nĩa xuống bàn rồi chờ đến khi đói lại.

Thay triết gia bằng luồng, thay nĩa bằng tài nguyên, ta có một vấn đề tương tự nhiều ứng dụng doanh nghiệp, nơi các tiến trình cạnh tranh tài nguyên. Nếu không được thiết kế cẩn thận, hệ thống cạnh tranh theo cách này có thể gặp bế tắc, bế tắc sống, suy giảm thông lượng và hiệu quả.

¹¹ http://en.wikipedia.org/wiki/Dining_philosophers_problem

Phần lớn vấn đề đồng thời bạn gặp có thể là một biến thể của ba vấn đề này. Hãy nghiên cứu các thuật toán ấy và tự viết giải pháp để khi gặp vấn đề đồng thời, bạn sẵn sàng xử lý hơn.

Khuyến nghị: Hãy học các thuật toán cơ bản này và hiểu những giải pháp của chúng.

## Cẩn thận với phụ thuộc giữa các phương thức đồng bộ

Phụ thuộc giữa các phương thức đồng bộ gây ra lỗi khó phát hiện trong mã đồng thời. Ngôn ngữ Java có khái niệm `synchronized` để bảo vệ một phương thức riêng lẻ. Tuy nhiên, nếu cùng một lớp dùng chung có nhiều hơn một phương thức đồng bộ, hệ thống của bạn có thể được viết sai.¹²

Khuyến nghị: Tránh dùng nhiều hơn một phương thức trên một đối tượng dùng chung.

Sẽ có lúc bạn buộc phải dùng nhiều phương thức trên một đối tượng dùng chung. Khi đó, có ba cách để làm cho mã đúng:

- Khóa phía máy khách: Máy khách khóa máy chủ trước khi gọi phương thức đầu tiên và bảo đảm khóa được giữ trong suốt đoạn mã gọi phương thức cuối cùng.
- Khóa phía máy chủ: Trong máy chủ, tạo một phương thức khóa máy chủ, gọi tất cả các phương thức rồi mở khóa. Máy khách gọi phương thức mới này.
- Máy chủ thích nghi: Tạo một thành phần trung gian thực hiện việc khóa. Đây là ví dụ về khóa phía máy chủ trong trường hợp không thể thay đổi máy chủ ban đầu.

¹² Xem “Dependencies Between Methods Can Break Concurrent Code” ở trang 329.

## Giữ các vùng đồng bộ nhỏ

Từ khóa `synchronized` tạo ra một khóa. Mọi đoạn mã được bảo vệ bằng cùng một khóa đều được bảo đảm chỉ có một luồng thực thi bên trong tại bất kỳ thời điểm nào. Khóa tốn kém vì gây chậm trễ và phát sinh chi phí phụ. Vì vậy, ta không muốn rải các câu lệnh `synchronized` khắp mã. Mặt khác, các vùng tới hạn¹³ phải được bảo vệ. Do đó, ta muốn thiết kế mã sao cho có ít vùng tới hạn nhất có thể.

Một số lập trình viên thiếu kinh nghiệm cố đạt mục tiêu này bằng cách làm cho vùng tới hạn thật lớn. Tuy nhiên, kéo dài việc đồng bộ hóa vượt quá vùng tới hạn tối thiểu làm tăng tranh chấp và giảm hiệu năng.¹⁴

Khuyến nghị: Hãy giữ các vùng đồng bộ nhỏ nhất có thể.

¹³ Vùng tới hạn là bất kỳ đoạn mã nào phải được bảo vệ khỏi việc sử dụng đồng thời để chương trình hoạt động đúng.
¹⁴ Xem “Increasing Throughput” ở trang 333.

## Viết mã tắt hệ thống đúng cách rất khó

Viết một hệ thống được thiết kế để luôn chạy và tồn tại mãi mãi khác với viết thứ gì đó hoạt động một thời gian rồi tắt một cách êm đẹp.

Tắt hệ thống êm đẹp cho đúng có thể khó. Các vấn đề thường gặp liên quan đến bế tắc,¹⁵ khi luồng chờ một tín hiệu để tiếp tục nhưng tín hiệu đó không bao giờ đến.

Ví dụ, hãy hình dung một hệ thống có luồng cha tạo ra một số luồng con rồi chờ tất cả chúng kết thúc trước khi giải phóng tài nguyên và tắt. Nếu một luồng được tạo ra rơi vào bế tắc thì sao? Luồng cha sẽ chờ mãi, và hệ thống không bao giờ tắt.

Hoặc xét một hệ thống tương tự đã nhận lệnh tắt. Luồng cha bảo tất cả luồng con bỏ tác vụ và kết thúc. Nhưng nếu hai luồng con đang hoạt động theo cặp nhà sản xuất/người tiêu thụ thì sao? Giả sử nhà sản xuất nhận tín hiệu từ luồng cha rồi nhanh chóng tắt. Người tiêu thụ có thể đang chờ thông điệp từ nhà sản xuất và bị chặn ở trạng thái không thể nhận tín hiệu tắt. Nó có thể mắc kẹt chờ nhà sản xuất và không bao giờ kết thúc, khiến luồng cha cũng không thể kết thúc.

Những tình huống như thế này không hề hiếm. Vì vậy, nếu phải viết mã đồng thời có yêu cầu tắt êm đẹp, hãy chuẩn bị dành phần lớn thời gian để làm cho việc tắt diễn ra đúng cách.

Khuyến nghị: Hãy nghĩ đến việc tắt hệ thống từ sớm và triển khai sớm. Việc này sẽ mất nhiều thời gian hơn bạn dự tính. Hãy xem lại các thuật toán hiện có, vì vấn đề này có lẽ khó hơn bạn nghĩ.

¹⁵ Xem “Deadlock” ở trang 335.

## Kiểm thử mã đa luồng

Không thực tế nếu muốn chứng minh mã là đúng. Kiểm thử không bảo đảm tính đúng đắn. Tuy nhiên, kiểm thử tốt có thể giảm thiểu rủi ro. Tất cả điều này đều đúng với giải pháp đơn luồng. Ngay khi có từ hai luồng trở lên dùng cùng mã và làm việc với dữ liệu dùng chung, mọi thứ trở nên phức tạp hơn đáng kể.

Khuyến nghị: Hãy viết các kiểm thử có khả năng bộc lộ vấn đề rồi chạy thường xuyên với các cấu hình chương trình, cấu hình hệ thống và mức tải khác nhau. Nếu kiểm thử thất bại, hãy truy tìm nguyên nhân. Đừng bỏ qua một lần thất bại chỉ vì lần chạy sau kiểm thử lại thành công.

Có rất nhiều điều cần cân nhắc. Sau đây là thêm một số khuyến nghị cụ thể:

- Xem các lỗi chập chờn là dấu hiệu có thể liên quan đến luồng.
- Trước hết, hãy làm cho mã không đa luồng hoạt động đúng.
- Làm cho mã đa luồng có thể thay thế linh hoạt.
- Làm cho mã đa luồng có thể điều chỉnh.
- Chạy với số luồng nhiều hơn số bộ xử lý.
- Chạy trên các nền tảng khác nhau.
- Gắn thiết bị đo đạc vào mã để cố ép lỗi xuất hiện.

¹⁶ Bạn có biết mô hình luồng trong Java không bảo đảm lập lịch luồng có tính chiếm quyền? Các hệ điều hành hiện đại hỗ trợ lập lịch chiếm quyền, nên ta có được điều đó “miễn phí”. Dù vậy, JVM không bảo đảm điều này.

### Xem các lỗi chập chờn là dấu hiệu có thể liên quan đến luồng

Mã đa luồng khiến những thứ “đơn giản là không thể lỗi” lại thất bại. Hầu hết nhà phát triển không có trực giác tốt về cách luồng tương tác với mã khác, kể cả các tác giả. Lỗi trong mã đa luồng có thể chỉ biểu hiện một lần trong một nghìn, thậm chí một triệu lần thực thi. Việc cố tái hiện lỗi hệ thống có thể khiến người ta nản lòng. Điều này thường khiến nhà phát triển gạt lỗi sang một bên, cho rằng đó là tia vũ trụ, trục trặc phần cứng hay một kiểu sự cố “chỉ xảy ra một lần” nào khác. Tốt nhất hãy giả định rằng không có sự cố nào chỉ xảy ra một lần. Càng phớt lờ những lỗi “một lần” như vậy, người ta càng xây thêm mã dựa trên một cách tiếp cận có thể đã sai.

Khuyến nghị: Đừng xem lỗi hệ thống là sự cố chỉ xảy ra một lần.

### Trước hết, hãy làm cho mã không đa luồng hoạt động đúng

Điều này có vẻ hiển nhiên, nhưng nhắc lại cũng chẳng hại gì. Hãy bảo đảm mã hoạt động bên ngoài môi trường luồng. Nói chung, điều đó có nghĩa là tạo các POJO để các luồng gọi đến. POJO không nhận biết luồng, vì vậy có thể được kiểm thử bên ngoài môi trường đa luồng. Càng đưa được nhiều phần trong hệ thống vào các POJO như vậy thì càng tốt.

Khuyến nghị: Đừng cố xử lý lỗi không liên quan đến luồng và lỗi liên quan đến luồng cùng lúc. Hãy bảo đảm mã hoạt động bên ngoài các luồng.

### Làm cho mã đa luồng có thể thay thế linh hoạt

Hãy viết mã hỗ trợ xử lý đồng thời sao cho có thể chạy với nhiều cấu hình:

- Một luồng, nhiều luồng, hoặc thay đổi số lượng trong khi chạy.
- Mã đa luồng tương tác với thành phần có thể là thật hoặc đối tượng giả dùng trong kiểm thử.
- Thực thi với các đối tượng giả chạy nhanh, chậm hoặc với tốc độ thay đổi.
- Cấu hình để kiểm thử có thể chạy qua một số vòng lặp nhất định.

Khuyến nghị: Hãy làm cho mã dựa trên luồng đặc biệt dễ thay thế để có thể chạy với nhiều cấu hình khác nhau.

### Làm cho mã đa luồng có thể điều chỉnh

Tìm được số luồng cân bằng phù hợp thường đòi hỏi thử và sai. Ngay từ đầu, hãy tìm cách đo hiệu năng hệ thống với các cấu hình khác nhau. Cho phép dễ dàng điều chỉnh số luồng. Cân nhắc cho phép thay đổi số lượng này khi hệ thống đang chạy. Cân nhắc cho phép hệ thống tự điều chỉnh dựa trên thông lượng và mức sử dụng hệ thống.

### Chạy với số luồng nhiều hơn số bộ xử lý

Khi hệ thống chuyển đổi giữa các tác vụ, nhiều chuyện có thể xảy ra. Để khuyến khích việc chuyển đổi tác vụ, hãy chạy với số luồng nhiều hơn số bộ xử lý hoặc số lõi. Tác vụ càng chuyển đổi thường xuyên, càng có khả năng bạn phát hiện mã thiếu vùng tới hạn hoặc gây bế tắc.

### Chạy trên các nền tảng khác nhau

Giữa năm 2007, chúng tôi xây dựng một khóa học về lập trình đồng thời. Việc xây dựng khóa học chủ yếu diễn ra trên OS X. Khóa học được giảng dạy bằng Windows XP chạy trong máy ảo. Các kiểm thử được viết để minh họa điều kiện thất bại không thất bại thường xuyên trên môi trường XP như khi chạy trên OS X.

Trong mọi trường hợp, mã được kiểm thử đều đã biết là sai. Điều này càng củng cố sự thật rằng các hệ điều hành khác nhau có chính sách xử lý luồng khác nhau, và mỗi chính sách ảnh hưởng đến quá trình thực thi mã. Mã đa luồng hoạt động khác nhau trong các môi trường khác nhau.¹⁶ Bạn nên chạy kiểm thử trong mọi môi trường có thể triển khai.

Khuyến nghị: Hãy chạy mã đa luồng trên tất cả nền tảng đích từ sớm và thường xuyên.

### Gắn thiết bị đo đạc vào mã để cố ép lỗi xuất hiện

Lỗi trong mã đồng thời thường ẩn mình. Các kiểm thử đơn giản thường không bộc lộ chúng. Thực tế, chúng thường ẩn trong quá trình xử lý bình thường. Lỗi có thể chỉ xuất hiện vài giờ, vài ngày, thậm chí vài tuần một lần!

Lý do lỗi luồng có thể hiếm gặp, thất thường và khó tái hiện là trong hàng nghìn đường đi có thể qua một vùng dễ có lỗi, chỉ một vài đường thực sự thất bại. Vì vậy, xác suất đi vào đường gây lỗi có thể thấp đến đáng ngạc nhiên. Điều này khiến việc phát hiện và gỡ lỗi rất khó.

Làm thế nào để tăng cơ hội bắt gặp những lỗi hiếm như vậy? Bạn có thể gắn thiết bị đo đạc vào mã và buộc mã chạy theo thứ tự khác nhau bằng cách thêm lời gọi đến các phương thức như `Object.wait()`, `Object.sleep()`, `Object.yield()` và `Object.priority()`.

Mỗi phương thức này có thể ảnh hưởng đến thứ tự thực thi, qua đó tăng khả năng phát hiện lỗi. Tốt hơn hết là mã sai thất bại sớm và thường xuyên nhất có thể.

Có hai lựa chọn để gắn thiết bị đo đạc vào mã:

- Viết thủ công.
- Tự động hóa.

### Viết thủ công

Bạn có thể tự thêm lời gọi `wait()`, `sleep()`, `yield()` và `priority()` vào mã. Cách này có thể phù hợp khi kiểm thử một đoạn mã đặc biệt khó nhằn.

Sau đây là một ví dụ:

```java
public synchronized String nextUrlOrNull() {
    if(hasNext()) {
        String url = urlGenerator.next();
        Thread.yield(); // được chèn vào để kiểm thử.
        updateHasNext();
        return url;
    }
    return null;
}
```

Lời gọi `yield()` được chèn vào sẽ thay đổi các đường thực thi mà mã đi qua và có thể khiến mã thất bại trong khi trước đó không thất bại. Nếu mã hỏng, không phải vì bạn thêm lời gọi `yield()`.¹⁷ Mã vốn đã sai, và việc này chỉ làm lỗi lộ ra.

Cách tiếp cận này có nhiều vấn đề:

- Bạn phải tự tìm các vị trí thích hợp để chèn.
- Làm sao biết nên đặt lời gọi ở đâu và dùng loại lời gọi nào?
- Nếu để mã như vậy trong môi trường sản phẩm, mã sẽ chậm đi không cần thiết.
- Đây là cách thử đại trà. Bạn có thể tìm ra lỗi, cũng có thể không. Thực tế, khả năng không đứng về phía bạn.

Điều ta cần là cách thực hiện việc này khi kiểm thử nhưng không phải khi chạy trong môi trường sản phẩm. Ta cũng cần dễ dàng thay đổi cấu hình giữa các lần chạy khác nhau, nhờ đó tăng cơ hội phát hiện lỗi khi tổng hợp kết quả.

Rõ ràng, nếu chia hệ thống thành các POJO không biết gì về luồng và các lớp điều khiển luồng, việc tìm vị trí thích hợp để gắn thiết bị đo đạc sẽ dễ hơn. Hơn nữa, ta có thể tạo nhiều bộ dụng cụ kiểm thử khác nhau để gọi các POJO trong những chế độ khác nhau, với lời gọi `sleep`, `yield` và những thứ tương tự.

¹⁷ Điều này không hoàn toàn đúng. Vì JVM không bảo đảm lập lịch luồng có tính chiếm quyền, một thuật toán cụ thể có thể luôn hoạt động trên hệ điều hành không chiếm quyền điều khiển luồng. Điều ngược lại cũng có thể xảy ra, nhưng vì những lý do khác.

### Tự động hóa

Bạn có thể dùng các công cụ như framework hướng khía cạnh, CGLIB hoặc ASM để tự động gắn thiết bị đo đạc vào mã. Chẳng hạn, bạn có thể dùng một lớp chỉ có một phương thức:

```java
public class ThreadJigglePoint {
    public static void jiggle() {
    }
}
```

Bạn có thể thêm lời gọi đến phương thức này ở nhiều nơi trong mã:

```java
public synchronized String nextUrlOrNull() {
    if(hasNext()) {
        ThreadJiglePoint.jiggle();
        String url = urlGenerator.next();
        ThreadJiglePoint.jiggle();
        updateHasNext();
        ThreadJiglePoint.jiggle();
        return url;
    }
    return null;
}
```

Giờ bạn dùng một aspect đơn giản chọn ngẫu nhiên giữa không làm gì, ngủ hoặc nhường luồng.

Hoặc hãy hình dung lớp `ThreadJigglePoint` có hai cách triển khai. Cách thứ nhất triển khai `jiggle` sao cho không làm gì và được dùng trong môi trường sản phẩm. Cách thứ hai tạo ra một số ngẫu nhiên để chọn giữa ngủ, nhường luồng hoặc đi tiếp. Nếu chạy kiểm thử một nghìn lần với thao tác lắc ngẫu nhiên, bạn có thể tìm ra một số lỗi. Nếu kiểm thử thành công, ít nhất bạn có thể nói rằng mình đã làm tròn trách nhiệm. Cách này hơi đơn giản, nhưng có thể là một lựa chọn hợp lý khi chưa có công cụ tinh vi hơn.

Có một công cụ tên là ConTest¹⁸ do IBM phát triển, có chức năng tương tự nhưng tinh vi hơn khá nhiều.

Mục đích là làm cho mã bị xáo trộn để các luồng chạy theo thứ tự khác nhau ở những thời điểm khác nhau. Kết hợp các kiểm thử được viết tốt với thao tác xáo trộn có thể tăng đáng kể cơ hội phát hiện lỗi.

Khuyến nghị: Hãy dùng các chiến lược xáo trộn để tìm lỗi.

¹⁸ http://www.alphaworks.ibm.com/tech/contest

## Kết luận

Viết mã đồng thời cho đúng rất khó. Mã vốn dễ theo dõi có thể trở thành ác mộng khi nhiều luồng và dữ liệu dùng chung xuất hiện. Nếu phải viết mã đồng thời, bạn cần viết mã sạch một cách nghiêm túc, nếu không sẽ phải đối mặt với những lỗi khó phát hiện và hiếm gặp.

Trước hết, hãy tuân theo Nguyên tắc Trách nhiệm Đơn nhất. Chia hệ thống thành các POJO để tách mã nhận biết luồng khỏi mã không nhận biết luồng. Khi kiểm thử mã nhận biết luồng, hãy bảo đảm bạn chỉ kiểm thử phần đó, không kiểm thử thứ gì khác. Điều này cho thấy mã nhận biết luồng nên nhỏ và tập trung.

Hãy biết các nguồn gây ra vấn đề đồng thời: nhiều luồng thao tác trên dữ liệu dùng chung hoặc dùng chung một nhóm tài nguyên. Các tình huống ở ranh giới, chẳng hạn tắt hệ thống gọn gàng hoặc hoàn thành một vòng lặp, có thể đặc biệt khó xử lý.

Hãy học thư viện và nắm các thuật toán cơ bản. Hiểu cách một số tính năng của thư viện hỗ trợ giải quyết những vấn đề tương tự các thuật toán cơ bản.

Hãy học cách tìm các vùng mã cần khóa rồi khóa chúng. Đừng khóa những vùng không cần khóa. Tránh gọi một vùng đã khóa từ một vùng đã khóa khác. Việc này đòi hỏi hiểu sâu điều gì được chia sẻ và điều gì không. Hãy giữ số lượng đối tượng dùng chung cũng như phạm vi chia sẻ ở mức hẹp nhất có thể. Thay đổi thiết kế của các đối tượng chứa dữ liệu dùng chung để đáp ứng nhu cầu của máy khách, thay vì buộc máy khách phải quản lý trạng thái dùng chung.

Vấn đề sẽ phát sinh. Những vấn đề không xuất hiện sớm thường bị gạt đi như thể chỉ xảy ra một lần. Những “lỗi một lần” này thường chỉ xảy ra khi tải cao hoặc vào những thời điểm tưởng như ngẫu nhiên. Vì vậy, bạn cần có khả năng chạy đi chạy lại mã liên quan đến luồng trong nhiều cấu hình và trên nhiều nền tảng. Khả năng kiểm thử, vốn đến một cách tự nhiên khi tuân theo Ba Quy luật TDD, đòi hỏi một mức độ linh hoạt nhất định, nhờ đó có thể chạy mã với nhiều cấu hình hơn.

Bạn sẽ cải thiện đáng kể cơ hội tìm ra mã sai nếu dành thời gian gắn thiết bị đo đạc vào mã. Bạn có thể làm thủ công hoặc dùng một loại công nghệ tự động nào đó. Hãy đầu tư vào việc này từ sớm. Bạn nên chạy mã dựa trên luồng càng lâu càng tốt trước khi đưa vào môi trường sản phẩm.

Nếu tiếp cận sạch sẽ, cơ hội làm đúng của bạn sẽ tăng lên đáng kể.

## Tài liệu tham khảo

[Lea99]: *Concurrent Programming in Java: Design Principles and Patterns*, ấn bản thứ 2, Doug Lea, Prentice Hall, 1999.

[PPP]: *Agile Software Development: Principles, Patterns, and Practices*, Robert C. Martin, Prentice Hall, 2002.

[PRAG]: *The Pragmatic Programmer*, Andrew Hunt, Dave Thomas, Addison-Wesley, 2000.
