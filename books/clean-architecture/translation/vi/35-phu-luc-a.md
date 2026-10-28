# Phụ lục A: Khảo cổ kiến trúc
![Minh họa](assets/illustrations/appendix-a-opener.png){w=300}

Để khai quật các nguyên tắc của kiến trúc tốt, hãy cùng nhìn lại 45 năm dự án tôi đã tham gia kể từ năm 1970. Một số dự án đáng chú ý từ góc độ kiến trúc. Những dự án khác đáng nhớ vì bài học rút ra và ảnh hưởng của chúng đến các dự án sau.

Phụ lục này có phần tự truyện. Tôi đã cố giữ nội dung liên quan đến chủ đề kiến trúc, nhưng trong một bài tự truyện thì đôi khi những yếu tố khác vẫn xen vào. ;-)

## Hệ thống kế toán công đoàn

Cuối những năm 1960, một công ty tên ASC Tabulating ký hợp đồng với Chi nhánh 705 của Công đoàn Teamsters để cung cấp hệ thống kế toán. Máy tính ASC chọn cho hệ thống là GE Datanet 30, như Hình A.1 cho thấy.

**Hình A.1** GE Datanet 30

Ảnh do Ed Thelen cung cấp, ed-thelen.org

Như bạn thấy trong ảnh, đây là một cỗ máy khổng lồ.[^1] Nó chiếm cả một căn phòng, và căn phòng cần được kiểm soát môi trường nghiêm ngặt.

Máy tính này được chế tạo trước thời mạch tích hợp, bằng các transistor rời. Bên trong còn có một số đèn điện tử, nhưng chỉ dùng trong bộ khuếch đại tín hiệu của ổ băng từ.

Theo tiêu chuẩn ngày nay, cỗ máy này vừa khổng lồ, vừa chậm, lại có dung lượng bộ nhớ nhỏ và khá thô sơ. Nó có 16K × 18 bit bộ nhớ lõi, chu kỳ khoảng 7 micro giây.[^2] Máy chiếm một căn phòng lớn được kiểm soát môi trường. Nó có ổ băng từ 7 track và một ổ đĩa dung lượng khoảng 20 megabyte.

Ổ đĩa ấy là một con quái vật. Bạn có thể thấy nó trong Hình A.2, nhưng ảnh chưa thể hiện hết kích thước. Đỉnh tủ cao hơn đầu tôi. Các phiến đĩa đường kính 36 inch, dày 3/8 inch. Hình A.3 cho thấy một phiến đĩa.

**Hình A.2** Bộ lưu trữ dữ liệu cùng các phiến đĩa

Ảnh do Ed Thelen cung cấp, ed-thelen.org

**Hình A.3** Một phiến đĩa: dày 3/8 inch, đường kính 36 inch

Bây giờ hãy đếm số phiến đĩa trong ảnh đầu tiên. Có hơn một tá. Mỗi phiến có một tay đọc riêng, được dẫn động bằng bộ truyền động khí nén. Bạn có thể nhìn các đầu đọc di chuyển ngang qua phiến đĩa. Thời gian tìm kiếm có lẽ từ nửa giây đến một giây.

Khi cỗ máy quái vật này khởi động, tiếng động giống động cơ phản lực. Sàn nhà rung lên cho đến khi máy đạt tốc độ.[^3]

Thành tựu nổi bật của Datanet 30 là khả năng điều khiển nhiều thiết bị đầu cuối không đồng bộ với tốc độ khá cao. Đó chính xác là điều ASC cần.

ASC đặt tại Lake Bluff, Illinois, cách Chicago 30 dặm về phía bắc. Văn phòng Local 705 ở trung tâm Chicago. Công đoàn muốn khoảng một tá nhân viên nhập liệu dùng thiết bị đầu cuối CRT[^4] để nhập dữ liệu vào hệ thống (Hình A.4). Báo cáo được in bằng máy điện báo ASR35 (Hình A.5).

**Hình A.4** Thiết bị đầu cuối CRT Datapoint

Ảnh do Bill Degnan cung cấp, vintagecomputer.net

**Hình A.5** Máy điện báo ASR35

Ảnh do Joe Mabel cung cấp, được phép sử dụng

Các thiết bị CRT chạy ở tốc độ 30 ký tự mỗi giây. Cuối những năm 1960, đó là tốc độ khá tốt vì modem còn tương đối thô sơ.

ASC thuê từ công ty điện thoại khoảng một tá đường dây riêng và gấp đôi số modem 300 baud để nối Datanet 30 với các thiết bị đầu cuối này.

Những máy tính ấy không có hệ điều hành. Chúng thậm chí không có hệ thống tệp. Thứ bạn có chỉ là trình hợp dịch.

Nếu cần lưu dữ liệu trên đĩa, bạn ghi dữ liệu trực tiếp lên đĩa. Không có tệp. Không có thư mục. Bạn phải xác định track, phiến đĩa và sector nào sẽ chứa dữ liệu, rồi điều khiển ổ đĩa để ghi vào đó. Đúng vậy, chúng tôi tự viết trình điều khiển đĩa.

Hệ thống kế toán công đoàn có ba loại bản ghi: Đại lý, Nhà tuyển dụng và Thành viên. Hệ thống hỗ trợ các thao tác CRUD cho những bản ghi này, đồng thời có các chức năng ghi nhận phí đoàn, tính toán thay đổi trong sổ cái và những việc tương tự.

Hệ thống ban đầu được một chuyên gia tư vấn viết bằng hợp dịch. Bằng cách nào đó, ông đã nhồi được toàn bộ chương trình vào 16K.

Có thể hình dung cỗ Datanet 30 lớn ấy rất tốn kém để vận hành và bảo trì. Chuyên gia tư vấn phần mềm giữ cho hệ thống hoạt động cũng rất đắt. Hơn nữa, máy tính mini đang dần phổ biến và rẻ hơn nhiều.

Năm 1971, khi tôi 18 tuổi, ASC thuê tôi cùng hai người bạn mọt máy tính để thay thế toàn bộ hệ thống kế toán công đoàn bằng một hệ thống chạy trên máy tính mini Varian 620/f (Hình A.6). Máy tính rẻ. Chúng tôi cũng rẻ. Vì vậy, đối với ASC, đây có vẻ là một món hời.

**Hình A.6** Máy tính mini Varian 620/f

Máy Varian có bus 16 bit và bộ nhớ lõi 32K × 16. Chu kỳ khoảng 1 micro giây. Nó mạnh hơn Datanet 30 nhiều. Máy dùng công nghệ đĩa IBM 2314 rất thành công, cho phép lưu 30 megabyte trên các phiến đĩa đường kính chỉ 14 inch, không thể xuyên thủng tường gạch bê tông khi nổ tung!

Dĩ nhiên, chúng tôi vẫn không có hệ điều hành, hệ thống tệp hay ngôn ngữ cấp cao. Chúng tôi chỉ có trình hợp dịch. Nhưng chúng tôi vẫn xoay xở được.

### Trại trẻ mồ côi máy tính mini

Thay vì cố nhồi toàn bộ hệ thống vào 32K, chúng tôi tạo một hệ thống overlay. Các ứng dụng được nạp từ đĩa vào một vùng bộ nhớ dành riêng cho overlay. Chúng chạy trong vùng nhớ đó, rồi bị hoán đổi trở lại đĩa cùng RAM cục bộ để nhường chỗ cho chương trình khác.

Chương trình được hoán đổi vào vùng overlay, chạy đủ lâu để làm đầy bộ đệm đầu ra, rồi bị hoán đổi ra để chương trình khác được nạp vào.

Dĩ nhiên, khi giao diện người dùng chỉ chạy ở 30 ký tự mỗi giây, chương trình dành rất nhiều thời gian chờ. Chúng tôi có nhiều thời gian để hoán đổi chương trình vào và ra khỏi đĩa, giữ cho mọi thiết bị đầu cuối chạy nhanh nhất có thể. Không ai phàn nàn về thời gian phản hồi.

Chúng tôi viết một bộ giám sát có khả năng ưu tiên, quản lý ngắt và IO. Chúng tôi viết ứng dụng, trình điều khiển đĩa, trình điều khiển thiết bị đầu cuối, trình điều khiển băng từ và mọi thứ khác trong hệ thống. Không có phần nào mà chúng tôi không tự viết. Dù phải vật lộn với quá nhiều tuần làm việc 80 giờ, chúng tôi cũng đưa được cỗ máy quái vật vào hoạt động chỉ trong 8 hoặc 9 tháng.

Kiến trúc hệ thống rất đơn giản (Hình A.7). Khi một ứng dụng khởi chạy, nó tạo đầu ra cho đến khi bộ đệm đầu cuối tương ứng đầy. Sau đó, bộ giám sát hoán đổi ứng dụng đó ra và nạp ứng dụng mới vào. Bộ giám sát tiếp tục gửi nội dung trong bộ đệm đến thiết bị đầu cuối với tốc độ 30 ký tự mỗi giây cho đến khi bộ đệm gần cạn. Khi đó, nó hoán đổi ứng dụng trở lại để nạp đầy bộ đệm.

**Hình A.7** Kiến trúc hệ thống

Trong hệ thống này có hai ranh giới. Ranh giới thứ nhất là ranh giới đầu ra ký tự. Ứng dụng không biết đầu ra sẽ đến thiết bị đầu cuối 30 ký tự mỗi giây. Thực tế, từ góc nhìn ứng dụng, đầu ra ký tự hoàn toàn trừu tượng. Ứng dụng chỉ chuyển chuỗi cho bộ giám sát. Bộ giám sát chịu trách nhiệm nạp bộ đệm, gửi ký tự đến thiết bị đầu cuối và hoán đổi ứng dụng vào, ra khỏi bộ nhớ.

Ranh giới này có phụ thuộc xuôi, tức phụ thuộc cùng hướng với luồng điều khiển. Ứng dụng phụ thuộc lúc biên dịch vào bộ giám sát, và luồng điều khiển đi từ ứng dụng đến bộ giám sát. Ranh giới ngăn ứng dụng biết đầu ra sẽ được gửi đến loại thiết bị nào.

Ranh giới thứ hai đảo ngược phụ thuộc. Bộ giám sát có thể khởi chạy ứng dụng, nhưng không có phụ thuộc lúc biên dịch vào chúng. Luồng điều khiển đi từ bộ giám sát đến ứng dụng. Giao diện đa hình đảo ngược phụ thuộc rất đơn giản: mọi ứng dụng đều được khởi chạy bằng cách nhảy đến cùng một địa chỉ bộ nhớ chính xác trong vùng overlay. Ranh giới ngăn bộ giám sát biết bất kỳ điều gì về ứng dụng, ngoại trừ điểm khởi chạy.

## Cắt laser

Năm 1973, tôi gia nhập một công ty ở Chicago tên là Teradyne Applied Systems (TAS). Đây là một bộ phận của Teradyne Inc., có trụ sở chính tại Boston. Sản phẩm của chúng tôi là hệ thống dùng laser công suất tương đối cao để cắt tỉa linh kiện điện tử với độ chính xác rất cao.

Thời đó, nhà sản xuất in lụa các linh kiện điện tử lên đế gốm. Các đế này cỡ khoảng một inch vuông. Linh kiện thường là điện trở, thiết bị cản dòng điện.

Điện trở phụ thuộc vào nhiều yếu tố, trong đó có thành phần vật liệu và hình dạng. Điện trở càng rộng thì điện trở suất càng thấp.

Hệ thống đặt đế gốm vào một giá đỡ có đầu dò tiếp xúc với điện trở. Hệ thống đo điện trở, rồi dùng laser đốt bỏ một phần để làm điện trở mỏng dần cho đến khi đạt giá trị mong muốn, với sai số khoảng một phần mười phần trăm.

Chúng tôi bán các hệ thống này cho nhà sản xuất. Chúng tôi cũng dùng một số hệ thống nội bộ để cắt tỉa các lô tương đối nhỏ cho nhà sản xuất nhỏ.

Máy tính là M365. Thời đó, nhiều công ty tự chế tạo máy tính của mình. Teradyne chế tạo M365 và cung cấp cho mọi bộ phận. M365 là phiên bản cải tiến của PDP-8, một máy tính mini phổ biến lúc bấy giờ.

M365 điều khiển bàn định vị, di chuyển đế gốm bên dưới đầu dò. Nó điều khiển hệ thống đo và laser. Laser được định vị bằng gương X-Y có thể xoay theo chương trình. Máy tính cũng điều khiển được công suất laser.

Môi trường phát triển trên M365 tương đối thô sơ. Không có đĩa. Bộ nhớ lưu trữ lớn là các băng từ dạng hộp giống băng âm thanh 8-track cũ. Băng và ổ đĩa do Tri-Data sản xuất.

Giống băng âm thanh 8-track thời đó, băng được nối thành vòng. Ổ chỉ chạy băng theo một hướng, không có chức năng tua lại! Muốn đưa băng về đầu, bạn phải cho nó chạy đến “điểm nạp”.

Băng chạy với tốc độ khoảng một foot mỗi giây. Vì vậy, nếu vòng băng dài 25 foot, có thể mất đến 25 giây để đưa nó về điểm nạp. Do đó, Tri-Data sản xuất hộp băng với nhiều độ dài, từ 10 đến 100 foot.

M365 có một nút ở mặt trước. Nhấn nút sẽ nạp một chương trình bootstrap nhỏ vào bộ nhớ và thực thi nó. Chương trình đọc khối dữ liệu đầu tiên từ băng rồi chạy khối đó. Thông thường, khối này chứa trình nạp, dùng để nạp hệ điều hành nằm trên phần còn lại của băng.

Hệ điều hành sẽ yêu cầu người dùng nhập tên chương trình cần chạy. Các chương trình được lưu trên băng ngay sau hệ điều hành. Ta nhập tên chương trình, chẳng hạn trình soạn thảo ED-402. Hệ điều hành tìm chương trình đó trên băng, nạp vào bộ nhớ rồi chạy.

Bảng điều khiển là CRT ASCII dùng phosphor xanh, rộng 72 ký tự[^5] và cao 24 dòng. Tất cả ký tự đều viết hoa.

Để sửa chương trình, bạn nạp trình soạn thảo ED-402 rồi đưa vào băng chứa mã nguồn. Bạn đọc một khối mã nguồn từ băng vào bộ nhớ, nội dung được hiển thị trên màn hình. Một khối băng có thể chứa 50 dòng mã. Bạn sửa bằng cách di chuyển con trỏ trên màn hình và gõ theo cách tương tự vi. Khi xong, bạn ghi khối đó sang một băng khác rồi đọc khối tiếp theo từ băng nguồn. Cứ thế cho đến khi hoàn tất.

Không thể cuộn ngược về các khối trước đó. Bạn sửa chương trình theo đường thẳng từ đầu đến cuối. Muốn quay lại đầu, bạn phải chép xong mã nguồn sang băng đầu ra rồi bắt đầu một phiên sửa mới trên băng đó. Có lẽ không ngạc nhiên khi chúng tôi in chương trình ra giấy, đánh dấu mọi chỉnh sửa bằng mực đỏ, rồi sửa mã từng khối dựa vào bản in đã đánh dấu. Khi chỉnh sửa xong, chúng tôi quay lại hệ điều hành và chạy trình hợp dịch. Trình hợp dịch đọc băng mã nguồn và ghi băng nhị phân, đồng thời in danh sách mã ra máy in dòng.

Băng không đáng tin cậy tuyệt đối, nên chúng tôi luôn ghi đồng thời hai băng. Như vậy, ít nhất một băng có xác suất cao không bị lỗi.

Chương trình của chúng tôi dài khoảng 20.000 dòng mã và mất gần 30 phút để biên dịch. Khả năng gặp lỗi đọc băng trong thời gian đó vào khoảng 1 trên 10. Nếu trình hợp dịch gặp lỗi băng, nó sẽ rung chuông ở bảng điều khiển rồi in một loạt lỗi. Bạn có thể nghe tiếng chuông điên dại khắp phòng thí nghiệm, cùng tiếng chửi rủa của lập trình viên vừa biết mình phải bắt đầu lại lượt biên dịch 30 phút.

Kiến trúc chương trình điển hình cho thời ấy. Có một Chương trình Điều hành Chính, gọi tắt là MOP. Nó quản lý các chức năng IO cơ bản và cung cấp những tiện ích sơ khai của một “shell” trên bảng điều khiển. Nhiều bộ phận của Teradyne dùng chung mã nguồn MOP, nhưng mỗi bộ phận đều rẽ nhánh để dùng riêng. Vì vậy, chúng tôi gửi cập nhật mã nguồn cho nhau dưới dạng bản in đánh dấu, rồi tích hợp thủ công một cách rất cẩn thận.

Một lớp tiện ích chuyên dụng điều khiển phần cứng đo, bàn định vị và laser. Ranh giới giữa lớp này và MOP tốt nhất cũng chỉ mơ hồ. Lớp tiện ích gọi MOP, nhưng MOP đã được sửa riêng cho lớp đó và thường gọi ngược trở lại. Thực tế, chúng tôi không xem chúng là hai lớp riêng biệt. Với chúng tôi, đó chỉ là mã được thêm vào MOP theo cách gắn kết chặt chẽ.

Tiếp theo là lớp cách ly. Lớp này cung cấp giao diện máy ảo cho các chương trình ứng dụng, được viết bằng một ngôn ngữ đặc thù miền hoàn toàn khác, dựa trên dữ liệu. Ngôn ngữ có các phép toán để di chuyển laser, di chuyển bàn, cắt, đo và những việc tương tự. Khách hàng viết chương trình cắt tỉa bằng ngôn ngữ này, còn lớp cách ly thực thi chúng.

Mục tiêu không phải tạo một ngôn ngữ cắt laser độc lập với máy. Thực tế, ngôn ngữ có nhiều đặc điểm riêng gắn chặt với các lớp bên dưới. Thay vào đó, nó cung cấp cho lập trình viên ứng dụng một ngôn ngữ “đơn giản hơn” hợp dịch M356 để lập trình công việc cắt tỉa.

Công việc cắt tỉa được nạp từ băng và thực thi bởi hệ thống. Về cơ bản, hệ thống của chúng tôi là một hệ điều hành cho các ứng dụng cắt tỉa.

Hệ thống được viết bằng hợp dịch M365 và biên dịch thành một đơn vị duy nhất, tạo ra mã nhị phân tuyệt đối.

Các ranh giới trong ứng dụng này tốt nhất cũng chỉ lỏng lẻo. Ngay cả ranh giới giữa mã hệ thống và ứng dụng viết bằng DSL cũng không được thực thi tốt. Phụ thuộc có ở khắp nơi.

Nhưng đó là tình trạng phổ biến của phần mềm vào đầu thập niên 1970.

## Giám sát đúc nhôm

Giữa thập niên 1970, khi OPEC cấm vận dầu mỏ và tình trạng thiếu xăng khiến các tài xế giận dữ đánh nhau ở trạm xăng, tôi bắt đầu làm việc tại Outboard Marine Corporation (OMC). Đây là công ty mẹ của Johnson Motors và máy cắt cỏ Lawnboy.

OMC có một cơ sở khổng lồ ở Waukegan, Illinois, chuyên đúc các bộ phận nhôm cho động cơ và sản phẩm của công ty. Nhôm được nung chảy trong những lò lớn, rồi chở bằng các thùng lớn đến hàng chục máy đúc áp lực nhôm vận hành riêng lẻ. Mỗi máy có một người vận hành chịu trách nhiệm lắp khuôn, chạy máy và lấy chi tiết vừa đúc ra. Lương của họ được tính theo số lượng chi tiết sản xuất.

Tôi được thuê tham gia dự án tự động hóa xưởng sản xuất. OMC mua một máy tính IBM System/7, câu trả lời của IBM cho dòng máy tính mini. Họ nối máy tính này với mọi máy đúc trên sàn để đếm và đo thời gian chu kỳ của từng máy. Vai trò của chúng tôi là thu thập thông tin rồi hiển thị trên màn hình xanh IBM 3270.

Ngôn ngữ lập trình là hợp dịch. Một lần nữa, mọi mã chạy trên máy tính này đều do chúng tôi viết. Không có hệ điều hành, thư viện chương trình con hay framework. Chỉ có mã thô.

Đây cũng là mã thời gian thực, điều khiển bằng ngắt. Mỗi khi máy đúc hoàn tất một chu kỳ, chúng tôi phải cập nhật một loạt thống kê và gửi thông điệp đến một máy IBM 370 khổng lồ ở xa, chạy chương trình CICS-COBOL để hiển thị thống kê trên màn hình xanh.

Tôi ghét công việc này. Trời ơi, ghét lắm. Công việc thì vui! Nhưng văn hóa công ty thì… Chỉ cần nói rằng tôi bị yêu cầu phải đeo cà vạt.

Ồ, tôi đã cố gắng. Thật sự đã cố. Nhưng rõ ràng tôi không vui khi làm ở đó, và đồng nghiệp đều biết. Họ biết vì tôi không nhớ được những ngày quan trọng hoặc không dậy đủ sớm để dự các cuộc họp cần thiết. Đây là công việc lập trình duy nhất mà tôi từng bị sa thải, và tôi đáng bị như vậy.

Từ góc độ kiến trúc, ở đây không có nhiều điều để học, ngoài một điểm. System/7 có một chỉ thị thú vị tên là set program interrupt (SPI). Nó cho phép kích hoạt ngắt bộ xử lý để xử lý các ngắt ưu tiên thấp hơn đang chờ. Ngày nay, trong Java, ta gọi việc đó là `Thread.yield()`.

## 4-TEL

Tháng 10 năm 1976, sau khi bị OMC sa thải, tôi quay lại một bộ phận khác của Teradyne, nơi tôi gắn bó suốt 12 năm. Sản phẩm tôi tham gia mang tên 4-TEL. Mục đích là kiểm tra mọi đường dây điện thoại trong một khu vực dịch vụ mỗi đêm, rồi lập báo cáo về các đường dây cần sửa chữa. Hệ thống cũng cho phép nhân viên kiểm tra chi tiết từng đường dây cụ thể.

Ban đầu hệ thống có kiến trúc giống hệ thống cắt laser. Đó là ứng dụng nguyên khối viết bằng hợp dịch, không có ranh giới đáng kể. Nhưng vào lúc tôi gia nhập công ty, điều đó sắp thay đổi.

Hệ thống được các nhân viên kiểm tra trong trung tâm dịch vụ (SC) sử dụng. Một trung tâm dịch vụ bao phủ nhiều tổng đài trung tâm (CO), mỗi tổng đài có thể phục vụ đến 10.000 đường dây điện thoại. Phần cứng quay số và đo lường phải được đặt bên trong CO, nên máy tính M365 được đặt ở đó. Chúng tôi gọi chúng là thiết bị kiểm tra đường dây tổng đài (COLT). Một máy M365 khác được đặt tại SC và gọi là máy tính khu vực dịch vụ (SAC). SAC có một số modem để gọi đến COLT và giao tiếp ở tốc độ 300 baud, tức 30 ký tự mỗi giây.

Ban đầu, máy tính COLT làm mọi việc, kể cả giao tiếp với bảng điều khiển, hiển thị menu và tạo báo cáo. SAC chỉ là bộ ghép kênh đơn giản, nhận đầu ra từ COLT rồi hiển thị lên màn hình.

Vấn đề là 30 ký tự mỗi giây rất chậm. Nhân viên không thích nhìn ký tự lần lượt hiện ra trên màn hình, nhất là khi họ chỉ quan tâm đến một vài thông tin quan trọng. Hơn nữa, lúc đó bộ nhớ lõi của M365 rất đắt và chương trình lại lớn.

Giải pháp là tách phần mềm quay số và đo đường dây khỏi phần phân tích kết quả và in báo cáo. Phần sau được chuyển sang SAC, còn phần trước vẫn ở COLT. Nhờ vậy, COLT có thể nhỏ hơn và cần ít bộ nhớ hơn. Phản hồi trên thiết bị đầu cuối cũng nhanh hơn nhiều vì SAC tạo báo cáo.

Kết quả rất thành công. Màn hình cập nhật nhanh, sau khi quay số đến COLT thích hợp, và dung lượng bộ nhớ của COLT giảm đáng kể.

Ranh giới được tạo ra rất rõ ràng và tách rời chặt chẽ. SAC và COLT trao đổi các gói dữ liệu rất ngắn. Những gói này là một dạng DSL rất đơn giản, biểu diễn các lệnh cơ bản như “DIAL XXXX” hoặc “MEASURE”.

M365 được nạp từ băng từ. Các ổ băng này đắt tiền và không đáng tin cậy, nhất là trong môi trường công nghiệp của tổng đài điện thoại. Ngoài ra, M365 đắt so với các thiết bị điện tử khác trong COLT. Vì vậy, chúng tôi bắt đầu dự án thay M365 bằng một máy tính vi mô dùng bộ xử lý 8085.

Máy tính mới gồm một bo mạch xử lý chứa 8085, một bo RAM chứa 32K RAM và ba bo ROM, mỗi bo chứa 12K bộ nhớ chỉ đọc. Tất cả các bo vừa vào cùng khung máy với phần cứng đo lường, nhờ đó không cần khung máy cồng kềnh riêng cho M365.

Các bo ROM chứa 12 chip EPROM Intel 2708, tức bộ nhớ chỉ đọc có thể xóa và lập trình.[^6] Hình A.8 cho thấy một chip như vậy. Chúng tôi nạp phần mềm vào chip bằng thiết bị đặc biệt gọi là bộ ghi PROM, được điều khiển từ môi trường phát triển. Có thể xóa chip bằng cách chiếu tia cực tím cường độ cao.[^7]

**Hình A.8** Chip EPROM

Bạn tôi CK và tôi dịch chương trình hợp dịch M365 của COLT sang hợp dịch 8085. Chúng tôi dịch thủ công và mất khoảng sáu tháng. Kết quả cuối cùng dài khoảng 30K mã 8085.

Môi trường phát triển của chúng tôi có 64K RAM và không có ROM, nên có thể nhanh chóng tải các tệp nhị phân đã biên dịch vào RAM để kiểm thử.

Khi chương trình hoạt động, chúng tôi chuyển sang dùng EPROM. Chúng tôi ghi chương trình vào 30 chip rồi lắp từng chip vào đúng khe trên ba bo ROM. Mỗi chip được dán nhãn để biết nó nằm ở khe nào.

Chương trình 30K là một tệp nhị phân duy nhất, dài 30K. Để ghi chip, chúng tôi chia ảnh nhị phân đó thành 30 đoạn, mỗi đoạn 1K, rồi ghi từng đoạn vào chip có nhãn tương ứng.

Cách này hoạt động rất tốt. Chúng tôi bắt đầu sản xuất hàng loạt phần cứng và triển khai hệ thống ngoài thực tế.

Nhưng phần mềm thì mềm.[^8] Mọi người cần thêm tính năng và sửa lỗi. Khi số hệ thống được lắp đặt tăng lên, việc cập nhật phần mềm bằng cách ghi 30 chip cho mỗi lần triển khai, rồi cử nhân viên dịch vụ hiện trường thay cả 30 chip tại từng địa điểm, trở thành cơn ác mộng.

Có đủ loại vấn đề. Đôi khi chip bị dán nhầm nhãn hoặc nhãn bong ra. Đôi khi kỹ sư dịch vụ hiện trường thay nhầm chip. Có lúc họ vô tình làm gãy một chân của chip mới. Vì vậy, kỹ sư hiện trường phải mang theo chip dự phòng cho cả 30 vị trí.

Vì sao phải thay cả 30 chip? Mỗi khi thêm hoặc xóa mã trong tệp thực thi 30K, địa chỉ nạp từng lệnh đều thay đổi. Địa chỉ các chương trình con và hàm được gọi cũng thay đổi. Vì thế, mọi chip đều bị ảnh hưởng, cho dù thay đổi nhỏ đến đâu.

Một ngày nọ, sếp đến hỏi tôi cách giải quyết vấn đề. Ông nói cần một cách sửa firmware mà không phải thay cả 30 chip mỗi lần. Chúng tôi cùng suy nghĩ một lúc rồi bắt đầu dự án “Vectorization”. Dự án kéo dài ba tháng.

Ý tưởng rất đơn giản. Chúng tôi chia chương trình 30K thành 32 tệp mã nguồn có thể biên dịch độc lập, mỗi tệp dưới 1K. Ở đầu mỗi tệp, chúng tôi chỉ dẫn cho trình biên dịch địa chỉ nạp chương trình tạo ra, chẳng hạn `ORG C400` cho chip sẽ được lắp ở vị trí C4.

Ở đầu mỗi tệp mã nguồn, chúng tôi cũng tạo một cấu trúc dữ liệu có kích thước cố định, chứa địa chỉ mọi chương trình con trên chip đó. Cấu trúc dài 40 byte, đủ chứa tối đa 20 địa chỉ. Điều đó nghĩa là mỗi chip không thể có quá 20 chương trình con.

Tiếp theo, chúng tôi tạo một vùng đặc biệt trong RAM gọi là vector. Vùng này chứa 32 bảng, mỗi bảng dài 40 byte, vừa đủ để lưu các con trỏ ở đầu mỗi chip.

Cuối cùng, chúng tôi đổi mọi lời gọi chương trình con trên mọi chip thành lời gọi gián tiếp qua vector RAM tương ứng.

Khi bộ xử lý khởi động, nó quét từng chip và nạp bảng vector ở đầu mỗi chip vào vùng vector trong RAM. Sau đó, nó nhảy vào chương trình chính.

Cách này hoạt động rất tốt. Khi sửa lỗi hoặc thêm tính năng, giờ đây chúng tôi chỉ cần biên dịch lại một hoặc hai chip rồi gửi riêng những chip đó cho kỹ sư dịch vụ hiện trường.

Chúng tôi đã làm cho các chip có thể triển khai độc lập. Chúng tôi đã phát minh ra điều phối đa hình. Chúng tôi đã phát minh ra đối tượng.

Đây thực sự là một kiến trúc plugin. Chúng tôi cắm các chip vào hệ thống. Cuối cùng, chúng tôi thiết kế để có thể cài một tính năng vào sản phẩm bằng cách cắm chip chứa tính năng đó vào khe còn trống. Menu điều khiển tự động xuất hiện và phần liên kết với ứng dụng chính cũng được thiết lập tự động.

Dĩ nhiên, lúc đó chúng tôi chưa biết các nguyên tắc hướng đối tượng, cũng không biết gì về việc tách giao diện người dùng khỏi quy tắc nghiệp vụ. Nhưng những yếu tố căn bản đã có mặt, và chúng rất mạnh mẽ.

Một lợi ích bất ngờ khác là chúng tôi có thể vá firmware qua kết nối quay số. Nếu tìm thấy lỗi trong firmware, chúng tôi gọi đến thiết bị và dùng chương trình giám sát tích hợp để đổi vector RAM của chương trình con lỗi sang một vùng RAM trống. Sau đó, chúng tôi nhập chương trình con đã sửa vào vùng RAM đó bằng mã máy hệ thập lục phân.

Điều này giúp ích rất nhiều cho hoạt động dịch vụ hiện trường và khách hàng. Khi có vấn đề, họ không cần chờ chúng tôi gửi chip mới và xếp lịch một chuyến bảo trì khẩn cấp. Hệ thống có thể được vá ngay, còn chip mới được lắp trong lần bảo trì định kỳ tiếp theo.

## Máy tính khu vực dịch vụ

Máy tính khu vực dịch vụ (SAC) của 4-TEL dựa trên máy tính mini M365. Hệ thống này giao tiếp với tất cả COLT ngoài hiện trường, qua modem riêng hoặc modem quay số. Nó yêu cầu COLT đo đường dây điện thoại, nhận kết quả thô rồi phân tích phức tạp để xác định và định vị lỗi.

### Xác định nơi điều phối

Một nền tảng kinh tế của hệ thống là phân bổ đúng thợ sửa chữa. Theo quy định công đoàn, thợ được chia thành ba nhóm: thợ tổng đài trung tâm, thợ cáp và thợ đường dây thuê bao. Thợ tổng đài sửa lỗi bên trong tổng đài trung tâm. Thợ cáp sửa lỗi trên mạng cáp nối tổng đài với khách hàng. Thợ đường dây thuê bao sửa lỗi bên trong cơ sở khách hàng và trên đường dây nối cáp bên ngoài với cơ sở đó, tức đoạn “drop”.

Khi khách hàng báo sự cố, hệ thống chẩn đoán và xác định cần điều phối nhóm thợ nào. Điều này giúp công ty điện thoại tiết kiệm rất nhiều vì điều phối sai khiến khách hàng phải chờ và thợ phải đi lại vô ích.

Mã quyết định điều phối được thiết kế và viết bởi một người rất thông minh nhưng giao tiếp rất kém. Quá trình viết mã được mô tả là: “Ba tuần nhìn chằm chằm lên trần nhà, rồi hai ngày mã tuôn ra từ mọi lỗ trên người anh ấy, sau đó anh ấy nghỉ việc.”

Không ai hiểu mã đó. Mỗi lần thêm tính năng hoặc sửa lỗi, chúng tôi đều làm hỏng nó theo cách nào đó. Vì một trong những lợi ích kinh tế chính của hệ thống dựa trên mã này, mỗi lỗi mới đều khiến công ty vô cùng xấu hổ.

Cuối cùng, ban quản lý yêu cầu chúng tôi khóa chặt mã đó và không bao giờ sửa nữa. Mã chính thức trở nên cứng nhắc.

Trải nghiệm này khiến tôi hiểu giá trị của mã sạch, tốt.

### Kiến trúc

Hệ thống được viết năm 1976 bằng hợp dịch M365. Đó là một chương trình nguyên khối duy nhất, khoảng 60.000 dòng. Hệ điều hành do công ty tự viết, không có ưu tiên và chuyển tác vụ dựa trên polling. Chúng tôi gọi nó là MPS, viết tắt của hệ thống đa xử lý. Máy tính M365 không có stack tích hợp, nên biến riêng của từng tác vụ được lưu trong vùng nhớ đặc biệt rồi hoán đổi ra vào khi chuyển ngữ cảnh. Biến dùng chung được quản lý bằng khóa và semaphore. Vấn đề tái nhập và điều kiện tranh chấp xảy ra liên tục.

Không có sự cách ly giữa logic điều khiển thiết bị, giao diện người dùng và quy tắc nghiệp vụ. Chẳng hạn, mã điều khiển modem bị rải khắp phần lớn mã quy tắc nghiệp vụ và giao diện người dùng. Không ai cố gom nó thành mô-đun hay trừu tượng hóa giao diện. Modem được điều khiển ở mức bit bằng mã phân tán khắp hệ thống.

Điều tương tự cũng đúng với giao diện thiết bị đầu cuối. Mã điều khiển thông điệp và định dạng không được cách ly. Chúng rải khắp codebase 60.000 dòng.

Các mô-đun modem chúng tôi dùng được thiết kế để gắn trên bo mạch in. Chúng tôi mua thiết bị từ bên thứ ba rồi tích hợp với các mạch khác trên một bo mạch lắp vào backplane tùy chỉnh. Các mô-đun này đắt tiền. Vài năm sau, chúng tôi quyết định tự thiết kế modem. Chúng tôi trong nhóm phần mềm van nài kỹ sư phần cứng giữ nguyên các định dạng bit điều khiển modem cũ. Chúng tôi giải thích rằng mã điều khiển modem bị rải khắp nơi, và trong tương lai hệ thống phải hỗ trợ cả hai loại modem. Chúng tôi nài nỉ, thuyết phục: “Xin hãy làm cho modem mới trông giống modem cũ từ góc nhìn điều khiển phần mềm.”

Nhưng khi nhận modem mới, cấu trúc điều khiển hoàn toàn khác. Không chỉ khác một chút, mà khác hoàn toàn.

Cảm ơn nhé, kỹ sư phần cứng.

Chúng tôi phải làm gì? Chúng tôi không chỉ thay toàn bộ modem cũ bằng modem mới. Thay vào đó, chúng tôi kết hợp modem cũ và mới trong cùng hệ thống. Phần mềm phải xử lý đồng thời cả hai loại. Chúng tôi có buộc phải bao quanh mọi chỗ điều khiển modem bằng cờ và trường hợp đặc biệt không? Có hàng trăm chỗ như vậy!

Cuối cùng, chúng tôi chọn một giải pháp còn tệ hơn.
Một chương trình con cụ thể ghi dữ liệu lên bus giao tiếp nối tiếp dùng để điều khiển mọi thiết bị, kể cả modem. Chúng tôi sửa chương trình con đó để nhận diện các mẫu bit riêng của modem cũ rồi chuyển chúng thành mẫu bit mà modem mới cần.

Việc này không hề đơn giản. Lệnh modem gồm chuỗi thao tác ghi vào các địa chỉ IO khác nhau trên bus nối tiếp. Bản vá phải diễn giải tuần tự các lệnh đó rồi chuyển thành chuỗi khác, với địa chỉ IO, thời gian và vị trí bit khác.

Chúng tôi làm cho nó hoạt động được, nhưng đó là bản vá tệ nhất có thể tưởng tượng. Chính thất bại này giúp tôi hiểu giá trị của việc cách ly phần cứng khỏi quy tắc nghiệp vụ và trừu tượng hóa giao diện.

### Cuộc đại thiết kế lại trong mơ

Đến thập niên 1980, ý tưởng tự sản xuất máy tính mini và kiến trúc máy tính riêng dần lỗi thời. Trên thị trường có nhiều máy tính vi mô, rẻ và tiêu chuẩn hóa hơn việc tiếp tục dựa vào kiến trúc độc quyền từ cuối thập niên 1960. Cùng với kiến trúc tồi tệ của phần mềm SAC, điều đó khiến ban quản lý kỹ thuật bắt đầu tái kiến trúc toàn bộ hệ thống SAC.

Hệ thống mới sẽ được viết bằng C, dùng hệ điều hành UNIX trên đĩa và chạy trên máy vi tính Intel 8086. Nhóm phần cứng bắt đầu làm máy tính mới, còn một nhóm nhỏ lập trình viên, “Đội Hổ” (Tiger Team), được giao viết lại phần mềm.

Tôi sẽ không làm bạn chán với chi tiết về thất bại ban đầu. Chỉ cần nói rằng Đội Hổ đầu tiên thất bại hoàn toàn sau khi tiêu tốn hai hoặc ba năm công sức cho dự án phần mềm không tạo ra được sản phẩm nào.

Một hoặc hai năm sau, có lẽ vào năm 1982, họ khởi động lại quy trình. Mục tiêu là thiết kế lại toàn bộ SAC bằng C và UNIX trên phần cứng 80286 mới do chúng tôi tự thiết kế, rất mạnh mẽ. Chúng tôi gọi máy tính đó là “Deep Thought”.

Quá trình kéo dài nhiều năm, rồi thêm nhiều năm nữa. Tôi không biết SAC chạy UNIX đầu tiên cuối cùng được triển khai khi nào. Tôi nghĩ lúc đó tôi đã rời công ty, vào năm 1988. Thực tế, tôi không chắc nó có bao giờ được triển khai hay không.

Vì sao trì hoãn? Nói ngắn gọn, nhóm thiết kế lại rất khó bắt kịp đội ngũ lập trình viên lớn đang tích cực duy trì hệ thống cũ. Đây chỉ là một ví dụ về khó khăn họ gặp phải.

### Châu Âu

Gần thời điểm SAC được viết lại bằng C, công ty bắt đầu mở rộng doanh số sang châu Âu. Họ không thể chờ phần mềm thiết kế lại hoàn tất, nên tất nhiên đã triển khai hệ thống M365 cũ ở châu Âu.

Vấn đề là hệ thống điện thoại châu Âu rất khác hệ thống ở Hoa Kỳ. Cách tổ chức nghề nghiệp và bộ máy hành chính cũng khác. Vì vậy, một trong những lập trình viên giỏi nhất của chúng tôi được cử sang Vương quốc Anh để dẫn dắt nhóm phát triển địa phương, sửa đổi phần mềm SAC cho phù hợp với các vấn đề ở châu Âu.

Dĩ nhiên, không có nỗ lực nghiêm túc nào được thực hiện để tích hợp những thay đổi đó vào phần mềm ở Hoa Kỳ. Đây là thời kỳ trước khi mạng có thể truyền những codebase lớn qua đại dương. Các lập trình viên ở Anh chỉ đơn giản rẽ nhánh mã Hoa Kỳ và sửa theo nhu cầu.
Điều đó gây ra nhiều khó khăn. Ở cả hai bờ Đại Tây Dương đều phát hiện lỗi cần được sửa từ phía bên kia. Nhưng các mô-đun đã thay đổi đáng kể, nên rất khó xác định bản sửa ở Hoa Kỳ có hoạt động ở Anh hay không.
Sau vài năm đau đầu và khi đường truyền tốc độ cao nối văn phòng Hoa Kỳ với Anh được lắp đặt, một nỗ lực nghiêm túc đã được tiến hành để hợp nhất hai nhánh mã, biến khác biệt thành vấn đề cấu hình. Nỗ lực này thất bại trong cả ba lần thử. Hai codebase rất giống nhau, nhưng vẫn quá khác biệt để hợp nhất, nhất là trong môi trường thị trường thay đổi nhanh lúc đó.
Trong khi đó, “Đội Hổ”, đang cố viết lại mọi thứ bằng C và UNIX, nhận ra họ cũng phải xử lý sự khác biệt giữa châu Âu và Hoa Kỳ. Điều đó dĩ nhiên không đẩy nhanh tiến độ.

## Kết luận về SAC

Còn nhiều câu chuyện khác tôi có thể kể về hệ thống này, nhưng chúng quá chán nản để tiếp tục. Chỉ cần nói rằng nhiều bài học khó khăn nhất trong sự nghiệp phần mềm của tôi đến từ việc đắm mình trong mã hợp dịch kinh khủng của SAC.

## Ngôn ngữ C

Phần cứng máy tính 8085 mà chúng tôi dùng trong dự án 4-Tel Micro cung cấp nền tảng tính toán chi phí thấp cho nhiều dự án có thể nhúng vào môi trường công nghiệp. Chúng tôi có thể trang bị cho nó 32K RAM và thêm 32K ROM, cùng một cơ chế rất linh hoạt và mạnh mẽ để điều khiển thiết bị ngoại vi. Nhưng chúng tôi không có một ngôn ngữ linh hoạt và tiện dụng để lập trình máy. Viết mã bằng hợp dịch 8085 thật chẳng vui chút nào.

Hơn nữa, trình hợp dịch chúng tôi dùng do chính các lập trình viên trong công ty viết. Nó chạy trên máy M365, dùng hệ điều hành băng từ hộp được mô tả trong mục “Cắt laser”.

Số phận đã sắp đặt để kỹ sư phần cứng trưởng thuyết phục giám đốc điều hành rằng chúng tôi cần một máy tính thật. Ông ấy không thực sự biết sẽ dùng nó làm gì, nhưng có ảnh hưởng chính trị lớn. Vì vậy, chúng tôi mua một máy PDP-11/60.

Khi đó tôi chỉ là một lập trình viên phần mềm cấp thấp, nhưng vô cùng phấn khích. Tôi biết chính xác mình muốn làm gì với máy tính ấy. Tôi quyết tâm biến nó thành máy của mình.

Hướng dẫn sử dụng được gửi đến nhiều tháng trước khi máy giao. Tôi mang chúng về nhà đọc ngấu nghiến. Đến khi máy được giao, tôi đã hiểu rất sâu về cả phần cứng lẫn phần mềm, ít nhất là sâu nhất có thể nhờ tự học ở nhà.

Tôi tham gia soạn đơn đặt hàng. Đặc biệt, tôi chỉ định loại lưu trữ đĩa cho máy tính mới. Tôi quyết định mua hai ổ đĩa có thể dùng các bộ đĩa tháo rời, mỗi bộ chứa 25 megabyte.[^9]

Năm mươi megabyte! Con số ấy dường như vô tận! Tôi nhớ mình đi dọc hành lang văn phòng vào đêm khuya, cười khúc khích như Phù thủy Độc ác phương Tây: “Năm mươi megabyte! Hahahahahahahahahah!”

Tôi nhờ người quản lý cơ sở vật chất xây một căn phòng nhỏ có sáu thiết bị đầu cuối VT100. Tôi trang trí phòng bằng ảnh chụp ngoài không gian. Các nhà phát triển phần mềm sẽ dùng phòng này để viết và biên dịch mã.

Khi máy được giao, tôi mất vài ngày lắp đặt, nối dây cho các thiết bị đầu cuối và làm cho mọi thứ hoạt động. Đó là niềm vui, một công việc xuất phát từ đam mê.

Chúng tôi mua các trình hợp dịch chuẩn cho 8085 từ Boston Systems Office và chuyển mã 4-Tel Micro sang cú pháp đó. Chúng tôi xây dựng hệ thống biên dịch chéo cho phép tải các tệp nhị phân đã biên dịch từ PDP-11 xuống môi trường phát triển 8085 và thiết bị ghi ROM. Và thế là mọi thứ hoạt động ngon lành.

### C

Nhưng vấn đề hợp dịch 8085 vẫn còn đó, và tôi không hài lòng. Tôi nghe nói có một ngôn ngữ “mới” được dùng rộng rãi ở Bell Labs. Họ gọi nó là “C”. Vì vậy, tôi mua cuốn *The C Programming Language* của Kernighan và Ritchie. Giống như sách hướng dẫn PDP-11 vài tháng trước, tôi đọc ngấu nghiến cuốn này.

Tôi kinh ngạc trước vẻ thanh lịch giản dị của ngôn ngữ này. Nó không hy sinh sức mạnh nào của hợp dịch, nhưng cho phép truy cập sức mạnh đó bằng cú pháp tiện dụng hơn nhiều. Tôi hoàn toàn bị thuyết phục.

Tôi mua trình biên dịch C của Whitesmiths và cho chạy trên PDP-11. Đầu ra của trình biên dịch là cú pháp hợp dịch tương thích với trình biên dịch 8085 của Boston Systems Office. Nhờ vậy, chúng tôi có con đường từ C đến phần cứng 8085! Chúng tôi đã sẵn sàng.

Vấn đề duy nhất còn lại là thuyết phục nhóm lập trình viên nhúng vốn chỉ viết hợp dịch chuyển sang dùng C. Nhưng đó là một câu chuyện ác mộng để kể vào lúc khác…

### BOSS

Nền tảng 8085 của chúng tôi không có hệ điều hành. Trải nghiệm với hệ thống MPS trên M365 và cơ chế ngắt thô sơ của IBM System/7 khiến tôi tin rằng 8085 cần một bộ chuyển tác vụ đơn giản. Vì vậy, tôi nghĩ ra BOSS: Hệ điều hành và Bộ lập lịch Cơ bản (Basic Operating System and Scheduler).[^10]

Phần lớn BOSS được viết bằng C. Nó cho phép tạo các tác vụ đồng thời. Các tác vụ không bị ngắt ưu tiên. Việc chuyển tác vụ không dựa trên ngắt, mà giống hệ thống MPS trên M365, dựa trên cơ chế polling đơn giản. Polling xảy ra mỗi khi một tác vụ chờ sự kiện.

Lời gọi BOSS để tạm dừng một tác vụ như sau:

```c
block(eventCheckFunction);
```

Lời gọi này tạm dừng tác vụ hiện tại, đưa `eventCheckFunction` vào danh sách polling và gắn hàm đó với tác vụ vừa bị chặn. Sau đó, hệ thống chờ trong vòng lặp polling, gọi từng hàm trong danh sách cho đến khi một hàm trả về `true`. Tác vụ gắn với hàm đó sẽ được phép chạy.

Nói cách khác, như tôi đã nói, đó là một bộ chuyển tác vụ đơn giản, không có ưu tiên.

Phần mềm này trở thành nền tảng cho vô số dự án trong những năm tiếp theo. Một trong những dự án đầu tiên là pCCU.

### pCCU

Cuối thập niên 1970 và đầu thập niên 1980 là giai đoạn biến động đối với các công ty điện thoại. Một nguyên nhân là cuộc cách mạng số.

Trong suốt thế kỷ trước đó, tổng đài trung tâm kết nối với điện thoại khách hàng bằng một cặp dây đồng. Các dây được bó thành cáp trải rộng khắp vùng nông thôn. Có dây được treo trên cột, có dây được chôn dưới đất.

Đồng là kim loại quý, và công ty điện thoại có hàng tấn, đúng nghĩa là hàng tấn, dây đồng phủ khắp cả nước. Khoản đầu tư ban đầu khổng lồ đó có thể được thu hồi phần nào bằng cách truyền cuộc gọi qua kết nối số. Một cặp dây đồng có thể truyền hàng trăm cuộc gọi dưới dạng số.

Để đáp ứng xu hướng này, các công ty điện thoại bắt đầu thay thiết bị chuyển mạch trung tâm analog cũ bằng tổng đài số hiện đại.

Sản phẩm 4-Tel của chúng tôi kiểm tra dây đồng, chứ không phải kết nối số. Trong môi trường số vẫn có nhiều dây đồng, nhưng chúng ngắn hơn trước và nằm gần điện thoại khách hàng. Tín hiệu được truyền dưới dạng số từ tổng đài trung tâm đến điểm phân phối cục bộ, tại đó nó được chuyển lại thành tín hiệu analog rồi truyền đến khách hàng qua dây đồng thông thường. Điều đó có nghĩa thiết bị đo phải đặt ở nơi bắt đầu các dây đồng, còn thiết bị quay số phải ở lại tổng đài trung tâm. Vấn đề là mọi COLT gộp cả chức năng quay số lẫn đo lường trong cùng một thiết bị. Nếu nhận ra ranh giới kiến trúc hiển nhiên này sớm hơn vài năm, chúng tôi đã tiết kiệm được cả một gia tài!

Vì vậy, chúng tôi nghĩ ra kiến trúc sản phẩm mới: CCU/CMU, tức bộ điều khiển COLT và bộ đo COLT. CCU đặt tại tổng đài trung tâm và quay số đến các đường dây cần kiểm tra. CMU đặt tại điểm phân phối cục bộ và đo dây đồng dẫn đến điện thoại khách hàng.

Vấn đề là mỗi CCU phục vụ nhiều CMU. Thông tin cho biết cần dùng CMU nào với từng số điện thoại nằm trong tổng đài số. Vì vậy, CCU phải truy vấn tổng đài số để xác định cần giao tiếp và điều khiển CMU nào.

Chúng tôi hứa với các công ty điện thoại sẽ hoàn thành kiến trúc mới đúng thời điểm họ chuyển đổi. Chúng tôi biết họ còn cách nhiều tháng, thậm chí nhiều năm, nên không cảm thấy vội. Chúng tôi cũng biết cần vài năm công sức để phát triển phần cứng và phần mềm CCU/CMU mới.

#### Cái bẫy lịch trình

Thời gian trôi qua, chúng tôi luôn có việc khẩn cấp khiến phải hoãn phát triển kiến trúc CCU/CMU. Chúng tôi thấy an toàn khi hoãn vì các công ty điện thoại liên tục trì hoãn triển khai tổng đài số. Xem lịch trình của họ, chúng tôi tin chắc mình còn nhiều thời gian và liên tục hoãn dự án.

Rồi một ngày, sếp gọi tôi vào văn phòng và nói: “Một khách hàng sẽ triển khai tổng đài số vào tháng tới. Chúng ta phải có CCU/CMU hoạt động trước lúc đó.”

Tôi bàng hoàng! Làm sao có thể hoàn thành nhiều năm công sức phát triển chỉ trong một tháng? Nhưng sếp tôi đã có kế hoạch…

Thực tế, chúng tôi không cần kiến trúc CCU/CMU hoàn chỉnh. Công ty điện thoại triển khai tổng đài số rất nhỏ. Họ chỉ có một tổng đài trung tâm và hai điểm phân phối cục bộ. Quan trọng hơn, các điểm phân phối “cục bộ” đó không gần lắm. Chúng thực ra có các tổng đài analog thông thường, kết nối đến vài trăm khách hàng. Tốt hơn nữa, đó là loại tổng đài có thể được COLT thông thường quay số đến. Còn tốt hơn nữa, số điện thoại khách hàng chứa mọi thông tin cần thiết để quyết định dùng điểm phân phối nào. Nếu số điện thoại có chữ số 5, 6 hoặc 7 ở vị trí nhất định thì gọi đến điểm phân phối 1, nếu không thì gọi đến điểm phân phối 2.

Vì vậy, như sếp giải thích, chúng tôi thực ra không cần CCU/CMU. Điều cần thiết là một máy tính đơn giản ở tổng đài trung tâm, nối qua modem với hai COLT tiêu chuẩn tại các điểm phân phối. SAC giao tiếp với máy tính ở tổng đài trung tâm. Máy tính đó giải mã số điện thoại rồi chuyển lệnh quay số và đo lường đến COLT tại điểm phân phối thích hợp.

Thế là pCCU ra đời.

Đây là sản phẩm đầu tiên được triển khai cho khách hàng, viết bằng C và dùng BOSS. Tôi mất khoảng một tuần phát triển. Câu chuyện này không có ý nghĩa kiến trúc sâu sắc, nhưng là lời dẫn hay cho dự án tiếp theo.

### DLU/DRU

Đầu thập niên 1980, một trong các khách hàng của chúng tôi là công ty điện thoại ở Texas. Họ phải phục vụ một khu vực địa lý rộng lớn. Thực tế, khu vực đó rộng đến mức một vùng dịch vụ cần nhiều văn phòng khác nhau để điều phối thợ. Những văn phòng ấy có nhân viên kỹ thuật cần thiết bị đầu cuối kết nối đến SAC.

Có thể bạn nghĩ đây là vấn đề đơn giản, nhưng hãy nhớ câu chuyện xảy ra đầu thập niên 1980. Thiết bị đầu cuối từ xa không phổ biến. Tệ hơn nữa, phần cứng SAC giả định rằng mọi thiết bị đầu cuối đều ở gần. Thiết bị của chúng tôi nối với nhau bằng bus nối tiếp tốc độ cao độc quyền.

Chúng tôi có khả năng kết nối thiết bị đầu cuối từ xa, nhưng cách đó dựa trên modem, mà đầu thập niên 1980 modem thường chỉ đạt 300 bit mỗi giây. Khách hàng không hài lòng với tốc độ chậm đó.

Modem tốc độ cao có bán trên thị trường nhưng rất đắt, và cần đường truyền riêng “đã xử lý”. Chất lượng đường dây quay số chắc chắn không đủ tốt.

Khách hàng yêu cầu giải pháp. Chúng tôi đưa ra DLU/DRU.

DLU/DRU là viết tắt của “Display Local Unit” và “Display Remote Unit”, tức Bộ Hiển thị Cục bộ và Bộ Hiển thị Từ xa. DLU là bo máy tính cắm vào khung máy SAC và giả làm bo quản lý thiết bị đầu cuối. Tuy nhiên, thay vì điều khiển bus nối tiếp cho thiết bị cục bộ, nó nhận luồng ký tự rồi ghép kênh qua một đường modem riêng 9600 bps.

DRU là một hộp đặt tại địa điểm từ xa của khách hàng. Nó nối với đầu kia của đường 9600 bps và có phần cứng điều khiển các thiết bị đầu cuối cục bộ trên bus nối tiếp độc quyền. Nó tách kênh các ký tự nhận qua đường 9600 bps rồi gửi đến đúng thiết bị đầu cuối cục bộ.

Lạ thật phải không? Chúng tôi phải chế tạo một giải pháp mà ngày nay phổ biến đến mức chẳng ai nghĩ đến. Nhưng thời đó…

Chúng tôi còn phải tự phát minh giao thức truyền thông vì khi ấy các giao thức chuẩn không phải phần mềm chia sẻ mã nguồn mở. Thực tế, lúc đó chúng tôi chưa có bất kỳ kết nối Internet nào.

### Kiến trúc

Kiến trúc hệ thống này rất đơn giản, nhưng có vài điểm thú vị tôi muốn nêu. Trước hết, cả hai thiết bị đều dùng công nghệ 8085, được viết bằng C và dùng BOSS. Nhưng đó là điểm tương đồng duy nhất.

Dự án có hai người. Tôi là trưởng dự án, Mike Carew là cộng sự thân thiết. Tôi thiết kế và viết mã cho DLU; Mike phụ trách DRU.

Kiến trúc DLU dựa trên mô hình luồng dữ liệu. Mỗi tác vụ làm một việc nhỏ, tập trung, rồi truyền đầu ra sang tác vụ kế tiếp qua hàng đợi. Hãy nghĩ đến mô hình ống và bộ lọc trong UNIX. Kiến trúc khá phức tạp. Một tác vụ có thể ghi vào hàng đợi do nhiều tác vụ khác xử lý. Một số tác vụ khác ghi vào hàng đợi chỉ có một tác vụ xử lý.

Hãy nghĩ đến dây chuyền lắp ráp. Mỗi vị trí có một nhiệm vụ duy nhất, đơn giản và tập trung. Sau đó sản phẩm chuyển sang vị trí kế tiếp. Đôi khi dây chuyền tách thành nhiều nhánh, đôi khi các nhánh lại hợp nhất. Đó chính là DLU.

DRU của Mike dùng một cách tiếp cận khác hẳn. Anh ấy tạo một tác vụ cho mỗi thiết bị đầu cuối, rồi trong tác vụ đó thực hiện toàn bộ công việc cho thiết bị ấy. Không có hàng đợi. Không có luồng dữ liệu. Chỉ có nhiều tác vụ lớn giống nhau, mỗi tác vụ quản lý thiết bị đầu cuối riêng.

Cách này đối lập với dây chuyền lắp ráp. Ở đây, hình ảnh thích hợp là nhiều thợ lành nghề, mỗi người tự xây dựng toàn bộ sản phẩm.

Lúc đó tôi nghĩ kiến trúc của mình tốt hơn. Mike dĩ nhiên cho rằng cách của anh ấy tốt hơn. Chúng tôi có nhiều cuộc tranh luận vui vẻ về chuyện này. Cuối cùng, cả hai đều hoạt động khá tốt. Tôi nhận ra rằng kiến trúc phần mềm có thể rất khác nhau nhưng hiệu quả ngang nhau.

## VRS

Trong thập niên 1980, nhiều công nghệ mới liên tục xuất hiện. Một trong số đó là điều khiển bằng giọng nói qua máy tính.

Một tính năng của hệ thống 4-Tel là giúp thợ xác định vị trí lỗi trong cáp. Quy trình như sau:

- Nhân viên kiểm tra tại tổng đài trung tâm dùng hệ thống để ước lượng khoảng cách, tính bằng foot, đến vị trí lỗi. Độ chính xác khoảng 20%. Sau đó, nhân viên điều phối thợ sửa cáp đến một điểm tiếp cận gần vị trí đó.
- Khi đến nơi, thợ sửa cáp gọi cho nhân viên kiểm tra và đề nghị bắt đầu quy trình xác định lỗi. Nhân viên kích hoạt chức năng xác định lỗi của 4-Tel. Hệ thống bắt đầu đo đặc tính điện tử của đường dây hỏng và in thông báo trên màn hình, yêu cầu thực hiện một số thao tác như mở cáp hoặc nối tắt cáp.
- Nhân viên cho thợ biết hệ thống yêu cầu thao tác nào, còn thợ thông báo khi hoàn tất. Nhân viên báo lại cho hệ thống rồi hệ thống tiếp tục kiểm tra.
- Sau hai hoặc ba lượt trao đổi, hệ thống tính lại khoảng cách đến lỗi. Thợ sửa cáp lái xe đến vị trí mới rồi bắt đầu lại quy trình.

Hãy tưởng tượng sẽ tiện lợi thế nào nếu thợ sửa cáp đang trên cột điện hoặc đứng bên hộp đấu dây có thể tự điều khiển hệ thống. Đó chính xác là điều công nghệ giọng nói mới cho phép. Thợ sửa cáp có thể gọi trực tiếp vào hệ thống, điều khiển bằng phím bấm và nghe kết quả được đọc lại bằng giọng nói dễ chịu.

### Đặt tên

Công ty tổ chức một cuộc thi nhỏ để chọn tên hệ thống mới. Một trong những tên sáng tạo nhất là SAM CARP, viết tắt của “Still Another Manifestation of Capitalist Avarice Repressing the Proletariat” (Một biểu hiện nữa của lòng tham tư bản đàn áp giai cấp vô sản).

Dĩ nhiên tên đó không được chọn.

Một đề xuất khác là Teradyne Interactive Test System, cũng không được chọn.

Một đề xuất nữa là Service Area Test Access Network. Tên này cũng không được chọn.

Cuối cùng, cái tên chiến thắng là VRS, viết tắt của Voice Response System.

### Kiến trúc

Tôi không làm việc trên hệ thống này, nhưng đã nghe chuyện xảy ra. Câu chuyện tôi sắp kể là chuyện nghe lại từ người khác, nhưng phần lớn tôi tin là chính xác.

Đó là thời kỳ hứng khởi của máy tính vi mô, hệ điều hành UNIX, C và cơ sở dữ liệu SQL. Chúng tôi quyết tâm dùng tất cả.

Trong số nhiều nhà cung cấp cơ sở dữ liệu, cuối cùng chúng tôi chọn UNIFY. UNIFY chạy trên UNIX nên rất phù hợp với chúng tôi.

UNIFY cũng hỗ trợ công nghệ mới gọi là SQL nhúng. Công nghệ này cho phép nhúng câu lệnh SQL dưới dạng chuỗi trực tiếp vào mã C. Và chúng tôi đã làm vậy, ở khắp nơi.

Thật tuyệt khi có thể đặt SQL trực tiếp vào mã ở bất cứ đâu. Và chúng tôi muốn đặt ở đâu? Ở khắp mọi nơi! Vì vậy, SQL bị rải khắp thân mã.

Dĩ nhiên, thời đó SQL chưa phải tiêu chuẩn vững chắc. Mỗi nhà cung cấp có nhiều đặc điểm riêng. Vì vậy, các câu lệnh SQL riêng và lời gọi API đặc thù của UNIFY cũng bị rải khắp mã.

Cách này hoạt động rất tốt! Hệ thống thành công. Thợ sử dụng nó, công ty điện thoại yêu thích nó. Mọi người đều vui vẻ.

Rồi sản phẩm UNIFY chúng tôi dùng bị ngừng cung cấp.

Ôi. Ôi không.

Vì vậy, chúng tôi quyết định chuyển sang SyBase. Hay là Ingress nhỉ? Tôi không nhớ. Chỉ biết chúng tôi phải tìm trong toàn bộ mã C, tìm mọi câu SQL nhúng và lời gọi API riêng rồi thay bằng thao tác tương ứng của nhà cung cấp mới.

Sau khoảng ba tháng, chúng tôi bỏ cuộc. Không thể làm cho nó hoạt động. Chúng tôi phụ thuộc vào UNIFY chặt đến mức không có hy vọng thực tế nào tái cấu trúc mã với chi phí hợp lý.

Vì vậy, chúng tôi thuê một bên thứ ba bảo trì UNIFY theo hợp đồng. Dĩ nhiên, phí bảo trì tăng năm này qua năm khác.

## Kết luận về VRS

Đây là một trong những cách tôi hiểu rằng cơ sở dữ liệu là chi tiết cần được cách ly khỏi mục đích nghiệp vụ tổng thể của hệ thống. Đây cũng là một lý do khiến tôi không thích gắn kết chặt với hệ thống phần mềm bên thứ ba.

## Lễ tân điện tử

Năm 1983, công ty chúng tôi đứng ở giao điểm của hệ thống máy tính, viễn thông và thoại. Giám đốc điều hành nghĩ rằng đây có thể là vị trí thuận lợi để phát triển sản phẩm mới. Để thực hiện ý tưởng này, ông lập một nhóm ba người, trong đó có tôi, giao nhiệm vụ lên ý tưởng, thiết kế và triển khai sản phẩm mới cho công ty.

Chúng tôi nhanh chóng nghĩ ra Lễ tân Điện tử (ER).

Ý tưởng rất đơn giản. Khi bạn gọi đến một công ty, ER sẽ trả lời và hỏi bạn muốn nói chuyện với ai. Bạn dùng phím bấm để đánh vần tên người đó, rồi ER kết nối cuộc gọi. Người dùng ER có thể gọi vào hệ thống và dùng các lệnh đơn giản bằng phím bấm để cho biết số điện thoại có thể liên lạc với người cần tìm, ở bất kỳ đâu trên thế giới. Thực tế, hệ thống có thể lưu nhiều số thay thế.

Khi bạn gọi ER và nhập RMART, mã của tôi, ER sẽ gọi số đầu tiên trong danh sách. Nếu tôi không trả lời và xác nhận danh tính, hệ thống sẽ gọi số tiếp theo, rồi số nữa. Nếu vẫn không liên lạc được với tôi, ER sẽ ghi lại lời nhắn của người gọi.

Sau đó, ER định kỳ tìm cách liên lạc với tôi để chuyển lời nhắn đó cùng mọi lời nhắn khác người khác để lại.

Đây là hệ thống thư thoại đầu tiên trên thế giới, và chúng tôi nắm bằng sáng chế về nó.[^11]

Chúng tôi tự chế tạo toàn bộ phần cứng cho hệ thống này: bo máy tính, bo bộ nhớ, bo thoại/viễn thông và mọi thứ khác. Bo máy tính chính là Deep Thought, bộ xử lý Intel 80286 mà tôi đã nhắc đến trước đó.

Mỗi bo thoại hỗ trợ một đường dây điện thoại. Bo gồm giao diện điện thoại, bộ mã hóa/giải mã thoại, một ít bộ nhớ và máy tính vi mô Intel 80186.

Phần mềm cho bo máy tính chính được viết bằng C. Hệ điều hành là MP/M-86, một hệ điều hành đa xử lý, chạy trên đĩa và dùng dòng lệnh sơ khai. MP/M là phiên bản UNIX dành cho người ít tiền.

Phần mềm trên các bo thoại được viết bằng hợp dịch và không có hệ điều hành. Deep Thought giao tiếp với các bo thoại qua bộ nhớ dùng chung.

Ngày nay, kiến trúc của hệ thống này được gọi là hướng dịch vụ. Mỗi đường dây điện thoại được giám sát bởi một tiến trình lắng nghe chạy dưới MP/M. Khi có cuộc gọi, hệ thống khởi động tiến trình xử lý ban đầu rồi chuyển cuộc gọi cho nó. Khi cuộc gọi chuyển từ trạng thái này sang trạng thái khác, tiến trình xử lý thích hợp được khởi động và tiếp quản.

Thông điệp giữa các dịch vụ được truyền qua tệp trên đĩa. Dịch vụ đang chạy xác định dịch vụ kế tiếp, ghi thông tin trạng thái cần thiết vào tệp, chạy lệnh để khởi động dịch vụ đó rồi thoát.

Đây là lần đầu tôi xây dựng một hệ thống như vậy. Thực tế, đây cũng là lần đầu tôi làm kiến trúc sư chính cho toàn bộ sản phẩm. Mọi việc liên quan đến phần mềm đều do tôi làm, và hệ thống chạy rất tốt.

Tôi không nói kiến trúc này “sạch” theo nghĩa của cuốn sách này. Nó không phải kiến trúc plugin. Tuy nhiên, các dấu hiệu của ranh giới thực sự đã xuất hiện. Các dịch vụ có thể triển khai độc lập và nằm trong phạm vi trách nhiệm riêng. Có tiến trình cấp cao lẫn cấp thấp, và nhiều phụ thuộc đi đúng hướng.

## Sự sụp đổ của ER

Tiếc là việc tiếp thị sản phẩm này không thành công. Teradyne là công ty bán thiết bị kiểm thử. Chúng tôi không biết cách thâm nhập thị trường thiết bị văn phòng.

Sau nhiều lần thử trong hai năm, giám đốc điều hành bỏ cuộc và, thật đáng tiếc, rút đơn xin cấp bằng sáng chế. Bằng sáng chế thuộc về công ty đã nộp đơn chỉ ba tháng sau chúng tôi. Vì vậy, chúng tôi nhường toàn bộ thị trường thư thoại và chuyển tiếp cuộc gọi điện tử cho họ.

Đau thật!

Mặt khác, bạn không thể trách tôi vì những chiếc máy phiền phức giờ đang quấy nhiễu cuộc sống của chúng ta.

## Hệ thống điều phối thợ

ER thất bại như một sản phẩm, nhưng chúng tôi vẫn còn phần cứng và phần mềm để cải tiến các dòng sản phẩm hiện có. Hơn nữa, thành công tiếp thị của VRS thuyết phục chúng tôi rằng nên cung cấp hệ thống phản hồi bằng giọng nói để giao tiếp với thợ điện thoại, không phụ thuộc vào hệ thống kiểm thử.

Thế là CDS, Hệ thống Điều phối Thợ (Craft Dispatch System), ra đời. Về cơ bản, CDS là ER nhưng tập trung vào một miền rất hẹp: quản lý việc phân công thợ sửa điện thoại ngoài hiện trường.

Khi phát hiện sự cố trên đường dây điện thoại, trung tâm dịch vụ tạo phiếu báo lỗi. Các phiếu được lưu trong một hệ thống tự động. Khi thợ ngoài hiện trường hoàn thành công việc, họ gọi đến trung tâm dịch vụ để nhận nhiệm vụ tiếp theo. Nhân viên trung tâm mở phiếu kế tiếp và đọc nội dung cho thợ.

Chúng tôi tìm cách tự động hóa quy trình đó. Mục tiêu là để thợ ngoài hiện trường gọi vào CDS và yêu cầu nhiệm vụ tiếp theo. CDS sẽ truy vấn hệ thống phiếu báo lỗi và đọc kết quả. CDS theo dõi thợ nào được giao phiếu nào, rồi thông báo trạng thái sửa chữa cho hệ thống phiếu.

Hệ thống này có một số tính năng thú vị liên quan đến việc giao tiếp với hệ thống phiếu báo lỗi, hệ thống quản lý mạng lưới và các hệ thống kiểm thử tự động.

Trải nghiệm với kiến trúc hướng dịch vụ của ER khiến tôi muốn thử ý tưởng này mạnh tay hơn. Máy trạng thái của phiếu báo lỗi phức tạp hơn nhiều so với máy trạng thái xử lý cuộc gọi của ER. Tôi bắt đầu tạo thứ ngày nay được gọi là kiến trúc vi dịch vụ.

Mọi chuyển trạng thái trong bất kỳ cuộc gọi nào, dù nhỏ đến đâu, đều khiến hệ thống khởi động một dịch vụ mới. Thực tế, máy trạng thái được đưa ra ngoài thành một tệp văn bản để hệ thống đọc. Mỗi sự kiện đến từ đường dây điện thoại trở thành một chuyển trạng thái trong máy trạng thái hữu hạn đó. Tiến trình hiện tại khởi động tiến trình mới do máy trạng thái chỉ định để xử lý sự kiện, sau đó tiến trình hiện tại thoát hoặc chờ trong hàng đợi.

Máy trạng thái bên ngoài này cho phép thay đổi luồng ứng dụng mà không cần đổi mã, đúng theo Nguyên tắc Đóng-Mở. Chúng tôi có thể dễ dàng thêm dịch vụ mới, độc lập với mọi dịch vụ khác, rồi nối nó vào luồng bằng cách sửa tệp văn bản chứa máy trạng thái. Thậm chí có thể làm vậy khi hệ thống đang chạy. Nói cách khác, chúng tôi có khả năng hoán đổi nóng và một dạng ngôn ngữ thực thi quy trình nghiệp vụ hiệu quả.

Cách ER dùng tệp đĩa để giao tiếp giữa các dịch vụ quá chậm đối với việc chuyển dịch vụ nhanh hơn nhiều này. Vì vậy, chúng tôi phát minh ra cơ chế bộ nhớ dùng chung gọi là 3DBB.[^12] 3DBB cho phép truy cập dữ liệu theo tên. Các tên được dùng là tên gán cho từng thực thể máy trạng thái.

3DBB rất phù hợp để lưu chuỗi và hằng số, nhưng không thể chứa cấu trúc dữ liệu phức tạp. Lý do liên quan đến kỹ thuật nhưng dễ hiểu. Mỗi tiến trình trong MP/M chạy trong phân vùng bộ nhớ riêng. Con trỏ đến dữ liệu trong phân vùng này không có ý nghĩa trong phân vùng khác. Vì vậy, dữ liệu trong 3DBB không thể chứa con trỏ. Chuỗi thì được, nhưng cây, danh sách liên kết hay cấu trúc dữ liệu nào có con trỏ đều không dùng được.

Phiếu báo lỗi đến từ nhiều nguồn. Một số được tạo tự động, số khác do con người nhập. Nhân viên tạo phiếu thủ công khi trao đổi với khách hàng về sự cố. Khi khách hàng mô tả vấn đề, nhân viên nhập lời phàn nàn và quan sát vào một luồng văn bản có cấu trúc. Nội dung trông như sau:

```text
/pno 8475551212 /noise /dropped-calls
```

Bạn hiểu ý rồi đấy. Ký tự `/` bắt đầu một chủ đề mới. Sau dấu gạch chéo là mã, tiếp theo là các tham số. Có hàng nghìn mã, và một phiếu báo lỗi có thể chứa hàng chục mã trong phần mô tả. Tệ hơn, vì được nhập thủ công, chúng thường bị viết sai chính tả hoặc định dạng không đúng. Chúng dành cho con người diễn giải, không phải để máy tính xử lý.

Vấn đề của chúng tôi là giải mã các chuỗi nửa tự do này, diễn giải và sửa lỗi, rồi chuyển chúng thành giọng nói để đọc cho thợ đang đứng trên cột điện, nghe bằng ống nghe. Việc đó đòi hỏi, trong số những thứ khác, kỹ thuật phân tích cú pháp và biểu diễn dữ liệu rất linh hoạt. Dữ liệu còn phải truyền qua 3DBB, vốn chỉ xử lý được chuỗi.

Trên máy bay, giữa các chuyến thăm khách hàng, tôi nghĩ ra một lược đồ gọi là FLD, Dữ liệu Gắn nhãn Trường (Field Labeled Data). Ngày nay, ta gọi những thứ tương tự là XML hoặc JSON. Định dạng khác nhau, nhưng ý tưởng giống nhau. FLD là cây nhị phân liên kết tên với dữ liệu theo cấu trúc đệ quy. Có thể truy vấn FLD bằng API đơn giản và chuyển đổi qua lại với định dạng chuỗi tiện dụng, phù hợp với 3DBB.

Vậy là năm 1985 chúng tôi đã có vi dịch vụ giao tiếp qua cơ chế giống socket trong bộ nhớ dùng chung, sử dụng thứ tương tự XML.

Dưới ánh mặt trời chẳng có gì mới.

## Clear Communications

Năm 1988, một nhóm nhân viên Teradyne rời công ty để lập công ty khởi nghiệp Clear Communications. Vài tháng sau, tôi gia nhập họ. Nhiệm vụ của chúng tôi là viết phần mềm cho hệ thống giám sát chất lượng truyền thông của đường dây T1, các đường dây số dùng để truyền thông tin đường dài khắp đất nước. Tầm nhìn là một màn hình lớn có bản đồ Hoa Kỳ, các đường T1 chạy chằng chịt và nhấp nháy màu đỏ khi chất lượng suy giảm.

Hãy nhớ rằng giao diện đồ họa mới xuất hiện năm 1988. Apple Macintosh mới chỉ năm tuổi. Windows lúc đó là chuyện đùa. Nhưng Sun Microsystems đang sản xuất các máy trạm Sparc có giao diện X Window đáng tin cậy. Vì vậy, chúng tôi chọn Sun, đồng nghĩa với C và UNIX.

Đây là công ty khởi nghiệp. Chúng tôi làm việc 70 đến 80 giờ mỗi tuần. Chúng tôi có tầm nhìn, động lực, ý chí, năng lượng và chuyên môn. Chúng tôi có cổ phần. Chúng tôi mơ làm triệu phú. Chúng tôi đầy ảo tưởng.

Mã C tuôn ra từ mọi lỗ trên người chúng tôi. Chúng tôi nhét nó vào đây, đẩy nó vào kia. Chúng tôi xây những lâu đài trên không khổng lồ. Chúng tôi tạo tiến trình, hàng đợi thông điệp và kiến trúc hoành tráng. Chúng tôi tự viết toàn bộ ngăn xếp truyền thông ISO bảy lớp, đến tận lớp liên kết dữ liệu.

Chúng tôi viết mã giao diện đồ họa. MÃ GOOEY! Trời ơi! Chúng tôi viết mã GOOOOOEY.

Cá nhân tôi viết một hàm C dài 3.000 dòng tên là `gi()`, viết tắt của Graphic Interpreter. Đó là kiệt tác bầy nhầy. Tôi còn viết nhiều đoạn mã bầy nhầy khác ở Clear, nhưng đoạn này tai tiếng nhất.

Kiến trúc ư? Đùa à? Đây là công ty khởi nghiệp. Chúng tôi không có thời gian cho kiến trúc. Chỉ cần viết mã, chết tiệt! Viết mã để sống còn!

Vì vậy, chúng tôi viết mã. Rồi tiếp tục viết mã. Và lại viết mã. Nhưng sau ba năm, điều chúng tôi không làm được là bán hàng. Đúng là có một hoặc hai hệ thống được lắp đặt. Nhưng thị trường không mấy quan tâm đến tầm nhìn hoành tráng của chúng tôi, còn các nhà đầu tư mạo hiểm thì bắt đầu chán nản.

Lúc đó tôi ghét cuộc sống của mình. Tôi thấy mọi công sức và ước mơ sụp đổ. Tôi mâu thuẫn ở nơi làm việc, ở nhà vì công việc và với chính mình.

Rồi tôi nhận được một cuộc điện thoại làm thay đổi mọi thứ.

## Chuẩn bị

Hai năm trước cuộc điện thoại đó, có hai việc quan trọng xảy ra.

Thứ nhất, tôi thiết lập được kết nối UUCP đến một công ty gần đó. Công ty đó có kết nối UUCP đến một cơ sở khác nối với Internet. Tất nhiên, đây là những kết nối quay số. Máy Sparcstation chính, đặt trên bàn tôi, dùng modem 1200 bps để gọi máy chủ UUCP hai lần mỗi ngày. Nhờ vậy, chúng tôi có email và Netnews, một mạng xã hội sơ khai nơi mọi người thảo luận về các vấn đề thú vị.

Thứ hai, Sun phát hành trình biên dịch C++. Tôi đã quan tâm đến C++ và hướng đối tượng từ năm 1983, nhưng rất khó kiếm trình biên dịch. Khi có cơ hội, tôi lập tức đổi ngôn ngữ. Tôi bỏ lại các hàm C dài 3.000 dòng và bắt đầu viết C++ ở Clear. Rồi tôi học hỏi…

Tôi đọc sách. Dĩ nhiên tôi đọc *The C++ Programming Language* và *The Annotated C++ Reference Manual* (The ARM) của Bjarne Stroustrup. Tôi đọc cuốn sách tuyệt vời về thiết kế hướng trách nhiệm của Rebecca Wirfs-Brock, *Designing Object Oriented Software*. Tôi đọc *OOA and OOD and OOP* của Peter Coad. Tôi đọc *Smalltalk-80* của Adele Goldberg. Tôi đọc *Advanced C++ Programming Styles and Idioms* của James O. Coplien. Nhưng có lẽ quan trọng nhất là tôi đọc *Object Oriented Design with Applications* của Grady Booch.

Tên hay thật! Grady Booch. Làm sao quên được cái tên đó? Hơn nữa, ông là nhà khoa học trưởng ở một công ty tên Rational! Tôi cũng muốn làm nhà khoa học trưởng! Vì vậy, tôi đọc sách của ông, rồi học hỏi, học hỏi và tiếp tục học…

Trong khi học, tôi cũng bắt đầu tranh luận trên Netnews, giống cách mọi người tranh luận trên Facebook ngày nay. Các cuộc tranh luận của tôi xoay quanh C++ và hướng đối tượng. Suốt hai năm, tôi giải tỏa nỗi bực bội tích tụ ở nơi làm việc bằng cách tranh luận với hàng trăm người trên Usenet về tính năng ngôn ngữ và nguyên tắc thiết kế tốt nhất. Sau một thời gian, tôi bắt đầu nói được vài điều có lý.

Chính trong một cuộc tranh luận như vậy, nền tảng của các nguyên tắc SOLID đã được đặt ra.

Và mọi cuộc tranh luận đó, có lẽ cả một vài điều có lý, đã khiến người ta chú ý đến tôi…

## Uncle Bob

Một trong các kỹ sư ở Clear là chàng trai trẻ tên Billy Vogel. Billy đặt biệt danh cho mọi người. Anh gọi tôi là Uncle Bob. Dù tên tôi là Bob, tôi nghi rằng anh ấy đang ám chỉ J. R. “Bob” Dobbs (xem https://en.wikipedia.org/wiki/File:Bobdobbs.png).

Lúc đầu tôi mặc kệ. Nhưng qua nhiều tháng, việc anh liên tục nói “Uncle Bob… Uncle Bob” giữa áp lực và thất vọng của công ty khởi nghiệp bắt đầu khiến tôi phát chán.

Rồi một ngày, điện thoại reo.

## Cuộc điện thoại

Đó là một nhà tuyển dụng. Anh ta biết tên tôi vì có người nói tôi biết C++ và thiết kế hướng đối tượng. Tôi không chắc bằng cách nào, nhưng nghi rằng điều đó liên quan đến sự hiện diện của tôi trên Netnews.


Anh ta nói có một cơ hội ở Thung lũng Silicon, tại một công ty tên Rational. Họ cần người giúp xây dựng công cụ CASE.[^13]

Mặt tôi tái mét. Tôi biết đây là chuyện gì. Tôi không biết bằng cách nào mình biết, nhưng tôi biết. Đây là công ty của Grady Booch. Tôi thấy trước mắt cơ hội được hợp tác với Grady Booch!

## ROSE

Năm 1990, tôi gia nhập Rational với tư cách lập trình viên hợp đồng. Tôi làm việc trên sản phẩm ROSE, một công cụ cho phép lập trình viên vẽ sơ đồ Booch, những sơ đồ Grady đã viết về trong *Object-Oriented Analysis and Design with Applications* (Hình A.9 cho thấy một ví dụ).

**Hình A.9** Sơ đồ Booch

Ký pháp Booch rất mạnh mẽ. Nó báo trước những ký pháp như UML.

ROSE có một kiến trúc thực sự. Nó được cấu trúc thành các lớp đúng nghĩa, và phụ thuộc giữa các lớp được kiểm soát hợp lý. Kiến trúc giúp sản phẩm có thể phát hành, phát triển và triển khai độc lập.

Ồ, nó không hoàn hảo. Có nhiều nguyên tắc kiến trúc mà chúng tôi vẫn chưa hiểu. Chẳng hạn, chúng tôi không tạo được cấu trúc plugin thực sự.

Chúng tôi cũng mắc phải một trong những trào lưu đáng tiếc nhất thời đó, dùng cái gọi là cơ sở dữ liệu hướng đối tượng.

Nhưng nhìn chung, đây là trải nghiệm tuyệt vời. Tôi dành một năm rưỡi làm việc với nhóm Rational trên ROSE. Đây là một trong những trải nghiệm kích thích trí tuệ nhất trong sự nghiệp của tôi.

## Các cuộc tranh luận tiếp diễn

Dĩ nhiên, tôi không ngừng tranh luận trên Netnews. Thực tế, tôi tăng đáng kể hoạt động trên mạng. Tôi bắt đầu viết bài cho *C++ Report*. Với sự giúp đỡ của Grady, tôi bắt đầu viết cuốn sách đầu tiên: *Designing Object-Oriented C++ Applications Using the Booch Method*.

Có một điều khiến tôi bận tâm. Nghe kỳ quặc nhưng đúng là vậy: chẳng ai gọi tôi là “Uncle Bob” nữa. Tôi nhận ra mình nhớ cái tên đó. Vì vậy, tôi phạm sai lầm khi đưa “Uncle Bob” vào chữ ký email và Netnews. Cái tên ấy cứ thế gắn với tôi. Cuối cùng, tôi nhận ra đó là một thương hiệu khá tốt.

## ... Dù mang tên nào khác

ROSE là một ứng dụng C++ khổng lồ. Nó được cấu trúc thành các lớp, với một quy tắc phụ thuộc được thực thi nghiêm ngặt. Đó không phải Quy tắc Phụ thuộc tôi mô tả trong cuốn sách này. Chúng tôi không hướng phụ thuộc về phía chính sách cấp cao. Thay vào đó, chúng tôi hướng phụ thuộc theo hướng luồng điều khiển truyền thống hơn. Giao diện đồ họa phụ thuộc vào phần biểu diễn, phần biểu diễn phụ thuộc vào quy tắc thao tác, rồi quy tắc thao tác phụ thuộc vào cơ sở dữ liệu. Cuối cùng, việc không hướng phụ thuộc về phía chính sách đã góp phần khiến sản phẩm suy tàn.

Kiến trúc ROSE giống kiến trúc của một trình biên dịch tốt. Ký pháp đồ họa được “phân tích cú pháp” thành biểu diễn nội bộ; biểu diễn đó được xử lý bằng các quy tắc rồi lưu vào cơ sở dữ liệu hướng đối tượng.

Cơ sở dữ liệu hướng đối tượng là ý tưởng tương đối mới, khiến giới lập trình hướng đối tượng xôn xao về những hệ quả của nó. Lập trình viên hướng đối tượng nào cũng muốn dùng loại cơ sở dữ liệu này trong hệ thống của mình. Ý tưởng tương đối đơn giản và đầy lý tưởng: cơ sở dữ liệu lưu đối tượng chứ không lưu bảng. Cơ sở dữ liệu được cho là trông như RAM. Khi truy cập một đối tượng, nó tự xuất hiện trong bộ nhớ. Nếu đối tượng trỏ đến một đối tượng khác, đối tượng kia sẽ xuất hiện trong bộ nhớ ngay khi được truy cập. Cứ như phép thuật.

Cơ sở dữ liệu đó có lẽ là sai lầm thực tế lớn nhất của chúng tôi. Chúng tôi muốn có phép thuật, nhưng nhận được một framework bên thứ ba cồng kềnh, chậm, xâm nhập và đắt đỏ, khiến tiến độ của chúng tôi bị cản trở ở gần như mọi khía cạnh.

Đó không phải sai lầm duy nhất. Thực tế, sai lầm lớn nhất là thiết kế quá mức. Có nhiều lớp hơn những gì tôi mô tả ở đây, và mỗi lớp tạo thêm chi phí giao tiếp riêng. Điều đó làm năng suất của nhóm giảm đáng kể.

Sau nhiều năm công sức, vô số khó khăn và hai lần phát hành nguội nhạt, toàn bộ công cụ bị loại bỏ và thay bằng một ứng dụng nhỏ xinh do một nhóm nhỏ ở Wisconsin viết.

Và tôi học được rằng kiến trúc vĩ đại đôi khi dẫn đến thất bại lớn. Kiến trúc phải đủ linh hoạt để phù hợp với quy mô vấn đề. Thiết kế kiến trúc cấp doanh nghiệp trong khi thực sự chỉ cần một công cụ máy tính để bàn nhỏ xinh là công thức dẫn đến thất bại.

## Kỳ thi đăng ký kiến trúc sư

Đầu thập niên 1990, tôi trở thành chuyên gia tư vấn thực thụ. Tôi đi khắp thế giới dạy mọi người về khái niệm hướng đối tượng mới mẻ này. Công việc tư vấn của tôi tập trung mạnh vào thiết kế và kiến trúc của hệ thống hướng đối tượng.

Một trong những khách hàng tư vấn đầu tiên là Educational Testing Service (ETS). Tổ chức này ký hợp đồng với Hội đồng Quốc gia các Ban Đăng ký Kiến trúc sư (NCARB) để tổ chức kỳ thi đăng ký cho ứng viên kiến trúc sư mới.

Ai muốn trở thành kiến trúc sư được đăng ký hành nghề, tức người thiết kế công trình, ở Hoa Kỳ hoặc Canada đều phải vượt qua kỳ thi. Kỳ thi yêu cầu ứng viên giải quyết một số bài toán kiến trúc liên quan đến thiết kế công trình. Ứng viên có thể nhận yêu cầu thiết kế thư viện công cộng, nhà hàng hoặc nhà thờ, rồi được yêu cầu vẽ các sơ đồ kiến trúc thích hợp.

Kết quả được thu thập và lưu lại cho đến khi có thể tập hợp một nhóm kiến trúc sư cấp cao làm giám khảo chấm bài. Các buổi chấm bài này rất lớn, tốn kém và là nguồn gốc của nhiều sự mơ hồ, chậm trễ.

NCARB muốn tự động hóa quy trình: ứng viên làm bài trên máy tính, rồi một máy tính khác đánh giá và chấm điểm. NCARB yêu cầu ETS phát triển phần mềm, còn ETS thuê tôi tập hợp nhóm lập trình viên để xây dựng sản phẩm.

ETS chia bài toán thành 18 tình huống kiểm tra riêng biệt. Mỗi tình huống cần một ứng dụng giao diện đồ họa kiểu CAD để ứng viên trình bày lời giải. Một ứng dụng chấm điểm riêng sẽ nhận lời giải và tạo điểm số.

Cộng sự của tôi, Jim Newkirk, và tôi nhận ra 36 ứng dụng này có rất nhiều điểm chung. 18 ứng dụng giao diện đồ họa dùng các thao tác và cơ chế tương tự. 18 ứng dụng chấm điểm dùng cùng kỹ thuật toán học. Vì có những yếu tố dùng chung này, chúng tôi quyết tâm xây dựng một framework có thể tái sử dụng cho cả 36 ứng dụng. Chúng tôi còn bán ý tưởng này cho ETS bằng cách nói sẽ dành nhiều thời gian cho ứng dụng đầu tiên, nhưng sau đó những ứng dụng còn lại sẽ ra lò vài tuần một lần.

Đến đây có lẽ bạn đang đập tay lên trán hoặc gõ đầu vào cuốn sách. Những ai đủ lớn tuổi có thể nhớ lời hứa “tái sử dụng” của hướng đối tượng. Khi đó, chúng tôi đều tin rằng chỉ cần viết mã C++ hướng đối tượng sạch sẽ thì tự nhiên sẽ tạo ra thật nhiều mã có thể tái sử dụng.

Vì vậy, chúng tôi bắt tay viết ứng dụng đầu tiên, phức tạp nhất trong loạt này. Nó có tên Vignette Grande. Hai chúng tôi làm toàn thời gian trên Vignette Grande, đồng thời hướng đến việc tạo framework có thể tái sử dụng. Việc đó mất một năm. Cuối năm ấy, chúng tôi có 45.000 dòng mã framework và 6.000 dòng mã ứng dụng. Chúng tôi bàn giao sản phẩm cho ETS, rồi họ ký hợp đồng để chúng tôi viết thật nhanh 17 ứng dụng còn lại.

Jim và tôi tuyển thêm ba lập trình viên, rồi bắt đầu làm các tình huống kế tiếp.

Nhưng có chuyện không ổn. Framework có thể tái sử dụng mà chúng tôi tạo ra không thực sự dễ tái sử dụng. Nó không phù hợp với các ứng dụng mới. Có những ma sát tinh vi khiến mọi thứ không hoạt động.

Điều đó khiến chúng tôi nản lòng, nhưng tin rằng biết cách xử lý. Chúng tôi đến ETS và báo rằng dự án sẽ chậm tiến độ, framework 45.000 dòng cần được viết lại hoặc ít nhất điều chỉnh. Chúng tôi nói sẽ mất thêm thời gian.

Không cần nói cũng biết ETS không vui với tin này.

Thế là chúng tôi bắt đầu lại. Chúng tôi gác framework cũ sang một bên và bắt đầu viết đồng thời bốn tình huống mới. Chúng tôi mượn ý tưởng và mã từ framework cũ, nhưng sửa lại để phù hợp với cả bốn ứng dụng mà không cần thay đổi. Nỗ lực này mất thêm một năm. Kết quả là framework 45.000 dòng mới cùng bốn tình huống, mỗi ứng dụng dài khoảng 3.000 đến 6.000 dòng.

Không cần nói cũng biết quan hệ giữa ứng dụng giao diện đồ họa và framework tuân theo Quy tắc Phụ thuộc. Các tình huống là plugin của framework. Mọi chính sách giao diện đồ họa cấp cao đều nằm trong framework. Mã tình huống chỉ là keo kết nối.

Quan hệ giữa ứng dụng chấm điểm và framework phức tạp hơn một chút. Chính sách chấm điểm cấp cao nằm trong tình huống. Framework chấm điểm cắm vào tình huống đó.

Dĩ nhiên, cả hai ứng dụng đều được liên kết tĩnh thành chương trình C++, nên khi đó chúng tôi không hề nghĩ đến khái niệm plugin. Tuy nhiên, phụ thuộc vẫn tuân theo Quy tắc Phụ thuộc.

Sau khi bàn giao bốn ứng dụng đó, chúng tôi bắt đầu làm bốn ứng dụng tiếp theo. Lần này, chúng bắt đầu xuất hiện ở đầu ra cứ vài tuần một lần, đúng như dự đoán. Sự chậm trễ đã khiến lịch trình lùi gần một năm, nên chúng tôi tuyển thêm một lập trình viên để đẩy nhanh tiến độ.

Chúng tôi kịp thời hạn và hoàn thành cam kết. Khách hàng vui. Chúng tôi cũng vui. Mọi việc đều tốt đẹp.

Nhưng chúng tôi đã học được một bài học quan trọng: không thể tạo framework có thể tái sử dụng trước khi tạo framework có thể sử dụng được. Muốn framework có thể tái sử dụng, phải phát triển nó cùng với một số ứng dụng thực sự sử dụng lại nó.

## Kết luận

Như tôi đã nói từ đầu, phụ lục này phần nào mang tính tự truyện. Tôi đã nêu những điểm nổi bật trong các dự án mà tôi cho là có ảnh hưởng đến kiến trúc. Dĩ nhiên, tôi cũng kể vài sự việc không hoàn toàn liên quan đến nội dung kỹ thuật của cuốn sách nhưng vẫn đáng kể.

Đây chỉ là một phần lịch sử. Tôi đã tham gia nhiều dự án khác trong suốt những thập kỷ qua. Tôi cũng cố ý dừng câu chuyện ở đầu thập niên 1990 vì còn phải viết một cuốn sách khác về các sự kiện cuối thập niên 1990.

Hy vọng bạn thích chuyến đi ngắn qua ký ức của tôi và học được vài điều trên đường đi.

[^1]: Một câu chuyện chúng tôi nghe về chiếc máy đặc biệt ở ASC là nó được chở bằng xe tải bán rơ-moóc lớn cùng với đồ nội thất gia đình. Trên đường đi, xe đâm vào cầu ở tốc độ cao. Máy tính vẫn nguyên vẹn, nhưng trượt về phía trước và nghiền nát đồ đạc thành mảnh vụn.
[^2]: Ngày nay, ta sẽ nói nó có tần số xung nhịp 142 kHz.
[^3]: Hãy tưởng tượng khối lượng của chiếc đĩa và động năng của nó! Một ngày nọ, chúng tôi đến nơi và thấy mạt kim loại nhỏ rơi ra từ đáy tủ. Chúng tôi gọi nhân viên bảo trì. Ông khuyên tắt máy. Khi đến sửa, ông nói một vòng bi đã mòn. Rồi ông kể rằng nếu không sửa, những chiếc đĩa này có thể tuột khỏi trục, xuyên qua tường gạch bê tông và cắm vào ô tô trong bãi đỗ.
[^4]: Đèn hình tia âm cực: màn hình đơn sắc nền xanh, hiển thị ASCII.
[^5]: Con số 72 bắt nguồn từ thẻ đục lỗ Hollerith, mỗi thẻ có 80 ký tự. Tám ký tự cuối được “dành riêng” cho số thứ tự phòng khi bạn làm rơi bộ thẻ.
[^6]: Đúng, tôi hiểu đây là một cách diễn đạt tự mâu thuẫn.
[^7]: Chip có một cửa sổ nhựa trong nhỏ để nhìn thấy silicon bên trong, đồng thời cho tia cực tím đi vào xóa dữ liệu.
[^8]: Đúng, tôi biết khi phần mềm được ghi vào ROM thì nó được gọi là firmware, nhưng ngay cả firmware thực chất vẫn “mềm”.
[^9]: RKO7.
[^10]: Sau này tên này được đổi thành “Bob’s Only Successful Software”.
[^11]: Công ty chúng tôi nắm bằng sáng chế. Hợp đồng lao động quy định mọi phát minh thuộc về công ty. Sếp nói với tôi: “Anh bán nó cho chúng tôi với giá một đô la, mà chúng tôi còn chẳng trả anh đồng đô la đó.”
[^12]: Bảng đen ba chiều. Nếu sinh vào thập niên 1950, có lẽ bạn hiểu câu đùa này: Drizzle, Drazzle, Druzzle, Drone.
[^13]: Computer Aided Software Engineering.