# Chương 18: Giải phẫu ranh giới
![Minh họa](assets/illustrations/18-chuong-18-opener.png){w=300}

Kiến trúc của một hệ thống được xác định bởi tập hợp các thành phần phần mềm và những ranh giới ngăn cách chúng. Các ranh giới ấy có nhiều dạng khác nhau. Trong chương này, chúng ta sẽ xem xét một số dạng phổ biến nhất.

## Vượt qua ranh giới

Khi chương trình đang chạy, vượt qua ranh giới chỉ đơn giản là một hàm ở phía này gọi một hàm ở phía kia và truyền theo một ít dữ liệu. Bí quyết để tạo ranh giới phù hợp là quản lý các phụ thuộc mã nguồn.

Vì sao phải quan tâm đến mã nguồn? Vì khi một mô-đun mã nguồn thay đổi, các mô-đun khác có thể cũng phải thay đổi, biên dịch lại rồi triển khai lại. Ranh giới có nhiệm vụ quản lý và ngăn chặn sự lan truyền của những thay đổi đó.

## Khối nguyên khối đáng sợ

Ranh giới kiến trúc đơn giản và phổ biến nhất không có biểu hiện vật lý cụ thể. Đó chỉ là sự phân tách có kỷ luật giữa các hàm và dữ liệu trong cùng một bộ xử lý và cùng một không gian địa chỉ. Trong chương trước, tôi gọi đây là chế độ tách rời ở cấp mã nguồn.

Xét từ góc độ triển khai, cấu trúc này chỉ gồm một tệp thực thi duy nhất, thường được gọi là khối nguyên khối. Tệp đó có thể là dự án C hoặc C++ liên kết tĩnh, tập hợp các tệp lớp Java đóng gói trong một tệp jar thực thi, các tệp nhị phân .NET gộp vào một tệp .EXE, v.v.

Việc các ranh giới không hiện ra trong quá trình triển khai khối nguyên khối không có nghĩa là chúng không tồn tại hoặc không có ý nghĩa. Ngay cả khi được liên kết tĩnh thành một tệp thực thi duy nhất, khả năng phát triển độc lập các thành phần khác nhau rồi điều phối chúng để lắp ráp cuối cùng vẫn vô cùng giá trị.

Những kiến trúc như vậy hầu như luôn dựa vào đa hình động[^1] để quản lý các phụ thuộc nội bộ. Đây là một trong những lý do khiến phát triển hướng đối tượng trở thành mô hình quan trọng trong vài thập kỷ gần đây. Nếu không có hướng đối tượng, hoặc một hình thức đa hình tương đương, kiến trúc sư phải dùng đến cách nguy hiểm là sử dụng con trỏ hàm để đạt được sự tách rời cần thiết. Hầu hết kiến trúc sư cho rằng dùng con trỏ hàm tràn lan quá rủi ro, nên họ buộc phải từ bỏ việc phân chia hệ thống thành các thành phần.

Cách vượt ranh giới đơn giản nhất là một hàm ở phía khách hàng cấp thấp gọi dịch vụ cấp cao hơn. Cả phụ thuộc lúc chạy lẫn phụ thuộc lúc biên dịch đều cùng hướng về thành phần cấp cao hơn.

Trong Hình 18.1, luồng điều khiển đi qua ranh giới từ trái sang phải. `Client` gọi hàm `f()` của `Service` và truyền theo một thể hiện của `Data`. Ký hiệu `<DS>` chỉ một cấu trúc dữ liệu. `Data` có thể được truyền như đối số hàm hoặc bằng một phương thức phức tạp hơn. Lưu ý rằng định nghĩa của `Data` nằm ở phía được gọi của ranh giới.

**Hình 18.1** Luồng điều khiển đi qua ranh giới từ cấp thấp lên cấp cao

Khi một khách hàng cấp cao cần gọi dịch vụ cấp thấp, đa hình động được dùng để đảo ngược phụ thuộc, ngược với hướng luồng điều khiển. Phụ thuộc lúc chạy đi ngược hướng với phụ thuộc lúc biên dịch.

Trong Hình 18.2, luồng điều khiển vẫn đi qua ranh giới từ trái sang phải. `Client` cấp cao gọi hàm `f()` của `ServiceImpl` cấp thấp thông qua giao diện `Service`. Tuy nhiên, hãy lưu ý rằng mọi phụ thuộc đều đi qua ranh giới từ phải sang trái, hướng về thành phần cấp cao hơn. Cũng cần lưu ý định nghĩa của cấu trúc dữ liệu nằm ở phía gọi.

**Hình 18.2** Vượt ranh giới ngược với luồng điều khiển

Ngay cả trong một tệp thực thi nguyên khối được liên kết tĩnh, việc phân chia có kỷ luật như vậy cũng có thể hỗ trợ đáng kể cho quá trình phát triển, kiểm thử và triển khai dự án. Các nhóm có thể làm việc độc lập trên thành phần của mình mà không cản trở nhau. Thành phần cấp cao vẫn độc lập với các chi tiết cấp thấp.

Giao tiếp giữa các thành phần trong một khối nguyên khối rất nhanh và ít tốn kém. Thông thường, chúng chỉ là các lời gọi hàm. Vì vậy, giao tiếp qua các ranh giới tách rời ở cấp mã nguồn có thể diễn ra rất thường xuyên.

Vì triển khai khối nguyên khối thường đòi hỏi biên dịch và liên kết tĩnh, các thành phần trong những hệ thống này thường được phân phối dưới dạng mã nguồn.

## Các thành phần triển khai

Biểu hiện vật lý đơn giản nhất của một ranh giới kiến trúc là thư viện liên kết động, chẳng hạn DLL của .NET, tệp jar của Java, Gem của Ruby hoặc thư viện dùng chung của UNIX. Việc triển khai không cần biên dịch. Thay vào đó, các thành phần được phân phối dưới dạng nhị phân hoặc một dạng tương đương có thể triển khai. Đây là chế độ tách rời ở cấp triển khai. Việc triển khai chỉ đơn giản là tập hợp các đơn vị có thể triển khai vào một dạng thuận tiện, chẳng hạn tệp WAR hoặc một thư mục.

Ngoại trừ điểm đó, các thành phần ở cấp triển khai giống với khối nguyên khối. Các hàm thường vẫn chạy trong cùng một bộ xử lý và không gian địa chỉ. Cách phân tách thành phần và quản lý phụ thuộc cũng như nhau.[^2]

Tương tự khối nguyên khối, giao tiếp qua ranh giới giữa các thành phần triển khai chỉ là lời gọi hàm nên rất ít tốn kém. Có thể phát sinh chi phí một lần cho việc liên kết động hoặc nạp lúc chạy, nhưng giao tiếp qua những ranh giới này vẫn có thể diễn ra rất thường xuyên.

## Luồng

Cả khối nguyên khối lẫn các thành phần triển khai đều có thể sử dụng luồng. Luồng không phải là ranh giới kiến trúc hay đơn vị triển khai; chúng là cách tổ chức lịch trình và thứ tự thực thi. Luồng có thể nằm hoàn toàn trong một thành phần hoặc trải rộng qua nhiều thành phần.

## Tiến trình cục bộ

Một ranh giới kiến trúc vật lý mạnh hơn nhiều là tiến trình cục bộ. Tiến trình cục bộ thường được tạo từ dòng lệnh hoặc một lệnh gọi hệ thống tương đương. Các tiến trình cục bộ chạy trên cùng một bộ xử lý, hoặc trong cùng một nhóm bộ xử lý đa lõi, nhưng ở các không gian địa chỉ riêng biệt. Cơ chế bảo vệ bộ nhớ thường ngăn các tiến trình chia sẻ bộ nhớ, dù các phân vùng bộ nhớ dùng chung vẫn thường được sử dụng.

Thông thường, các tiến trình cục bộ giao tiếp với nhau qua socket hoặc một phương tiện giao tiếp khác của hệ điều hành, chẳng hạn mailbox hay hàng đợi thông điệp.

Mỗi tiến trình cục bộ có thể là một khối nguyên khối liên kết tĩnh, hoặc được cấu thành từ các thành phần triển khai liên kết động. Trong trường hợp thứ nhất, một số tiến trình nguyên khối có thể chứa cùng các thành phần đã được biên dịch và liên kết vào chúng. Trong trường hợp thứ hai, chúng có thể dùng chung các thành phần triển khai liên kết động.

Hãy xem tiến trình cục bộ như một siêu thành phần: nó gồm các thành phần cấp thấp quản lý phụ thuộc của mình bằng đa hình động.

Chiến lược tách biệt giữa các tiến trình cục bộ cũng giống như với khối nguyên khối và các thành phần nhị phân. Phụ thuộc mã nguồn qua ranh giới vẫn cùng hướng, luôn hướng về thành phần cấp cao hơn.

Với tiến trình cục bộ, điều đó có nghĩa mã nguồn của tiến trình cấp cao hơn không được chứa tên, địa chỉ vật lý hoặc khóa tra cứu trong registry của tiến trình cấp thấp hơn. Hãy nhớ rằng mục tiêu kiến trúc là biến các tiến trình cấp thấp thành plugin của tiến trình cấp cao.

Giao tiếp qua ranh giới giữa các tiến trình cục bộ đòi hỏi lời gọi hệ điều hành, tổ chức truyền và giải mã dữ liệu, cùng các lần chuyển ngữ cảnh giữa tiến trình. Những thao tác này tốn kém ở mức vừa phải. Vì vậy, cần hạn chế việc giao tiếp quá thường xuyên.

## Dịch vụ

Ranh giới mạnh nhất là dịch vụ. Dịch vụ là một tiến trình, thường được khởi chạy từ dòng lệnh hoặc thông qua một lệnh gọi hệ thống tương đương. Dịch vụ không phụ thuộc vào vị trí vật lý của nó. Hai dịch vụ giao tiếp với nhau có thể chạy trên cùng một bộ xử lý hoặc nhóm bộ xử lý đa lõi, nhưng cũng có thể không. Các dịch vụ giả định rằng mọi giao tiếp đều diễn ra qua mạng.

Giao tiếp qua ranh giới dịch vụ chậm hơn rất nhiều so với lời gọi hàm. Thời gian phản hồi có thể từ vài chục mili giây đến vài giây. Cần tránh giao tiếp quá thường xuyên khi có thể. Giao tiếp ở cấp này phải tính đến độ trễ cao.

Ngoài ra, các quy tắc áp dụng cho dịch vụ cũng giống như với tiến trình cục bộ. Dịch vụ cấp thấp nên “cắm vào” dịch vụ cấp cao. Mã nguồn của dịch vụ cấp cao không được chứa bất kỳ hiểu biết cụ thể nào về mặt vật lý, chẳng hạn URI, của dịch vụ cấp thấp.

## Kết luận

Hầu hết hệ thống, ngoại trừ các khối nguyên khối, sử dụng nhiều hơn một chiến lược ranh giới. Hệ thống dùng ranh giới dịch vụ cũng có thể có một số ranh giới tiến trình cục bộ. Thực tế, một dịch vụ thường chỉ là mặt tiền cho một tập hợp các tiến trình cục bộ tương tác với nhau. Dịch vụ hoặc tiến trình cục bộ gần như chắc chắn là một khối nguyên khối gồm các thành phần mã nguồn, hoặc một tập hợp các thành phần triển khai liên kết động.

Điều này có nghĩa ranh giới trong một hệ thống thường là sự pha trộn giữa các ranh giới cục bộ cho phép giao tiếp thường xuyên và các ranh giới chú trọng hơn đến độ trễ.

[^1]: Đa hình tĩnh (chẳng hạn generics hoặc templates) đôi khi có thể là cách quản lý phụ thuộc khả thi trong hệ thống nguyên khối, nhất là với các ngôn ngữ như C++. Tuy nhiên, sự tách rời nhờ generics không thể tránh yêu cầu biên dịch lại và triển khai lại như đa hình động.
[^2]: Trong trường hợp này, đa hình tĩnh không phải là một lựa chọn.