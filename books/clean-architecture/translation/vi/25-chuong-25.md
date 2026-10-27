# Chương 25: Các lớp và ranh giới
![Minh họa](assets/illustrations/25-chuong-25-opener.png){w=300}

Ta dễ hình dung hệ thống gồm ba thành phần: giao diện người dùng, quy tắc nghiệp vụ và cơ sở dữ liệu. Với một số hệ thống đơn giản, như vậy là đủ. Nhưng với hầu hết hệ thống, số thành phần nhiều hơn.

Chẳng hạn, hãy nghĩ đến một trò chơi máy tính đơn giản. Ta dễ hình dung ba thành phần. Giao diện người dùng xử lý mọi thông điệp từ người chơi gửi đến luật chơi. Luật chơi lưu trạng thái trò chơi trong một cấu trúc dữ liệu bền vững nào đó. Nhưng liệu chỉ có vậy thôi không?

## Săn Wumpus

Hãy cụ thể hóa ví dụ này. Giả sử trò chơi là cuộc phiêu lưu *Hunt the Wumpus* nổi tiếng từ năm 1972. Trò chơi dạng văn bản này dùng các lệnh rất đơn giản như `GO EAST` và `SHOOT WEST`. Người chơi nhập lệnh, máy tính phản hồi bằng những gì người chơi nhìn thấy, ngửi thấy, nghe thấy và trải nghiệm. Người chơi săn Wumpus trong một hệ thống hang động, đồng thời phải tránh bẫy, hố sâu và những mối nguy khác đang rình rập. Nếu quan tâm, bạn có thể dễ dàng tìm thấy luật chơi trên web.

Giả sử ta giữ giao diện dạng văn bản nhưng tách nó khỏi luật chơi, để có thể dùng các ngôn ngữ khác nhau ở những thị trường khác nhau. Luật chơi sẽ giao tiếp với thành phần giao diện qua một API độc lập với ngôn ngữ, còn giao diện sẽ chuyển API đó sang ngôn ngữ thích hợp cho người dùng.

Nếu quản lý phụ thuộc mã nguồn đúng cách như Hình 25.1, bất kỳ số lượng thành phần giao diện nào cũng có thể dùng chung luật chơi. Luật chơi không biết và cũng không quan tâm người dùng đang sử dụng ngôn ngữ nào.

**Hình 25.1** Nhiều thành phần giao diện có thể dùng chung luật chơi

Giả sử thêm rằng trạng thái trò chơi được lưu trong một kho lưu trữ bền vững, có thể là bộ nhớ flash, đám mây hoặc chỉ là RAM. Dù trong trường hợp nào, ta cũng không muốn luật chơi biết các chi tiết đó. Vì vậy, một lần nữa, ta tạo API để luật chơi giao tiếp với thành phần lưu trữ dữ liệu.

Ta không muốn luật chơi biết gì về các loại lưu trữ dữ liệu khác nhau. Do đó, phụ thuộc phải được sắp xếp đúng theo Quy tắc Phụ thuộc, như Hình 25.2 cho thấy.

**Hình 25.2** Tuân theo Quy tắc Phụ thuộc

## Kiến trúc sạch?

Rõ ràng ta có thể dễ dàng áp dụng cách tiếp cận Kiến trúc Sạch trong bối cảnh này,[^1] với đầy đủ ca sử dụng, ranh giới, Entity và cấu trúc dữ liệu tương ứng. Nhưng liệu ta đã tìm ra tất cả ranh giới kiến trúc quan trọng chưa?

Chẳng hạn, ngôn ngữ không phải trục thay đổi duy nhất của giao diện người dùng. Ta cũng có thể muốn thay đổi cơ chế giao tiếp nội dung. Ví dụ, ta có thể dùng cửa sổ shell thông thường, tin nhắn văn bản hoặc ứng dụng chat. Có rất nhiều khả năng.

Điều đó có nghĩa là trục thay đổi này có thể xác định một ranh giới kiến trúc. Có lẽ ta nên tạo một API đi qua ranh giới đó và tách biệt ngôn ngữ khỏi cơ chế giao tiếp. Ý tưởng này được minh họa ở Hình 25.3.

**Hình 25.3** Sơ đồ đã chỉnh sửa

Sơ đồ ở Hình 25.3 đã hơi phức tạp, nhưng không có gì bất ngờ. Các đường viền nét đứt biểu thị những thành phần trừu tượng xác định API do các thành phần phía trên hoặc phía dưới triển khai. Chẳng hạn, API `Language` được triển khai bởi `English` và `Spanish`.

`GameRules` giao tiếp với `Language` qua một API do `GameRules` xác định và `Language` triển khai. `Language` giao tiếp với `TextDelivery` qua API do `Language` xác định nhưng `TextDelivery` triển khai. API do thành phần sử dụng quyết định và sở hữu, không phải thành phần triển khai.

Nếu nhìn vào bên trong `GameRules`, ta sẽ thấy các giao diện ranh giới đa hình được mã bên trong `GameRules` sử dụng và mã bên trong thành phần `Language` triển khai. Ta cũng sẽ thấy các giao diện ranh giới đa hình được `Language` sử dụng và mã bên trong `GameRules` triển khai.

Bên trong `Language` cũng có cấu trúc tương tự: các giao diện ranh giới đa hình được mã trong `TextDelivery` triển khai, cùng các giao diện ranh giới đa hình do `TextDelivery` sử dụng và `Language` triển khai.

Trong mỗi trường hợp, API do các giao diện ranh giới xác định thuộc quyền sở hữu của thành phần ở phía gọi.

Các biến thể như `English`, `SMS` và `CloudData` được cung cấp qua các giao diện đa hình do thành phần API trừu tượng xác định, rồi được các thành phần cụ thể phục vụ chúng triển khai. Chẳng hạn, ta kỳ vọng các giao diện đa hình được xác định trong `Language` sẽ được `English` và `Spanish` triển khai.

Ta có thể đơn giản hóa sơ đồ bằng cách bỏ mọi biến thể và chỉ tập trung vào các thành phần API. Hình 25.4 cho thấy sơ đồ này.

**Hình 25.4** Sơ đồ đã đơn giản hóa

Hãy lưu ý rằng Hình 25.4 được bố trí sao cho mọi mũi tên đều hướng lên trên. Như vậy, `GameRules` nằm ở trên cùng. Cách bố trí này hợp lý vì `GameRules` chứa các chính sách cấp cao nhất.

Xét hướng luồng thông tin. Mọi đầu vào từ người dùng đi vào `TextDelivery` ở góc dưới bên trái. Thông tin đi lên qua thành phần `Language`, được chuyển thành lệnh gửi đến `GameRules`. `GameRules` xử lý đầu vào của người dùng rồi gửi dữ liệu thích hợp xuống `DataStorage` ở góc dưới bên phải.

Sau đó, `GameRules` gửi kết quả xuống `Language`. Thành phần này chuyển API trở lại ngôn ngữ phù hợp rồi chuyển ngôn ngữ đó đến người dùng qua `TextDelivery`.

Cấu trúc này chia luồng dữ liệu thành hai nhánh.[^2] Nhánh bên trái đảm nhiệm giao tiếp với người dùng, còn nhánh bên phải xử lý việc lưu trữ dữ liệu. Hai nhánh gặp nhau ở phía trên,[^3] tại `GameRules`, thành phần cuối cùng xử lý dữ liệu đi qua cả hai nhánh.

## Giao cắt các luồng

Có phải lúc nào cũng chỉ có hai luồng dữ liệu như trong ví dụ này không? Không hề. Hãy tưởng tượng ta muốn chơi *Hunt the Wumpus* trên mạng với nhiều người cùng lúc. Khi đó, ta cần thêm một thành phần mạng như trong Hình 25.5. Cấu trúc này chia luồng dữ liệu thành ba nhánh, tất cả đều do `GameRules` điều khiển.

**Hình 25.5** Thêm thành phần mạng

Khi hệ thống phức tạp hơn, cấu trúc thành phần có thể tách thành nhiều nhánh như vậy.

## Tách các luồng

Có thể bạn đang nghĩ rằng mọi luồng cuối cùng đều gặp nhau ở trên cùng trong một thành phần duy nhất. Giá mà mọi chuyện đơn giản như vậy! Thực tế phức tạp hơn nhiều.

Hãy xét thành phần `GameRules` của *Hunt the Wumpus*. Một phần luật chơi xử lý cơ chế bản đồ. Phần này biết các hang động nối với nhau như thế nào và vật thể nào nằm trong từng hang. Nó biết cách di chuyển người chơi từ hang này sang hang khác và xác định những sự kiện người chơi phải xử lý.

Nhưng còn một tập hợp chính sách khác ở cấp cao hơn nữa, biết tình trạng sức khỏe của người chơi cùng chi phí hoặc lợi ích của từng sự kiện. Các chính sách này có thể khiến sức khỏe người chơi giảm dần hoặc tăng lên khi tìm được thức ăn. Chính sách cơ chế cấp thấp sẽ thông báo sự kiện cho chính sách cấp cao, chẳng hạn `FoundFood` hoặc `FellInPit`. Chính sách cấp cao hơn sau đó quản lý trạng thái người chơi, như Hình 25.6 cho thấy. Cuối cùng, chính sách đó quyết định người chơi thắng hay thua.

**Hình 25.6** Chính sách cấp cao hơn quản lý người chơi

Đây có phải là một ranh giới kiến trúc không? Ta có cần API tách `MoveManagement` khỏi `PlayerManagement` không? Hãy làm ví dụ thú vị hơn một chút bằng cách thêm vi dịch vụ.

Giả sử ta có phiên bản *Hunt the Wumpus* nhiều người chơi quy mô lớn. `MoveManagement` chạy cục bộ trên máy tính của người chơi, còn `PlayerManagement` chạy trên máy chủ. `PlayerManagement` cung cấp API vi dịch vụ cho mọi thành phần `MoveManagement` được kết nối.

Hình 25.7 mô tả kịch bản này theo cách rút gọn. Các thành phần mạng phức tạp hơn những gì sơ đồ thể hiện, nhưng có lẽ bạn vẫn hình dung được. Trong trường hợp này, giữa `MoveManagement` và `PlayerManagement` có một ranh giới kiến trúc hoàn chỉnh.

**Hình 25.7** Thêm API vi dịch vụ

## Kết luận

Điều này có ý nghĩa gì? Vì sao tôi lấy một chương trình đơn giản đến mức vô lý, có thể viết trong 200 dòng Kornshell, rồi mở rộng nó với tất cả những ranh giới kiến trúc phức tạp này?

Ví dụ này nhằm cho thấy ranh giới kiến trúc tồn tại ở khắp nơi. Với tư cách kiến trúc sư, chúng ta phải cẩn thận nhận ra khi nào cần đến chúng. Ta cũng phải hiểu rằng khi được triển khai đầy đủ, những ranh giới ấy rất tốn kém. Đồng thời, nếu bỏ qua ranh giới, chi phí bổ sung chúng về sau có thể rất cao, ngay cả khi đã có bộ kiểm thử toàn diện và quy trình tái cấu trúc có kỷ luật.

Vậy chúng ta, những kiến trúc sư, phải làm gì? Câu trả lời không dễ chịu. Một mặt, nhiều người thông minh đã khuyên chúng ta không nên dự đoán trước nhu cầu trừu tượng hóa. Đó là triết lý YAGNI: “You Aren’t Going to Need It” (Bạn sẽ không cần đến nó). Lời khuyên này có phần đúng, vì thiết kế quá mức thường tệ hơn thiết kế chưa đủ. Mặt khác, khi phát hiện mình thật sự cần một ranh giới kiến trúc nhưng chưa có, chi phí và rủi ro để bổ sung có thể rất cao.

Vậy đấy. Hỡi kiến trúc sư phần mềm, bạn phải nhìn thấy tương lai. Bạn phải dự đoán một cách sáng suốt. Bạn phải cân nhắc chi phí và xác định vị trí các ranh giới kiến trúc, đồng thời quyết định ranh giới nào cần triển khai đầy đủ, ranh giới nào chỉ triển khai một phần và ranh giới nào nên bỏ qua.

Nhưng đây không phải quyết định chỉ đưa ra một lần. Bạn không thể ngay đầu dự án quyết định ranh giới nào sẽ triển khai, ranh giới nào sẽ bỏ qua rồi thôi. Thay vào đó, hãy quan sát. Chú ý khi hệ thống phát triển. Ghi nhận nơi có thể cần ranh giới, rồi cẩn thận theo dõi dấu hiệu ma sát đầu tiên do thiếu những ranh giới ấy.

Khi đó, hãy cân nhắc chi phí triển khai ranh giới so với chi phí bỏ qua nó, rồi thường xuyên xem xét lại quyết định. Mục tiêu là triển khai ranh giới đúng tại điểm mà chi phí triển khai bắt đầu thấp hơn chi phí bỏ qua.

Cần một con mắt luôn cảnh giác.

[^1]: Cũng cần thấy rõ rằng ta sẽ không áp dụng Kiến trúc Sạch cho một trò chơi đơn giản như thế này. Toàn bộ chương trình có lẽ chỉ cần viết trong 200 dòng mã hoặc ít hơn. Ở đây, ta dùng một chương trình đơn giản làm đại diện cho hệ thống lớn hơn với các ranh giới kiến trúc quan trọng.
[^2]: Nếu thấy khó hiểu hướng của các mũi tên, hãy nhớ rằng chúng chỉ hướng phụ thuộc mã nguồn, không phải hướng luồng dữ liệu.
[^3]: Ngày trước, ta có thể gọi thành phần trên cùng là Central Transform. Xem *Practical Guide to Structured Systems Design*, ấn bản thứ hai, Meilir Page-Jones, 1988.