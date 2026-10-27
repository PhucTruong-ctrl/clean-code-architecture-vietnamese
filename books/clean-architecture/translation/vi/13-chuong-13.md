# Chương 13: Tính gắn kết của thành phần
![Minh họa](assets/illustrations/13-chuong-13-opener.png){w=300}

Trong chương này, chúng ta sẽ thảo luận về ba nguyên tắc của tính gắn kết của thành phần (component cohesion):

- REP: Nguyên tắc tương đương giữa tái sử dụng và phát hành (Reuse/Release Equivalence Principle)
- CCP: Nguyên tắc Đóng chung (Common Closure Principle)
- CRP: Nguyên tắc Tái sử dụng chung (Common Reuse Principle)

## Nguyên tắc tương đương giữa tái sử dụng và phát hành

Đơn vị của việc tái sử dụng là đơn vị của việc phát hành.

Thập kỷ qua đã chứng kiến sự trỗi dậy của đủ loại công cụ quản lý mô-đun, như Maven, Leiningen và RVM. Các công cụ này tăng lên tầm quan trọng bởi vì, trong khoảng thời gian đó, một số lượng lớn các thành phần có thể tái sử dụng và thư viện thành phần đã được tạo ra. Chúng ta đang sống trong kỷ nguyên của việc tái sử dụng phần mềm, sự hiện thực hóa của một trong những lời hứa lâu đời nhất của mô hình hướng đối tượng.

Nguyên tắc tương đương giữa tái sử dụng và phát hành (REP) là một nguyên tắc có vẻ hiển nhiên, ít nhất là khi nhìn lại từ hiện tại. Những người muốn tái sử dụng các thành phần phần mềm không thể, và sẽ không, làm điều đó trừ khi các thành phần đó được theo dõi qua một quy trình phát hành và được gán số phát hành.

Điều này không đơn giản là vì, nếu không có số phát hành, sẽ không có cách nào để đảm bảo rằng tất cả các thành phần được tái sử dụng đều tương thích với nhau. Thực tế, điều này còn phản ánh việc các nhà phát triển phần mềm cần biết khi nào các bản phát hành mới sẽ ra mắt, và những bản phát hành đó sẽ mang lại những thay đổi gì.

Không hiếm khi các nhà phát triển được thông báo về một bản phát hành mới và quyết định, dựa trên các thay đổi được thực hiện trong bản phát hành đó, tiếp tục sử dụng bản phát hành cũ. Do đó, quy trình phát hành phải tạo ra các thông báo và tài liệu phát hành thích hợp để người dùng có thể đưa ra quyết định có thông tin về việc khi nào và có nên tích hợp bản phát hành mới hay không.

Từ quan điểm thiết kế và kiến trúc phần mềm, nguyên tắc này có nghĩa là các lớp và mô-đun được gom lại thành một thành phần phải thuộc về một nhóm gắn kết. Thành phần không thể đơn thuần bao gồm một hỗn độn ngẫu nhiên các lớp và mô-đun; ngược lại, phải có một chủ đề hoặc mục đích cốt lõi nào đó mà tất cả các mô-đun đó đều chia sẻ.

Tuy nhiên, có một cách nhìn khác về vấn đề này có lẽ không hẳn hiển nhiên. Các lớp và mô-đun được gom nhóm lại vào một thành phần nên có thể được phát hành cùng một lúc. Việc chúng chia sẻ cùng một số phiên bản, cùng một hệ thống theo dõi phát hành, và được bao gồm trong cùng một tài liệu phát hành, nên có ý nghĩa cả với tác giả lẫn với người dùng. Đây là một lời khuyên yếu: Việc nói rằng cái gì đó nên "có ý nghĩa" chỉ là cách vung tay lên không trung và cố gắng nghe có vẻ có thẩm quyền. Lời khuyên yếu vì rất khó giải thích chính xác chất keo dính giữ các lớp và mô-đun lại với nhau thành một thành phần duy nhất. Dù lời khuyên có yếu, bản thân nguyên tắc lại quan trọng, bởi vì các vi phạm rất dễ phát hiện: chúng "không có ý nghĩa". Nếu bạn vi phạm REP, người dùng của bạn sẽ biết, và họ sẽ không ấn tượng với kỹ năng kiến trúc của bạn.

Sự yếu kém của nguyên tắc này được bù đắp nhiều hơn bởi sức mạnh của hai nguyên tắc tiếp theo. Thực tế, CCP và CRP định hình mạnh mẽ nguyên tắc này, nhưng theo nghĩa tiêu cực.

## Nguyên tắc Đóng chung

Hãy gom vào thành phần những lớp thay đổi vì cùng lý do và vào cùng lúc.
Hãy tách vào các thành phần khác nhau những lớp thay đổi vào lúc khác nhau và vì những lý do khác nhau.

Đây là Nguyên tắc Trách nhiệm đơn nhất (SRP) được diễn đạt lại cho thành phần. Cũng như SRP nói rằng một lớp không nên chứa nhiều lý do để thay đổi, Nguyên tắc Đóng chung (CCP) nói rằng một thành phần không nên có nhiều lý do để thay đổi.

Đối với hầu hết các ứng dụng, khả năng bảo trì quan trọng hơn khả năng tái sử dụng. Nếu mã trong một ứng dụng phải thay đổi, bạn sẽ muốn tất cả các thay đổi đó xảy ra trong một thành phần, thay vì bị phân tán trên nhiều thành phần. Nếu các thay đổi được gói gọn trong một thành phần, thì chúng ta chỉ cần triển khai lại (redeploy) thành phần thay đổi đó. Các thành phần khác không phụ thuộc vào thành phần đã thay đổi không cần được xác thực lại (revalidated) hay triển khai lại.

Nguyên tắc Đóng chung (CCP) thúc đẩy chúng ta gom lại vào một nơi tất cả các lớp có khả năng thay đổi vì cùng lý do. Nếu hai lớp bị ràng buộc chặt chẽ với nhau, về mặt vật lý hay khái niệm, đến mức chúng luôn thay đổi cùng nhau, thì chúng thuộc về cùng một thành phần. Điều này tối thiểu hóa khối lượng công việc liên quan đến việc phát hành, xác thực lại và triển khai lại phần mềm.

Nguyên tắc này liên hệ mật thiết với Nguyên tắc Đóng/Mở (OCP). Thực tế, chính "sự đóng" (closure) theo nghĩa của OCP là điều mà Nguyên tắc Đóng chung giải quyết. OCP nói rằng các lớp nên đóng đối với sửa đổi nhưng mở đối với mở rộng. Vì sự đóng 100% không thể đạt được, sự đóng phải mang tính chiến lược. Chúng ta thiết kế các lớp sao cho chúng đóng đối với những loại thay đổi phổ biến nhất mà chúng ta mong đợi hoặc đã từng trải qua.

Nguyên tắc Đóng chung mở rộng bài học này bằng cách gom lại vào cùng một thành phần những lớp được đóng đối với cùng loại thay đổi. Như vậy, khi một thay đổi yêu cầu xuất hiện, thay đổi đó có cơ hội tốt được giới hạn trong một số lượng thành phần tối thiểu.

### Sự tương tự với SRP

Như đã nói trước, CCP là dạng thành phần của SRP. SRP bảo chúng ta tách các phương thức vào các lớp khác nhau, nếu chúng thay đổi vì lý do khác nhau. CCP bảo chúng ta tách các lớp vào các thành phần khác nhau, nếu chúng thay đổi vì lý do khác nhau. Cả hai nguyên tắc đều có thể tóm gọn trong câu slogan sau:

> Hãy gom lại những thứ thay đổi vào cùng lúc và vì cùng lý do. Hãy tách những thứ thay đổi vào lúc khác nhau hoặc vì những lý do khác nhau.

## Nguyên tắc Tái sử dụng chung

Đừng ép người dùng của một thành phần phải phụ thuộc vào những thứ họ không cần.

Nguyên tắc Tái sử dụng chung (CRP) là thêm một nguyên tắc giúp chúng ta quyết định những lớp và mô-đun nào nên được đặt vào một thành phần. Nó nói rằng các lớp và mô-đun có xu hướng được tái sử dụng cùng nhau nên thuộc về cùng một thành phần.

Các lớp hiếm khi được tái sử dụng đơn lẻ. Thường thấy hơn, các lớp có thể tái sử dụng cộng tác với các lớp khác thuộc về cùng một trừu tượng có thể tái sử dụng. CRP nói rằng các lớp này nên cùng nằm trong một thành phần. Trong một thành phần như vậy, chúng ta sẽ thấy các lớp có rất nhiều sự phụ thuộc lẫn nhau.

Một ví dụ đơn giản có thể là một lớp chứa (container) và các trình lặp (iterator) liên kết của nó. Các lớp này được tái sử dụng cùng nhau vì chúng bị ràng buộc chặt chẽ với nhau. Do đó, chúng nên nằm trong cùng một thành phần.

Nhưng CRP cho chúng ta biết không chỉ về việc lớp nào nên đặt cùng nhau vào một thành phần: Nó còn cho biết lớp nào **không** nên được giữ chung trong một thành phần. Khi một thành phần sử dụng một thành phần khác, một sự phụ thuộc giữa các thành phần được tạo ra. Có lẽ thành phần sử dụng chỉ dùng một lớp trong thành phần được sử dụng, nhưng điều đó vẫn không làm yếu đi sự phụ thuộc. Thành phần sử dụng vẫn phụ thuộc vào thành phần được sử dụng.

Bởi vì sự phụ thuộc đó, mỗi khi thành phần được sử dụng thay đổi, thành phần sử dụng có thể sẽ cần các thay đổi tương ứng. Ngay cả khi không cần thay đổi thành phần sử dụng, nó vẫn có khả năng cao phải được biên dịch lại, xác thực lại và triển khai lại. Điều này đúng ngay cả khi thành phần sử dụng không quan tâm đến thay đổi được thực hiện trong thành phần được sử dụng.

Do đó, khi chúng ta phụ thuộc vào một thành phần, chúng ta muốn đảm bảo rằng chúng ta phụ thuộc vào **mọi** lớp trong thành phần đó. Nói cách khác, chúng ta muốn đảm bảo rằng các lớp chúng ta đưa vào một thành phần là không tách rời được, mà không thể phụ thuộc vào một số mà không phụ thuộc vào những số khác. Nếu không, chúng ta sẽ phải triển khai lại nhiều thành phần hơn cần thiết, và lãng phí công sức đáng kể.

Vì vậy, CRP cho chúng ta biết nhiều hơn về những lớp **không** nên cùng nhau hơn là về những lớp **nên** cùng nhau. CRP nói rằng các lớp không bị ràng buộc chặt chẽ với nhau không nên nằm trong cùng một thành phần.

### Mối quan hệ với ISP

CRP là phiên bản tổng quát của ISP. ISP khuyên chúng ta không nên phụ thuộc vào các lớp có phương thức mà chúng ta không dùng. CRP khuyên chúng ta không nên phụ thuộc vào các thành phần có lớp mà chúng ta không dùng.

Tất cả lời khuyên này có thể rút gọn thành một câu slogan duy nhất:

> Đừng phụ thuộc vào những thứ bạn không cần.

## Biểu đồ căng thẳng về tính gắn kết của thành phần

Có thể bạn đã nhận ra rằng ba nguyên tắc gắn kết này có xu hướng chống lại nhau. REP và CCP là các nguyên tắc bao gồm (inclusive): Cả hai đều có xu hướng làm cho thành phần trở nên lớn hơn. CRP là một nguyên tắc loại trừ (exclusive), thúc đẩy thành phần nhỏ hơn. Chính sự căng thẳng giữa các nguyên tắc này là những gì các kiến trúc sư giỏi tìm cách giải quyết.

Hình 13.1 là một biểu đồ căng thẳng (tension diagram)[^2] cho thấy ba nguyên tắc gắn kết tương tác với nhau như thế nào. Các cạnh của biểu đồ mô tả chi phí của việc từ bỏ nguyên tắc ở đỉnh đối diện.

**Hình 13.1** Biểu đồ căng thẳng các nguyên tắc gắn kết

Một kiến trúc sư chỉ tập trung vào REP và CRP sẽ thấy quá nhiều thành phần bị ảnh hưởng khi thực hiện các thay đổi đơn giản. Ngược lại, một kiến trúc sư tập trung quá mạnh vào CCP và REP sẽ khiến quá nhiều bản phát hành không cần thiết được tạo ra.

Một kiến trúc sư giỏi tìm được một vị trí trong tam giác căng thẳng đó đáp ứng được mối quan tâm hiện tại của nhóm phát triển, nhưng cũng nhận thức rằng những mối quan tâm đó sẽ thay đổi theo thời gian. Ví dụ, sớm trong quá trình phát triển một dự án, CCP quan trọng hơn REP nhiều, bởi vì khả năng phát triển (develop-ability) quan trọng hơn tái sử dụng.

Nói chung, các dự án thường bắt đầu ở bên phải của tam giác, nơi hy sinh duy nhất là tái sử dụng. Khi dự án trưởng thành, và các dự án khác bắt đầu lấy từ nó, dự án sẽ trượt sang bên trái. Điều này có nghĩa là cấu trúc thành phần của một dự án có thể thay đổi theo thời gian và mức độ trưởng thành. Nó liên quan nhiều hơn đến cách dự án được phát triển và sử dụng, hơn là đến việc dự án thực sự làm gì.

## Kết luận

Trong quá khứ, quan điểm của chúng ta về sự gắn kết (cohesion) đơn giản hơn nhiều so với những gì REP, CCP và CRP hàm ý. Chúng ta từng nghĩ rằng sự gắn kết đơn giản là thuộc tính cho thấy một mô-đun thực hiện một, và chỉ một, chức năng. Tuy nhiên, ba nguyên tắc về sự gắn kết của thành phần miêu tả một dạng gắn kết phức tạp hơn nhiều. Khi chọn các lớp để gom nhóm lại thành thành phần, chúng ta phải cân nhắc các lực đối lập liên quan đến khả năng tái sử dụng và khả năng phát triển. Việc cân bằng các lực này với nhu cầu của ứng dụng là không tầm thường. Hơn nữa, sự cân bằng đó gần như luôn động. Tức là, sự phân chia phù hợp hôm nay có thể không còn phù hợp vào năm sau. Hệ quả là, cách tổ chức các thành phần trong hệ thống có thể dao động (jitter)[^1] và tiến hóa theo thời gian khi trọng tâm của dự án thay đổi từ khả năng phát triển sang khả năng tái sử dụng.

[^1]: Xem mục "The Kitty Problem" trong Chương 27, "Services: Great and Small".
[^2]: Cảm ơn Tim Ottinger vì ý tưởng này.