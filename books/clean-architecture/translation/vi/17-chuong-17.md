# Chương 17: Ranh giới: Vạch đường phân cách
![Minh họa](assets/illustrations/17-chuong-17-opener.png){w=300}

## Hai câu chuyện buồn

Đây là câu chuyện buồn về công ty P, lời cảnh báo cho việc ra quyết định quá sớm. Trong những năm 1980, những người sáng lập P viết một ứng dụng desktop nguyên khối đơn giản. Sản phẩm thành công vang dội và trong thập niên 1990 phát triển thành một ứng dụng desktop GUI phổ biến.

Nhưng rồi, vào cuối những năm 1990, web nổi lên như một thế lực. Bỗng nhiên, ai cũng cần giải pháp web, và P cũng không ngoại lệ. Khách hàng của P đòi hỏi một phiên bản sản phẩm trên web. Để đáp ứng nhu cầu này, công ty tuyển một nhóm lập trình viên Java tài năng ở độ tuổi đôi mươi, rồi bắt đầu dự án chuyển sản phẩm sang web.

Những anh chàng Java có giấc mơ về các trang trại máy chủ, nên họ áp dụng một "kiến trúc" ba tầng phức tạp[^1] mà họ có thể phân phối qua các trang trại đó. Sẽ có máy chủ cho GUI, máy chủ cho middleware, và máy chủ cho cơ sở dữ liệu. Tất nhiên.

Các lập trình viên quyết định từ rất sớm rằng mỗi đối tượng miền sẽ có ba bản thể hiện (instances): một ở tầng GUI, một ở tầng middleware và một ở tầng cơ sở dữ liệu. Vì các bản thể hiện đó chạy trên những máy khác nhau, họ xây dựng một cơ chế giao tiếp phức tạp giữa các bộ xử lý và các tầng. Các lời gọi phương thức giữa các tầng được chuyển thành đối tượng, tuần tự hóa (serialized) rồi tổ chức truyền (marshaled) qua mạng.

Bây giờ hãy tưởng tượng việc triển khai một tính năng đơn giản như thêm một trường mới vào một bản ghi hiện có tốn bao nhiêu công sức. Trường đó phải được thêm vào các lớp ở cả ba tầng, và vào một vài thông điệp liên tầng. Vì dữ liệu di chuyển theo cả hai hướng, bốn giao thức thông điệp cần được thiết kế. Mỗi giao thức có một phía gửi và một phía nhận, do đó cần tám trình xử lý giao thức. Ba file thực thi phải được build, mỗi file có ba đối tượng nghiệp vụ cập nhật, bốn thông điệp mới, và tám trình xử lý mới.

Và hãy nghĩ xem những file thực thi đó phải làm gì để triển khai đơn giản nhất các tính năng. Hãy nghĩ đến tất cả các lần khởi tạo đối tượng, tất cả các lần tuần tự hóa, tất cả các lần tổ chức truyền và giải mã (de-marshaling), tất cả việc xây dựng và phân tích thông điệp, tất cả giao tiếp socket, trình quản lý timeout, kịch bản thử lại (retry scenarios), và tất cả những công việc phụ trợ khác mà bạn phải làm chỉ để hoàn thành một việc đơn giản.

Tất nhiên, trong quá trình phát triển, các lập trình viên không có trang trại máy chủ. Thực tế, họ chỉ chạy ba file thực thi đó trong ba tiến trình khác nhau trên một máy đơn lẻ. Họ phát triển theo cách này trong vài năm. Nhưng họ tin rằng kiến trúc của mình là đúng. Vì vậy, dù họ đang chạy trên một máy đơn lẻ, họ vẫn tiếp tục tất cả các lần khởi tạo đối tượng, tất cả các lần tuần tự hóa, tất cả các lần tổ chức truyền và giải mã, tất cả việc xây dựng và phân tích thông điệp, tất cả giao tiếp socket, và tất cả những thứ rườm rà khác trong một máy đơn lẻ.

Điều trớ trêu là công ty P chưa bao giờ bán một hệ thống cần trang trại máy chủ. Mọi hệ thống họ triển khai đều chạy trên một máy chủ duy nhất. Dù vậy, cả ba chương trình thực thi trong hệ thống ấy vẫn thực hiện mọi thao tác khởi tạo đối tượng, tuần tự hóa, tổ chức truyền và giải mã, tạo và phân tích thông điệp, giao tiếp qua socket cùng vô số công việc phụ trợ khác, chỉ để chờ một trang trại máy chủ chưa từng tồn tại và sẽ chẳng bao giờ xuất hiện.

Bi kịch là các kiến trúc sư, bằng cách ra một quyết định quá sớm, đã làm tăng nỗ lực phát triển lên gấp nhiều lần.

Câu chuyện của P không phải là trường hợp độc lập. Tôi đã thấy nó nhiều lần ở nhiều nơi. Thực ra, P là sự chồng chéo (superposition) của tất cả những nơi đó.

Nhưng có số phận tồi tệ hơn P.

Hãy xét W, một doanh nghiệp địa phương quản lý đội xe. Gần đây, họ tuyển một “kiến trúc sư” để kiểm soát nỗ lực phát triển phần mềm vốn đang rối ren. Và anh ta đúng là người thích kiểm soát. Anh ta nhanh chóng kết luận rằng doanh nghiệp nhỏ này cần một kiến trúc hướng dịch vụ (SoA) toàn diện ở cấp doanh nghiệp. Anh ta xây dựng mô hình miền khổng lồ cho mọi “đối tượng” trong doanh nghiệp, thiết kế một bộ dịch vụ quản lý chúng, rồi đẩy các lập trình viên vào một cơn ác mộng. Chẳng hạn, muốn thêm tên, địa chỉ và số điện thoại của một người liên hệ vào bản ghi bán hàng, bạn phải truy vấn `ServiceRegistry` để lấy ID dịch vụ `ContactService`. Sau đó, bạn gửi thông điệp `CreateContact` đến `ContactService`. Thông điệp này có hàng chục trường, mỗi trường phải chứa dữ liệu hợp lệ, nhưng lập trình viên không có những dữ liệu đó, vì họ chỉ biết tên, địa chỉ và số điện thoại. Sau khi tự bịa dữ liệu, lập trình viên phải chèn ID của người liên hệ mới vào bản ghi bán hàng rồi gửi thông điệp `UpdateContact` đến `SaleRecordService`.
Tất nhiên, để kiểm thử bất kỳ chức năng nào, bạn phải lần lượt khởi động mọi dịch vụ cần thiết, rồi khởi động message bus và máy chủ BPEL. Sau đó còn phải chờ thông điệp truyền từ dịch vụ này sang dịch vụ khác và nằm trong hết hàng đợi này đến hàng đợi kia.

Và rồi nếu bạn muốn thêm một tính năng mới, bạn có thể tưởng tượng được sự kết dính giữa tất cả những dịch vụ đó, và khối lượng WSDL khổng lồ cần thay đổi, và tất cả các lần triển khai lại mà những thay đổi đó bắt buộc …

Địa ngục bắt đầu trông như một nơi dễ chịu so với cái này.

Không có gì sai về bản chất của một hệ thống phần mềm được tổ chức quanh các dịch vụ. Sai lầm ở W là triển khai và áp đặt quá sớm một bộ công cụ hứa hẹn SoA, tức là quá sớm dựng lên cả một hệ thống dịch vụ đồ sộ cho các đối tượng miền. Cái giá phải trả chỉ là giờ công, rất nhiều giờ công, bị ném vào hố đen SoA.

Tôi có thể tiếp tục liệt kê thất bại kiến trúc này mãi. Nhưng hãy nói về một thành công kiến trúc nào.

## FitNesse

Con trai tôi, Micah, và tôi bắt đầu làm việc trên FitNesse vào năm 2001. Ý tưởng là tạo một wiki đơn giản bao bọc công cụ FIT của Ward Cunningham để viết các kiểm thử chấp nhận.

Đây là những ngày trước khi Maven "giải quyết" vấn đề file jar. Tôi kiên quyết rằng bất cứ thứ gì chúng tôi tạo ra không nên yêu cầu người dùng tải xuống hơn một file jar. Tôi gọi quy tắc này là "Tải về và Chạy" (Download and Go). Quy tắc này chi phối nhiều quyết định của chúng tôi.

Một trong những quyết định đầu tiên là viết máy chủ web của chính chúng tôi, chuyên biệt cho nhu cầu của FitNesse. Điều này nghe có vẻ ngớ ngẩn. Ngay cả năm 2001 đã có nhiều máy chủ web mã nguồn mở chúng tôi có thể dùng. Tuy nhiên, viết máy chủ của riêng mình kết quả là một quyết định thực sự tốt vì một máy chủ web cơ bản là một phần mềm rất đơn giản để viết và nó cho phép chúng tôi hoãn quyết định về framework web đến muộn hơn nhiều[^2].

Một quyết định sớm khác là tránh nghĩ về cơ sở dữ liệu. Chúng tôi vẫn nghĩ đến MySQL, nhưng chúng tôi cố ý trì hoãn quyết định đó bằng cách dùng một thiết kế khiến quyết định trở nên vô nghĩa. Thiết kế đó đơn giản là đặt một giao diện (interface) giữa tất cả các truy cập dữ liệu và kho dữ liệu (repository) chính nó.

Chúng tôi đặt các phương thức truy cập dữ liệu vào một giao diện tên là `WikiPage`. Những phương thức đó cung cấp tất cả chức năng chúng tôi cần để tìm, tải, và lưu các trang. Tất nhiên, chúng tôi không triển khai các phương thức đó ngay; chúng tôi chỉ để các phương thức đó ở trạng thái stub trong khi làm việc trên các tính năng không liên quan đến tải và lưu dữ liệu.

Thực tế, trong ba tháng chúng tôi chỉ làm việc dịch văn bản wiki sang HTML. Điều này không yêu cầu bất kỳ loại lưu trữ dữ liệu nào, nên chúng tôi tạo một lớp tên là `MockWikiPage` chỉ để các phương thức truy cập dữ liệu ở trạng thái stub.

Cuối cùng, những stub đó trở nên không đủ cho các tính năng chúng tôi muốn viết. Chúng tôi cần truy cập dữ liệu thật, không phải stub. Vì vậy chúng tôi tạo một lớp dẫn xuất mới của `WikiPage` tên là `InMemoryPage`. Lớp dẫn xuất này triển khai phương thức truy cập dữ liệu để quản lý một bảng băm (hash table) các trang wiki, được giữ trong RAM.

Điều này cho phép chúng tôi viết tính năng theo tính năng suốt một năm trời. Thực tế, chúng tôi làm chạy được toàn bộ phiên bản đầu tiên của chương trình FitNesse theo cách này. Chúng tôi có thể tạo trang, liên kết đến trang khác, làm tất cả định dạng wiki phức tạp, thậm chí chạy kiểm thử với FIT. Điều chúng tôi không làm được là lưu bất kỳ công việc nào.

Khi đến lúc triển khai tính năng lưu trữ (persistence), chúng tôi lại nghĩ đến MySQL, nhưng quyết định rằng không cần thiết trong ngắn hạn, vì viết bảng băm ra file phẳng (flat file) sẽ rất dễ dàng. Vì vậy chúng tôi triển khai `FileSystemWikiPage`, chỉ chuyển chức năng ra file phẳng, và tiếp tục phát triển thêm tính năng. Ba tháng sau, chúng tôi kết luận giải pháp file phẳng đủ tốt; quyết định bỏ qua ý định MySQL hoàn toàn. Chúng tôi hoãn quyết định đó đến mức nó biến mất và không bao giờ nhìn lại.

Câu chuyện sẽ kết thúc ở đây nếu không có một khách hàng quyết định anh ta cần đưa wiki vào MySQL cho mục đích riêng. Chúng tôi chỉ cho anh ta kiến trúc `WikiPage` đã cho phép chúng tôi trì hoãn quyết định. Anh ta quay lại một ngày sau với toàn bộ hệ thống chạy trên MySQL. Anh ta chỉ viết một lớp dẫn xuất `MySqlWikiPage` và làm cho nó chạy.

Chúng tôi từng gói tùy chọn đó cùng FitNesse, nhưng không ai khác dùng nó, nên cuối cùng chúng tôi bỏ nó. Ngay cả khách hàng viết lớp dẫn xuất cuối cùng cũng bỏ nó.

Sớm trong quá trình phát triển FitNesse, chúng tôi vạch một đường ranh giới giữa quy tắc nghiệp vụ và cơ sở dữ liệu. Đường đó ngăn cản quy tắc nghiệp vụ biết bất cứ điều gì về cơ sở dữ liệu, trừ các phương thức truy cập dữ liệu đơn giản. Quyết định đó cho phép chúng tôi trì hoãn lựa chọn và triển khai cơ sở dữ liệu được hơn một năm. Nó cho phép chúng tôi thử tùy chọn hệ thống file, và cho phép chúng tôi đổi hướng khi thấy giải pháp tốt hơn. Tuy nhiên nó không cản trở, hay thậm chí làm chậm, việc di chuyển theo hướng ban đầu (MySQL) khi ai đó muốn.

Việc không có cơ sở dữ liệu chạy trong 18 tháng phát triển có nghĩa là, trong 18 tháng, chúng tôi không có vấn đề schema, vấn đề truy vấn, vấn đề máy chủ cơ sở dữ liệu, vấn đề mật khẩu, vấn đề thời gian kết nối, và tất cả những vấn đề xấu xí khác xuất hiện khi bạn khởi động một cơ sở dữ liệu. Nó cũng có nghĩa là tất cả kiểm thử của chúng tôi chạy nhanh, vì không có cơ sở dữ liệu làm chậm chúng.

Tóm lại, vạch các đường ranh giới giúp chúng tôi trì hoãn và hoãn các quyết định, và cuối cùng nó giúp chúng tôi tiết kiệm một lượng lớn thời gian và đau đầu. Và đó chính là những gì một kiến trúc tốt nên làm.

## Vạch những đường nào, và vạch khi nào?

Bạn vạch đường giữa những thứ quan trọng và những thứ không quan trọng. GUI không quan trọng đối với quy tắc nghiệp vụ, nên có một đường ranh giới giữa chúng. Cơ sở dữ liệu không quan trọng đối với GUI, nên có một đường ranh giới giữa chúng. Cơ sở dữ liệu không quan trọng đối với quy tắc nghiệp vụ, nên có một đường ranh giới giữa chúng.

Một số bạn có thể đã bác bỏ một hoặc nhiều phát biểu trên, đặc biệt là phần về quy tắc nghiệp vụ không quan tâm đến cơ sở dữ liệu. Nhiều trong chúng ta đã được dạy tin rằng cơ sở dữ liệu gắn liền không tách rời với quy tắc nghiệp vụ. Một số trong chúng ta thậm chí đã bị thuyết phục rằng cơ sở dữ liệu là bản thể hiện của quy tắc nghiệp vụ.

Nhưng, như chúng ta sẽ thấy ở một chương khác, ý tưởng này sai lầm. Cơ sở dữ liệu là một công cụ mà quy tắc nghiệp vụ có thể dùng gián tiếp. Quy tắc nghiệp vụ không cần biết về schema, ngôn ngữ truy vấn, hoặc bất kỳ chi tiết nào khác về cơ sở dữ liệu. Tất cả những gì quy tắc nghiệp vụ cần biết là có một tập hợp hàm có thể dùng để tải hoặc lưu dữ liệu. Điều này cho phép chúng ta đặt cơ sở dữ liệu sau một giao diện.

Bạn có thể thấy rõ điều này trong Hình 17.1. `BusinessRules` (Quy tắc nghiệp vụ) dùng `DatabaseInterface` (Giao diện cơ sở dữ liệu) để tải và lưu dữ liệu. `DatabaseAccess` (Truy cập cơ sở dữ liệu) triển khai giao diện đó và điều khiển hoạt động của `Database` (Cơ sở dữ liệu) thực tế.

**Hình 17.1** Cơ sở dữ liệu sau một giao diện

Các lớp và giao diện trong sơ đồ này mang tính biểu tượng. Trong một ứng dụng thực, sẽ có nhiều lớp quy tắc nghiệp vụ, nhiều lớp giao diện cơ sở dữ liệu, và nhiều triển khai truy cập cơ sở dữ liệu. Tất cả chúng, tuy nhiên, sẽ tuân theo đại thể cùng một mẫu.

Đường ranh giới nằm ở đâu? Nó đi qua quan hệ kế thừa (inheritance), ngay bên dưới `DatabaseInterface` (Hình 17.2).

**Hình 17.2** Đường ranh giới

Hãy chú ý hai mũi tên hướng ra khỏi `DatabaseAccess`. Điều đó cho thấy các lớp còn lại không biết `DatabaseAccess` tồn tại.

Bây giờ hãy lùi lại một bước. Ta sẽ xem thành phần chứa các quy tắc nghiệp vụ và thành phần chứa cơ sở dữ liệu cùng mọi lớp truy cập của nó (Hình 17.3).

**Hình 17.3** Thành phần quy tắc nghiệp vụ và thành phần cơ sở dữ liệu

Chú ý hướng của mũi tên. `Database` (Cơ sở dữ liệu) biết về `BusinessRules` (Quy tắc nghiệp vụ). `BusinessRules` không biết về `Database`. Điều này ngụ ý các lớp `DatabaseInterface` sống trong thành phần `BusinessRules`, trong khi các lớp `DatabaseAccess` sống trong thành phần `Database`.

Hướng của đường này quan trọng. Nó cho thấy `Database` không quan trọng đối với `BusinessRules`, nhưng `Database` không thể tồn tại nếu không có `BusinessRules`.

Nếu điều đó nghe lạ, hãy nhớ điểm này: Thành phần `Database` chứa mã dịch các lời gọi do `BusinessRules` thực hiện sang ngôn ngữ truy vấn của cơ sở dữ liệu. Chính mã dịch đó biết về `BusinessRules`.

Đã vạch đường ranh giới giữa hai thành phần này, và đã thiết lập hướng mũi tên trỏ về `BusinessRules`, chúng ta giờ thấy `BusinessRules` có thể dùng bất kỳ loại cơ sở dữ liệu nào. Thành phần `Database` có thể được thay thế bằng nhiều triển khai khác nhau, `BusinessRules` không quan tâm.

Cơ sở dữ liệu có thể triển khai bằng Oracle, hoặc MySQL, hoặc Couch, hoặc Datomic, thậm chí file phẳng. Quy tắc nghiệp vụ hoàn toàn không quan tâm. Và điều đó có nghĩa là quyết định về cơ sở dữ liệu có thể trì hoãn, và bạn có thể tập trung vào việc viết và kiểm thử quy tắc nghiệp vụ trước khi phải ra quyết định về cơ sở dữ liệu.

## Còn đầu vào và đầu ra thì sao?

Lập trình viên và khách hàng thường nhầm lẫn về bản chất của hệ thống. Họ nhìn thấy GUI và cho rằng đó chính là hệ thống. Họ định nghĩa hệ thống qua GUI, nên tin rằng GUI phải xuất hiện ngay lập tức. Họ bỏ qua một nguyên tắc cực kỳ quan trọng: **IO không liên quan** (The IO is irrelevant).

Điều này ban đầu có thể khó hiểu. Ta thường mô tả hành vi hệ thống qua hành vi IO. Hãy xét trò chơi điện tử. Trải nghiệm của bạn chịu ảnh hưởng bởi giao diện: màn hình, chuột, nút bấm và âm thanh. Bạn có thể quên rằng phía sau giao diện là một mô hình, gồm những cấu trúc dữ liệu và hàm tinh vi điều khiển trò chơi. Quan trọng hơn, mô hình ấy không cần giao diện. Nó vẫn thực hiện công việc của mình, duy trì trạng thái của mọi sự kiện trong trò chơi, ngay cả khi trò chơi không hề được hiển thị trên màn hình. Giao diện không liên quan đến mô hình, tức là các quy tắc nghiệp vụ.

Và một lần nữa, chúng ta thấy các thành phần `GUI` và `BusinessRules` được tách biệt bởi một đường ranh giới (Hình 17.4). Thành phần ít liên quan hơn phụ thuộc vào thành phần quan trọng hơn. Các mũi tên cho thấy thành phần nào biết về thành phần kia, và do đó thành phần nào quan tâm đến thành phần kia. `GUI` quan tâm đến `BusinessRules`.

**Hình 17.4** Ranh giới giữa thành phần GUI và thành phần BusinessRules

Đã vạch ranh giới này và mũi tên này, chúng ta giờ thấy `GUI` có thể được thay thế bằng bất kỳ loại giao diện nào khác, và `BusinessRules` sẽ không quan tâm.

## Kiến trúc plugin

Kết hợp lại, hai quyết định này về cơ sở dữ liệu và GUI tạo ra một kiểu mẫu để thêm các thành phần khác. Mẫu đó chính là mẫu được các hệ thống cho phép plugin của bên thứ ba sử dụng.

Thực tế, lịch sử phát triển phần mềm là câu chuyện về việc tạo ra các plugin để xây dựng kiến trúc hệ thống có thể mở rộng và bảo trì. Các quy tắc nghiệp vụ cốt lõi được giữ tách biệt, độc lập với những thành phần tùy chọn hoặc có thể được triển khai theo nhiều cách khác nhau (Hình 17.5).

**Hình 17.5** Cắm vào quy tắc nghiệp vụ

Vì giao diện người dùng trong thiết kế này được coi là một plugin, chúng ta đã làm cho việc cắm nhiều loại giao diện người dùng khác nhau trở nên khả thi. Chúng có thể dựa trên web, dựa trên client/server, dựa trên SOA, dựa trên Console, hoặc dựa trên bất kỳ công nghệ giao diện người dùng nào khác.

Tương tự đối với cơ sở dữ liệu. Vì chúng ta chọn coi nó như một plugin, chúng ta có thể thay thế nó bằng bất kỳ cơ sở dữ liệu SQL nào, hoặc cơ sở dữ liệu NoSQL, hoặc cơ sở dữ liệu dựa trên hệ thống file, hoặc bất kỳ công nghệ cơ sở dữ liệu nào chúng ta có thể cho là cần thiết trong tương lai.

Những sự thay thế này có thể không tầm thường. Nếu triển khai ban đầu của hệ thống là dựa trên web, thì viết plugin cho giao diện client-server có thể thách thức. Có khả năng một số giao tiếp giữa quy tắc nghiệp vụ và GUI mới phải được viết lại. Tuy nhiên, bằng cách bắt đầu với giả định một cấu trúc plugin, chúng ta đã ít nhất làm cho một thay đổi như vậy trở nên thực tế.

## Lý lẽ về plugin

Xét mối quan hệ giữa ReSharper và Visual Studio. Hai thành phần này được tạo ra bởi các nhóm phát triển hoàn toàn khác nhau trong các công ty hoàn toàn khác nhau. Thực tế, JetBrains, nhà làm ReSharper, đặt tại Nga. Microsoft, tất nhiên, đặt tại Redmond, Washington. Khó tưởng tượng hai nhóm phát triển tách biệt hơn thế.

Nhóm nào có thể gây hại cho nhóm kia? Nhóm nào được bảo vệ khỏi nhóm kia? Cấu trúc phụ thuộc cho thấy rõ điều đó (Hình 17.6). Mã nguồn của ReSharper phụ thuộc vào mã nguồn của Visual Studio. Vì thế, nhóm ReSharper không thể làm ảnh hưởng đến nhóm Visual Studio. Nhưng nếu muốn, nhóm Visual Studio có thể khiến ReSharper hoàn toàn không hoạt động.

**Hình 17.6** ReSharper phụ thuộc vào Visual Studio

Đó là một mối quan hệ bất đối xứng sâu sắc, và đó là mối quan hệ chúng ta mong muốn trong hệ thống của mình. Chúng ta muốn một số mô-đun ít bị ảnh hưởng bởi các mô-đun khác. Ví dụ, chúng ta không muốn quy tắc nghiệp vụ bị phá vỡ khi ai đó thay đổi định dạng trang web, hoặc thay đổi schema cơ sở dữ liệu. Chúng ta không muốn thay đổi ở một phần của hệ thống gây hỏng các phần không liên quan khác. Chúng ta không muốn hệ thống thể hiện sự mong manh (fragility) kiểu đó.

Việc sắp xếp hệ thống thành kiến trúc plugin tạo ra các tường lửa (firewalls) mà thay đổi không thể lan truyền qua. Nếu GUI cắm vào quy tắc nghiệp vụ, thì thay đổi trong GUI không thể ảnh hưởng đến những quy tắc nghiệp vụ đó.

Ranh giới được vạch ở nơi có trục thay đổi (axis of change). Các thành phần ở một bên ranh giới thay đổi với tốc độ khác nhau, và vì lý do khác nhau, so với các thành phần ở bên kia ranh giới.

GUI thay đổi ở các thời điểm và tốc độ khác nhau so với quy tắc nghiệp vụ, nên có ranh giới giữa chúng. Quy tắc nghiệp vụ thay đổi ở các thời điểm và vì những lý do khác nhau so với framework tiêm phụ thuộc (dependency injection framework), nên có ranh giới giữa chúng.

Đây đơn giản là Nguyên tắc Trách nhiệm Đơn nhất (SRP) trở lại. SRP cho chúng ta biết vạch ranh giới ở đâu.

## Kết luận

Để vạch đường ranh giới trong một kiến trúc phần mềm, bạn trước tiên phân chia hệ thống thành các thành phần. Một số thành phần là quy tắc nghiệp vụ cốt lõi; những thành phần khác là plugin chứa các chức năng cần thiết nhưng không liên quan trực tiếp đến nghiệp vụ cốt lõi. Sau đó bạn sắp xếp mã trong các thành phần đó sao cho các mũi tên giữa chúng chỉ theo một hướng, về phía nghiệp vụ cốt lõi.

Bạn nên nhận ra đây là một ứng dụng của Nguyên tắc Đảo ngược Phụ thuộc (Dependency Inversion Principle) và Nguyên tắc Trừu tượng Ổn định (Stable Abstractions Principle). Các mũi tên phụ thuộc được sắp xếp để trỏ từ chi tiết mức thấp về phía trừu tượng mức cao.

[^1]: Từ "architecture" xuất hiện trong ngoặc kép ở đây vì ba tầng (three-tier) không phải là kiến trúc; đó là một topology (cấu trúc liên kết). Đó chính là loại quyết định mà một kiến trúc tốt nỗ lực trì hoãn.
[^2]: Nhiều năm sau chúng tôi mới nhúng framework Velocity vào FitNesse.