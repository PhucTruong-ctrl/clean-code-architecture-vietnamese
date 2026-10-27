# Chương 32: Framework chỉ là chi tiết
![Minh họa](assets/illustrations/32-chuong-32-opener.png){w=300}

Framework trở nên rất phổ biến. Nhìn chung, đây là điều tốt. Có nhiều framework miễn phí, mạnh mẽ và hữu ích.

Tuy nhiên, framework không phải kiến trúc, dù một số framework cố gắng làm như vậy.

## Tác giả framework

Hầu hết tác giả cung cấp framework miễn phí vì muốn giúp đỡ cộng đồng và đóng góp lại. Đó là điều đáng quý. Tuy nhiên, dù động cơ của họ có cao đẹp đến đâu, họ không đặt lợi ích tốt nhất của bạn lên hàng đầu. Họ không thể làm vậy vì không biết bạn là ai và không biết vấn đề của bạn.

Tác giả framework hiểu vấn đề của chính họ, đồng nghiệp và bạn bè. Họ viết framework để giải quyết những vấn đề đó, không phải vấn đề của bạn.

Dĩ nhiên, vấn đề của bạn có thể trùng lặp khá nhiều với vấn đề của họ. Nếu không, framework đã chẳng phổ biến đến vậy. Trong phạm vi có sự trùng lặp, framework quả thực có thể rất hữu ích.

## Mối ràng buộc bất cân xứng

Mối quan hệ giữa bạn và tác giả framework bất cân xứng một cách đáng kinh ngạc. Bạn phải cam kết rất nhiều với framework, nhưng tác giả không cam kết với bạn chút nào.

Hãy suy nghĩ kỹ về điều này. Khi dùng framework, bạn đọc tài liệu do tác giả cung cấp. Trong tài liệu đó, tác giả và những người dùng framework khác khuyên bạn cách tích hợp phần mềm với framework. Thông thường, điều đó có nghĩa là bọc kiến trúc của bạn quanh framework. Tác giả khuyên bạn kế thừa các lớp cơ sở của framework và đưa tiện ích của framework vào đối tượng nghiệp vụ. Họ thúc giục bạn gắn ứng dụng với framework chặt nhất có thể.

Với tác giả framework, gắn phần mềm với chính framework của họ không phải rủi ro. Họ muốn gắn với framework đó vì họ hoàn toàn kiểm soát nó.

Hơn nữa, tác giả muốn bạn gắn ứng dụng với framework vì một khi đã gắn như vậy, việc thoát ra sẽ rất khó. Không gì khiến tác giả framework cảm thấy được công nhận hơn một nhóm người dùng sẵn sàng kế thừa không thể tách rời từ các lớp cơ sở của họ.

Thực chất, tác giả đang đề nghị bạn kết hôn với framework, tức cam kết lớn và lâu dài. Thế nhưng, trong bất kỳ trường hợp nào, tác giả cũng không đưa ra cam kết tương ứng với bạn. Đây là cuộc hôn nhân một chiều. Bạn gánh mọi rủi ro và trách nhiệm, còn tác giả framework không gánh gì cả.

## Những rủi ro

Bạn cần cân nhắc một số rủi ro sau:

- Kiến trúc của framework thường không sạch. Framework thường vi phạm Quy tắc Phụ thuộc. Chúng muốn bạn kế thừa mã của chúng vào đối tượng nghiệp vụ, tức Entity của bạn. Chúng muốn framework được gắn vào vòng tròn trong cùng. Một khi đã vào đó, framework sẽ không rời đi. Chiếc nhẫn cưới đã ở trên tay bạn và sẽ còn ở đó.
- Framework có thể giúp bạn triển khai một số tính năng ban đầu. Nhưng khi sản phẩm trưởng thành, nó có thể vượt quá khả năng của framework. Nếu đã đeo chiếc nhẫn ấy, bạn sẽ thấy framework ngày càng cản trở mình.
- Framework có thể phát triển theo hướng không hữu ích với bạn. Bạn có thể buộc phải nâng cấp lên phiên bản mới không giúp ích gì. Thậm chí, các tính năng cũ mà bạn dùng có thể biến mất hoặc thay đổi theo cách khó theo kịp.
- Có thể xuất hiện framework mới và tốt hơn mà bạn muốn chuyển sang dùng.

## Giải pháp

Giải pháp là gì?

> Đừng kết hôn với framework!

Bạn vẫn có thể dùng framework, chỉ đừng gắn chặt với nó. Hãy giữ nó ở khoảng cách an toàn. Xem framework như chi tiết thuộc một trong các vòng tròn ngoài của kiến trúc. Đừng để nó lọt vào các vòng tròn trong.

Nếu framework muốn bạn kế thừa các lớp cơ sở của nó cho đối tượng nghiệp vụ, hãy từ chối. Thay vào đó, hãy tạo proxy và đặt chúng vào các thành phần plugin của quy tắc nghiệp vụ.

Đừng để framework lọt vào mã lõi. Thay vào đó, hãy tích hợp framework vào các thành phần cắm vào mã lõi, tuân theo Quy tắc Phụ thuộc.

Chẳng hạn, có thể bạn thích Spring. Spring là framework tiêm phụ thuộc tốt. Có thể bạn dùng Spring để tự động nối các phụ thuộc. Điều đó ổn, nhưng đừng rải chú thích `@Autowired` khắp các đối tượng nghiệp vụ. Đối tượng nghiệp vụ không nên biết về Spring.

Thay vào đó, bạn có thể dùng Spring để tiêm phụ thuộc vào thành phần `Main`. `Main` được phép biết về Spring vì nó là thành phần bẩn nhất và cấp thấp nhất trong kiến trúc.

## Bây giờ tôi tuyên bố hai bạn thành vợ chồng...

Có một số framework mà bạn buộc phải kết hôn. Chẳng hạn, nếu dùng C++, có lẽ bạn phải kết hôn với STL, rất khó tránh. Nếu dùng Java, gần như chắc chắn bạn phải gắn với thư viện chuẩn.

Điều đó bình thường, nhưng vẫn nên là một quyết định có cân nhắc. Bạn phải hiểu rằng khi kết hôn framework với ứng dụng, bạn sẽ gắn bó với framework đó trong suốt vòng đời ứng dụng. Dù tốt hay xấu, khi khỏe mạnh hay lúc đau ốm, khi giàu sang hay nghèo khó, dù từ bỏ mọi framework khác, bạn vẫn sẽ dùng framework này. Đây không phải là cam kết nên đưa ra nhẹ nhàng.

## Kết luận

Khi gặp một framework, hãy cố đừng kết hôn với nó ngay. Hãy tìm cách “hẹn hò” một thời gian trước khi quyết định gắn bó. Nếu có thể, hãy giữ framework sau một ranh giới kiến trúc càng lâu càng tốt.

Có lẽ bạn tìm được cách lấy sữa mà không cần mua cả con bò.