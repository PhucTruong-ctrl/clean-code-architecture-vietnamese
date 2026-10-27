# Chương 31: Web chỉ là chi tiết
![Minh họa](assets/illustrations/31-chuong-31-opener.png){w=300}

Bạn có phải là lập trình viên trong thập niên 1990 không? Bạn có nhớ web đã làm thay đổi mọi thứ ra sao không? Bạn có nhớ chúng ta đã nhìn các kiến trúc máy khách-máy chủ cũ bằng ánh mắt khinh miệt như thế nào trước công nghệ mới sáng bóng mang tên Web không?

Thực ra, web chẳng thay đổi điều gì cả. Hoặc ít nhất, nó không nên thay đổi. Web chỉ là dao động mới nhất trong chuỗi dao động của ngành từ thập niên 1960. Những dao động này luân phiên giữa việc tập trung toàn bộ sức mạnh tính toán vào máy chủ trung tâm và phân tán toàn bộ sức mạnh tính toán ra các thiết bị đầu cuối.

Chỉ trong khoảng một thập kỷ kể từ khi web trở nên phổ biến, chúng ta đã chứng kiến vài lần dao động như vậy. Ban đầu, ta nghĩ toàn bộ sức mạnh tính toán sẽ nằm trong các cụm máy chủ, còn trình duyệt chỉ làm nhiệm vụ đơn giản. Sau đó, ta bắt đầu đưa applet vào trình duyệt. Nhưng rồi ta không thích cách đó, nên chuyển nội dung động trở lại máy chủ. Sau đó lại không thích như vậy, nên phát minh ra Web 2.0 và đưa nhiều xử lý trở lại trình duyệt bằng Ajax và JavaScript. Ta đi xa đến mức tạo ra những ứng dụng khổng lồ chạy hoàn toàn trong trình duyệt. Giờ đây, mọi người lại hào hứng chuyển JavaScript về máy chủ bằng Node.

(Thở dài.)

## Con lắc vô tận

Dĩ nhiên, sẽ sai nếu nghĩ những dao động ấy bắt đầu cùng với web. Trước web là kiến trúc máy khách-máy chủ. Trước đó là các máy tính mini trung tâm với nhiều thiết bị đầu cuối đơn giản. Trước nữa là máy tính lớn với các thiết bị đầu cuối màn hình xanh thông minh, khá giống trình duyệt ngày nay. Trước đó nữa là phòng máy tính và những chồng thẻ đục lỗ…

Câu chuyện cứ thế tiếp diễn. Chúng ta dường như không thể quyết định sức mạnh tính toán nên đặt ở đâu. Ta liên tục chuyển qua lại giữa tập trung và phân tán. Tôi nghĩ những dao động ấy sẽ còn tiếp tục trong một thời gian dài.

Xét trong toàn bộ lịch sử công nghệ thông tin, web chẳng thay đổi điều gì cả. Web chỉ là một trong nhiều dao động của cuộc giằng co bắt đầu trước khi hầu hết chúng ta ra đời và sẽ tiếp tục rất lâu sau khi phần lớn chúng ta nghỉ hưu.

Tuy nhiên, với tư cách kiến trúc sư, chúng ta phải nhìn dài hạn. Những dao động đó chỉ là vấn đề ngắn hạn mà ta muốn đẩy ra xa khỏi lõi quy tắc nghiệp vụ.

Hãy nghe câu chuyện về công ty Q. Công ty Q xây dựng một hệ thống tài chính cá nhân rất phổ biến. Đó là ứng dụng máy tính để bàn có giao diện đồ họa hữu ích. Tôi rất thích dùng nó.

Rồi web xuất hiện. Trong phiên bản tiếp theo, công ty Q thay đổi giao diện để trông và hoạt động giống trình duyệt. Tôi sửng sốt! Thiên tài tiếp thị nào lại nghĩ rằng phần mềm tài chính cá nhân chạy trên máy tính để bàn nên mang hình thức và cách hoạt động của trình duyệt web?

Dĩ nhiên tôi ghét giao diện mới. Có vẻ mọi người khác cũng vậy, vì sau vài phiên bản, công ty Q dần loại bỏ dáng vẻ giống trình duyệt và đưa hệ thống tài chính cá nhân trở lại giao diện máy tính để bàn thông thường.

Giờ hãy tưởng tượng bạn là kiến trúc sư phần mềm của Q. Một thiên tài tiếp thị thuyết phục ban lãnh đạo rằng toàn bộ giao diện người dùng phải thay đổi để giống web hơn. Bạn sẽ làm gì? Hay đúng hơn, trước đó bạn nên làm gì để bảo vệ ứng dụng khỏi thiên tài tiếp thị ấy?

Bạn nên tách quy tắc nghiệp vụ khỏi giao diện người dùng. Tôi không biết các kiến trúc sư của Q đã làm vậy chưa. Một ngày nào đó tôi rất muốn nghe câu chuyện của họ. Nếu ở đó vào thời điểm ấy, chắc chắn tôi đã cố gắng hết sức để cô lập quy tắc nghiệp vụ khỏi giao diện đồ họa, vì chẳng ai biết các thiên tài tiếp thị sẽ làm gì tiếp theo.

Giờ hãy xét công ty A, nhà sản xuất một chiếc điện thoại thông minh tuyệt đẹp. Gần đây, họ phát hành phiên bản nâng cấp “hệ điều hành” của điện thoại. Thật kỳ lạ khi ta nói về hệ điều hành bên trong điện thoại. Trong số những thay đổi khác, bản nâng cấp “hệ điều hành” đó thay đổi hoàn toàn hình thức và cách hoạt động của mọi ứng dụng. Vì sao? Tôi đoán là do một thiên tài tiếp thị nào đó.

Tôi không phải chuyên gia về phần mềm trong thiết bị đó, nên không biết thay đổi này có gây khó khăn đáng kể cho lập trình viên ứng dụng trên điện thoại của công ty A hay không. Tôi hy vọng kiến trúc sư của A và kiến trúc sư các ứng dụng đã giữ giao diện người dùng tách biệt khỏi quy tắc nghiệp vụ, vì luôn có những thiên tài tiếp thị rình chờ lợi dụng mối phụ thuộc nhỏ tiếp theo mà bạn tạo ra.

## Kết luận

Kết luận rất đơn giản: giao diện đồ họa chỉ là chi tiết. Web là một giao diện đồ họa, nên web cũng chỉ là chi tiết. Với tư cách kiến trúc sư, bạn nên đặt những chi tiết như vậy phía sau các ranh giới để tách chúng khỏi logic nghiệp vụ cốt lõi.

Hãy nghĩ theo cách này: WEB là một thiết bị IO. Từ thập niên 1960, chúng ta đã hiểu giá trị của việc viết ứng dụng độc lập với thiết bị. Động lực để giữ tính độc lập đó chưa hề thay đổi. Web không phải ngoại lệ.

Hay có phải không? Có thể lập luận rằng giao diện đồ họa, cũng như web, độc đáo và phong phú đến mức theo đuổi kiến trúc độc lập thiết bị là vô lý. Khi nghĩ đến sự phức tạp của việc xác thực bằng JavaScript, các lời gọi Ajax kéo-thả hay vô số tiện ích có thể đặt lên trang web, người ta dễ cho rằng độc lập thiết bị là không thực tế.

Ở một mức độ nào đó, điều này đúng. Tương tác giữa ứng dụng và giao diện đồ họa diễn ra dồn dập theo những cách rất riêng của từng loại giao diện. Cách trình duyệt và ứng dụng web phối hợp khác với cách giao diện đồ họa máy tính để bàn và ứng dụng phối hợp. Có vẻ khó mà trừu tượng hóa sự phối hợp ấy theo cách UNIX trừu tượng hóa thiết bị.

Tuy nhiên, có thể trừu tượng hóa một ranh giới khác giữa giao diện người dùng và ứng dụng. Ta có thể xem logic nghiệp vụ là một tập hợp ca sử dụng, mỗi ca sử dụng thực hiện một chức năng thay mặt người dùng. Có thể mô tả từng ca sử dụng bằng dữ liệu đầu vào, quá trình xử lý và dữ liệu đầu ra.

Tại một thời điểm nào đó trong quá trình tương tác giữa giao diện người dùng và ứng dụng, dữ liệu đầu vào sẽ hoàn tất và ca sử dụng có thể được thực thi. Khi hoàn tất, dữ liệu kết quả có thể được đưa trở lại quá trình tương tác giữa giao diện và ứng dụng.

Có thể đặt toàn bộ dữ liệu đầu vào và dữ liệu đầu ra kết quả vào các cấu trúc dữ liệu, rồi dùng chúng làm giá trị đầu vào và đầu ra cho tiến trình thực thi ca sử dụng. Với cách tiếp cận này, có thể xem mỗi ca sử dụng đang điều khiển thiết bị IO của giao diện người dùng theo cách độc lập với thiết bị.