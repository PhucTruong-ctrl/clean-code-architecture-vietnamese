# Chương 12: Các thành phần
![Minh họa](assets/illustrations/12-chuong-12-opener.png){w=180}

**Các thành phần (Components) là đơn vị triển khai (deployment).** Chúng là các thực thể nhỏ nhất có thể được triển khai như một phần của hệ thống. Trong Java, chúng là các tệp jar (jar files). Trong Ruby, chúng là các tệp gem (gem files). Trong .Net, chúng là các DLL. Trong các ngôn ngữ biên dịch, chúng là tập hợp các tệp nhị phân (binary files). Trong các ngôn ngữ thông dịch, chúng là tập hợp các tệp nguồn (source files). Trong tất cả các ngôn ngữ, chúng là đơn vị triển khai (granule of deployment).

Các thành phần có thể được liên kết (linked) lại với nhau thành một tệp thực thi đơn lẻ (single executable). Hoặc chúng có thể được gom lại thành một kho lưu trữ đơn lẻ, chẳng hạn như tệp .war. Hoặc chúng có thể được triển khai độc lập như các plugin được tải động (dynamically loaded plugins) riêng biệt, chẳng hạn như tệp .jar, .dll hoặc .exe. Dù chúng cuối cùng được triển khai như thế nào, các thành phần được thiết kế tốt luôn giữ khả năng triển khai độc lập (independently deployable) và, do đó, phát triển độc lập (independently developable).

## Lịch sử ngắn về các thành phần

Trong những năm đầu của phát triển phần mềm, các lập trình viên kiểm soát vị trí và bố cục bộ nhớ của chương trình. Một trong những dòng mã đầu tiên trong chương trình là câu lệnh origin (origin statement), khai báo địa chỉ mà chương trình sẽ được nạp vào.

Xét chương trình PDP-8 đơn giản sau. Nó bao gồm một thủ tục con (subroutine) tên GETSTR, nhập một chuỗi từ bàn phím và lưu vào một bộ đệm (buffer). Nó cũng có một chương trình kiểm thử đơn vị (unit test) nhỏ để chạy thử GETSTR.

```text
*200
TLS
START, CLA
TAD BUFR
JMS GETSTR
CLA
TAD BUFR
JMS PUTSTR
JMP START
BUFR, 3000
GETSTR, 0
DCA PTR
NXTCH, KSF
JMP -1
KRB
DCA I PTR
TAD I PTR
AND K177
ISZ PTR
TAD MCR
SZA
JMP NXTCH
K177, 177
MCR, -15
```

Lưu ý lệnh *200 ở đầu chương trình. Nó báo cho trình biên dịch tạo mã sẽ được nạp vào địa chỉ $200_8$.

Loại lập trình này là khái niệm xa lạ đối với hầu hết lập trình viên ngày nay. Họ hiếm khi phải nghĩ đến việc chương trình được nạp ở đâu trong bộ nhớ máy tính. Nhưng xưa kia, đây là một trong những quyết định đầu tiên lập trình viên phải làm. Vào những ngày ấy, chương trình **không thể tái định vị (relocatable)**.

Làm sao bạn truy cập hàm thư viện (library function) trong những ngày xưa ấy? Đoạn mã trước minh họa cách tiếp cận được dùng. Lập trình viên đưa mã nguồn của các hàm thư viện vào mã ứng dụng của mình, và biên dịch tất cả thành một chương trình đơn lẻ.[^1] Thư viện được giữ ở dạng nguồn, không phải nhị phân.

Vấn đề của cách này là, thời đó, thiết bị chậm và bộ nhớ đắt, do đó hạn chế. Trình biên dịch cần thực hiện nhiều lần đọc (passes) qua mã nguồn, nhưng bộ nhớ quá nhỏ để chứa toàn bộ mã nguồn. Do đó, trình biên dịch phải đọc mã nguồn nhiều lần bằng các thiết bị chậm.

Việc này mất nhiều thời gian, và thư viện hàm càng lớn, trình biên dịch càng lâu. Biên dịch một chương trình lớn có thể mất hàng giờ.

Để rút ngắn thời gian biên dịch, lập trình viên tách mã nguồn của thư viện hàm ra khỏi ứng dụng. Chúng biên dịch thư viện hàm riêng biệt và nạp nhị phân vào địa chỉ đã biết, ví dụ $2000_8$. Chúng tạo bảng ký hiệu (symbol table) cho thư viện hàm và biên dịch bảng đó cùng mã ứng dụng. Khi muốn chạy ứng dụng, chúng nạp thư viện hàm nhị phân[^2] rồi nạp ứng dụng. Bộ nhớ trông như bố cục trong **Hình 12.1**.

**Hình 12.1** Bố cục bộ nhớ sơ khai

Cách này chạy tốt miễn sao ứng dụng vừa trong khoảng địa chỉ $0000_8$ đến $1777_8$. Nhưng sớm thôi ứng dụng lớn vượt quá không gian dành cho chúng. Lúc đó lập trình viên phải chia ứng dụng thành hai đoạn địa chỉ (address segments), nhảy vòng qua thư viện hàm (**Hình 12.2**).

**Hình 12.2** Chia ứng dụng thành hai đoạn địa chỉ

Rõ ràng đây không phải tình trạng bền vững. Khi lập trình viên thêm hàm vào thư viện, nó vượt quá giới hạn, và họ phải cấp thêm không gian (ở ví dụ này, gần $7000_8$). Sự phân mảnh (fragmentation) chương trình và thư viện này buộc phải tiếp diễn khi bộ nhớ máy tính tăng lên.

Rõ ràng phải có giải pháp.

## Khả năng tái định vị

Giải pháp là **nhị phân có thể tái định vị (relocatable binaries)**. Ý tưởng đằng sau rất đơn giản. Trình biên dịch được thay đổi để xuất mã nhị phân có thể được di chuyển trong bộ nhớ bởi một nạp trình thông minh (smart loader). Nạp trình được báo nơi nạp mã tái định vị (relocatable). Mã tái định vị được gắn cờ (flags) báo cho nạp trình biết phần nào của dữ liệu nạp phải thay đổi để nạp tại địa chỉ đã chọn. Thường chỉ nghĩa là cộng địa chỉ bắt đầu vào bất kỳ địa chỉ tham chiếu bộ nhớ nào trong nhị phân.

Bây giờ lập trình viên có thể bảo nạp trình nạp thư viện hàm ở đâu, và nạp ứng dụng ở đâu. Thực tế, nạp trình chấp nhận nhiều đầu vào nhị phân và chỉ việc nạp chúng vào bộ nhớ lần lượt, tái định vị (relocate) chúng trong khi nạp. Điều này cho phép lập trình viên chỉ nạp những hàm họ cần.

Trình biên dịch cũng được thay đổi để phát ra tên hàm dưới dạng siêu dữ liệu (metadata) trong nhị phân tái định vị. Nếu chương trình gọi hàm thư viện, trình biên dịch phát ra tên đó như một tham chiếu ngoài (external reference). Nếu chương trình định nghĩa hàm thư viện, trình biên dịch phát ra tên đó như một định nghĩa ngoài (external definition). Sau đó nạp trình có thể liên kết (link) các tham chiếu ngoài đến các định nghĩa ngoài khi nó đã xác định được các định nghĩa đó được nạp ở đâu.

Và **trình nạp liên kết (linking loader)** ra đời.

## Các trình liên kết

Trình nạp liên kết cho phép lập trình viên chia chương trình thành các đoạn (segments) có thể biên dịch và nạp riêng biệt. Cách này chạy tốt khi các chương trình tương đối nhỏ được liên kết với thư viện nhỏ. Tuy nhiên, cuối những năm 1960 và đầu 1970, lập trình viên có tham vọng lớn hơn, và chương trình của họ lớn hơn rất nhiều.

Cuối cùng, các trình nạp liên kết (linking loaders) quá chậm để chịu đựng. Thư viện hàm lưu trên thiết bị chậm như băng từ (magnetic tape). Ngay cả đĩa, thời đó, cũng khá chậm. Dùng những thiết bị chậm này, trình nạp liên kết phải đọc chục, nếu không phải hàng trăm, thư viện nhị phân để giải quyết tham chiếu ngoài. Khi chương trình càng lớn, và nhiều hàm thư viện tích lũy hơn, một trình nạp liên kết có thể mất hơn một giờ chỉ để nạp chương trình.

Cuối cùng, việc nạp (loading) và liên kết (linking) được tách thành hai giai đoạn. Lập trình viên lấy phần chậm, phần làm việc liên kết, và đưa vào một ứng dụng riêng gọi là **trình liên kết (linker)**. Đầu ra của trình liên kết là một tệp nhị phân tái định vị đã liên kết (linked relocatable) mà một trình nạp tái định vị (relocating loader) có thể nạp rất nhanh. Điều này cho phép lập trình viên chuẩn bị một tệp thực thi (executable) dùng trình liên kết chậm, nhưng sau đó nạp nó nhanh chóng, bất kỳ lúc nào.

Rồi đến những năm 1980. Lập trình viên làm việc với C hoặc ngôn ngữ bậc cao khác. Khi tham vọng tăng, chương trình cũng lớn theo. Chương trình hàng trăm nghìn dòng mã không hiếm.

Các mô-đun nguồn (source modules) được biên dịch từ tệp .c thành tệp .o, rồi đưa vào trình liên kết để tạo tệp thực thi có thể nạp nhanh. Biên dịch từng mô-đun riêng lẻ khá nhanh, nhưng biên dịch tất cả mất chút thời gian. Trình liên kết lại mất thêm thời gian. Chu kỳ hoàn tất (turnaround) lại tăng lên một giờ trở lên trong nhiều trường hợp.

Dường như lập trình viên bị định mệnh phải đua đuôi mình vô tận. Trong suốt những năm 1960, 1970 và 1980, mọi thay đổi làm tăng tốc quy trình đều bị bác bỏ bởi tham vọng của lập trình viên, và kích thước chương trình họ viết. Họ không thể thoát khỏi chu kỳ hoàn tất một giờ. Thời gian nạp vẫn nhanh, nhưng thời gian biên dịch-liên kết (compile-link) là nút cổ chai (bottleneck).

Chúng ta đang trải qua **luật Murphy về kích thước chương trình**:

> Chương trình sẽ lớn lên để lấp đầy toàn bộ thời gian biên dịch và liên kết có sẵn.

Nhưng Murphy không phải là đối thủ duy nhất. Moore[^3] xuất hiện, và cuối những năm 1980, hai "đấu" nhau. Moore thắng. Đĩa bắt đầu thu nhỏ và nhanh hơn đáng kể. Bộ nhớ máy tính rẻ đến mức dữ liệu trên đĩa phần lớn có thể cache trong RAM. Tần số nhịp máy tăng từ 1 MHz lên 100 MHz.

Đến giữa những năm 1990, thời gian liên kết bắt đầu giảm nhanh hơn tham vọng làm chương trình lớn. Trong nhiều trường hợp, thời gian liên kết giảm đến vài giây. Đối với tác vụ nhỏ, ý tưởng trình nạp liên kết (linking loader) lại trở nên khả thi.

Đây là kỷ nguyên của Active-X, thư viện chia sẻ (shared libraries), và khởi đầu của tệp .jar. Máy tính và thiết bị nhanh đến mức ta có thể, một lần nữa, làm liên kết tại thời điểm nạp (load time). Ta có thể liên kết vài tệp .jar, hoặc vài thư viện chia sẻ, trong vài giây, và chạy chương trình kết quả. Và như vậy **kiến trúc plugin thành phần (component plugin architecture)** ra đời.

Ngày nay chúng ta thường xuyên phân phối tệp .jar, DLL, hoặc thư viện chia sẻ như plugin cho ứng dụng hiện có. Nếu bạn muốn tạo mod cho Minecraft, ví dụ, bạn chỉ cần đưa tệp .jar tùy chỉnh vào thư mục nhất định. Nếu bạn muốn gắn Resharper vào Visual Studio, bạn chỉ cần đưa các DLL thích hợp.

## Kết luận

Những tệp liên kết động (dynamically linked files) này, có thể gắn kết nhau tại thời điểm chạy (runtime), chính là các thành phần phần mềm (software components) của kiến trúc chúng ta. Đã mất 50 năm, nhưng chúng ta đã đến nơi mà kiến trúc plugin thành phần có thể là lựa chọn mặc định thông thường (casual default), thay vì nỗ lực vĩ đại (herculean effort) như xưa.

[^1]: Người tuyển dụng đầu tiên của tôi giữ vài chục bộ bài (decks) mã nguồn thư viện thủ tục con trên kệ. Khi bạn viết chương trình mới, bạn chỉ cần lấy một trong những bộ bài đó và gắn nó vào cuối bộ bài của mình.

[^2]: Thực tế, hầu hết những máy cũ dùng bộ nhớ lõi (core memory), không bị xóa khi tắt máy. Chúng ta thường để thư viện hàm nạp sẵn hàng ngày liền.

[^3]: Định luật Moore: Tốc độ máy tính, bộ nhớ, và mật độ gấp đôi mỗi 18 tháng. Định luật này đúng từ những năm 1950 đến 2000, nhưng sau đó, ít nhất đối với tần số nhịp, dừng hẳn.