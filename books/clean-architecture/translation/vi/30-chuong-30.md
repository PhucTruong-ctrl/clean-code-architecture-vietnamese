# Chương 30: Cơ sở dữ liệu chỉ là chi tiết
![Minh họa](assets/illustrations/30-chuong-30-opener.png){w=300}

Từ góc nhìn kiến trúc, cơ sở dữ liệu không phải một thực thể kiến trúc. Nó chỉ là chi tiết, không đạt đến mức một yếu tố kiến trúc. Quan hệ của nó với kiến trúc hệ thống phần mềm cũng giống như quan hệ giữa núm cửa và kiến trúc ngôi nhà.

Tôi biết đây là lời dễ gây tranh cãi. Tin tôi đi, tôi từng tranh luận về chuyện này. Để nói rõ: tôi không nói đến mô hình dữ liệu. Cấu trúc dữ liệu trong ứng dụng có ý nghĩa lớn đối với kiến trúc hệ thống. Nhưng cơ sở dữ liệu không phải mô hình dữ liệu. Cơ sở dữ liệu là phần mềm, một tiện ích giúp truy cập dữ liệu. Từ góc nhìn kiến trúc, tiện ích đó không liên quan vì nó là chi tiết cơ chế cấp thấp. Kiến trúc sư giỏi không để các cơ chế cấp thấp làm ô nhiễm kiến trúc hệ thống.

## Cơ sở dữ liệu quan hệ

Edgar Codd xác định các nguyên tắc của cơ sở dữ liệu quan hệ vào năm 1970. Đến giữa những năm 1980, mô hình quan hệ đã trở thành hình thức lưu trữ dữ liệu thống trị. Sự phổ biến ấy có lý do chính đáng: mô hình quan hệ thanh lịch, có kỷ luật và vững chắc. Đây là công nghệ lưu trữ và truy cập dữ liệu rất tốt.

Nhưng dù công nghệ có xuất sắc, hữu ích và vững chắc về mặt toán học đến đâu, nó vẫn chỉ là công nghệ. Vì vậy, nó vẫn là chi tiết.

Bảng quan hệ có thể thuận tiện cho một số cách truy cập dữ liệu, nhưng việc sắp xếp dữ liệu thành các hàng trong bảng không có ý nghĩa kiến trúc. Ca sử dụng của ứng dụng không nên biết hay quan tâm đến những vấn đề đó. Thực tế, hiểu biết về cấu trúc bảng của dữ liệu phải được giới hạn trong các hàm tiện ích cấp thấp nhất ở những vòng tròn ngoài của kiến trúc.

Nhiều framework truy cập dữ liệu cho phép truyền các hàng và bảng cơ sở dữ liệu khắp hệ thống dưới dạng đối tượng. Đây là lỗi kiến trúc. Cách làm đó ràng buộc ca sử dụng, quy tắc nghiệp vụ và đôi khi cả giao diện người dùng vào cấu trúc quan hệ của dữ liệu.

## Vì sao hệ thống cơ sở dữ liệu phổ biến đến vậy?

Vì sao hệ thống phần mềm và doanh nghiệp phần mềm lại bị các hệ thống cơ sở dữ liệu chi phối? Vì sao Oracle, MySQL và SQL Server có vị thế vượt trội? Chỉ một từ thôi: đĩa.

Đĩa từ quay là nền tảng lưu trữ dữ liệu chính suốt năm thập kỷ. Nhiều thế hệ lập trình viên không biết đến hình thức lưu trữ nào khác. Công nghệ đĩa đã phát triển từ những chồng đĩa khổng lồ có phiến đĩa đường kính 48 inch, nặng hàng nghìn pound và chứa được 20 megabyte, đến những đĩa tròn mỏng đường kính 3 inch, chỉ nặng vài gram nhưng chứa được một terabyte hoặc hơn. Đó là một chặng đường dài. Trong suốt thời gian ấy, lập trình viên luôn phải đối mặt với đặc tính tai hại của công nghệ đĩa: đĩa rất chậm.

Dữ liệu trên đĩa được lưu trong các rãnh tròn. Các rãnh được chia thành sector, mỗi sector chứa một lượng byte tiện dụng, thường là 4 KB. Mỗi phiến đĩa có thể có hàng trăm rãnh, và cả ổ có thể gồm hơn chục phiến. Muốn đọc một byte cụ thể, ta phải di chuyển đầu đọc đến đúng rãnh, chờ đĩa quay đến đúng sector, đọc toàn bộ 4 KB của sector đó vào RAM rồi truy cập vị trí cần tìm trong vùng đệm RAM. Tất cả việc đó mất thời gian, tính bằng mili giây.

Mili giây nghe có vẻ ngắn, nhưng dài hơn chu kỳ của hầu hết bộ xử lý đến một triệu lần. Nếu dữ liệu không nằm trên đĩa, ta có thể truy cập nó trong nano giây thay vì mili giây.

Để giảm độ trễ do đĩa gây ra, cần có chỉ mục, bộ nhớ đệm và các cách truy vấn được tối ưu hóa. Cũng cần một cách biểu diễn dữ liệu thống nhất để các chỉ mục, bộ nhớ đệm và truy vấn biết mình đang xử lý dữ liệu nào. Nói ngắn gọn, cần một hệ thống truy cập và quản lý dữ liệu. Theo thời gian, các hệ thống này chia thành hai loại riêng biệt: hệ thống tệp và hệ quản trị cơ sở dữ liệu quan hệ (RDBMS).

Hệ thống tệp dựa trên tài liệu. Chúng cung cấp cách tự nhiên và tiện lợi để lưu trữ toàn bộ tài liệu. Chúng phù hợp khi cần lưu và truy xuất một tập tài liệu theo tên, nhưng không giúp nhiều khi cần tìm trong nội dung tài liệu. Dễ tìm tệp `login.c`, nhưng khó và chậm tìm mọi tệp `.c` có biến tên `x`.

Hệ thống cơ sở dữ liệu dựa trên nội dung. Chúng giúp tìm bản ghi theo nội dung một cách tự nhiên và thuận tiện. Chúng rất giỏi liên kết nhiều bản ghi dựa trên một phần nội dung chung. Tiếc là chúng khá kém trong việc lưu và truy xuất những tài liệu không có cấu trúc nội bộ mà cơ sở dữ liệu hiểu được.

Cả hai loại hệ thống đều tổ chức dữ liệu trên đĩa để lưu và truy xuất hiệu quả nhất theo nhu cầu truy cập riêng. Mỗi loại có cách lập chỉ mục và sắp xếp dữ liệu riêng. Ngoài ra, cuối cùng chúng đều đưa dữ liệu cần thiết vào RAM, nơi có thể thao tác nhanh.

## Nếu không có đĩa thì sao?

Đĩa từng phổ biến đến đâu thì nay đang dần biến mất. Chẳng bao lâu nữa, chúng sẽ đi theo ổ băng từ, đĩa mềm và CD, nhường chỗ cho RAM.

Hãy tự hỏi: khi không còn đĩa và mọi dữ liệu đều được lưu trong RAM, bạn sẽ tổ chức dữ liệu thế nào? Bạn sẽ xếp nó thành bảng rồi truy cập bằng SQL? Bạn sẽ sắp xếp nó thành tệp rồi truy cập qua thư mục?

Dĩ nhiên là không. Bạn sẽ tổ chức dữ liệu thành danh sách liên kết, cây, bảng băm, ngăn xếp, hàng đợi hoặc vô số cấu trúc dữ liệu khác, rồi truy cập bằng con trỏ hoặc tham chiếu, vì đó là cách lập trình viên làm việc.

Thực tế, nếu suy nghĩ kỹ, bạn sẽ nhận ra mình vẫn luôn làm như vậy. Dù dữ liệu nằm trong cơ sở dữ liệu hay hệ thống tệp, bạn vẫn đọc nó vào RAM rồi sắp xếp lại cho thuận tiện thành danh sách, tập hợp, ngăn xếp, hàng đợi, cây hoặc cấu trúc dữ liệu nào bạn thích. Rất hiếm khi ta để dữ liệu nguyên dạng bảng hoặc tệp.

## Chi tiết

Đây là lý do tôi nói cơ sở dữ liệu chỉ là chi tiết. Nó chỉ là cơ chế dùng để chuyển dữ liệu qua lại giữa bề mặt đĩa và RAM. Xét cho cùng, cơ sở dữ liệu không hơn gì một thùng chứa lớn chứa các bit để lưu dữ liệu lâu dài. Nhưng ta hiếm khi sử dụng dữ liệu ở dạng đó.

Vì vậy, từ góc nhìn kiến trúc, ta không nên quan tâm dữ liệu có dạng gì khi nằm trên bề mặt đĩa từ quay. Thực tế, ta không nên thừa nhận rằng đĩa tồn tại.

## Còn hiệu năng thì sao?

Hiệu năng chẳng phải là mối quan tâm kiến trúc sao? Tất nhiên là có. Nhưng với lưu trữ dữ liệu, đây là mối quan tâm có thể được đóng gói và tách biệt hoàn toàn khỏi quy tắc nghiệp vụ. Đúng là cần đọc và ghi dữ liệu nhanh, nhưng đó là mối quan tâm cấp thấp. Ta có thể xử lý nó bằng các cơ chế truy cập dữ liệu cấp thấp. Nó hoàn toàn không liên quan đến kiến trúc tổng thể của hệ thống.

## Câu chuyện

Cuối những năm 1980, tôi dẫn dắt một nhóm kỹ sư phần mềm ở công ty khởi nghiệp đang xây dựng và tiếp thị hệ thống quản lý mạng để đo độ toàn vẹn truyền thông của các đường dây viễn thông T1. Hệ thống truy xuất dữ liệu từ các thiết bị ở hai đầu đường dây, rồi chạy một loạt thuật toán dự đoán để phát hiện và báo cáo vấn đề.

Chúng tôi dùng nền tảng UNIX và lưu dữ liệu trong các tệp truy cập ngẫu nhiên đơn giản. Không cần cơ sở dữ liệu quan hệ vì dữ liệu có rất ít mối liên hệ dựa trên nội dung. Lưu dữ liệu trong cây và danh sách liên kết trong các tệp truy cập ngẫu nhiên phù hợp hơn. Nói ngắn gọn, chúng tôi giữ dữ liệu ở dạng tiện nhất để nạp vào RAM và thao tác.

Chúng tôi thuê một quản lý tiếp thị cho công ty khởi nghiệp, một người dễ mến và hiểu biết. Nhưng ngay lập tức, anh ta nói chúng tôi phải có cơ sở dữ liệu quan hệ trong hệ thống. Đây không phải lựa chọn hay vấn đề kỹ thuật, mà là yêu cầu tiếp thị.

Tôi không hiểu. Vì sao phải sắp xếp lại danh sách liên kết và cây thành hàng loạt hàng và bảng được truy cập qua SQL? Vì sao phải gánh toàn bộ chi phí và độ phức tạp của một RDBMS khổng lồ khi hệ thống tệp truy cập ngẫu nhiên đơn giản đã quá đủ? Tôi kiên quyết phản đối.

Một kỹ sư phần cứng trong công ty cũng hùa theo quan điểm cần RDBMS. Anh ta tin rằng hệ thống phần mềm cần RDBMS vì lý do kỹ thuật. Anh ta tổ chức các cuộc họp sau lưng tôi với ban lãnh đạo công ty, vẽ lên bảng những hình người que đứng trên mái nhà đặt trên một cây cột, rồi hỏi: “Bạn có xây nhà trên một cây cột không?” Hàm ý của anh ta là RDBMS lưu các bảng trong những tệp truy cập ngẫu nhiên bằng cách nào đó đáng tin cậy hơn các tệp truy cập ngẫu nhiên chúng tôi đang dùng.

Tôi đã tranh luận với anh ta. Tôi tranh luận với người làm tiếp thị. Tôi giữ vững nguyên tắc kỹ thuật trước sự thiếu hiểu biết đáng kinh ngạc. Tôi cứ tranh luận mãi.

Cuối cùng, kỹ sư phần cứng được thăng chức, vượt qua tôi để trở thành quản lý phần mềm. Cuối cùng, họ đưa RDBMS vào hệ thống tội nghiệp đó. Và cuối cùng, họ hoàn toàn đúng còn tôi sai.

Không phải vì lý do kỹ thuật, tôi nói rõ điều đó. Về mặt kỹ thuật, tôi đúng. Tôi đã đúng khi phản đối đưa RDBMS vào lõi kiến trúc hệ thống. Tôi sai vì khách hàng kỳ vọng sản phẩm phải có cơ sở dữ liệu quan hệ. Họ không biết sẽ dùng nó làm gì. Họ cũng không có cách thực tế nào để dùng dữ liệu quan hệ trong hệ thống của chúng tôi. Nhưng điều đó không quan trọng: khách hàng hoàn toàn mong đợi một RDBMS. Nó đã trở thành một ô đánh dấu trong danh sách yêu cầu của người mua phần mềm. Không có lý do kỹ thuật nào cả, tính hợp lý không liên quan. Nhu cầu ấy phi lý, đến từ bên ngoài và hoàn toàn không có cơ sở, nhưng vẫn là nhu cầu có thật.

Nhu cầu đó đến từ đâu? Nó bắt nguồn từ các chiến dịch tiếp thị rất hiệu quả của những nhà cung cấp cơ sở dữ liệu thời ấy. Họ đã thuyết phục được các lãnh đạo cấp cao rằng “tài sản dữ liệu” của doanh nghiệp cần được bảo vệ, và hệ thống cơ sở dữ liệu của họ là phương tiện lý tưởng để làm việc đó.

Ngày nay, ta vẫn thấy những chiến dịch tiếp thị tương tự. Từ “doanh nghiệp” và khái niệm “Kiến trúc hướng dịch vụ” liên quan đến tiếp thị nhiều hơn thực tế.

Tôi nên làm gì trong tình huống ngày xưa đó? Tôi nên gắn RDBMS ở bên cạnh hệ thống và cung cấp một kênh truy cập dữ liệu hẹp, an toàn, đồng thời giữ các tệp truy cập ngẫu nhiên trong lõi hệ thống. Tôi đã làm gì? Tôi nghỉ việc và trở thành chuyên gia tư vấn.

## Kết luận

Cách tổ chức dữ liệu, tức mô hình dữ liệu, có ý nghĩa kiến trúc. Các công nghệ và hệ thống chuyển dữ liệu ra vào bề mặt từ quay thì không. Hệ quản trị cơ sở dữ liệu quan hệ buộc dữ liệu phải được tổ chức thành bảng và truy cập bằng SQL liên quan đến nhóm thứ hai nhiều hơn nhóm thứ nhất. Dữ liệu có ý nghĩa. Cơ sở dữ liệu chỉ là chi tiết.