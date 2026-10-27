# Chương 1: Mã sạch

> Bạn đọc cuốn sách này vì hai lý do. Thứ nhất, bạn là lập trình viên. Thứ hai, bạn muốn trở thành lập trình viên giỏi hơn. Tốt. Chúng ta cần những lập trình viên giỏi hơn.

Đây là cuốn sách về lập trình tốt. Sách đầy code. Chúng ta sẽ nhìn code từ mọi hướng: từ trên xuống, từ dưới lên, rồi xuyên qua nó từ trong ra ngoài. Đọc xong, chúng ta sẽ hiểu khá nhiều về code. Hơn nữa, chúng ta sẽ phân biệt được code tốt với code xấu, biết cách viết code tốt và biến code xấu thành code tốt.

## Sẽ vẫn có code

Có người cho rằng một cuốn sách về code đã lỗi thời, rằng code không còn là vấn đề và chúng ta nên quan tâm đến mô hình cùng yêu cầu thay vì code. Quả thật, có người nói chúng ta sắp bước vào thời kỳ không còn code. Chẳng bao lâu nữa, mọi code sẽ được tạo ra thay vì viết. Lập trình viên cũng sẽ không còn cần thiết, vì người làm kinh doanh có thể tạo chương trình từ đặc tả.

Vô lý! Chúng ta sẽ không bao giờ thoát khỏi code, vì code thể hiện những chi tiết của yêu cầu. Ở một mức nào đó, không thể bỏ qua hay trừu tượng hóa các chi tiết ấy; chúng phải được đặc tả. Đặc tả yêu cầu chi tiết đến mức máy có thể thực thi chính là lập trình. Một bản đặc tả như vậy là code.

Tôi cho rằng mức trừu tượng của các ngôn ngữ chúng ta dùng sẽ tiếp tục tăng. Số lượng ngôn ngữ chuyên miền (domain-specific language) cũng sẽ tăng. Đó là điều tốt, nhưng sẽ không xóa bỏ code. Thật vậy, mọi đặc tả viết bằng những ngôn ngữ bậc cao hơn và ngôn ngữ chuyên miền ấy đều là code! Chúng vẫn phải chặt chẽ, chính xác và trang trọng, chi tiết đến mức máy có thể hiểu rồi thực thi.

Những người nghĩ rằng một ngày nào đó code sẽ biến mất cũng giống các nhà toán học hy vọng tìm ra một nền toán học không cần hình thức hóa. Họ mong một ngày chúng ta sẽ tạo được những cỗ máy làm điều mình muốn thay vì điều mình nói. Những cỗ máy ấy phải hiểu chúng ta đủ rõ để chuyển các nhu cầu được đặc tả mơ hồ thành những chương trình chạy hoàn hảo, đáp ứng chính xác các nhu cầu đó.

Điều ấy sẽ không bao giờ xảy ra. Ngay cả con người, với tất cả trực giác và óc sáng tạo, cũng chưa tạo được những hệ thống thành công chỉ từ cảm nhận mơ hồ của khách hàng. Thật vậy, nếu kỷ luật đặc tả yêu cầu đã dạy chúng ta điều gì, thì đó là yêu cầu được đặc tả tốt cũng trang trọng như code và có thể làm bài kiểm thử thực thi được cho chính code ấy!

Hãy nhớ rằng code chính là ngôn ngữ cuối cùng chúng ta dùng để diễn đạt yêu cầu. Ta có thể tạo ra những ngôn ngữ gần với yêu cầu hơn, cùng những công cụ giúp phân tích và ghép các yêu cầu thành cấu trúc trang trọng. Nhưng độ chính xác cần thiết sẽ không bao giờ mất đi, nên code sẽ luôn tồn tại.

## Mã xấu

Gần đây tôi đọc lời tựa cuốn *Implementation Patterns* của Kent Beck.[^1] Ông viết: “... cuốn sách này dựa trên một tiền đề khá mong manh: rằng code tốt có ý nghĩa ...” Một tiền đề mong manh ư? Tôi không đồng ý! Theo tôi, đó là một trong những tiền đề vững chắc, được ủng hộ rộng rãi và bị lạm dụng nhiều nhất trong nghề của chúng ta (và tôi nghĩ Kent biết điều đó). Chúng ta biết code tốt có ý nghĩa vì đã quá lâu phải sống chung với sự thiếu vắng nó.

![Kent Beck](assets/illustrations/01-kent-beck.png){w=144}


Tôi biết một công ty vào cuối thập niên 80 đã viết ra một ứng dụng cực kỳ ăn khách. Sản phẩm rất phổ biến, được nhiều chuyên gia mua và sử dụng. Rồi các chu kỳ phát hành bắt đầu kéo dài. Lỗi không được sửa từ bản phát hành này sang bản tiếp theo. Thời gian tải tăng lên, số lần sụp cũng nhiều hơn. Tôi nhớ ngày mình tắt sản phẩm trong cơn bực bội và không bao giờ dùng lại. Không lâu sau, công ty phá sản.

Hai thập kỷ sau, tôi gặp một trong những nhân viên đầu tiên của công ty ấy và hỏi chuyện gì đã xảy ra. Câu trả lời xác nhận nỗi lo của tôi. Họ vội đưa sản phẩm ra thị trường và để lại một mớ hỗn độn khổng lồ trong code. Càng thêm tính năng, code càng tệ, cho đến khi họ không còn quản lý nổi. Chính code xấu đã kéo công ty xuống.

Bạn đã bao giờ bị code xấu cản trở đáng kể chưa? Nếu đã có chút kinh nghiệm lập trình, hẳn bạn từng gặp chuyện đó nhiều lần. Thật vậy, chúng ta có một từ để gọi nó: “lội”. Chúng ta lội qua code xấu, lê bước trong một đầm lầy đầy bụi gai rối rắm và cạm bẫy ẩn giấu. Ta cố tìm đường, mong bắt gặp một gợi ý, một manh mối về chuyện đang diễn ra. Nhưng thứ duy nhất hiện ra lại là thêm nhiều code vô nghĩa.

Dĩ nhiên bạn từng bị code xấu cản trở. Vậy tại sao bạn lại viết ra nó?

Bạn muốn làm nhanh? Bạn đang vội? Có lẽ vậy. Có thể bạn nghĩ mình không có thời gian làm cho tử tế, hoặc sếp sẽ nổi giận nếu bạn dành thời gian dọn dẹp code. Có thể bạn đã mệt với chương trình này và chỉ muốn kết thúc. Hoặc nhìn vào đống việc khác đã hứa sẽ làm, bạn nhận ra mình phải ghép vội module này để còn chuyển sang việc tiếp theo. Ai trong chúng ta cũng từng như vậy.

Ai trong chúng ta cũng từng nhìn mớ hỗn độn vừa tạo ra rồi để dành việc dọn dẹp cho hôm khác. Ta từng nhẹ nhõm khi thấy chương trình bừa bộn chạy được và nghĩ rằng một mớ hỗn độn còn chạy được vẫn hơn là chẳng có gì. Ta cũng từng hẹn sẽ quay lại dọn sau. Hồi ấy, dĩ nhiên, chúng ta chưa biết định luật LeBlanc: Sau này nghĩa là không bao giờ.

## Tổng chi phí sở hữu một mớ hỗn độn

Nếu đã làm lập trình viên hơn hai ba năm, có lẽ bạn từng bị code bừa bộn của người khác làm chậm đi đáng kể. Làm lâu hơn nữa, hẳn bạn cũng từng bị code bừa bộn làm chậm. Mức độ chậm lại có thể rất lớn. Trong một hai năm, những nhóm khởi đầu dự án với tốc độ rất nhanh có thể thấy mình bò chậm như sên. Mỗi thay đổi lại làm hỏng hai ba chỗ khác trong code. Không thay đổi nào là nhỏ. Mỗi lần thêm hay sửa hệ thống, họ đều phải “hiểu” những mớ rối, chỗ xoắn và nút thắt trước khi có thể thêm vào đó những mớ rối, chỗ xoắn và nút thắt mới. Dần dà, mớ hỗn độn lớn đến mức không thể dọn nổi. Hoàn toàn không còn cách nào.

Mớ hỗn độn càng lớn, năng suất của nhóm càng giảm, dần tiến về không. Khi năng suất đi xuống, ban quản lý chỉ còn biết thêm người vào dự án, hy vọng năng suất sẽ tăng. Nhưng người mới không nắm thiết kế hệ thống. Họ không biết phân biệt thay đổi phù hợp với ý đồ thiết kế và thay đổi phá vỡ ý đồ ấy. Hơn nữa, tất cả mọi người trong nhóm đều chịu áp lực khủng khiếp phải tăng năng suất. Thế là họ tạo ra ngày càng nhiều mớ hỗn độn, khiến năng suất tiếp tục tụt về không. (Xem Hình 1-1.)

**Hình 1-1**
*Năng suất theo thời gian*

### Cuộc đại tái thiết kế trên trời

Cuối cùng, nhóm nổi loạn. Họ báo với ban quản lý rằng không thể tiếp tục phát triển trên code base đáng ghét này và đòi thiết kế lại. Ban quản lý không muốn bỏ nguồn lực vào việc thiết kế lại toàn bộ dự án, nhưng cũng không thể phủ nhận năng suất đang rất tệ. Cuối cùng, họ nhượng bộ trước yêu cầu của các nhà phát triển và phê duyệt cuộc đại tái thiết kế trên trời.

Một nhóm hổ mới được chọn. Ai cũng muốn vào nhóm này vì đây là dự án bắt đầu từ đầu. Họ được làm lại và tạo ra một thứ thật sự đẹp. Nhưng chỉ những người giỏi nhất và sáng giá nhất được chọn. Những người còn lại phải tiếp tục bảo trì hệ thống hiện tại.

Giờ hai nhóm chạy đua. Nhóm hổ phải xây dựng hệ thống mới có đủ mọi chức năng của hệ thống cũ. Họ còn phải theo kịp những thay đổi liên tục được đưa vào hệ thống cũ. Ban quản lý sẽ không thay hệ thống cũ cho đến khi hệ thống mới làm được mọi thứ mà hệ thống cũ làm.

Cuộc đua ấy có thể kéo dài rất lâu. Tôi từng thấy nó mất 10 năm. Đến khi hoàn tất, những thành viên ban đầu của nhóm hổ đã rời đi từ lâu, còn các thành viên hiện tại lại đòi thiết kế lại hệ thống mới vì nó quá bừa bộn.

Nếu từng trải qua dù chỉ một phần nhỏ của câu chuyện này, bạn hẳn đã hiểu rằng dành thời gian giữ code sạch không chỉ có lợi về chi phí, mà còn là chuyện sống còn trong nghề.

### Thái độ

Bạn đã bao giờ lội qua một mớ hỗn độn nghiêm trọng đến mức phải mất hàng tuần để làm việc lẽ ra chỉ mất vài giờ chưa? Bạn đã từng thấy một thay đổi lẽ ra chỉ cần một dòng lại phải thực hiện ở hàng trăm module khác nhau chưa? Những chuyện này xảy ra quá thường xuyên.

Vì sao code lại thành ra như vậy? Vì sao code tốt nhanh chóng mục ruỗng thành code xấu? Chúng ta có đủ kiểu giải thích. Ta than phiền rằng yêu cầu thay đổi theo cách phá vỡ thiết kế ban đầu, than tiến độ quá gấp khiến không thể làm cho đúng. Ta lải nhải về những ông sếp ngốc nghếch, khách hàng thiếu bao dung, dân marketing vô dụng và những kẻ làm sạch điện thoại. Nhưng lỗi, Dilbert thân mến, không nằm ở các vì sao, mà ở chính chúng ta. Chúng ta thiếu tính chuyên nghiệp.

Đây có thể là viên thuốc đắng khó nuốt. Sao mớ hỗn độn này lại là lỗi của chúng ta? Còn yêu cầu, tiến độ thì sao? Những ông sếp ngốc nghếch và dân marketing vô dụng chẳng phải cũng phải chịu một phần trách nhiệm ư?

Không. Người quản lý và dân marketing trông cậy vào chúng ta để có thông tin họ cần, từ đó đưa ra lời hứa và cam kết. Ngay cả khi họ không hỏi, chúng ta cũng không nên ngại nói rõ suy nghĩ của mình. Người dùng trông vào chúng ta để xác nhận yêu cầu sẽ khớp với hệ thống ra sao. Quản lý dự án trông vào chúng ta để cùng lập tiến độ. Chúng ta tham gia sâu vào việc lập kế hoạch và cùng chịu phần lớn trách nhiệm cho mọi thất bại, nhất là những thất bại do code xấu!

“Nhưng khoan!” bạn nói. “Nếu tôi không làm điều sếp bảo, tôi sẽ bị sa thải.” Có lẽ không đâu. Hầu hết người quản lý muốn nghe sự thật, kể cả khi họ không thể hiện như vậy. Họ muốn code tốt, kể cả khi đang ám ảnh về tiến độ. Họ có thể hết lòng bảo vệ tiến độ và yêu cầu; đó là việc của họ. Còn việc của bạn là hết lòng bảo vệ code.

Để thấy rõ điều này, hãy tưởng tượng bạn là bác sĩ, có một bệnh nhân yêu cầu bỏ qua việc rửa tay tưởng như vô nghĩa trước ca mổ vì mất quá nhiều thời gian.[^2] Bệnh nhân rõ ràng là ông chủ, vậy mà bác sĩ phải kiên quyết từ chối. Vì sao? Bác sĩ hiểu nguy cơ bệnh tật và nhiễm trùng hơn bệnh nhân. Làm theo yêu cầu ấy sẽ là thiếu chuyên nghiệp, chưa kể còn phạm pháp.

Lập trình viên cũng vậy. Uốn theo ý muốn của những người quản lý không hiểu rủi ro khi tạo ra mớ hỗn độn là thiếu chuyên nghiệp.

### Nghịch lý căn bản

Lập trình viên đối mặt với một nghịch lý về những giá trị cơ bản. Nhà phát triển nào có vài năm kinh nghiệm cũng biết những mớ hỗn độn trước đây làm mình chậm lại. Vậy mà ai cũng cảm thấy áp lực phải tạo thêm mớ hỗn độn để kịp hạn chót. Nói ngắn gọn, họ không dành thời gian để đi nhanh!

Người chuyên nghiệp thật sự biết vế thứ hai của nghịch lý là sai. Tạo ra mớ hỗn độn không giúp bạn kịp hạn. Nó lập tức làm bạn chậm lại và khiến bạn trễ hạn. Cách duy nhất để kịp hạn, cũng là cách duy nhất để đi nhanh, là luôn giữ code sạch hết mức có thể.

### Nghệ thuật của mã sạch?

Giả sử bạn tin rằng code bừa bộn là trở ngại đáng kể, và chấp nhận rằng cách duy nhất để đi nhanh là giữ code sạch. Khi ấy, bạn phải tự hỏi: “Làm sao để viết code sạch?” Cố viết code sạch mà không biết code sạch nghĩa là gì thì chẳng ích gì!

Tin xấu là viết code sạch cũng giống như vẽ tranh. Hầu hết chúng ta đều nhận ra một bức tranh đẹp hay dở, nhưng biết phân biệt nghệ thuật hay với dở không có nghĩa là biết vẽ. Tương tự, nhận ra code sạch hay bẩn không có nghĩa là biết viết code sạch!

Viết code sạch đòi hỏi kỷ luật áp dụng vô số kỹ thuật nhỏ, cùng một “cảm giác sạch sẽ” phải rèn luyện rất lâu mới có. “Cảm giác code” ấy là điều cốt yếu. Một số người sinh ra đã có nó, số khác phải vất vả mới có được. Nó giúp ta nhận ra code tốt hay xấu, đồng thời chỉ cho ta cách dùng kỷ luật để biến code xấu thành code sạch.

Lập trình viên không có “cảm giác code” có thể nhìn module bừa bộn và nhận ra mớ hỗn độn, nhưng không biết phải làm gì. Người có “cảm giác code” sẽ nhìn thấy nhiều lựa chọn và cách biến đổi. Cảm giác ấy giúp họ chọn phương án tốt nhất, rồi vạch ra một chuỗi thay đổi giữ nguyên hành vi để đi từ đây đến đó.

Nói ngắn gọn, lập trình viên viết code sạch là một nghệ sĩ có thể đưa màn hình trắng qua một chuỗi biến đổi cho đến khi thành một hệ thống được lập trình thanh lịch.

### Mã sạch là gì?

Có lẽ mỗi lập trình viên có một định nghĩa riêng. Vì vậy, tôi đã hỏi một số lập trình viên nổi tiếng, giàu kinh nghiệm xem họ nghĩ gì.

![Bjarne Stroustrup](assets/illustrations/01-bjarne-stroustrup.png){w=144}

**Bjarne Stroustrup, người phát minh ra C++ và tác giả cuốn *The C++ Programming Language***

> Tôi muốn code của mình vừa thanh lịch vừa hiệu quả. Logic phải thẳng thắn để lỗi khó ẩn nấp, phụ thuộc phải tối thiểu để dễ bảo trì, xử lý lỗi phải đầy đủ theo một chiến lược rõ ràng, hiệu năng phải gần mức tối ưu để người ta không bị cám dỗ làm code bừa bộn bằng những tối ưu hóa thiếu nguyên tắc. Mã sạch làm tốt một việc.

Bjarne dùng từ “thanh lịch”. Quả là một từ đáng chú ý! Từ điển trên chiếc MacBook® của tôi định nghĩa nó là duyên dáng, phong cách trong diện mạo hoặc cử chỉ; tài tình và giản dị. Hãy để ý chữ “dễ chịu” trong các định nghĩa ấy. Có lẽ Bjarne cho rằng đọc code sạch cũng dễ chịu. Đọc nó phải khiến bạn mỉm cười, như khi nghe một chiếc hộp nhạc được chế tác khéo hay ngắm một chiếc xe thiết kế đẹp.

Bjarne cũng nhắc đến hiệu quả, đến hai lần. Có lẽ điều đó không lạ khi ông là người phát minh ra C++, nhưng theo tôi, ý ông không chỉ là mong muốn tốc độ. Chu kỳ máy bị lãng phí thì thiếu thanh lịch, chẳng dễ chịu gì. Hãy để ý từ Bjarne dùng để nói về hệ quả ấy: “cám dỗ”. Đây là một sự thật sâu sắc: code xấu khiến mớ hỗn độn ngày càng lớn! Khi sửa code xấu, người ta thường làm nó tệ hơn.

Pragmatic Dave Thomas và Andy Hunt diễn đạt ý ấy theo cách khác bằng ẩn dụ cửa sổ vỡ.[^3] Một tòa nhà có cửa sổ vỡ trông như chẳng ai quan tâm. Người khác cũng thôi quan tâm, để thêm nhiều cửa sổ vỡ. Cuối cùng, họ chủ động đập vỡ cửa sổ, bôi bẩn mặt tiền bằng hình vẽ nguệch ngoạc và để rác chất đống. Một cửa sổ vỡ khởi đầu quá trình mục ruỗng.

Bjarne còn nói xử lý lỗi phải đầy đủ. Điều đó đòi hỏi kỷ luật chú ý đến chi tiết. Xử lý lỗi qua loa là một cách lập trình viên bỏ qua chi tiết. Rò rỉ bộ nhớ là một cách khác, điều kiện tranh chấp cũng vậy. Đặt tên thiếu nhất quán cũng thế. Tóm lại, code sạch cho thấy sự chú ý sát sao đến chi tiết.

Bjarne kết luận rằng code sạch làm tốt một việc. Không phải ngẫu nhiên mà nhiều nguyên lý thiết kế phần mềm có thể gói gọn trong lời khuyên giản dị ấy. Nhiều tác giả đã cố truyền đạt cùng một ý. Code xấu cố làm quá nhiều việc, khiến ý định lẫn lộn và mục đích mơ hồ. Mã sạch tập trung. Mỗi hàm, lớp hay module đều thể hiện một mục đích duy nhất, không bị những chi tiết xung quanh làm phân tâm hay vấy bẩn.

![Grady Booch](assets/illustrations/01-grady-booch.png){w=150}

**Grady Booch, tác giả cuốn *Object Oriented Analysis and Design with Applications***

> Mã sạch đơn giản và trực tiếp. Mã sạch đọc như văn xuôi được viết khéo. Mã sạch không bao giờ che khuất ý đồ của người thiết kế, mà đầy những trừu tượng sắc nét và những dòng điều khiển thẳng thắn.

Grady nêu một số ý giống Bjarne, nhưng nhìn từ góc độ khả năng đọc. Tôi đặc biệt thích ý của ông rằng code sạch phải đọc như văn xuôi được viết khéo. Hãy nhớ lại một cuốn sách thật hay bạn từng đọc. Bạn còn nhớ những con chữ dường như biến mất, nhường chỗ cho hình ảnh không? Cứ như đang xem phim vậy, phải không? Còn hơn thế: bạn thấy nhân vật, nghe âm thanh, cảm nhận nỗi bi thương và sự hài hước.

Đọc code sạch sẽ không bao giờ giống hẳn đọc *Lord of the Rings*. Dù vậy, ẩn dụ văn chương ấy không tồi. Như một cuốn tiểu thuyết hay, code sạch phải làm lộ rõ những căng thẳng trong bài toán cần giải. Nó phải đẩy những căng thẳng ấy lên cao trào, rồi để người đọc thốt lên “À! Dĩ nhiên rồi!” khi vấn đề được giải quyết và một lời giải hiển nhiên hiện ra.

Tôi thấy cách Grady dùng cụm “trừu tượng sắc nét” (crisp abstraction) thật thú vị, gần như một nghịch hợp! Suy cho cùng, “crisp” gần nghĩa với “concrete”. Từ điển trên MacBook của tôi định nghĩa “crisp” là quyết đoán nhanh gọn, thực tế, không do dự hay thêm chi tiết thừa. Hai nghĩa tưởng như trái ngược ấy lại truyền tải một thông điệp mạnh mẽ. Code phải thực tế, không suy đoán. Nó chỉ nên chứa những gì cần thiết. Người đọc phải thấy rằng chúng ta đã quyết đoán.

![Dave Thomas](assets/illustrations/01-dave-thomas.png){w=144}

**“Big” Dave Thomas, người sáng lập OTI, cha đỡ đầu của chiến lược Eclipse**

> Mã sạch có thể được một nhà phát triển khác, không phải tác giả ban đầu, đọc và mở rộng. Nó có kiểm thử đơn vị và kiểm thử chấp nhận. Tên gọi có ý nghĩa. Nó đưa ra một cách làm thay vì nhiều cách cho cùng một việc. Nó có ít phụ thuộc, được định nghĩa rõ ràng, và một API rõ ràng, tối giản. Code phải có tính văn học, vì tùy ngôn ngữ mà không phải thông tin cần thiết nào cũng có thể diễn đạt rõ chỉ bằng code.

Big Dave cũng mong code dễ đọc như Grady, nhưng ông nhấn mạnh thêm một điểm: mã sạch giúp người khác dễ mở rộng. Điều này nghe có vẻ hiển nhiên, nhưng vẫn cần nhắc kỹ. Dù sao, code dễ đọc và code dễ thay đổi là hai chuyện khác nhau.

Dave gắn sự sạch sẽ với kiểm thử! Mười năm trước, nhiều người hẳn sẽ ngạc nhiên. Nhưng Phát triển hướng kiểm thử (Test Driven Development) đã tác động sâu sắc đến ngành và trở thành một trong những kỷ luật nền tảng nhất. Dave nói đúng. Code không có kiểm thử thì không sạch. Dù thanh lịch, dễ đọc và dễ tiếp cận đến đâu, thiếu kiểm thử thì code vẫn bẩn.

Dave dùng từ “tối giản” hai lần. Có vẻ ông coi trọng code nhỏ hơn code lớn. Thật vậy, đây là điệp khúc quen thuộc trong văn liệu phần mềm từ thuở ban đầu. Nhỏ hơn thì tốt hơn.

Dave cũng nói code phải có tính văn học. Đây là cách nhắc nhẹ đến lập trình văn học của Knuth.[^4] Nói cách khác, code phải được viết sao cho con người có thể đọc.

![Michael Feathers](assets/illustrations/01-michael-feathers.png){w=161}

**Michael Feathers, tác giả cuốn *Working Effectively with Legacy Code***

> Tôi có thể kể ra mọi phẩm chất mình thấy ở mã sạch, nhưng có một phẩm chất bao trùm dẫn đến tất cả những phẩm chất kia. Mã sạch luôn trông như được viết bởi một người quan tâm. Không có điều gì hiển nhiên bạn có thể làm để khiến nó tốt hơn. Tác giả code đã nghĩ đến tất cả những điều đó. Nếu bạn thử hình dung cách cải thiện, cuối cùng bạn lại trở về chỗ cũ, ngồi trân trọng đoạn code người khác để lại, đoạn code của một người thực sự quan tâm đến tay nghề.

Một từ: quan tâm. Đó chính là chủ đề của cuốn sách này. Có lẽ phụ đề phù hợp là *Cách quan tâm đến code*.

Michael nói trúng phóc. Mã sạch là code đã được chăm chút. Có người dành thời gian giữ nó đơn giản, ngăn nắp và chú ý đúng mức đến từng chi tiết. Họ đã quan tâm.

![Ron Jeffries](assets/illustrations/01-ron-jeffries.png){w=143}

**Ron Jeffries, tác giả cuốn *Extreme Programming Installed* và *Extreme Programming Adventures in C#***

Ron bắt đầu sự nghiệp lập trình bằng Fortran tại Strategic Air Command. Ông đã viết code bằng gần như mọi ngôn ngữ, trên gần như mọi loại máy. Lời ông rất đáng để cân nhắc.

> Những năm gần đây, tôi thường bắt đầu, và gần như kết thúc, bằng các quy tắc về code đơn giản của Beck. Theo thứ tự ưu tiên, code đơn giản:
>
> - Chạy được mọi bài kiểm thử;
> - Không chứa trùng lặp;
> - Thể hiện mọi ý tưởng thiết kế có trong hệ thống;
> - Giảm số lượng thực thể như lớp, phương thức, hàm và những thứ tương tự.
>
> Trong số đó, tôi tập trung nhiều nhất vào trùng lặp. Khi cùng một việc cứ lặp đi lặp lại, có thể trong đầu chúng ta đang có một ý tưởng chưa được thể hiện tốt trong code. Tôi cố tìm ra ý tưởng ấy, rồi diễn đạt nó rõ hơn.
>
> Với tôi, diễn đạt tốt bao gồm cả tên gọi có ý nghĩa. Tôi thường đổi tên vài lần mới chốt được. Các công cụ lập trình hiện đại như Eclipse giúp việc đổi tên khá dễ dàng, nên tôi không ngại thay đổi. Nhưng khả năng diễn đạt không chỉ nằm ở tên gọi. Tôi cũng xem một đối tượng hay phương thức có đang làm nhiều hơn một việc không. Nếu là đối tượng, có lẽ nên tách thành hai hay nhiều đối tượng. Nếu là phương thức, tôi luôn dùng tái cấu trúc Extract Method, để tạo ra một phương thức nói rõ hơn nó làm gì và vài phương thức con mô tả cách thực hiện.
>
> Chỉ riêng việc loại bỏ trùng lặp và diễn đạt rõ hơn đã giúp tôi tiến rất xa trên con đường đến với mã sạch. Chỉnh code bẩn chỉ với hai điều này trong đầu cũng có thể tạo ra khác biệt lớn. Nhưng còn một điều nữa tôi biết mình vẫn làm, dù khó giải thích hơn.
>
> Sau nhiều năm làm việc này, tôi thấy chương trình nào cũng được tạo nên từ những thành phần khá giống nhau. Chẳng hạn, “tìm thứ gì đó trong một tập hợp”. Dù là cơ sở dữ liệu hồ sơ nhân viên, hash map gồm khóa và giá trị, hay một mảng phần tử nào đó, ta thường cần lấy một phần tử cụ thể trong tập hợp. Khi gặp trường hợp ấy, tôi thường bọc cách hiện thực cụ thể trong một phương thức hay lớp trừu tượng hơn. Cách này đem lại cho tôi vài lợi ích thú vị.
>
> Tôi có thể hiện thực chức năng ngay bằng thứ đơn giản, chẳng hạn hash map. Nhưng vì mọi chỗ tham chiếu đến thao tác tìm kiếm đều được lớp trừu tượng nhỏ của tôi bao bọc, tôi có thể đổi cách hiện thực bất cứ lúc nào. Nhờ vậy, tôi tiến nhanh mà vẫn giữ được khả năng thay đổi về sau.
>
> Hơn nữa, lớp trừu tượng cho tập hợp thường khiến tôi chú ý đến điều “thật sự” đang diễn ra, giúp tôi không lao vào hiện thực những hành vi tùy tiện cho tập hợp khi điều mình cần chỉ là vài cách đơn giản để tìm thứ mong muốn.
>
> Giảm trùng lặp, diễn đạt rõ ràng và sớm xây dựng những trừu tượng đơn giản. Với tôi, đó là những gì tạo nên mã sạch.

Chỉ trong vài đoạn ngắn, Ron đã tóm tắt nội dung cuốn sách này: không trùng lặp, mỗi thứ làm một việc, diễn đạt rõ ràng, trừu tượng nhỏ. Đủ cả.

![Ward Cunningham](assets/illustrations/01-ward-cunningham.png){w=144}

**Ward Cunningham, người phát minh ra Wiki và Fit, đồng phát minh eXtreme Programming. Động lực đằng sau *Design Patterns*. Người dẫn dắt tư tưởng Smalltalk và OO. Cha đỡ đầu của tất cả những ai quan tâm đến code.**

> Bạn biết mình đang làm việc với mã sạch khi mỗi thủ tục bạn đọc đều đúng như mong đợi. Có thể gọi code là đẹp khi nó còn khiến ngôn ngữ trông như được tạo ra cho bài toán.

Những câu như vậy rất đặc trưng của Ward. Bạn đọc, gật đầu rồi chuyển sang chủ đề khác. Nghe hợp lý và hiển nhiên đến mức khó nhận ra chiều sâu của nó. Có thể bạn nghĩ rằng điều ấy đúng như mong đợi. Nhưng hãy nhìn kỹ hơn.

“... đúng như mong đợi.” Lần cuối bạn thấy một module đúng như mong đợi là khi nào? Có phải những module bạn gặp thường khó hiểu, phức tạp, rối rắm hơn không? Chẳng phải chúng thường dẫn bạn đi sai hướng? Bạn đã quen với việc vùng vẫy để nắm lấy những mạch lập luận tuôn ra từ toàn hệ thống rồi đan vào module mình đang đọc, phải không? Lần cuối bạn đọc code và gật đầu như khi đọc câu của Ward là khi nào?

Ward cho rằng khi đọc code sạch, bạn sẽ không ngạc nhiên chút nào, thậm chí chẳng cần tốn nhiều công sức. Bạn đọc nó và thấy mọi thứ đúng như mong đợi: hiển nhiên, đơn giản, thuyết phục. Mỗi module mở đường cho module tiếp theo, đồng thời cho bạn biết module sau sẽ được viết thế nào. Chương trình sạch được viết tốt đến mức bạn khó nhận ra điều đó. Người thiết kế khiến nó trông đơn giản đến buồn cười, như mọi thiết kế xuất sắc.

Còn quan niệm về cái đẹp của Ward thì sao? Chúng ta vẫn phàn nàn rằng ngôn ngữ không được thiết kế cho bài toán của mình. Nhưng Ward đặt trách nhiệm trở lại lên chúng ta. Ông nói code đẹp khiến ngôn ngữ trông như được tạo ra cho bài toán. Vậy chúng ta phải làm cho ngôn ngữ trông đơn giản! Những kẻ cuồng ngôn ngữ khắp nơi, hãy coi chừng! Chính lập trình viên, chứ không phải ngôn ngữ, khiến chương trình trông đơn giản.

## Các trường phái
![Uncle Bob](assets/illustrations/01-uncle-bob.png){w=144}


Còn tôi (Uncle Bob) nghĩ mã sạch là gì? Cuốn sách này sẽ trình bày thật chi tiết quan niệm của tôi và các đồng nghiệp về mã sạch. Chúng tôi sẽ nói điều gì tạo nên tên biến, hàm, lớp sạch và những thứ tương tự. Chúng tôi sẽ nêu ý kiến như những chân lý tuyệt đối, không xin lỗi vì giọng điệu gay gắt. Ở thời điểm này trong sự nghiệp, với chúng tôi, chúng là chân lý. Đó là trường phái của chúng tôi về mã sạch.

Những người tập võ không phải ai cũng đồng ý môn võ nào tốt nhất hay kỹ thuật nào tốt nhất trong một môn. Các bậc thầy võ thuật thường lập trường phái riêng và tập hợp học trò đến học. Có Gracie Jiu Jitsu do gia đình Gracie sáng lập và truyền dạy ở Brazil; Hakkoryu Jiu Jitsu do Okuyama Ryuho sáng lập và truyền dạy tại Tokyo; Jeet Kune Do do Bruce Lee sáng lập và truyền dạy ở Hoa Kỳ.

Học trò của các trường phái này đắm mình trong giáo huấn của người sáng lập. Họ dốc sức học theo vị thầy ấy, thường gạt bỏ giáo huấn của những người khác. Sau này, khi tiến bộ trong môn võ, họ có thể theo học một vị thầy khác để mở rộng kiến thức và cách luyện tập. Một số người tiếp tục trau dồi kỹ năng, khám phá kỹ thuật mới rồi lập trường phái riêng.

Không trường phái nào đúng tuyệt đối. Thế nhưng trong một trường phái cụ thể, chúng ta vẫn hành xử như thể giáo huấn và kỹ thuật của trường phái ấy là đúng. Suy cho cùng, vẫn có cách đúng để luyện Hakkoryu Jiu Jitsu hay Jeet Kune Do. Nhưng cái đúng trong một trường phái không khiến giáo huấn của trường phái khác trở thành sai.

Hãy xem cuốn sách này như lời giới thiệu về Trường phái Mã sạch Object Mentor. Những kỹ thuật và giáo huấn trong sách là cách chúng tôi thực hành nghề của mình. Chúng tôi sẵn sàng khẳng định rằng nếu làm theo, bạn sẽ nhận được những lợi ích chúng tôi từng có và học được cách viết code sạch, chuyên nghiệp. Nhưng đừng nghĩ chúng tôi “đúng” theo nghĩa tuyệt đối. Có những trường phái và bậc thầy khác cũng có quyền tuyên bố mình chuyên nghiệp như chúng tôi. Bạn cũng nên học hỏi từ họ.

Quả thật, nhiều khuyến nghị trong sách này gây tranh cãi. Có lẽ bạn sẽ không đồng ý với tất cả, thậm chí có thể phản đối gay gắt một số điều. Không sao. Chúng tôi không thể nhận mình là thẩm quyền cuối cùng. Dù vậy, những khuyến nghị này đều là điều chúng tôi đã suy nghĩ lâu dài, kỹ càng và học được qua nhiều thập kỷ kinh nghiệm cùng những lần thử sai lặp đi lặp lại. Dù đồng ý hay không, bạn cũng nên đọc và tôn trọng quan điểm của chúng tôi.

## Chúng ta là tác giả

Trường `@author` trong Javadoc cho biết chúng ta là ai. Chúng ta là tác giả. Tác giả luôn có người đọc và có trách nhiệm giao tiếp tốt với họ. Lần tới khi viết một dòng code, hãy nhớ rằng bạn là tác giả, đang viết cho những người đọc sẽ đánh giá công sức của mình.

Bạn có thể hỏi: Code thật sự được đọc bao nhiêu? Chẳng phải phần lớn công sức là viết code sao?

Bạn đã bao giờ phát lại một phiên chỉnh sửa chưa? Thập niên 80 và 90, chúng ta có những trình soạn thảo như Emacs ghi lại từng lần gõ phím. Bạn có thể làm việc một giờ rồi phát lại cả phiên như xem một bộ phim tua nhanh. Khi tôi làm vậy, kết quả thật hấp dẫn.

Phần lớn thời gian phát lại là cuộn màn hình và chuyển đến các module khác!

> Bob bước vào module.
>
> Anh cuộn xuống hàm cần sửa.
>
> Anh dừng lại, cân nhắc các lựa chọn.
>
> Ồ, anh cuộn lên đầu module để kiểm tra việc khởi tạo một biến.
>
> Giờ anh cuộn trở xuống rồi bắt đầu gõ.
>
> Ối, anh xóa phần vừa gõ!
>
> Anh gõ lại.
>
> Anh lại xóa!
>
> Anh gõ được nửa đoạn khác rồi cũng xóa luôn!
>
> Anh cuộn xuống một hàm khác đang gọi hàm mình sửa để xem nó được gọi thế nào.
>
> Anh cuộn lên và gõ lại đúng đoạn code vừa xóa.
>
> Anh dừng lại.
>
> Anh lại xóa đoạn code đó!
>
> Anh mở cửa sổ khác và xem một lớp con. Hàm đó có bị ghi đè không?

...

Bạn hiểu ý rồi đấy. Thật vậy, thời gian đọc nhiều hơn thời gian viết gấp hơn 10 lần. Chúng ta liên tục đọc code cũ trong lúc viết code mới.

Vì tỷ lệ này cao như vậy, chúng ta muốn code dễ đọc, kể cả khi điều đó khiến việc viết khó hơn. Dĩ nhiên, không thể viết code mà không đọc nó; vì thế, làm code dễ đọc cũng khiến việc viết dễ hơn.

Không thể thoát khỏi lẽ đó. Bạn không thể viết code nếu không đọc được code xung quanh. Việc viết đoạn code hôm nay dễ hay khó tùy vào việc code xung quanh dễ hay khó đọc. Muốn đi nhanh, hoàn thành sớm và viết code dễ hơn, hãy làm cho code dễ đọc.

## Quy tắc Hướng đạo sinh

Viết code tốt thôi chưa đủ. Code phải luôn sạch theo thời gian. Ai cũng từng thấy code mục ruỗng, xuống cấp theo năm tháng. Vì vậy, chúng ta phải chủ động ngăn sự xuống cấp ấy.

Hướng đạo sinh Hoa Kỳ có một quy tắc đơn giản mà chúng ta có thể áp dụng vào nghề mình:

> Hãy để khu cắm trại sạch hơn lúc bạn đến.[^5]

Nếu ai cũng check-in code sạch hơn một chút so với lúc check-out, code sẽ không thể mục ruỗng. Việc dọn dẹp không cần lớn lao: đổi một tên biến cho hay hơn, tách một hàm hơi quá lớn, bỏ một đoạn trùng lặp nhỏ, dọn một câu lệnh if phức hợp.

Bạn có tưởng tượng được cảnh làm việc trong một dự án mà code ngày càng tốt hơn không? Bạn có nghĩ lựa chọn nào khác cũng chuyên nghiệp không? Chẳng phải cải tiến liên tục vốn là một phần của tính chuyên nghiệp sao?

## Tiền truyện và các nguyên lý

Theo nhiều cách, cuốn sách này là “tiền truyện” của cuốn sách tôi viết năm 2002, *Agile Software Development: Principles, Patterns, and Practices* (PPP). PPP bàn về các nguyên lý thiết kế hướng đối tượng và nhiều thực hành của các nhà phát triển chuyên nghiệp. Nếu chưa đọc PPP, có thể bạn sẽ thấy cuốn sách ấy tiếp nối câu chuyện trong cuốn này. Nếu đã đọc, bạn sẽ nhận ra nhiều tư tưởng của cuốn trước được nhắc lại ở đây, nhưng ở cấp độ code.

Trong sách này, bạn sẽ gặp những chỗ nhắc rải rác đến các nguyên tắc thiết kế như Nguyên tắc Trách nhiệm Đơn nhất (Single Responsibility Principle, SRP), Nguyên lý Mở Đóng (Open Closed Principle, OCP) và Nguyên lý Đảo ngược Phụ thuộc (Dependency Inversion Principle, DIP). PPP trình bày kỹ những nguyên lý ấy.

## Kết luận

Sách về nghệ thuật không hứa biến bạn thành nghệ sĩ. Chúng chỉ có thể trao cho bạn một số công cụ, kỹ thuật và cách tư duy mà nghệ sĩ khác từng dùng. Cuốn sách này cũng không thể hứa biến bạn thành lập trình viên giỏi hay trao cho bạn “cảm giác code”. Nó chỉ có thể cho bạn thấy cách các lập trình viên giỏi tư duy, cùng những mẹo, kỹ thuật và công cụ họ dùng.

Cũng như sách về nghệ thuật, cuốn này có rất nhiều chi tiết và code. Bạn sẽ thấy code tốt lẫn code xấu, thấy code xấu được biến thành code tốt. Bạn sẽ gặp những danh sách nguyên tắc kinh nghiệm, kỷ luật và kỹ thuật, hết ví dụ này đến ví dụ khác. Sau đó, tùy bạn.

Hãy nhớ câu chuyện cười cũ về một nghệ sĩ violin hòa tấu bị lạc đường đến buổi biểu diễn. Ông dừng một cụ già ở góc phố và hỏi đường đến Carnegie Hall. Cụ già nhìn người nghệ sĩ cùng cây đàn kẹp dưới cánh tay rồi nói: “Luyện tập đi, con trai. Luyện tập!”

## Tài liệu tham khảo

[Beck07]: *Implementation Patterns*, Kent Beck, Addison-Wesley, 2007.

[Knuth92]: *Literate Programming*, Donald E. Knuth, Center for the Study of Language and Information, Leland Stanford Junior University, 1992.

[^1]: [Beck07].

[^2]: Khi Ignaz Semmelweis lần đầu khuyến nghị bác sĩ rửa tay vào năm 1847, đề xuất này bị bác bỏ với lý do bác sĩ quá bận, không có thời gian rửa tay giữa các lần thăm bệnh nhân.

[^3]: http://www.pragmaticprogrammer.com/booksellers/2004-12.html

[^4]: [Knuth92].

[^5]: Câu này phỏng theo lời từ biệt của Robert Stephenson Smyth Baden-Powell gửi các Hướng đạo sinh: “Hãy cố gắng để lại thế giới này tốt đẹp hơn một chút so với lúc bạn đến ...”
