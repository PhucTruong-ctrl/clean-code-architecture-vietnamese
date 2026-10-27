# Chương 15: Kiến trúc là gì?
![Minh họa](assets/illustrations/15-chuong-15-opener.png){w=240}

Từ "kiến trúc" gợi lên những hình ảnh về quyền lực và sự bí ẩn. Nó khiến ta nghĩ đến những quyết định quan trọng và sự am hiểu kỹ thuật thâm sâu. Kiến trúc phần mềm nằm ở đỉnh cao của thành tựu kỹ thuật. Khi nghĩ đến một kiến trúc sư phần mềm, ta hình dung một người có quyền lực và được kính trọng. Lập trình viên trẻ nào không từng mơ ước một ngày nào đó trở thành kiến trúc sư phần mềm?

Nhưng kiến trúc phần mềm là gì? Kiến trúc sư phần mềm làm gì, và khi nào họ làm nó?

Thứ nhất, một kiến trúc sư phần mềm là một lập trình viên; và tiếp tục là một lập trình viên. Đừng bao giờ tin vào lời nói dối cho rằng kiến trúc sư phần mềm lui lại khỏi mã nguồn để tập trung vào các vấn đề cấp độ cao hơn. Họ không làm vậy! Kiến trúc sư phần mềm là những lập trình viên xuất sắc nhất, và họ tiếp tục nhận các nhiệm vụ lập trình, đồng thời dẫn dắt phần còn lại của nhóm về phía một thiết kế giúp tối đa hóa năng suất. Kiến trúc sư phần mềm có thể không viết nhiều mã như các lập trình viên khác, nhưng họ tiếp tục tham gia vào các công việc lập trình. Họ làm như vậy vì không thể thực hiện tốt công việc của mình nếu không trải qua những vấn đề mà họ tạo ra cho các lập trình viên khác.

Kiến trúc của một hệ thống phần mềm là hình dáng được trao cho hệ thống đó bởi những người xây dựng nó. Hình dáng đó thể hiện trong việc chia hệ thống thành các thành phần, sự sắp xếp của các thành phần đó, và cách thức mà các thành phần đó giao tiếp với nhau.

Mục đích của hình dáng đó là để tạo điều kiện cho việc phát triển, triển khai, vận hành và bảo trì hệ thống phần mềm bên trong nó.
> Chiến lược đằng sau sự tạo điều kiện đó là để giữ càng nhiều lựa chọn mở càng tốt, trong thời gian càng dài càng tốt.

Có lẽ câu nói này khiến bạn ngạc nhiên. Có lẽ bạn nghĩ mục tiêu của kiến trúc phần mềm là làm cho hệ thống hoạt động đúng đắn. Chắc chắn chúng ta muốn hệ thống hoạt động đúng, và chắc chắn kiến trúc của hệ thống phải hỗ trợ điều đó như một trong những ưu tiên cao nhất.

Tuy nhiên, kiến trúc của một hệ thống hầu như không có ảnh hưởng gì đến việc hệ thống đó có hoạt động hay không. Có rất nhiều hệ thống bên ngoài kia, với kiến trúc tồi tệ, vẫn hoạt động tốt đẹp. Khó khăn của chúng không nằm ở việc vận hành; mà nằm ở việc triển khai, bảo trì và phát triển liên tục.

Đây không có nghĩa là kiến trúc không đóng vai trò trong việc hỗ trợ hành vi đúng đắn của hệ thống. Nó chắc chắn đóng vai trò, và vai trò đó là quan trọng. Nhưng vai trò đó là bị động và hình thức, không phải chủ động hay thiết yếu. Có rất ít, nếu không có, tùy chọn hành vi nào mà kiến trúc của một hệ thống có thể để mở.

Mục đích chính của kiến trúc là hỗ trợ vòng đời của hệ thống. Kiến trúc tốt làm cho hệ thống dễ hiểu, dễ phát triển, dễ bảo trì và dễ triển khai. Mục tiêu tối thượng là giảm thiểu chi phí vòng đời của hệ thống và tối đa hóa năng suất của lập trình viên.

## Phát triển

Một hệ thống phần mềm khó phát triển khó lòng có một vòng đời lâu dài và khỏe mạnh. Vì vậy, kiến trúc của một hệ thống nên làm cho hệ thống đó dễ dàng phát triển, cho các nhóm phát triển nó.

Các cấu trúc nhóm khác nhau ngụ ý các quyết định kiến trúc khác nhau. Mặt khác, một nhóm nhỏ năm lập trình viên có thể làm việc cùng nhau rất hiệu quả để phát triển một hệ thống nguyên khối (monolithic) nếu không có các thành phần hay giao diện được định nghĩa rõ ràng. Thực tế, nhóm như vậy có thể thấy các quy phạm của một kiến trúc trở thành một trở ngại trong những ngày đầu của quá trình phát triển. Đây có lẽ là lý do tại sao nhiều hệ thống lại thiếu kiến trúc tốt: Chúng bắt đầu không có kiến trúc, vì nhóm nhỏ và không muốn gánh nặng của một siêu cấu trúc.

Mặt khác, một hệ thống được phát triển bởi năm nhóm khác nhau, mỗi nhóm bảy lập trình viên, không thể tiến triển trừ khi hệ thống được chia thành các thành phần được định nghĩa rõ ràng với các giao diện ổn định và tin cậy. Nếu không xem xét yếu tố nào khác, kiến trúc của hệ thống đó có thể sẽ tiến hóa thành năm thành phần, một cho mỗi nhóm.

Kiến trúc một-thành-phần-một-nhóm (component-per-team) như vậy khó có thể là kiến trúc tốt nhất cho việc triển khai, vận hành và bảo trì. Dù vậy, nếu các nhóm chỉ bị thúc đẩy bởi lịch trình phát triển, hệ thống rất dễ hình thành theo mô hình này.

## Triển khai

Để có hiệu quả, một hệ thống phần mềm phải có thể triển khai được. Chi phí triển khai càng cao, hệ thống càng ít hữu ích. Mục tiêu của một kiến trúc phần mềm, do đó, nên là tạo ra một hệ thống có thể dễ dàng triển khai bằng một thao tác duy nhất.

Thật không may, chiến lược triển khai hiếm khi được xem xét trong giai đoạn phát triển ban đầu. Điều này dẫn đến những kiến trúc có thể làm cho hệ thống dễ phát triển, nhưng lại khiến nó rất khó triển khai.

Ví dụ, trong giai đoạn phát triển sớm của một hệ thống, các lập trình viên có thể quyết định sử dụng "kiến trúc vi dịch vụ" (micro-service architecture). Họ có thể thấy cách tiếp cận này làm cho hệ thống rất dễ phát triển vì các ranh giới thành phần rất chặt chẽ và các giao diện tương đối ổn định. Tuy nhiên, khi đến lúc triển khai hệ thống, họ có thể phát hiện số lượng vi dịch vụ đã trở nên đáng sợ; việc cấu hình các kết nối giữa chúng, và thời điểm khởi động của chúng, cũng có thể trở thành một nguồn lỗi khổng lồ.

Nếu các kiến trúc sư đã xem xét các vấn đề triển khai sớm, họ có thể đã quyết định dùng ít dịch vụ hơn, một sự kết hợp giữa dịch vụ và các thành phần trong tiến trình (in-process), và một cách quản lý liên kết tích hợp hơn.

## Vận hành

Tác động của kiến trúc đến vận hành hệ thống thường ít rõ rệt hơn tác động của nó đến phát triển, triển khai và bảo trì. Hầu hết khó khăn trong vận hành đều có thể giải quyết bằng cách bổ sung phần cứng mà không cần thay đổi đáng kể kiến trúc phần mềm.

Chúng ta đã thấy điều này xảy ra lặp đi lặp lại. Những hệ thống phần mềm có kiến trúc kém hiệu quả thường có thể được làm cho hoạt động hiệu quả chỉ bằng cách thêm bộ nhớ và thêm máy chủ. Thực tế là phần cứng rẻ và con người đắt có nghĩa là những kiến trúc cản trở vận hành không tốn kém bằng những kiến trúc cản trở phát triển, triển khai và bảo trì.

Điều này không có nghĩa là một kiến trúc được tinh chỉnh tốt cho việc vận hành hệ thống là không đáng mong muốn. Ngược lại, điều đó rất đáng mong muốn. Chỉ là phép tính chi phí nghiêng về phía phát triển, triển khai và bảo trì.

Dù vậy, kiến trúc còn có một vai trò khác đối với việc vận hành hệ thống: một kiến trúc phần mềm tốt truyền đạt các nhu cầu vận hành của hệ thống.

Có thể nói chính xác hơn rằng kiến trúc khiến cách hệ thống vận hành hiện rõ với lập trình viên. Kiến trúc cần làm rõ yêu cầu vận hành. Nó nên nâng các ca sử dụng, tính năng và hành vi bắt buộc lên thành những yếu tố hạng nhất, những mốc dễ nhận biết đối với lập trình viên. Nhờ vậy, hệ thống dễ hiểu hơn, hỗ trợ đáng kể cho phát triển và bảo trì.

## Bảo trì

Trong mọi khía cạnh của một hệ thống phần mềm, bảo trì là phần tốn kém nhất. Chuỗi tính năng mới không dứt cùng hàng loạt lỗi và bản sửa chữa tiêu tốn một lượng lớn nguồn lực con người.

Chi phí bảo trì chủ yếu đến từ việc lần mò trong mã nguồn và rủi ro. Lần mò là thời gian đào sâu vào phần mềm hiện có để tìm nơi thích hợp nhất và cách tốt nhất để bổ sung tính năng hoặc sửa lỗi. Trong khi thực hiện những thay đổi ấy, nguy cơ vô tình tạo thêm lỗi luôn hiện hữu, làm tăng chi phí rủi ro.

Một kiến trúc được suy xét cẩn thận giúp giảm đáng kể các chi phí này. Việc chia hệ thống thành các thành phần và cô lập chúng bằng những giao diện ổn định giúp làm rõ lối đi cho các tính năng tương lai, đồng thời giảm mạnh nguy cơ vô tình làm hỏng hệ thống.

## Giữ các lựa chọn mở

Như chúng ta đã mô tả ở một chương trước, phần mềm có hai loại giá trị: giá trị của hành vi và giá trị của cấu trúc. Loại thứ hai là lớn hơn vì chính giá trị này làm cho phần mềm "mềm" (soft).

Phần mềm ra đời vì chúng ta cần một cách nhanh chóng và dễ dàng để thay đổi hành vi của máy móc. Nhưng tính linh hoạt ấy phụ thuộc phần lớn vào hình dáng của hệ thống, cách sắp xếp các thành phần và cách chúng kết nối với nhau.

Cách bạn giữ phần mềm mềm là để càng nhiều lựa chọn mở càng tốt, trong thời gian càng dài càng tốt. Những lựa chọn chúng ta cần để mở là gì? Chúng là những chi tiết không quan trọng.

Tất cả các hệ thống phần mềm có thể được phân tách thành hai yếu tố chính: chính sách (policy) và chi tiết (details). Yếu tố chính sách thể hiện tất cả các quy tắc và thủ tục nghiệp vụ. Chính sách là nơi giá trị thực sự của hệ thống nằm.

Chi tiết là những thứ cần thiết để con người, các hệ thống khác và lập trình viên giao tiếp với chính sách, nhưng hoàn toàn không ảnh hưởng đến hành vi của chính sách. Chúng bao gồm thiết bị IO, cơ sở dữ liệu, hệ thống web, máy chủ, framework, giao thức truyền thông và những thứ tương tự.

Mục tiêu của kiến trúc sư là định hình hệ thống sao cho chính sách nổi bật lên như yếu tố cốt lõi, còn các chi tiết không ảnh hưởng đến chính sách. Nhờ vậy, các quyết định về chi tiết có thể được trì hoãn.

Ví dụ:

- Không cần chọn một hệ thống cơ sở dữ liệu trong những ngày đầu của phát triển, vì chính sách cấp cao không nên quan tâm loại cơ sở dữ liệu nào sẽ được sử dụng. Thực tế, nếu kiến trúc sư cẩn thận, chính sách cấp cao sẽ không quan tâm cơ sở dữ liệu là quan hệ (relational), phân tán (distributed), phân cấp (hierarchical), hay chỉ là các tệp phẳng (flat files) đơn thuần.
- Không cần chọn máy chủ web ngay từ đầu, vì chính sách cấp cao không nên biết mình được cung cấp qua web. Nếu chính sách cấp cao không nhận biết HTML, AJAX, JSP, JSF hay bất kỳ từ viết tắt nào trong mớ thuật ngữ phát triển web, thì bạn có thể trì hoãn việc chọn hệ thống web đến giai đoạn sau của dự án. Thậm chí, bạn chưa cần quyết định hệ thống có được cung cấp qua web hay không.
- Không cần áp dụng REST sớm trong phát triển, vì chính sách cấp cao nên trung lập về giao diện với thế giới bên ngoài. Cũng không cần áp dụng một khung vi dịch vụ (micro-services framework), hay một khung SOA. Lại nữa, chính sách cấp cao không nên quan tâm đến những thứ này.
- Không cần áp dụng một khung tiêm phụ thuộc (dependency injection framework) sớm trong phát triển, vì chính sách cấp cao không nên quan tâm phụ thuộc được giải quyết như thế nào.

Tôi nghĩ bạn đã hiểu ý. Nếu bạn có thể phát triển chính sách cấp cao mà không cam kết vào các chi tiết bao quanh nó, bạn có thể trì hoãn và trì hoãn thêm các quyết định về những chi tiết đó trong một thời gian dài. Và càng đợi lâu để đưa ra những quyết định đó, bạn càng có nhiều thông tin hơn để đưa ra chúng đúng đắn.

Điều này cũng cho phép bạn thử nhiều phương án khác nhau. Nếu chính sách cấp cao đã hoạt động và không phụ thuộc vào cơ sở dữ liệu, bạn có thể kết nối nó với vài cơ sở dữ liệu để kiểm tra độ phù hợp và hiệu năng. Điều tương tự cũng đúng với các hệ thống web, framework web, thậm chí cả bản thân web.

Càng để các lựa chọn mở lâu, bạn càng có thể chạy nhiều thí nghiệm hơn, thử nhiều thứ hơn, và có nhiều thông tin hơn khi bạn đạt đến thời điểm những quyết định đó không thể trì hoãn thêm được.

Nếu người khác đã đưa ra các quyết định đó thì sao? Nếu công ty bạn đã cam kết dùng một cơ sở dữ liệu, máy chủ web hay framework cụ thể thì sao? Một kiến trúc sư giỏi vẫn làm việc như thể các quyết định ấy chưa được chốt, và định hình hệ thống sao cho chúng có thể tiếp tục được trì hoãn hoặc thay đổi càng lâu càng tốt.
> Một kiến trúc sư tốt tối đa hóa số lượng quyết định *chưa* được đưa ra.

## Độc lập thiết bị

Để minh họa lối tư duy này, hãy quay về những năm 1960, khi máy tính còn non trẻ và phần lớn lập trình viên là các nhà toán học hoặc kỹ sư thuộc những ngành khác. Ít nhất một phần ba trong số họ là phụ nữ.

Những ngày ấy chúng ta phạm nhiều sai lầm. Chúng ta không biết đó là sai lầm vào lúc đó, tất nhiên. Làm sao có thể biết?

Một trong những sai lầm đó là gắn mã của chúng ta trực tiếp vào các thiết bị IO. Nếu chúng ta cần in một cái gì đó trên máy in, chúng ta viết mã sử dụng các lệnh IO để điều khiển máy in. Mã của chúng ta phụ thuộc vào thiết bị (device dependent).

Ví dụ, khi tôi viết chương trình PDP-8 in trên máy in điện báo (teleprinter), tôi dùng một tập lệnh máy trông như sau:

```
PRTCHR, 0
TSF
JMP .-1
TLS
JMP I PRTCHR
```

`PRTCHR` là một chương trình con in một ký tự trên máy in điện báo. Số không ở đầu được dùng làm nơi lưu trữ địa chỉ trả về. (Đừng hỏi.) Lệnh `TSF` bỏ qua lệnh tiếp theo nếu máy in điện báo sẵn sàng in một ký tự. Nếu máy in bận, `TSF` chỉ việc rơi xuống lệnh `JMP .-1`, nhảy ngược lại chính lệnh `TSF`. Nếu máy in sẵn sàng, `TSF` sẽ nhảy qua lệnh `TLS`, gửi ký tự trong thanh ghi A đến máy in. Sau đó lệnh `JMP I PRTCHR` trả về cho người gọi.

Ban đầu, chiến lược này hoạt động tốt. Khi cần đọc thẻ, chúng ta dùng mã giao tiếp trực tiếp với máy đọc thẻ. Khi cần đục lỗ thẻ, chúng ta viết mã điều khiển trực tiếp máy đục lỗ. Các chương trình hoạt động hoàn hảo. Làm sao biết đó là một sai lầm?

Nhưng các lô thẻ đục lỗ lớn rất khó quản lý. Chúng có thể bị mất, hư hỏng, cong vênh, xáo trộn hoặc rơi vãi. Từng thẻ có thể bị thất lạc hoặc thẻ thừa có thể bị chèn vào. Vì vậy, tính toàn vẹn dữ liệu trở thành vấn đề đáng kể.

Băng từ là giải pháp. Ta có thể chuyển ảnh của các tấm thẻ sang băng. Nếu làm rơi một cuộn băng từ, các bản ghi không bị xáo trộn. Không thể vô tình làm mất một bản ghi hay chèn bản ghi trống chỉ vì cầm cuộn băng. Băng an toàn hơn nhiều. Nó cũng đọc và ghi nhanh hơn, đồng thời dễ sao lưu.

Thật không may, toàn bộ phần mềm của chúng ta đều được viết để điều khiển máy đọc thẻ và máy đục lỗ thẻ. Muốn chuyển sang dùng băng từ, chúng ta phải viết lại các chương trình. Đó là một công việc lớn.

Đến cuối những năm 1960, chúng ta đã rút ra bài học và phát minh ra khái niệm *độc lập thiết bị* (device independence). Hệ điều hành thời đó trừu tượng hóa thiết bị IO thành các hàm phần mềm xử lý những bản ghi đơn vị (unit records) có dạng như thẻ. Chương trình gọi các dịch vụ của hệ điều hành để xử lý những bản ghi trừu tượng này. Người vận hành có thể yêu cầu hệ điều hành kết nối các dịch vụ ấy với máy đọc thẻ, băng từ hoặc bất kỳ thiết bị xử lý bản ghi đơn vị nào khác.

Bây giờ cùng một chương trình có thể đọc và ghi thẻ, hoặc đọc và ghi băng, mà không cần bất kỳ thay đổi nào. Nguyên tắc Đóng-Mở (Open-Closed Principle) đã ra đời (dù chưa được đặt tên).


## Thư quảng cáo hàng loạt (Junk Mail)

Bạn biết loại này:

> Kính chào anh Martin,
> Chúc mừng!
> Chúng tôi đã chọn ANH trong tất cả mọi người sống trên đường Witchwood để tham gia vào ưu đãi tuyệt vời một lần duy nhất…

Khách hàng gửi cho chúng ta những cuộn thư mẫu khổng lồ chứa tất cả các từ trừ tên và địa chỉ, và bất kỳ yếu tố nào khác họ muốn chúng ta in. Chúng ta viết chương trình trích xuất tên, địa chỉ, và các yếu tố khác từ băng từ, và in chính xác những yếu tố đó lên đúng vị trí trên các mẫu.

Những cuộn thư mẫu này nặng 500 pound và chứa hàng ngàn lá thư. Khách hàng gửi cho chúng ta hàng trăm cuộn như vậy. Chúng ta in từng cuộn một.

Ban đầu, chúng ta có một IBM 360 làm việc in trên máy in dòng (line printer) duy nhất của nó. Chúng ta có thể in vài ngàn lá thư mỗi ca. Thật không may, điều này chiếm dụng một máy rất đắt trong thời gian rất dài. Những ngày ấy, IBM 360 thuê với giá hàng chục nghìn đô la mỗi tháng.

Vì vậy, chúng ta bảo hệ điều hành dùng băng từ thay vì máy in dòng. Chương trình của chúng ta không quan tâm, vì chúng đã được viết để dùng các trừu tượng IO của hệ điều hành.

IBM 360 có thể đẩy ra một cuộn băng đầy trong 10 phút, đủ để in vài cuộn thư mẫu.

Giá trị của độc lập thiết bị là rất lớn! Chúng ta có thể viết chương trình mà không cần biết hay quan tâm thiết bị nào sẽ được sử dụng. Ta có thể kiểm thử chương trình trên máy tính nối với máy in dòng cục bộ. Sau đó, ta có thể yêu cầu hệ điều hành “in” ra băng từ để tạo hàng trăm nghìn bức thư quảng cáo cá nhân hóa.

Chương trình của chúng ta có một hình dáng. Hình dáng đó tách biệt chính sách khỏi chi tiết. Chính sách là việc định dạng các bản ghi tên và địa chỉ. Chi tiết là thiết bị. Chúng ta đã trì hoãn quyết định về việc sẽ dùng thiết bị nào.

## Địa chỉ vật lý (Physical Addressing)

Đầu những năm 1970, tôi làm việc trên một hệ thống kế toán lớn cho một công đoàn tài xế xe tải địa phương. Chúng tôi có một ổ đĩa 25 MB để lưu bản ghi về Đại lý (Agents), Nhà tuyển dụng (Employers) và Thành viên (Members). Các bản ghi có kích thước khác nhau, nên chúng tôi định dạng vài trụ đầu tiên của đĩa sao cho mỗi sector vừa với một bản ghi Đại lý. Vài trụ tiếp theo được định dạng để chứa các sector vừa với bản ghi Nhà tuyển dụng. Những trụ cuối cùng dành cho các bản ghi Thành viên.

Chúng ta viết phần mềm biết chính xác cấu trúc vật lý của đĩa. Mã biết đĩa có 200 trụ (cylinders) và 10 đầu đọc (heads), mỗi trụ có vài chục sector trên mỗi đầu. Nó biết trụ nào chứa dữ liệu Đại lý, Nhà tuyển dụng và Thành viên. Tất cả thông tin đó được đóng cứng (hard-wired) vào mã.

Chúng ta duy trì một chỉ mục (index) trên đĩa để tra cứu từng Đại lý, Nhà tuyển dụng và Thành viên. Chỉ mục nằm trên một nhóm trụ khác được định dạng đặc biệt. Chỉ mục Đại lý chứa các bản ghi lưu ID của đại lý cùng số trụ, số đầu đọc và số sector của bản ghi đó. Nhà tuyển dụng và Thành viên có chỉ mục tương tự. Các bản ghi Thành viên còn được nối thành danh sách liên kết đôi (doubly linked list) trên đĩa. Mỗi bản ghi lưu số trụ, số đầu đọc và số sector của bản ghi Thành viên kế tiếp và trước đó.

Nếu cần nâng cấp lên ổ đĩa mới có nhiều đầu đọc hơn, nhiều trụ hơn hoặc nhiều sector hơn trên mỗi trụ thì sao? Chúng ta phải viết chương trình đặc biệt để đọc dữ liệu từ ổ cũ rồi ghi sang ổ mới, điều chỉnh mọi số trụ, đầu đọc và sector. Chúng ta cũng phải sửa tất cả các giá trị đóng cứng trong mã, mà chúng lại nằm rải rác khắp nơi. Mọi quy tắc nghiệp vụ đều biết sơ đồ trụ, đầu đọc và sector chi tiết.

Một ngày nọ, một lập trình viên giàu kinh nghiệm hơn gia nhập nhóm. Khi thấy những gì chúng ta đã làm, mặt anh tái mét. Anh nhìn chúng ta kinh hoàng như thể chúng ta là người ngoài hành tinh. Rồi anh nhẹ nhàng khuyên nên đổi sơ đồ địa chỉ sang địa chỉ tương đối (relative addresses).

Người đồng nghiệp giàu kinh nghiệm hơn gợi ý xem đĩa như một mảng tuyến tính khổng lồ gồm các sector, mỗi sector được đánh địa chỉ bằng một số nguyên liên tiếp. Khi đó, ta có thể viết một chương trình chuyển đổi nhỏ, biết cấu trúc vật lý của đĩa và chuyển đổi địa chỉ tương đối sang số trụ, đầu đọc và sector ngay khi cần (on the fly).

May mắn cho chúng ta, chúng ta đã nghe theo lời khuyên. Chúng ta thay đổi chính sách cấp cao của hệ thống để trung lập về cấu trúc vật lý của đĩa. Điều đó cho phép chúng ta tách rời quyết định về cấu trúc ổ đĩa khỏi ứng dụng.

## Kết luận

Hai câu chuyện nhỏ trong chương này minh họa nguyên tắc mà các kiến trúc sư áp dụng ở quy mô lớn. Kiến trúc sư giỏi tách biệt chi tiết khỏi chính sách, rồi tách chính sách khỏi chi tiết đến mức chính sách không biết và không phụ thuộc vào bất kỳ chi tiết nào. Họ thiết kế chính sách sao cho các quyết định về chi tiết có thể được trì hoãn, và giữ nguyên lựa chọn ấy càng lâu càng tốt.