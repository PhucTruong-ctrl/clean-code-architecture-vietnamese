# Chương 2: Câu chuyện về hai giá trị

![Minh họa](assets/illustrations/02-chuong-02.png){w=250}

## Hành vi

Mọi hệ thống phần mềm mang lại hai giá trị khác nhau cho các bên liên quan: hành vi và cấu trúc. Các nhà phát triển phần mềm chịu trách nhiệm đảm bảo cả hai giá trị đó luôn cao. Thật đáng buồn, họ thường chỉ tập trung vào một bên mà bỏ qua bên kia. Còn đáng buồn hơn, họ thường tập trung vào giá trị kém hơn trong hai cái, khiến hệ thống phần mềm cuối cùng trở nên vô giá trị.

Giá trị đầu tiên của phần mềm là hành vi. Lập trình viên được thuê để khiến máy móc hoạt động theo cách giúp các bên liên quan kiếm được hoặc tiết kiệm tiền. Chúng ta làm điều đó bằng cách hỗ trợ các bên liên quan xây dựng bản đặc tả chức năng, hay tài liệu yêu cầu. Sau đó, chúng ta viết mã để máy móc đáp ứng những yêu cầu ấy.

Khi máy móc vi phạm các yêu cầu đó, lập trình viên lấy bộ gỡ lỗi ra và khắc phục sự cố.

Nhiều lập trình viên tin rằng đó là toàn bộ công việc của họ. Họ tin rằng việc của họ là khiến máy móc thực hiện các yêu cầu và sửa bất kỳ lỗi nào. Họ lầm to.

## Kiến trúc

Giá trị thứ hai của phần mềm liên quan đến chính từ "software", một từ ghép từ "soft" và "ware". "Ware" có nghĩa là "sản phẩm"; còn "soft"… Chính ở đó nằm giá trị thứ hai.

Phần mềm được phát minh để trở nên "mềm". Nó được xem là cách giúp thay đổi hành vi máy móc dễ dàng. Nếu muốn hành vi máy móc khó thay đổi, hẳn chúng ta đã gọi nó là phần cứng.

Để thực hiện mục đích ấy, phần mềm phải mềm, tức là phải dễ thay đổi. Khi các bên liên quan đổi ý về một tính năng, thay đổi đó phải đơn giản và dễ thực hiện. Độ khó của thay đổi chỉ nên tỷ lệ thuận với phạm vi thay đổi, chứ không phụ thuộc vào hình dạng của nó.

Chính sự khác biệt giữa phạm vi và hình dạng thường làm chi phí phát triển phần mềm tăng. Vì thế chi phí có thể tăng vượt xa mức tương ứng với quy mô thay đổi được yêu cầu. Đó là lý do năm phát triển đầu tiên rẻ hơn năm thứ hai, còn năm thứ hai rẻ hơn năm thứ ba.

Từ góc nhìn của các bên liên quan, họ chỉ cung cấp một luồng các thay đổi có phạm vi tương đương nhau. Từ góc nhìn của nhà phát triển, các bên liên quan đang đưa cho họ một luồng các mảnh ghép xếp hình mà họ phải lắp vào một bức tranh ghép ngày càng phức tạp. Mỗi yêu cầu mới lại khó lắp hơn yêu cầu trước, vì hình dáng của hệ thống không khớp với hình dáng của yêu cầu.

Tôi dùng từ "hình dáng" (shape) theo một cách không thông dụng, nhưng nghĩ rằng ẩn dụ này phù hợp. Các nhà phát triển phần mềm thường cảm thấy như bị ép phải nhét chốt vuông vào lỗ tròn.

Vấn đề nằm ở kiến trúc hệ thống. Kiến trúc càng ưu tiên hình dạng này hơn hình dạng khác, các tính năng mới càng khó lắp vào cấu trúc đó. Vì vậy, trong chừng mực khả thi, kiến trúc nên không thiên về bất kỳ hình dạng cụ thể nào.

## Giá trị lớn hơn

Chức năng hay kiến trúc? Hai giá trị này, cái nào lớn hơn? Việc hệ thống phần mềm hoạt động quan trọng hơn, hay việc nó dễ thay đổi quan trọng hơn?

Nếu hỏi các nhà quản lý kinh doanh, họ thường nói rằng việc hệ thống phần mềm hoạt động quan trọng hơn. Các nhà phát triển, ngược lại, thường đồng ý với thái độ này. Nhưng đó là thái độ sai. Tôi có thể chứng minh nó sai bằng công cụ logic đơn giản là xem xét các cực đoan.

- Nếu bạn cho tôi một chương trình chạy hoàn hảo nhưng không thể thay đổi, khi yêu cầu thay đổi thì chương trình sẽ không còn hoạt động và tôi cũng không thể sửa nó. Khi ấy, chương trình trở nên vô dụng.
- Nếu bạn cho tôi một chương trình không hoạt động nhưng dễ thay đổi, tôi có thể sửa nó và giữ cho nó hoạt động khi yêu cầu thay đổi. Nhờ vậy, chương trình tiếp tục hữu ích.

Bạn có thể không thấy lập luận này thuyết phục. Dù sao, không có chương trình nào hoàn toàn không thể thay đổi.

Tuy nhiên, có những hệ thống gần như không thể thay đổi vì chi phí thay đổi vượt quá lợi ích của nó. Nhiều hệ thống đạt đến ngưỡng ấy ở một số tính năng hoặc cấu hình.

## Ma trận Eisenhower

Hãy xem ma trận tầm quan trọng so với sự cấp bách của Tổng thống Dwight D. Eisenhower (Hình 2.1). Về ma trận này, Eisenhower từng nói:

> Tôi có hai loại vấn đề: cấp bách và quan trọng. Những việc cấp bách không quan trọng, và những việc quan trọng không bao giờ cấp bách.¹

**Hình 2.1** Ma trận Eisenhower

Câu châm ngôn xưa này đúng ở nhiều điểm. Những việc cấp bách hiếm khi thật sự quan trọng, còn những việc quan trọng hiếm khi cấp bách.

Giá trị đầu tiên của phần mềm (hành vi) cấp bách nhưng không nhất thiết quan trọng.

Giá trị thứ hai của phần mềm (kiến trúc) quan trọng nhưng gần như không bao giờ cấp bách.

Tất nhiên, có những việc vừa cấp bách vừa quan trọng. Cũng có những việc không cấp bách và không quan trọng. Cuối cùng, chúng ta có thể sắp xếp bốn cặp này thành các mức ưu tiên:

1. Cấp bách và quan trọng
2. Không cấp bách và quan trọng
3. Cấp bách và không quan trọng
4. Không cấp bách và không quan trọng

Lưu ý rằng kiến trúc của mã (phần quan trọng) nằm ở hai vị trí đầu trong danh sách này, còn hành vi của mã chiếm vị trí thứ nhất và thứ ba.

Sai lầm mà các nhà quản lý kinh doanh và nhà phát triển thường mắc là nâng các mục ở vị trí 3 lên vị trí 1. Nói cách khác, họ không phân biệt được những tính năng cấp bách nhưng không quan trọng với những tính năng thực sự vừa cấp bách vừa quan trọng. Sự thất bại này dẫn đến việc bỏ qua kiến trúc quan trọng của hệ thống để ưu tiên các tính năng không quan trọng.

Bài toán khó cho các nhà phát triển phần mềm là các nhà quản lý kinh doanh không được trang bị để đánh giá tầm quan trọng của kiến trúc. Đó chính là thứ các nhà phát triển phần mềm được thuê để làm. Do đó, trách nhiệm của đội ngũ phát triển phần mềm là khẳng định tầm quan trọng của kiến trúc lên trên sự cấp bách của các tính năng.

## Chiến đấu cho kiến trúc

Thực hiện trách nhiệm này có nghĩa là bước vào một cuộc chiến, hay nói đúng hơn là một cuộc đấu tranh. Thú thực, mọi việc vẫn diễn ra như vậy. Đội ngũ phát triển phải đấu tranh cho điều họ tin là tốt nhất cho công ty, cũng như đội ngũ quản lý, marketing, bán hàng và vận hành. Luôn có sự đấu tranh.

Các đội ngũ phát triển phần mềm hiệu quả đối mặt trực diện với cuộc đấu tranh đó. Họ không ngần ngại tranh luận với các bên liên quan khác như những người ngang hàng. Hãy nhớ rằng với tư cách nhà phát triển phần mềm, bạn cũng là một bên liên quan. Bạn có lợi ích gắn với phần mềm và cần bảo vệ lợi ích ấy. Đó là một phần trong vai trò và bổn phận của bạn, cũng là lý do quan trọng khiến bạn được tuyển dụng.

Thách thức này quan trọng gấp đôi nếu bạn là một kiến trúc sư phần mềm. Kiến trúc sư phần mềm, nhờ mô tả công việc của họ, tập trung nhiều hơn vào cấu trúc của hệ thống hơn là các tính năng và chức năng. Các kiến trúc sư tạo ra một kiến trúc cho phép các tính năng và chức năng đó dễ dàng phát triển, dễ dàng sửa đổi, và dễ dàng mở rộng.

Chỉ cần nhớ: Nếu kiến trúc đến sau cùng, hệ thống sẽ ngày càng tốn kém để phát triển, và cuối cùng việc thay đổi sẽ trở nên gần như không thể đối với một phần hoặc toàn bộ hệ thống. Nếu để chuyện đó xảy ra, nghĩa là đội ngũ phát triển phần mềm không chiến đấu đủ mạnh cho những gì họ biết là cần thiết.

¹. Trích từ bài phát biểu tại Đại học Northwestern năm 1954.