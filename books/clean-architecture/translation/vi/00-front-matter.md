# Lời tựa

Khi nói về kiến trúc, chúng ta đang nói đến điều gì?

Cũng như mọi phép ẩn dụ, nhìn phần mềm qua lăng kính kiến trúc có thể giúp ta thấy rõ một số điều, đồng thời che khuất những điều khác. Nó có thể hứa nhiều hơn khả năng thực hiện, nhưng cũng có thể làm được nhiều hơn những gì đã hứa.

Sức hấp dẫn dễ thấy của kiến trúc nằm ở cấu trúc. Cấu trúc chi phối các mô hình và cuộc thảo luận về phát triển phần mềm: thành phần, lớp, hàm, mô-đun, tầng, dịch vụ lớn nhỏ. Nhưng cấu trúc tổng thể của nhiều hệ thống phần mềm lại khiến người ta khó tin hoặc khó hiểu. Có những sơ đồ doanh nghiệp kiểu Xô Viết được định sẵn thành mã cũ; những tháp Jenga chông chênh vươn lên đám mây; những tầng khảo cổ bị chôn trong dòng trượt của một mớ bòng bong. Cấu trúc phần mềm không hiển nhiên tuân theo trực giác của chúng ta như cấu trúc tòa nhà.

Tòa nhà có cấu trúc vật lý dễ nhận thấy, dù đặt trên đá hay bê tông, vươn cao thành vòm hay trải rộng, dù lớn hay nhỏ, lộng lẫy hay bình thường. Cấu trúc của chúng buộc phải tuân theo trọng lực và đặc tính vật liệu. Phần mềm thì ít phải bận tâm đến trọng lực, trừ khi ta dùng từ ấy để nói về mức độ nghiêm trọng. Vậy phần mềm được làm từ gì? Khác với tòa nhà làm bằng gạch, bê tông, gỗ, thép và kính, phần mềm được làm từ phần mềm. Những cấu trúc phần mềm lớn được ghép từ các thành phần nhỏ hơn, rồi những thành phần ấy lại được ghép từ các thành phần nhỏ hơn nữa. Cứ thế mãi, như những con rùa chồng lên nhau.

Khi nói về kiến trúc phần mềm, ta đang nói về một thứ có bản chất đệ quy và phân dạng, được khắc họa trong mã. Mọi thứ đều là chi tiết. Các cấp độ chi tiết đan xen cũng góp phần tạo nên kiến trúc tòa nhà, nhưng nói về quy mô vật lý trong phần mềm thì không có nhiều ý nghĩa. Phần mềm có cấu trúc, có nhiều cấu trúc và nhiều kiểu cấu trúc; sự đa dạng ấy vượt xa những gì ta thấy trong công trình xây dựng. Thậm chí, có thể lập luận khá thuyết phục rằng hoạt động thiết kế và sự tập trung vào thiết kế trong phần mềm còn nhiều hơn trong kiến trúc công trình. Theo nghĩa đó, gọi kiến trúc phần mềm là “kiến trúc” còn sát nghĩa hơn gọi kiến trúc tòa nhà như vậy!

Con người hiểu quy mô vật lý và thường tìm kiếm nó trong thế giới xung quanh. Dù sơ đồ PowerPoint trông hấp dẫn và dễ nhìn, những chiếc hộp trên sơ đồ không phải là kiến trúc của hệ thống phần mềm. Chúng chắc chắn thể hiện một góc nhìn về kiến trúc, nhưng nếu nhầm các hộp ấy với toàn cảnh, với chính kiến trúc, ta sẽ bỏ lỡ cả hai. Kiến trúc phần mềm không có một hình dạng cố định. Một cách trực quan hóa cụ thể là lựa chọn, không phải điều tất yếu. Lựa chọn ấy lại dựa trên nhiều lựa chọn khác: đưa gì vào, bỏ gì đi, nhấn mạnh điều gì bằng hình dạng hoặc màu sắc, làm mờ điều gì bằng cách trình bày đồng đều hoặc lược bỏ. Không có góc nhìn nào tự nhiên hay vốn dĩ ưu việt hơn góc nhìn khác.

Dù nói về vật lý hay quy mô vật lý trong kiến trúc phần mềm không thật phù hợp, chúng ta vẫn quan tâm đến một số giới hạn vật lý. Tốc độ bộ xử lý và băng thông mạng có thể quyết định khắc nghiệt hiệu năng của hệ thống. Bộ nhớ và lưu trữ có thể giới hạn tham vọng của bất kỳ cơ sở mã nào. Phần mềm có thể được dệt từ những giấc mơ, nhưng nó vẫn vận hành trong thế giới vật chất.

> “Đây là điều quái dị của tình yêu, thưa nàng: ý chí thì vô hạn, còn việc thực hiện lại bị giới hạn; khát vọng thì vô biên, nhưng hành động phải làm nô lệ cho giới hạn.”
>
> (William Shakespeare)

Thế giới vật chất là nơi chúng ta, công ty và nền kinh tế của mình tồn tại. Nhờ đó, ta có thêm một thước đo để hiểu kiến trúc phần mềm: những lực và đại lượng ít mang tính vật lý hơn, nhưng vẫn có thể dùng để trao đổi và suy luận.

> “Kiến trúc thể hiện những quyết định thiết kế quan trọng định hình hệ thống; mức độ quan trọng được đo bằng chi phí thay đổi.”
>
> (Grady Booch)

Thời gian, tiền bạc và công sức giúp ta hình dung quy mô, phân biệt việc lớn với việc nhỏ, phần thuộc về kiến trúc với phần còn lại. Chúng cũng cho ta cách đánh giá kiến trúc có tốt hay không: kiến trúc tốt đáp ứng nhu cầu của người dùng, người phát triển và chủ sở hữu ở một thời điểm nhất định, đồng thời tiếp tục đáp ứng những nhu cầu ấy theo thời gian.

> “Nếu bạn cho rằng kiến trúc tốt tốn kém, hãy thử dùng kiến trúc tồi.”
>
> (Brian Foote và Joseph Yoder)

Những thay đổi thường xảy ra trong quá trình phát triển hệ thống không nên trở thành các thay đổi tốn kém, khó thực hiện, phải lập dự án riêng để quản lý thay vì được đưa vào nhịp công việc hằng ngày và hằng tuần.

Từ đó nảy sinh một vấn đề liên quan đến vật lý, cũng chẳng nhỏ chút nào: du hành thời gian. Làm sao biết trước những thay đổi thường gặp để đưa ra các quyết định quan trọng dựa trên chúng? Làm sao giảm công sức và chi phí phát triển trong tương lai nếu không có quả cầu tiên tri hay cỗ máy thời gian?

> “Kiến trúc gồm những quyết định mà ta ước mình có thể đưa ra đúng ngay từ đầu dự án, nhưng khả năng ta làm đúng chúng cũng chẳng cao hơn khả năng làm đúng bất kỳ quyết định nào khác.”
>
> (Ralph Johnson)

Hiểu quá khứ vốn đã khó; nắm bắt hiện tại thì luôn chông chênh; còn dự đoán tương lai chẳng phải chuyện đơn giản.

Đây là lúc con đường rẽ ra nhiều hướng.

Con đường tối tăm nhất dẫn đến quan niệm rằng kiến trúc vững chắc, ổn định phải dựa vào quyền uy và sự cứng nhắc. Nếu thay đổi tốn kém thì hãy loại bỏ thay đổi, dập tắt nguyên nhân hoặc đẩy chúng vào một mê cung quan liêu. Kiến trúc sư nắm quyền tuyệt đối, còn kiến trúc trở thành một xã hội phản địa đàng với các nhà phát triển và là nguồn bực bội triền miên cho tất cả mọi người.

Một con đường khác nồng nặc mùi khái quát hóa suy đoán. Lối đi ấy rải đầy phỏng đoán hard-code, vô số tham số, những ngôi mộ chứa mã chết và độ phức tạp ngẫu nhiên nhiều đến mức ngân sách bảo trì cũng không gánh nổi.

Con đường chúng tôi quan tâm nhất là con đường sạch nhất. Nó thừa nhận phần mềm vốn mềm dẻo và muốn giữ đặc tính ấy thành một thuộc tính hạng nhất của hệ thống. Nó chấp nhận rằng hiểu biết của chúng ta luôn không đầy đủ, đồng thời hiểu rằng con người vốn thường xuyên làm việc trong hoàn cảnh thiếu thông tin, và chúng ta làm việc ấy khá tốt. Con đường này phát huy sở trường thay vì khoét sâu điểm yếu. Chúng ta tạo ra sự vật rồi khám phá chúng. Chúng ta đặt câu hỏi và tiến hành thí nghiệm. Kiến trúc tốt hình thành khi ta xem việc xây dựng nó như một hành trình chứ không phải đích đến, như một quá trình tìm hiểu không ngừng chứ không phải một hiện vật bất động.

> “Kiến trúc là một giả thuyết, cần được kiểm chứng bằng việc triển khai và đo lường.”
>
> (Tom Gilb)

Bước đi trên con đường ấy đòi hỏi sự cẩn trọng và chú ý, suy nghĩ và quan sát, thực hành và nguyên tắc. Thoạt nghe có thể tưởng là chậm, nhưng mọi thứ phụ thuộc vào cách ta bước đi.

> “Muốn đi nhanh, hãy làm cho tốt.”
>
> (Robert C. Martin)

Chúc bạn tận hưởng hành trình.

> (Kevlin Henney, tháng 5 năm 2017)

## Lời nói đầu

Tên cuốn sách này là *Clean Architecture*. Đó là một cái tên đầy tham vọng. Có người còn cho rằng nó ngạo mạn. Vì sao tôi chọn tên ấy, và vì sao tôi viết cuốn sách này?

Tôi viết dòng mã đầu tiên năm 1964, khi mới 12 tuổi. Năm nay là 2016; như vậy tôi đã viết mã hơn nửa thế kỷ. Trong thời gian ấy, tôi học được một số điều về cách cấu trúc hệ thống phần mềm mà tôi nghĩ người khác cũng có thể thấy hữu ích.

Tôi học được những điều đó bằng cách xây dựng nhiều hệ thống, lớn có nhỏ có. Tôi từng làm hệ thống nhúng nhỏ và hệ thống xử lý theo lô lớn; hệ thống thời gian thực và hệ thống web; ứng dụng dòng lệnh, giao diện đồ họa, điều khiển quy trình, trò chơi, kế toán, viễn thông, công cụ thiết kế, ứng dụng vẽ và nhiều loại khác.

Tôi từng xây dựng ứng dụng đơn luồng, đa luồng, dùng một vài tiến trình nặng hoặc nhiều tiến trình nhẹ, đa bộ xử lý, cơ sở dữ liệu, toán học, hình học tính toán và nhiều loại khác nữa.

Tôi đã xây dựng rất nhiều ứng dụng, rất nhiều hệ thống. Nhìn lại tất cả chúng, tôi rút ra một điều khiến mình kinh ngạc:

> Các quy tắc kiến trúc đều giống nhau!

Điều đó thật bất ngờ vì các hệ thống tôi từng xây dựng khác nhau đến mức cực đoan. Vì sao những hệ thống khác xa nhau như vậy lại tuân theo các quy tắc kiến trúc tương tự? Tôi kết luận rằng quy tắc kiến trúc phần mềm độc lập với mọi biến số khác.

Kết luận ấy càng đáng ngạc nhiên khi nhìn vào những thay đổi của phần cứng trong nửa thế kỷ đó. Tôi bắt đầu lập trình trên những cỗ máy lớn như tủ lạnh nhà bếp, có chu kỳ nửa megahertz, bộ nhớ lõi 4K, bộ nhớ đĩa 32K và giao diện teletype truyền được 10 ký tự mỗi giây. Còn tôi đang viết lời nói đầu này trên xe buýt trong chuyến đi qua Nam Phi. Tôi dùng MacBook có bốn lõi i7, mỗi lõi chạy ở tốc độ 2,8 gigahertz. Máy có RAM 16 gigabyte, SSD một terabyte và màn hình Retina 2880×1800 hiển thị được video độ phân giải rất cao. Chênh lệch năng lực tính toán thật choáng ngợp. Một phép phân tích hợp lý cho thấy chiếc MacBook này mạnh hơn ít nhất $10^{22}$ lần những máy tính đầu tiên tôi dùng cách đây nửa thế kỷ.

Hai mươi hai bậc độ lớn là một con số khổng lồ. Đó là số ångström từ Trái Đất đến Alpha-Centuri. Đó là số electron trong tiền lẻ trong túi hoặc ví của bạn. Và con số ấy, ít nhất là con số ấy, thể hiện mức tăng năng lực tính toán tôi đã trải qua trong đời mình.

Với mức tăng năng lực tính toán khổng lồ đó, phần mềm tôi viết thay đổi ra sao? Chắc chắn nó lớn hơn. Trước kia, tôi nghĩ 2.000 dòng mã là một chương trình lớn. Dù sao, đó là cả một hộp thẻ đục lỗ nặng 10 pound. Giờ đây, một chương trình chỉ thật sự lớn khi vượt quá 100.000 dòng.

Phần mềm cũng chạy hiệu quả hơn nhiều. Ngày nay, chúng ta làm được những việc mà thập niên 1960 khó lòng tưởng tượng. *The Forbin Project*, *The Moon Is a Harsh Mistress* và *2001: A Space Odyssey* đều từng hình dung tương lai hiện tại, nhưng đã dự đoán trật khá xa. Những tác phẩm ấy tưởng tượng ra các cỗ máy khổng lồ có ý thức. Thực tế, chúng ta có những cỗ máy nhỏ đến khó tin, nhưng vẫn chỉ là máy móc.

Còn một điều khác về phần mềm ngày nay so với phần mềm ngày trước: nó được tạo nên từ cùng một thứ. Nó vẫn gồm các câu lệnh `if`, câu lệnh gán và vòng lặp `while`.

Bạn có thể phản đối rằng chúng ta đã có ngôn ngữ tốt hơn và mô hình lập trình ưu việt hơn. Dù sao thì ta cũng lập trình bằng Java, C# hoặc Ruby, dùng thiết kế hướng đối tượng. Đúng vậy, nhưng mã vẫn là sự kết hợp của trình tự, lựa chọn và lặp, đúng như hồi thập niên 1960 và 1950. Quan sát kỹ thực hành lập trình máy tính, ta sẽ nhận ra rất ít điều thay đổi trong 50 năm. Ngôn ngữ tốt hơn một chút. Công cụ tốt hơn rất nhiều. Nhưng các khối xây dựng cơ bản của chương trình máy tính vẫn nguyên như cũ.

Nếu đưa một lập trình viên từ năm 1966 đến năm 2016, đặt cô ấy¹ trước chiếc MacBook của tôi đang chạy IntelliJ và chỉ cho cô ấy Java, có lẽ cô ấy cần 24 giờ để hết choáng. Sau đó, cô ấy vẫn viết mã được. Java chẳng khác C nhiều, thậm chí cũng không khác Fortran bao nhiêu.

Nếu đưa bạn về năm 1966, chỉ cho bạn cách viết và sửa mã PDP-8 bằng cách đục băng giấy trên chiếc teletype 10 ký tự mỗi giây, có lẽ bạn cần 24 giờ để hết thất vọng. Sau đó, bạn vẫn viết mã được. Mã không thay đổi nhiều đến thế.

Bí mật nằm ở đây: mã không thay đổi là lý do khiến các quy tắc kiến trúc phần mềm nhất quán giữa nhiều loại hệ thống. Quy tắc kiến trúc phần mềm là quy tắc sắp xếp và lắp ghép các khối xây dựng chương trình. Vì những khối ấy phổ biến và không thay đổi, quy tắc sắp xếp chúng cũng phổ biến và bất biến.

Lập trình viên trẻ có thể cho rằng điều đó vô lý. Họ có thể khăng khăng rằng mọi thứ ngày nay đều mới và khác, rằng các quy tắc cũ đã lỗi thời. Nếu nghĩ vậy, họ đã nhầm nghiêm trọng. Các quy tắc vẫn vậy. Bất chấp ngôn ngữ, framework và mô hình mới, các quy tắc hiện nay vẫn giống thời Alan Turing viết mã máy đầu tiên vào năm 1946.

Có một điều đã thay đổi: trước kia, chúng ta chưa biết những quy tắc ấy là gì, nên cứ vi phạm chúng hết lần này đến lần khác. Sau nửa thế kỷ kinh nghiệm, giờ đây chúng ta đã hiểu được chúng.

Cuốn sách này nói về chính những quy tắc ấy, những quy tắc không đổi theo thời gian.

Đăng ký bản Clean Architecture của bạn trên trang InformIT để nhận các bản cập nhật và sửa lỗi khi chúng được phát hành. Để đăng ký, truy cập `informit.com/register` rồi đăng nhập hoặc tạo tài khoản. Nhập ISBN sản phẩm `9780134494166` và nhấn Submit. Mở thẻ Registered Products, tìm liên kết Access Bonus Content bên cạnh sản phẩm này, rồi truy cập tài liệu bổ sung theo liên kết đó.

¹ Người lập trình năm 1966 rất có thể là nữ, vì thời ấy phụ nữ chiếm một phần lớn trong lực lượng lập trình viên.

## Lời cảm ơn

Những người đã góp phần tạo nên cuốn sách này, không theo thứ tự cụ thể:

Chris Guzikowski, Chris Zahn, Matt Heuser, Jeff Overbey, Micah Martin, Justin Martin, Carl Hickman, James Grenning, Simon Brown, Kevlin Henney, Jason Gorman, Doug Bradbury, Colin Jones, Grady Booch, Kent Beck, Martin Fowler, Alistair Cockburn, James O. Coplien, Tim Conrad, Richard Lloyd, Ken Finder, Kris Iyer (CK), Mike Carew, Jerry Fitzpatrick, Jim Newkirk, Ed Thelen, Joe Mabel và Bill Degnan.

Còn rất nhiều người khác không thể kể hết.

Trong lần đọc soát cuối cuốn sách, khi đọc chương về Kiến trúc biết nói, nụ cười rạng rỡ và tiếng cười du dương của Jim Weirich vang lên trong tâm trí tôi. Chúc Jim lên đường bình an!

## Về tác giả
![Robert C. Martin](assets/illustrations/00-about-author.png){w=240}

Robert C. Martin (Uncle Bob) là lập trình viên từ năm 1970. Ông đồng sáng lập cleancoders.com, trang cung cấp khóa học video trực tuyến cho nhà phát triển phần mềm, và sáng lập Uncle Bob Consulting LLC, đơn vị cung cấp dịch vụ tư vấn phần mềm, đào tạo và phát triển kỹ năng cho các tập đoàn lớn trên toàn thế giới. Ông từng giữ chức Master Craftsman tại 8th Light, Inc., công ty tư vấn phần mềm ở Chicago. Ông đã đăng hàng chục bài viết trên các tạp chí chuyên ngành và thường xuyên diễn thuyết tại hội nghị, triển lãm quốc tế. Ông làm tổng biên tập *C++ Report* trong ba năm và là chủ tịch đầu tiên của Agile Alliance.

Martin là tác giả và biên tập viên của nhiều cuốn sách, trong đó có *The Clean Coder*, *Clean Code*, *UML for Java Programmers*, *Agile Software Development*, *Extreme Programming in Practice*, *More C++ Gems*, *Pattern Languages of Program Design 3* và *Designing Object Oriented C++ Applications Using the Booch Method*.

## Giới thiệu

Không cần nhiều kiến thức hay kỹ năng để khiến một chương trình chạy được. Học sinh trung học vẫn làm điều đó mỗi ngày. Sinh viên đại học lập những công ty trị giá hàng tỷ đô-la bằng cách chắp vá vài dòng PHP hoặc Ruby. Ở các văn phòng làm việc kiểu ô bàn trên khắp thế giới, vô số lập trình viên mới vào nghề cày qua những tài liệu yêu cầu khổng lồ trong hệ thống theo dõi vấn đề cồng kềnh, cố ép hệ thống “hoạt động” bằng ý chí. Mã họ viết có thể chẳng đẹp, nhưng chạy được. Vì làm cho thứ gì đó chạy được một lần vốn không khó đến vậy.

Làm cho phần mềm đúng lại là chuyện khác. Điều đó khó. Nó cần kiến thức và kỹ năng mà phần lớn lập trình viên trẻ chưa tích lũy được. Nó cần suy nghĩ và sự thấu hiểu mà nhiều lập trình viên không dành thời gian rèn luyện. Nó đòi hỏi kỷ luật và sự tận tâm ở mức mà nhiều người chưa từng nghĩ mình sẽ cần. Trên hết, nó cần niềm đam mê nghề và mong muốn trở thành một người làm nghề chuyên nghiệp.

Khi làm phần mềm cho đúng, một điều kỳ diệu xảy ra: bạn không cần hàng đống lập trình viên để duy trì nó. Bạn không cần tài liệu yêu cầu khổng lồ hay hệ thống theo dõi vấn đề cồng kềnh. Bạn cũng không cần những văn phòng đầy người ở khắp nơi cùng lập trình suốt ngày đêm.

Phần mềm được làm tốt chỉ cần một phần nhỏ nguồn lực con người để xây dựng và bảo trì. Thay đổi đơn giản và nhanh chóng. Lỗi hiếm khi xuất hiện. Công sức được giảm thiểu, còn chức năng và khả năng thích ứng được tăng tối đa. Đúng là viễn cảnh này nghe hơi lý tưởng. Nhưng tôi từng thấy nó xảy ra. Tôi đã tham gia dự án có thiết kế và kiến trúc giúp việc viết mã, bảo trì trở nên dễ dàng. Tôi đã làm những dự án chỉ cần một phần nhỏ nhân lực dự kiến. Tôi từng làm hệ thống có tỷ lệ lỗi cực thấp. Tôi đã thấy kiến trúc phần mềm tốt có thể tạo ra khác biệt lớn cho hệ thống, dự án và nhóm. Tôi đã đến miền đất hứa.

Nhưng đừng chỉ tin lời tôi. Hãy nhìn vào trải nghiệm của chính bạn. Bạn đã từng gặp tình cảnh ngược lại chưa? Bạn có từng làm trên hệ thống liên kết và phụ thuộc chằng chịt đến mức mọi thay đổi, dù nhỏ đến đâu, cũng mất hàng tuần và đầy rủi ro? Bạn đã từng chịu cảnh mã tồi và thiết kế mục nát cản trở công việc chưa? Thiết kế của những hệ thống bạn làm có từng khiến tinh thần nhóm sa sút, khách hàng mất lòng tin, còn quản lý mất kiên nhẫn không? Bạn đã từng thấy nhóm, phòng ban, thậm chí cả công ty bị kéo sụp bởi cấu trúc phần mềm mục nát chưa? Bạn đã từng xuống địa ngục lập trình chưa?

Tôi đã từng. Và ở mức độ nào đó, phần lớn chúng ta cũng vậy. Vật lộn với thiết kế phần mềm tồi phổ biến hơn nhiều so với tận hưởng niềm vui làm việc trên một thiết kế tốt.
