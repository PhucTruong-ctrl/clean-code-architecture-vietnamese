# Chương 1: Thiết kế và kiến trúc là gì?
![Minh họa](assets/illustrations/01-chuong-01-opener.png){w=270}

## Thiết kế và kiến trúc

Trong nhiều năm, người ta đã nhầm lẫn về thiết kế và kiến trúc. Thiết kế là gì? Kiến trúc là gì? Hai khái niệm này khác nhau ra sao?

Một mục tiêu của cuốn sách này là gỡ bỏ mọi nhầm lẫn và định nghĩa dứt khoát thiết kế và kiến trúc là gì. Trước hết, tôi khẳng định rằng chúng chẳng khác nhau. Không khác chút nào.

Từ "kiến trúc" thường được dùng để chỉ những thứ ở cấp cao, tách rời khỏi các chi tiết cấp thấp; còn "thiết kế" thường gợi đến những cấu trúc và quyết định ở cấp thấp hơn. Nhưng cách dùng này vô lý nếu nhìn vào công việc của một kiến trúc sư thực thụ.

Hãy nghĩ đến kiến trúc sư đã thiết kế ngôi nhà mới của tôi. Ngôi nhà ấy có kiến trúc không? Dĩ nhiên là có. Kiến trúc của nó là gì? Là hình dáng, diện mạo bên ngoài, các mặt đứng, cách bố trí không gian và phòng ốc. Nhưng khi xem các bản vẽ kiến trúc sư tạo ra, tôi thấy vô số chi tiết cấp thấp. Tôi thấy vị trí của từng ổ cắm, công tắc đèn và bóng đèn. Tôi thấy công tắc nào điều khiển đèn nào. Tôi thấy vị trí lò sưởi, kích thước và vị trí bình nước nóng cùng máy bơm hố thu. Tôi thấy những bản vẽ chi tiết mô tả cách xây tường, mái nhà và móng.

Nói ngắn gọn, tôi thấy mọi chi tiết nhỏ hỗ trợ cho các quyết định cấp cao. Tôi cũng thấy các chi tiết cấp thấp và quyết định cấp cao đều là một phần trong toàn bộ thiết kế ngôi nhà.

Thiết kế phần mềm cũng vậy. Các chi tiết cấp thấp và cấu trúc cấp cao cùng thuộc về một tổng thể. Chúng kết thành một thể liên tục, định hình hệ thống. Không thể có cái này mà thiếu cái kia; thật ra, chẳng có đường ranh rõ ràng nào ngăn cách chúng. Các quyết định trải liên tục từ cấp cao nhất đến cấp thấp nhất.

## Mục tiêu?

Mục tiêu của những quyết định ấy là gì? Mục tiêu của thiết kế phần mềm tốt là gì? Mục tiêu ấy chính là mô tả lý tưởng của tôi:

> Mục tiêu của kiến trúc phần mềm là giảm thiểu nguồn lực con người cần thiết để xây dựng và bảo trì hệ thống theo yêu cầu.

Chất lượng thiết kế được đo bằng nỗ lực cần bỏ ra để đáp ứng nhu cầu của khách hàng. Nếu nỗ lực ấy thấp và duy trì ở mức thấp suốt vòng đời hệ thống, thiết kế tốt. Nếu mỗi bản phát hành lại cần nhiều công sức hơn, thiết kế kém. Đơn giản vậy thôi.

## Nghiên cứu tình huống

Hãy xem xét ví dụ sau. Tình huống này sử dụng dữ liệu thực từ một công ty muốn được giấu tên.

Trước tiên, hãy xem quy mô đội ngũ kỹ thuật tăng lên như thế nào. Tôi tin bạn sẽ đồng ý rằng xu hướng này rất đáng khích lệ. Mức tăng trưởng như Hình 1.1 cho thấy hẳn là công ty đã thành công đáng kể!

**Hình 1.1** Tăng trưởng của đội ngũ kỹ thuật. Tái hiện với sự cho phép của Jason Gorman, từ một buổi thuyết trình.


Bây giờ, hãy xem năng suất của công ty trong cùng giai đoạn, tính đơn giản bằng số dòng mã (Hình 1.2).

**Hình 1.2** Năng suất trong cùng giai đoạn

Rõ ràng đã có chuyện không ổn. Mỗi bản phát hành đều có thêm nhiều nhà phát triển hỗ trợ, nhưng lượng mã tăng lên có vẻ đang tiến dần đến một giới hạn.

Đây mới là biểu đồ đáng sợ: Hình 1.3 cho thấy chi phí trên mỗi dòng mã thay đổi theo thời gian.

**Hình 1.3** Chi phí trên mỗi dòng mã theo thời gian

Những xu hướng này không thể kéo dài. Dù hiện tại công ty có lãi đến đâu, các đường cong ấy rồi sẽ bào mòn lợi nhuận của mô hình kinh doanh và đẩy công ty vào tình trạng đình trệ, thậm chí sụp đổ.

Điều gì gây ra sự thay đổi đáng kể về năng suất này? Vì sao chi phí tạo ra mã ở bản phát hành 8 lại cao gấp 40 lần bản phát hành 1?

### Dấu hiệu của một mớ hỗn độn

Bạn đang nhìn vào dấu hiệu của một mớ hỗn độn. Khi hệ thống bị chắp vá trong vội vã, khi số lượng lập trình viên là yếu tố duy nhất quyết định sản lượng, và khi người ta hầu như chẳng nghĩ đến sự sạch sẽ của mã hay cấu trúc thiết kế, bạn có thể tin rằng đường cong ấy sẽ tiếp tục đi xuống đến tận cùng tồi tệ.

Hình 1.4 cho thấy đường cong này trông ra sao với các nhà phát triển. Ban đầu, năng suất của họ gần 100%, nhưng giảm dần sau mỗi bản phát hành. Đến bản phát hành thứ tư, có thể thấy năng suất sẽ chạm đáy khi tiến dần về không.

**Hình 1.4** Năng suất qua từng bản phát hành

Từ góc nhìn của các nhà phát triển, tình cảnh này vô cùng bực bội vì ai cũng làm việc chăm chỉ. Không ai giảm nỗ lực.

Dù đã cố hết sức, làm thêm giờ và tận tâm, họ vẫn chẳng hoàn thành được bao nhiêu. Toàn bộ nỗ lực bị rút khỏi việc phát triển tính năng và phải dùng để xoay xở với mớ hỗn độn. Công việc của họ, nếu còn gọi là công việc, đã biến thành chuyển đống bừa bộn từ chỗ này sang chỗ khác, hết lần này đến lần khác, chỉ để thêm một tính năng nhỏ nhoi.

### Góc nhìn của lãnh đạo

Nếu bạn nghĩ tình hình đó đã tệ, hãy hình dung lãnh đạo nhìn vào biểu đồ này sẽ thấy gì! Hình 1.5 mô tả quỹ lương phát triển hằng tháng trong cùng giai đoạn.

**Hình 1.5** Quỹ lương phát triển hằng tháng theo bản phát hành

Bản phát hành 1 được bàn giao với quỹ lương hằng tháng chỉ vài trăm nghìn đô-la. Bản thứ hai tốn thêm vài trăm nghìn. Đến bản phát hành thứ tám, quỹ lương mỗi tháng đã lên tới 20 triệu đô-la và vẫn còn tăng.

Chỉ riêng biểu đồ này đã đủ đáng sợ. Rõ ràng đang có chuyện đáng báo động. Ta hy vọng doanh thu tăng nhanh hơn chi phí để bù đắp khoản chi đó. Nhưng nhìn theo cách nào thì đường cong này cũng đáng lo.

Giờ hãy so sánh đường cong ở Hình 1.5 với số dòng mã được viết trong mỗi bản phát hành ở Hình 1.2. Mấy trăm nghìn đô-la mỗi tháng ban đầu mua được rất nhiều chức năng, nhưng 20 triệu đô-la ở giai đoạn cuối gần như chẳng mua được gì! Bất kỳ giám đốc tài chính nào nhìn hai biểu đồ này cũng hiểu rằng cần hành động ngay để ngăn thảm họa.

Nhưng có thể làm gì? Chuyện gì đã xảy ra? Điều gì khiến năng suất giảm mạnh đến vậy? Ngoài việc giậm chân và nổi giận với các nhà phát triển, lãnh đạo còn có thể làm gì?

### Chuyện gì đã xảy ra?

Gần 2.600 năm trước, Aesop kể câu chuyện Rùa và Thỏ. Bài học của câu chuyện được nhắc đi nhắc lại bằng nhiều cách:

- "Chậm mà chắc sẽ thắng cuộc đua."
- "Cuộc đua không dành cho người nhanh, cũng như trận chiến không dành cho người mạnh."
- "Càng vội vã, càng chậm chạp."

Câu chuyện cho thấy sự tự tin thái quá thật dại dột ra sao. Thỏ tin chắc mình nhanh hơn hẳn nên chẳng coi cuộc đua là nghiêm túc, rồi nằm ngủ trong lúc Rùa cán đích.

Các nhà phát triển ngày nay cũng đang trong một cuộc đua tương tự và thể hiện sự tự tin thái quá như vậy. Họ không ngủ, trái lại, phần lớn làm việc đến kiệt sức. Nhưng một phần trong đầu họ lại ngủ quên: phần hiểu rằng mã tốt, sạch và được thiết kế cẩn thận rất quan trọng.

Họ tin vào một lời nói dối quen thuộc: "Cứ ra thị trường trước đã, sau này ta sẽ dọn dẹp mã!" Dĩ nhiên, việc dọn dẹp chẳng bao giờ diễn ra, vì áp lực thị trường không giảm đi. Ra thị trường trước chỉ có nghĩa là giờ đây bạn có cả đám đối thủ bám sát phía sau, và phải chạy nhanh hết sức để vượt lên.

Vì vậy, các nhà phát triển chẳng bao giờ đổi cách làm. Họ không thể quay lại dọn dẹp vì phải hoàn thành tính năng tiếp theo, rồi tính năng kế tiếp, rồi nữa. Mớ hỗn độn ngày càng lớn, còn năng suất tiếp tục tiến dần về không.

Thỏ quá tự tin vào tốc độ của mình; các nhà phát triển cũng quá tự tin rằng họ sẽ duy trì được năng suất. Mớ mã ngày càng rối, âm thầm bào mòn năng suất, chẳng bao giờ dừng lại. Nếu cứ để mặc, nó sẽ kéo năng suất xuống bằng không chỉ trong vài tháng.

Lời nói dối lớn hơn mà các nhà phát triển tin vào là viết mã cẩu thả giúp họ làm nhanh trong ngắn hạn, chỉ khiến họ chậm lại về lâu dài. Những người tin điều đó vừa quá tự tin vào khả năng chuyển từ tạo ra mớ hỗn độn sang dọn dẹp nó trong tương lai, vừa mắc một sai lầm thực tế đơn giản. Sự thật là làm việc trong cảnh hỗn độn luôn chậm hơn giữ cho mọi thứ gọn gàng, bất kể xét trong khoảng thời gian nào.

Hãy xem kết quả thí nghiệm đáng chú ý của Jason Gorman, được thể hiện ở Hình 1.6. Jason tiến hành thử nghiệm trong sáu ngày. Mỗi ngày, ông hoàn thành một chương trình đơn giản để chuyển số nguyên sang chữ số La Mã. Ông biết mình đã xong khi bộ kiểm thử chấp nhận được xác định trước đều chạy qua. Mỗi ngày, công việc mất chưa đến 30 phút. Trong ngày thứ nhất, thứ ba và thứ năm, Jason áp dụng một kỷ luật phát triển phần mềm có tên phát triển hướng kiểm thử (TDD). Ba ngày còn lại, ông viết mã mà không áp dụng kỷ luật đó.

**Hình 1.6** Thời gian hoàn thành qua các lần lặp, có và không dùng TDD

Trước hết, hãy chú ý đến đường cong học tập trong Hình 1.6. Công việc những ngày sau hoàn thành nhanh hơn những ngày đầu. Cũng hãy để ý rằng các ngày dùng TDD hoàn thành nhanh hơn khoảng 10% so với các ngày không dùng TDD; ngay cả ngày dùng TDD chậm nhất cũng nhanh hơn ngày không dùng TDD nhanh nhất.

Một số người có thể nhìn kết quả này và cho rằng đó là điều phi thường. Nhưng với những ai không bị sự tự tin thái quá của Thỏ đánh lừa, kết quả ấy hoàn toàn dễ đoán, vì họ biết sự thật giản dị này về phát triển phần mềm:

> Cách duy nhất để làm nhanh là làm cho tốt.

Đó là câu trả lời cho thế khó của lãnh đạo. Cách duy nhất để đảo ngược đà giảm năng suất và tăng chi phí là khiến các nhà phát triển thôi suy nghĩ như Thỏ tự phụ và bắt đầu chịu trách nhiệm về mớ hỗn độn họ đã tạo ra.

Các nhà phát triển có thể nghĩ giải pháp là bắt đầu lại từ đầu và thiết kế lại toàn bộ hệ thống. Nhưng đó lại là Thỏ đang lên tiếng. Chính sự tự tin thái quá từng dẫn đến mớ hỗn độn giờ lại bảo họ rằng chỉ cần được chạy lại cuộc đua, họ sẽ làm tốt hơn. Thực tế chẳng đẹp đẽ như vậy:

> Sự tự tin thái quá sẽ khiến lần thiết kế lại tạo ra mớ hỗn độn y như dự án ban đầu.

## Kết luận

Trong mọi trường hợp, lựa chọn tốt nhất là để tổ chức phát triển nhận ra và tránh sự tự tin thái quá của chính mình, đồng thời nghiêm túc xem xét chất lượng kiến trúc phần mềm.

Muốn coi trọng kiến trúc phần mềm, bạn cần biết kiến trúc phần mềm tốt là gì. Muốn xây dựng hệ thống có thiết kế và kiến trúc giúp giảm nỗ lực, tăng năng suất, bạn cần biết những thuộc tính nào của kiến trúc hệ thống sẽ dẫn đến kết quả đó.

Đó là nội dung cuốn sách này. Sách mô tả diện mạo của những kiến trúc và thiết kế phần mềm tốt, sạch, để các nhà phát triển có thể xây dựng hệ thống sinh lợi trong thời gian dài.