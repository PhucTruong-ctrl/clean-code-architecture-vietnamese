# Chương 16: Tính độc lập
![Minh họa](assets/illustrations/16-chuong-16-opener.png){w=260}

Như đã nêu trước đó, một kiến trúc tốt phải hỗ trợ:

- Các trường hợp sử dụng (use cases) và vận hành của hệ thống.
- Bảo trì hệ thống.
- Phát triển hệ thống.
- Triển khai (deployment) hệ thống.

## Trường hợp sử dụng (Use Cases)

Mục đầu tiên, trường hợp sử dụng, có nghĩa là kiến trúc của hệ thống phải hỗ trợ ý định của hệ thống. Nếu hệ thống là một ứng dụng giỏ hàng mua sắm, thì kiến trúc phải hỗ trợ các trường hợp sử dụng của giỏ hàng mua sắm. Thực tế, đây là mối quan tâm đầu tiên của kiến trúc sư, và ưu tiên đầu tiên của kiến trúc. Kiến trúc phải hỗ trợ các trường hợp sử dụng.

Tuy nhiên, như chúng ta đã thảo luận trước đó, kiến trúc không có nhiều ảnh hưởng lên hành vi của hệ thống. Có rất ít các lựa chọn hành vi mà kiến trúc có thể để mở. Nhưng ảnh hưởng không phải là mọi thứ. Điều quan trọng nhất mà một kiến trúc tốt có thể làm để hỗ trợ hành vi là làm rõ và trình bày hành vi đó để ý định của hệ thống nhìn thấy được ở cấp độ kiến trúc.

Một ứng dụng giỏ hàng mua sắm với kiến trúc tốt sẽ trông như một ứng dụng giỏ hàng mua sắm. Các trường hợp sử dụng của hệ thống đó sẽ nhìn thấy rõ ràng trong cấu trúc của hệ thống. Các nhà phát triển sẽ không phải săn lùng các hành vi, bởi vì những hành vi đó sẽ là các yếu tố hạng nhất (first-class elements) nhìn thấy được ở cấp cao nhất của hệ thống. Các yếu tố đó sẽ là các lớp hoặc hàm hoặc mô-đun có vị trí nổi bật trong kiến trúc, và chúng sẽ có tên mô tả rõ ràng chức năng của chúng.

Chương 21, "Kiến trúc Tự Hào" (Screaming Architecture), sẽ làm rõ điểm này hơn.

## Vận hành (Operation)

Kiến trúc đóng vai trò quan trọng hơn nhiều, và ít mang tính trang trí hơn, trong việc hỗ trợ vận hành của hệ thống. Nếu hệ thống phải xử lý 100.000 khách hàng mỗi giây, kiến trúc phải hỗ trợ loại thông lượng (throughput) và thời gian phản hồi đó cho mỗi trường hợp sử dụng yêu cầu nó. Nếu hệ thống phải truy vấn các khối dữ liệu lớn (big data cubes) trong mili-giây, thì kiến trúc phải được cấu trúc để cho phép loại vận hành đó.

Đối với một số hệ thống, điều này có nghĩa là sắp xếp các yếu tố xử lý của hệ thống thành một mảng các dịch vụ nhỏ (little services) có thể chạy song song trên nhiều máy chủ khác nhau. Đối với các hệ thống khác, nó sẽ nghĩa là một loạt luồng nhẹ (lightweight threads) chia sẻ không gian địa chỉ của một tiến trình (process) đơn lẻ trong một bộ xử lý đơn. Những hệ thống khác sẽ chỉ cần một vài tiến trình chạy trong các không gian địa chỉ biệt lập. Và một số hệ thống thậm chí có thể tồn tại dưới dạng các chương trình nguyên khối (monolithic) đơn giản chạy trong một tiến trình đơn.

Nghe có vẻ lạ lùng, nhưng quyết định này chính là một trong những lựa chọn mà một kiến trúc tốt để mở. Một hệ thống được viết dưới dạng nguyên khối (monolith), và phụ thuộc vào cấu trúc nguyên khối đó, không thể dễ dàng nâng cấp lên nhiều tiến trình, nhiều luồng, hoặc micro-services nếu nhu cầu nảy sinh. Ngược lại, một kiến trúc duy trì sự biệt lập thích hợp của các thành phần (components) của nó, và không giả định cách thức giao tiếp giữa các thành phần đó, sẽ dễ dàng hơn nhiều trong việc chuyển đổi qua lại xuyên qua phổ các luồng, tiến trình, và dịch vụ khi nhu cầu vận hành của hệ thống thay đổi theo thời gian.

## Phát triển (Development)

Kiến trúc đóng vai trò đáng kể trong việc hỗ trợ môi trường phát triển. Đây là nơi định luật Conway (Conway's law) phát huy tác dụng. Định luật Conway nói:

> Mọi tổ chức thiết kế một hệ thống sẽ tạo ra một thiết kế có cấu trúc sao chép cấu trúc truyền thông của tổ chức đó.

Một hệ thống phải được phát triển bởi một tổ chức có nhiều nhóm (teams) và nhiều mối quan tâm (concerns) phải có một kiến trúc tạo điều kiện cho các hành động độc lập của các nhóm đó, để các nhóm không can thiệp lẫn nhau trong quá trình phát triển. Điều này đạt được bằng cách phân vùng (partitioning) hệ thống đúng cách thành các thành phần biệt lập tốt, có thể phát triển độc lập. Các thành phần đó sau đó có thể được phân bổ cho các nhóm có thể làm việc độc lập với nhau.

## Triển khai (Deployment)

Kiến trúc cũng đóng vai trò lớn trong việc xác định mức độ dễ dàng triển khai hệ thống. Mục tiêu là "triển khai tức thì" (immediate deployment). Một kiến trúc tốt không dựa vào hàng chục tập tin kịch bản cấu hình (configuration scripts) nhỏ và các chỉnh sửa tệp thuộc tính (property file tweaks). Nó không yêu cầu tạo thủ công các thư mục hoặc tệp phải được sắp xếp đúng cách. Một kiến trúc tốt giúp hệ thống có thể triển khai ngay lập tức sau khi build (xây dựng).

Lại một lần nữa, điều này đạt được thông qua việc phân vùng và biệt lập thích hợp các thành phần của hệ thống, bao gồm cả các thành phần chủ (master components) gắn kết toàn bộ hệ thống lại với nhau và đảm bảo mỗi thành phần được khởi động, tích hợp, và giám sát (supervised) đúng cách.

## Giữ các lựa chọn mở (Leaving Options Open)

Tóm lại, các mục tiêu chúng ta phải đạt được là không rõ ràng và thiếu ổn định (indistinct and inconstant). Chào mừng đến với thế giới thực.

Nhưng chưa phải là đường cùng: Một số nguyên tắc kiến trúc thực hiện với chi phí tương đối thấp và có thể giúp cân bằng những mối quan tâm đó, ngay cả khi bạn không có bức tranh rõ ràng về các mục tiêu bạn phải đánh trúng. Những nguyên tắc đó giúp chúng ta phân vùng hệ thống thành các thành phần biệt lập tốt, cho phép chúng ta giữ càng nhiều lựa chọn mở càng tốt, trong càng lâu càng tốt.

Một kiến trúc tốt làm cho hệ thống dễ dàng thay đổi, theo tất cả các cách mà nó phải thay đổi, bằng cách giữ các lựa chọn mở.

## Tách biệt các lớp (Decoupling Layers)

...là một hệ thống xử lý đơn hàng. Vì vậy, kiến trúc sư có thể sử dụng Nguyên tắc Trách nhiệm Đơn lẻ (Single Responsibility Principle - SRP) và Nguyên tắc Đóng chung (Common Closure Principle - CCP) để tách biệt những thứ thay đổi vì những lý do khác nhau, và gom nhóm những thứ thay đổi vì cùng một lý do, trong bối cảnh ý định của hệ thống.

Điều gì thay đổi vì những lý do khác nhau? Có một số điều hiển nhiên. Giao diện người dùng (UI) thay đổi vì những lý do không liên quan gì đến các quy tắc nghiệp vụ (business rules). Các trường hợp sử dụng có cả hai yếu tố. Rõ ràng, một kiến trúc sư tốt sẽ muốn tách phần UI của một trường hợp sử dụng ra khỏi phần quy tắc nghiệp vụ sao cho chúng có thể thay đổi độc lập lẫn nhau, đồng thời vẫn giữ các trường hợp sử dụng nhìn thấy rõ ràng và rõ ràng.

...giá trị tính toán lãi suất trên một tài khoản và việc đếm tồn kho là các quy tắc nghiệp vụ gắn liền chặt chẽ hơn với miền (domain). Hai loại quy tắc khác nhau này sẽ thay đổi ở tốc độ khác nhau, và vì những lý do khác nhau, vì vậy chúng nên được tách biệt để có thể thay đổi độc lập.

Cơ sở dữ liệu (database), ngôn ngữ truy vấn, và thậm chí schema là các chi tiết kỹ thuật không có liên quan gì đến các quy tắc nghiệp vụ hay UI. Chúng sẽ thay đổi ở các tỷ lệ, và vì những lý do, độc lập với các khía cạnh khác của hệ thống. Do đó, kiến trúc nên tách chúng ra khỏi phần còn lại của hệ thống để chúng có thể thay đổi độc lập.

Do đó, chúng ta thấy hệ thống bị chia thành các lớp ngang (horizontal layers) tách biệt: UI, quy tắc nghiệp vụ đặc thù ứng dụng (application-specific business rules), quy tắc nghiệp vụ độc lập ứng dụng (application-independent business rules), và cơ sở dữ liệu, chỉ để nhắc đến một vài.

## Tách biệt các trường hợp sử dụng (Decoupling Use Cases)

Điều gì khác thay đổi vì những lý do khác nhau? Các trường hợp sử dụng bản thân! Trường hợp sử dụng để thêm một đơn hàng vào hệ thống nhập đơn hàng gần như chắc chắn sẽ thay đổi ở tỷ lệ khác nhau, và vì những lý do khác nhau, so với trường hợp sử dụng xóa một đơn hàng khỏi hệ thống. Các trường hợp sử dụng là một cách rất tự nhiên để chia hệ thống.

Cùng lúc đó, các trường hợp sử dụng là các lát cắt dọc hẹp (narrow vertical slices) cắt xuyên qua các lớp ngang của hệ thống. Mỗi trường hợp sử dụng sử dụng một chút UI, một chút quy tắc nghiệp vụ đặc thù ứng dụng, một chút quy tắc nghiệp vụ độc lập ứng dụng, và một chút chức năng cơ sở dữ liệu. Do đó, khi chúng ta chia hệ thống thành các lớp ngang, chúng ta cũng chia hệ thống thành các trường hợp sử dụng mỏng dọc cắt xuyên qua các lớp đó.

Để đạt được sự tách biệt này, chúng ta tách UI của trường hợp sử dụng thêm đơn hàng (add-order) ra khỏi UI của trường hợp sử dụng xóa đơn hàng (delete-order). Chúng ta làm tương tự với các quy tắc nghiệp vụ, và với cơ sở dữ liệu. Chúng ta giữ các trường hợp sử dụng tách biệt dọc theo chiều cao dọc của hệ thống.

Bạn có thể thấy khuôn mẫu ở đây. Nếu bạn tách biệt các yếu tố của hệ thống thay đổi vì những lý do khác nhau, thì bạn có thể tiếp tục thêm các trường hợp sử dụng mới mà không can thiệp vào các trường hợp cũ. Nếu bạn cũng gom nhóm UI và cơ sở dữ liệu để hỗ trợ các trường hợp sử dụng đó, sao cho mỗi trường hợp sử dụng sử dụng một khía cạnh khác nhau của UI và cơ sở dữ liệu, thì việc thêm các trường hợp sử dụng mới sẽ khó làm ảnh hưởng đến các trường hợp cũ.

## Chế độ tách biệt (Decoupling Mode)

Bây giờ hãy nghĩ về ý nghĩa của tất cả sự tách biệt đó đối với mục thứ hai: vận hành. Nếu các khía cạnh khác nhau của các trường hợp sử dụng được tách biệt, thì những khía cạnh phải chạy ở thông lượng cao có thể đã được tách biệt khỏi những khía cạnh phải chạy ở thông lượng thấp. Nếu UI và cơ sở dữ liệu đã được tách biệt khỏi các quy tắc nghiệp vụ, thì chúng có thể chạy trên các máy chủ khác nhau. Những khía cạnh yêu cầu băng thông cao hơn có thể được nhân bản (replicated) trên nhiều máy chủ.

Tóm lại, sự tách biệt mà chúng ta làm vì các trường hợp sử dụng cũng giúp ích cho vận hành. Tuy nhiên, để tận hưởng lợi ích vận hành đó, sự tách biệt phải có chế độ (mode) thích hợp. Để chạy trên các máy chủ riêng biệt, các thành phần đã tách biệt không thể phụ thuộc vào việc cùng nằm trong không gian địa chỉ của một bộ xử lý. Chúng phải là các dịch vụ độc lập (independent services), giao tiếp qua một mạng nào đó.

Nhiều kiến trúc sư gọi các thành phần như vậy là "dịch vụ" (services) hoặc "micro-services", tùy thuộc vào một khái niệm mơ hồ về số dòng mã. Thực tế, một kiến trúc dựa trên dịch vụ thường được gọi là kiến trúc hướng dịch vụ (service-oriented architecture - SOA).

Nếu thuật ngữ đó làm bật lên chuông cảnh báo trong đầu bạn, đừng lo. Tôi không sẽ nói rằng SOA là kiến trúc tốt nhất có thể, hay rằng micro-services là làn sóng của tương lai. Điểm được nói ở đây là đôi khi chúng ta phải tách biệt các thành phần của mình hoàn toàn đến cấp độ dịch vụ.

Hãy nhớ, một kiến trúc tốt để các lựa chọn mở. Chế độ tách biệt là một trong những lựa chọn đó.

Trước khi khám phá chủ đề đó sâu hơn, hãy nhìn sang hai mục còn lại.

## Khả năng phát triển độc lập (Independent Develop-ability)

Mục thứ ba là phát triển. Rõ ràng khi các thành phần được tách biệt mạnh (strongly decoupled), sự can thiệp giữa các nhóm được giảm thiểu. Nếu các quy tắc nghiệp vụ không biết về UI, thì một nhóm tập trung vào UI không thể ảnh hưởng nhiều đến một nhóm tập trung vào các quy tắc nghiệp vụ. Nếu các trường hợp sử dụng bản thân được tách biệt lẫn nhau, thì một nhóm tập trung vào trường hợp sử dụng thêm đơn hàng (addOrder) không có khả năng can thiệp vào một nhóm tập trung vào trường hợp sử dụng xóa đơn hàng (deleteOrder).

Miễn là các lớp và trường hợp sử dụng được tách biệt, kiến trúc của hệ thống sẽ hỗ trợ tổ chức của các nhóm, bất kể chúng được tổ chức như các nhóm tính năng (feature teams), nhóm thành phần (component teams), nhóm lớp (layer teams), hoặc một biến thể nào khác.

## Khả năng triển khai độc lập (Independent Deployability)

Sự tách biệt của các trường hợp sử dụng và các lớp cũng cung cấp một mức độ linh hoạt cao trong triển khai. Thực tế, nếu sự tách biệt được làm tốt, thì nên có thể hot-swap (thay đổi nóng) các lớp và trường hợp sử dụng trong các hệ thống đang chạy. Việc thêm một trường hợp sử dụng mới có thể đơn giản như việc thêm một vài tệp jar mới hoặc dịch vụ vào hệ thống trong khi để phần còn lại nguyên vẹn.

## Trùng lặp (Duplication)

Các kiến trúc sư thường rơi vào một cái bẫy, cái bẫy dựa trên nỗi sợ hãi của họ về sự trùng lặp (duplication).

Sự trùng lặp nói chung là một điều xấu trong phần mềm. Chúng ta không thích mã trùng lặp. Khi mã thực sự bị trùng lặp (true duplication), chúng ta bị ràng buộc bởi đạo đức nghề nghiệp phải giảm thiểu và loại bỏ nó.

Nhưng có nhiều loại trùng lặp khác nhau. Có trùng lặp thật (true duplication), nơi mọi thay đổi đối với một thể hiện (instance) đòi hỏi cùng một thay đổi đối với mọi bản sao của thể hiện đó. Sau đó có trùng lặp giả hoặc trùng lặp ngẫu nhiên (false or accidental duplication). Nếu hai phần mã có vẻ trùng lặp phát triển theo các con đường khác nhau, nếu chúng thay đổi ở các tỷ lệ khác nhau, và vì những lý do khác nhau, thì chúng không phải là bản sao thật. Quay lại chúng sau vài năm, và bạn sẽ thấy chúng rất khác nhau.

Hãy tưởng tượng hai trường hợp sử dụng có cấu trúc màn hình rất giống nhau. Các kiến trúc sư sẽ có xu hướng mạnh muốn chia sẻ mã cho cấu trúc đó. Nhưng họ nên làm như vậy không? Đó có phải là trùng lặp thật? Hay là ngẫu nhiên?

Có khả năng lớn là ngẫu nhiên. Theo thời gian, khả năng là hai màn hình đó sẽ phân hóa (diverge) và cuối cùng trông rất khác nhau. Vì lý do đó, phải cẩn thận tránh việc hợp nhất (unifying) chúng. Nếu không, việc tách biệt chúng sau này sẽ là một thách thức.

Khi bạn tách dọc các trường hợp sử dụng ra khỏi nhau, bạn sẽ gặp vấn đề này, và cám dỗ của bạn sẽ là gắn kết (coupling) các trường hợp sử dụng vì chúng có cấu trúc màn hình giống nhau, hoặc thuật toán giống nhau, hoặc các truy vấn và/hoặc schema cơ sở dữ liệu giống nhau. Hãy cẩn thận. Hãy kháng cự cám dỗ loại bỏ trùng lặp theo phản xạ gân cốt (knee-jerk). Hãy chắc chắn rằng sự trùng lặp là thật.

Theo cùng token đó, khi bạn tách các lớp theo chiều ngang, bạn có thể nhận thấy cấu trúc dữ liệu của một bản ghi cơ sở dữ liệu cụ thể rất giống với cấu trúc dữ liệu của một khung nhìn màn hình (screen view) cụ thể. Bạn có thể bị cám dỗ đơn giản truyền bản ghi cơ sở dữ liệu lên cho UI, thay vì tạo một view model trông giống y hệt và sao chép các phần tử qua. Hãy cẩn thận: Sự trùng lặp này gần như chắc chắn là ngẫu nhiên. Việc tạo view model riêng biệt không tốn nhiều công sức, và nó sẽ giúp bạn giữ các lớp tách biệt đúng cách.

## Các chế độ tách biệt (lại) (Decoupling Modes (Again))

Quay lại các chế độ. Có nhiều cách để tách biệt các lớp và trường hợp sử dụng. Chúng có thể được tách biệt ở cấp độ mã nguồn (source code level), ở cấp độ mã nhị phân/triển khai (binary code/deployment level), và ở cấp độ đơn vị thực thi/dịch vụ (execution unit/service level).

- **Cấp mã nguồn (Source level).** Chúng ta có thể kiểm soát các phụ thuộc giữa các mô-đun mã nguồn sao cho thay đổi đối với một mô-đun không buộc thay đổi hoặc biên dịch lại các mô-đun khác (ví dụ: Ruby Gems).
  Trong chế độ tách biệt này, tất cả các thành phần thực thi trong cùng một không gian địa chỉ, và giao tiếp với nhau bằng các lời gọi hàm đơn giản (function calls). Có một tệp thực thi đơn (single executable) được tải vào bộ nhớ máy tính. Mọi người thường gọi đây là cấu trúc nguyên khối (monolithic structure).

- **Cấp triển khai (Deployment level).** Chúng ta có thể kiểm soát các phụ thuộc giữa các đơn vị triển khai (deployable units) như tệp jar, DLL, hoặc thư viện chia sẻ (shared libraries), sao cho thay đổi mã nguồn trong một mô-đun không buộc các mô-đun khác phải được build lại và triển khai lại.
  Nhiều thành phần vẫn có thể nằm trong cùng một không gian địa chỉ, và giao tiếp qua lời gọi hàm. Các thành phần khác có thể nằm trong các tiến trình khác trên cùng một bộ xử lý, và giao tiếp qua truyền thông liên tiến trình (interprocess communications), socket, hoặc bộ nhớ chia sẻ. Điều quan trọng ở đây là các thành phần tách biệt được phân vùng thành các đơn vị triển khai độc lập như tệp jar, Gem files, hoặc DLL.

- **Cấp dịch vụ (Service level).** Chúng ta có thể giảm các phụ thuộc xuống cấp độ cấu trúc dữ liệu (data structures), và giao tiếp hoàn toàn qua các gói tin mạng (network packets) sao cho mọi đơn vị thực thi hoàn toàn độc lập với thay đổi mã nguồn và nhị phân của các đơn vị khác (ví dụ: services hoặc micro-services).

Chế độ nào là tốt nhất để sử dụng?

Câu trả lời là khó biết chế độ nào tốt nhất trong giai đoạn đầu của dự án. Thực tế, khi dự án trưởng thành, chế độ tối ưu có thể thay đổi.

Ví dụ, không khó tưởng tượng một hệ thống chạy thoải mái trên một máy chủ ngay bây giờ có thể phát triển đến mức một số thành phần của nó nên chạy trên các máy chủ riêng biệt. Trong khi hệ thống chạy trên một máy chủ đơn, tách biệt ở cấp mã nguồn có thể đã đủ. Tuy nhiên, sau này, nó có thể đòi hỏi tách biệt thành các đơn vị triển khai, hoặc thậm chí các dịch vụ.

Một giải pháp (có vẻ phổ biến lúc này) là đơn giản tách biệt ở cấp dịch vụ theo mặc định. Một vấn đề với cách tiếp cận này là nó tốn kém và khuyến khích tách biệt thô (coarse-grained decoupling). Dù micro-services có "micro" đến đâu, tách biệt đó không có khả năng đủ mịn (fine-grained).

Một vấn đề khác với tách biệt cấp dịch vụ là nó tốn kém, cả về thời gian phát triển và tài nguyên hệ thống. Xử lý ranh giới dịch vụ ở nơi không cần thiết là lãng phí công sức, bộ nhớ, và chu kỳ CPU. Và, đúng, tôi biết hai cái sau rẻ, nhưng cái đầu thì không.

Sở thích của tôi là đẩy sự tách biệt đến điểm mà một dịch vụ có thể được hình thành, *nếu nó trở nên cần thiết*; nhưng sau đó để các thành phần ở trong cùng không gian địa chỉ càng lâu càng tốt. Điều này để lựa chọn dịch vụ mở.

Với cách tiếp cận này, ban đầu các thành phần được tách biệt ở cấp mã nguồn. Điều đó có thể đủ tốt cho suốt vòng đời dự án. Nếu, tuy nhiên, các vấn đề triển khai hoặc phát triển nảy sinh, đẩy một số tách biệt lên cấp triển khai có thể đủ, ít nhất là một thời gian.

Khi các vấn đề phát triển, triển khai, và vận hành tăng lên, tôi cẩn trọng chọn những đơn vị triển khai nào để biến thành dịch vụ, và dần dần chuyển dịch hệ thống theo hướng đó.

Theo thời gian, nhu cầu vận hành của hệ thống có thể giảm. Điều từng đòi hỏi tách biệt ở cấp dịch vụ bây giờ có thể chỉ yêu cầu tách biệt cấp triển khai hoặc thậm chí cấp mã nguồn.

Một kiến trúc tốt sẽ cho phép một hệ thống ra đời như một nguyên khối (monolith), được triển khai trong một tệp đơn, nhưng sau đó phát triển thành một tập hợp các đơn vị triển khai độc lập, và luôn luôn đến các dịch vụ và/hoặc micro-services độc lập. Sau này, khi mọi thứ thay đổi, nó nên cho phép đảo ngược tiến trình đó và trượt ngược về nguyên khối.

Một kiến trúc tốt bảo vệ phần lớn mã nguồn khỏi những thay đổi đó. Nó để chế độ tách biệt mở như một lựa chọn sao cho các triển khai lớn có thể dùng một chế độ, trong khi các triển khai nhỏ có thể dùng chế độ khác.

## Kết luận (Conclusion)

Đúng, đây là chuyện rắc rối. Và tôi không nói rằng việc thay đổi chế độ tách biệt nên là một tùy chọn cấu hình hời hợt (trivial configuration option) (dù đôi khi điều đó thích hợp). Tôi đang nói rằng chế độ tách biệt của một hệ thống là một trong những thứ có khả năng thay đổi theo thời gian, và một kiến trúc sư tốt dự đoán và tạo điều kiện thích hợp cho những thay đổi đó.