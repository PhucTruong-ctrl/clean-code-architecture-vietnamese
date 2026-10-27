# Chương 21: Kiến trúc lên tiếng
![Minh họa](assets/illustrations/21-chuong-21-opener.png){w=300}

Hãy tưởng tượng bạn đang xem bản vẽ một tòa nhà. Tài liệu do kiến trúc sư chuẩn bị này trình bày kế hoạch xây dựng. Những bản vẽ đó cho bạn biết điều gì?

Nếu đó là bản vẽ một ngôi nhà dành cho một gia đình, bạn sẽ thấy lối vào chính, tiền sảnh dẫn đến phòng khách và có thể cả phòng ăn. Nhà bếp có lẽ ở gần đó, cách phòng ăn không xa. Bên cạnh nhà bếp có thể là một góc ăn uống nhỏ, và phòng sinh hoạt chung có lẽ cũng ở gần. Nhìn vào bản vẽ, bạn sẽ không thể nhầm đó là một ngôi nhà dành cho một gia đình. Kiến trúc của nó sẽ cất tiếng: “NHÀ”.

Còn nếu bạn đang xem bản vẽ thư viện thì sao? Có lẽ bạn sẽ thấy lối vào lớn, khu vực dành cho nhân viên làm thủ tục mượn và trả sách, các khu đọc sách, những phòng họp nhỏ, cùng nhiều dãy không gian đặt giá sách chứa toàn bộ sách trong thư viện. Kiến trúc ấy sẽ cất tiếng: “THƯ VIỆN”.

Vậy kiến trúc ứng dụng của bạn thể hiện điều gì? Khi nhìn vào cấu trúc thư mục cấp cao nhất và các tệp mã nguồn trong gói cấp cao nhất, bạn có nhận ra “Hệ thống Chăm sóc Sức khỏe”, “Hệ thống Kế toán” hay “Hệ thống Quản lý Hàng tồn kho” không? Hay bạn chỉ thấy “Rails”, “Spring/Hibernate” hoặc “ASP”?

## Chủ đề của kiến trúc

Hãy đọc lại công trình có ảnh hưởng lớn của Ivar Jacobson về kiến trúc phần mềm, *Object Oriented Software Engineering*. Hãy chú ý phụ đề: *A Use Case Driven Approach*. Trong sách này, Jacobson cho rằng kiến trúc phần mềm là cấu trúc hỗ trợ các ca sử dụng của hệ thống. Cũng như bản vẽ ngôi nhà hay thư viện thể hiện rõ các ca sử dụng của công trình, kiến trúc ứng dụng phần mềm cũng nên thể hiện rõ các ca sử dụng của ứng dụng.

Kiến trúc không phải, và cũng không nên là, framework. Framework không nên quyết định cấu trúc kiến trúc. Framework là công cụ để sử dụng, không phải khuôn mẫu mà kiến trúc phải tuân theo. Nếu kiến trúc của bạn dựa trên framework, thì nó không thể đồng thời dựa trên các ca sử dụng.

## Mục đích của kiến trúc

Kiến trúc tốt lấy các ca sử dụng làm trung tâm, để kiến trúc sư có thể mô tả an toàn cấu trúc hỗ trợ chúng mà không phải cam kết với framework, công cụ hay môi trường cụ thể. Hãy nghĩ lại về bản vẽ ngôi nhà. Mối quan tâm đầu tiên của kiến trúc sư là bảo đảm ngôi nhà có thể sử dụng được, chứ không phải bảo đảm nó được xây bằng gạch. Thực tế, kiến trúc sư còn cố gắng để chủ nhà có thể quyết định vật liệu ngoại thất, như gạch, đá hay gỗ tuyết tùng, vào giai đoạn sau, khi bản vẽ đã bảo đảm đáp ứng các ca sử dụng.

Kiến trúc phần mềm tốt cho phép trì hoãn các quyết định về framework, cơ sở dữ liệu, máy chủ web và những vấn đề hay công cụ thuộc môi trường khác. Framework là những lựa chọn nên được để mở. Kiến trúc tốt giúp bạn không cần quyết định dùng Rails, Spring, Hibernate, Tomcat hay MySQL cho đến giai đoạn muộn hơn của dự án. Kiến trúc tốt cũng giúp bạn dễ dàng đổi ý về những lựa chọn ấy. Nó nhấn mạnh các ca sử dụng và tách chúng khỏi những mối quan tâm ngoại vi.

## Thế còn web thì sao?

Web có phải là kiến trúc không? Việc hệ thống được cung cấp qua web có quyết định kiến trúc hệ thống không? Tất nhiên là không. Web là một cơ chế phân phối, một thiết bị IO, và kiến trúc ứng dụng nên xem nó như vậy. Việc ứng dụng được cung cấp qua web chỉ là chi tiết, không nên chi phối cấu trúc hệ thống. Thực ra, quyết định cung cấp ứng dụng qua web là quyết định nên được trì hoãn. Kiến trúc hệ thống nên càng ít biết về cách phân phối càng tốt. Bạn nên có thể cung cấp hệ thống dưới dạng ứng dụng console, ứng dụng web, ứng dụng máy tính cài đặt cục bộ hoặc dịch vụ web, mà không cần thay đổi hay làm phức tạp quá mức kiến trúc nền tảng.

## Framework là công cụ, không phải lối sống

Framework có thể rất mạnh mẽ và hữu ích. Tác giả framework thường tin tưởng sâu sắc vào framework của mình. Những ví dụ họ viết về cách sử dụng framework thường được trình bày từ góc nhìn của một người hết lòng tin theo. Các tác giả khác viết về framework cũng thường là môn đồ của niềm tin ấy. Họ chỉ cho bạn cách dùng framework. Họ thường giả định rằng framework phải bao trùm mọi thứ và làm tất cả.

> Đó không phải là cách tiếp cận bạn nên chọn.

Hãy xem xét từng framework với thái độ tỉnh táo và hoài nghi. Có thể nó hữu ích, nhưng cái giá phải trả là gì? Hãy tự hỏi nên dùng nó ra sao và làm thế nào để tự bảo vệ khỏi nó. Hãy nghĩ cách giữ cho kiến trúc tiếp tục đặt các ca sử dụng làm trọng tâm. Xây dựng chiến lược ngăn framework chiếm quyền kiểm soát kiến trúc.

## Kiến trúc có thể kiểm thử

Nếu kiến trúc hệ thống tập trung vào các ca sử dụng và bạn giữ framework ở khoảng cách an toàn, bạn sẽ có thể kiểm thử đơn vị tất cả ca sử dụng mà không cần cài đặt bất kỳ framework nào. Bạn không cần máy chủ web đang chạy để thực hiện kiểm thử. Bạn không cần kết nối cơ sở dữ liệu. Các đối tượng Entity nên là những đối tượng thông thường, không phụ thuộc vào framework, cơ sở dữ liệu hay những thứ phức tạp khác. Các đối tượng ca sử dụng nên điều phối các Entity. Cuối cùng, tất cả những thành phần đó phải có thể được kiểm thử tại chỗ, không vướng các phức tạp do framework gây ra.

## Kết luận

Kiến trúc của bạn nên cho người đọc biết về hệ thống, không phải về framework bạn đã dùng. Nếu bạn đang xây dựng hệ thống chăm sóc sức khỏe, thì khi lập trình viên mới xem kho mã nguồn, ấn tượng đầu tiên của họ nên là: “Ồ, đây là hệ thống chăm sóc sức khỏe”. Họ phải có thể tìm hiểu mọi ca sử dụng của hệ thống mà vẫn chưa cần biết hệ thống được phân phối bằng cách nào. Có thể họ sẽ hỏi:

> “Chúng tôi thấy vài thứ trông giống như model, nhưng view và controller ở đâu?”

Và bạn nên trả lời:

> “Ồ, đó là những chi tiết hiện chưa cần quan tâm. Chúng ta sẽ quyết định sau.”