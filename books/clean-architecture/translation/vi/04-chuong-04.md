# Chương 4: Lập trình có cấu trúc
![Minh họa](assets/illustrations/04-chuong-04-opener.png){w=230}

Edsger Wybe Dijkstra sinh tại Rotterdam năm 1930. Ông sống sót qua vụ ném bom Rotterdam trong Thế chiến thứ hai và thời kỳ Đức chiếm đóng Hà Lan. Năm 1948, ông tốt nghiệp trung học với điểm cao nhất có thể đạt được ở toán, vật lý, hóa học và sinh học. Tháng 3 năm 1952, khi 21 tuổi (chỉ chín tháng trước khi tôi chào đời), Dijkstra nhận việc tại Trung tâm Toán học Amsterdam với tư cách là lập trình viên đầu tiên của Hà Lan.

Năm 1955, sau ba năm làm lập trình viên, và vẫn còn là sinh viên, Dijkstra kết luận rằng thách thức trí tuệ của việc lập trình lớn hơn thách thức trí tuệ của vật lý lý thuyết. Kết quả là ông chọn lập trình làm nghề nghiệp dài hạn.
Năm 1957, Dijkstra kết hôn với Maria Debets. Lúc đó, bạn phải khai nghề nghiệp như một phần trong lễ cưới tại Hà Lan. Cơ quan Hà Lan từ chối chấp nhận "lập trình viên" là nghề của Dijkstra; họ chưa bao giờ nghe nói đến nghề ấy. Để làm hài lòng họ, Dijkstra chấp nhận "vật lý lý thuyết" làm chức danh công việc.

Là một phần của việc quyết định theo đuổi lập trình như một nghề nghiệp, Dijkstra đã bàn bạc với người quản lý của mình, Adriaan van Wijngaarden. Dijkstra lo ngại rằng chưa ai xác định ra một kỷ luật, hay một khoa học, của lập trình, và do đó ông sẽ không được coi trọng. Người quản lý trả lời rằng Dijkstra có thể là một trong những người sẽ khám phá ra những kỷ luật đó, từ đó biến phần mềm thành một khoa học.

Dijkstra bắt đầu sự nghiệp vào thời kỳ ống chân không, khi máy tính to lớn, mong manh, chậm chạp, thiếu tin cậy và (theo tiêu chuẩn ngày nay) cực kỳ hạn chế. Những năm đầu đó, chương trình được viết bằng nhị phân hoặc bằng hợp ngữ rất thô sơ. Đầu vào được đưa vào bằng băng giấy hoặc thẻ đục lỗ. Vòng lặp sửa mã, biên dịch rồi kiểm thử kéo dài hàng giờ, có khi hàng ngày.

Chính trong môi trường nguyên thủy ấy mà Dijkstra đã có những khám phá vĩ đại của mình.

## Chứng minh

Vấn đề mà Dijkstra nhận ra sớm là lập trình rất khó, và lập trình viên không làm tốt lắm. Một chương trình có độ phức tạp vừa phải chứa quá nhiều chi tiết để não bộ con người có thể quản lý nếu không có sự giúp đỡ.
Bỏ sót chỉ một chi tiết nhỏ dẫn đến những chương trình có vẻ như chạy được, nhưng lại thất bại theo những cách bất ngờ.

Giải pháp của Dijkstra là áp dụng kỷ luật chứng minh trong toán học. Ông hình dung việc xây dựng một hệ thống phân cấp kiểu Euclid gồm các tiên đề, định lý, hệ quả và bổ đề. Dijkstra nghĩ rằng lập trình viên có thể dùng hệ thống đó như các nhà toán học vẫn làm: dùng những cấu trúc đã được chứng minh, rồi ghép chúng bằng mã mà họ sẽ tự chứng minh là đúng.

Để khởi đầu, Dijkstra nhận ra mình phải minh họa kỹ thuật lập các chứng minh cơ bản cho những thuật toán đơn giản. Ông thấy việc đó khá khó khăn.

Trong quá trình nghiên cứu, Dijkstra phát hiện một số cách dùng câu lệnh `goto` ngăn cản việc chia đệ quy mô-đun thành những đơn vị ngày càng nhỏ. Điều đó khiến ta không thể áp dụng phương pháp chia để trị cần thiết để lập các chứng minh hợp lý.

Tuy nhiên, các cách dùng goto khác thì không gặp vấn đề này. Dijkstra nhận ra rằng những cách dùng "tốt" của goto này tương ứng với các cấu trúc điều khiển lựa chọn và lặp đơn giản như if/then/else và do/while. Các mô-đun chỉ dùng những loại cấu trúc điều khiển đó có thể được chia đệ quy thành các đơn vị có thể chứng minh.

Dijkstra biết rằng những cấu trúc điều khiển đó, khi kết hợp với thực thi tuần tự, là đặc biệt. Chúng đã được xác định hai năm trước đó bởi Böhm và Jacopini, những người đã chứng minh rằng tất cả chương trình đều có thể được xây dựng chỉ từ ba cấu trúc: tuần tự, lựa chọn và lặp.

Khám phá này thật đáng chú ý: chính những cấu trúc điều khiển giúp mô-đun có thể chứng minh được cũng là tập hợp tối thiểu các cấu trúc điều khiển đủ để xây dựng mọi chương trình. Lập trình có cấu trúc ra đời từ đó.

Dijkstra chỉ ra rằng các câu lệnh tuần tự có thể được chứng minh đúng bằng liệt kê đơn giản. Kỹ thuật này theo dõi toán học các đầu vào của chuỗi tuần tự đến các đầu ra của chuỗi đó. Cách tiếp cận này không khác gì một chứng minh toán học thông thường.

Dijkstra giải quyết lựa chọn bằng cách áp dụng lại liệt kê. Mỗi đường đi qua cấu trúc lựa chọn đều được liệt kê. Nếu cả hai đường đi cuối cùng đều tạo ra kết quả toán học phù hợp, thì chứng minh là chắc chắn.

Lặp thì hơi khác. Để chứng minh một vòng lặp đúng, Dijkstra phải dùng quy nạp. Ông chứng minh trường hợp 1 bằng liệt kê. Sau đó chứng minh trường hợp rằng nếu N được giả định đúng, thì N + 1 cũng đúng, lại bằng liệt kê. Ông cũng chứng minh tiêu chí bắt đầu và kết thúc của vòng lặp bằng liệt kê.

Những chứng minh ấy tẻ nhạt và phức tạp, nhưng chúng vẫn là những chứng minh. Khi các phương pháp này được phát triển, dường như đã có thể xây dựng một hệ thống phân cấp các định lý kiểu Euclid.

## Một tuyên ngôn có hại

Năm 1968, Dijkstra viết một thư gửi biên tập viên của CACM, được đăng trong số tháng 3. Tiêu đề của bức thư là "Go To Statement Considered Harmful" (Câu lệnh Go To được xem là có hại). Bài viết nêu rõ lập trường của ông về ba cấu trúc điều khiển.

Và thế giới lập trình bùng nổ. Lúc đó chúng ta chưa có Internet, nên mọi người không thể đăng những meme chê bai Dijkstra, và không thể công kích ông trực tuyến. Nhưng họ có thể, và họ đã làm, viết thư gửi biên tập viên của nhiều tạp chí xuất bản.

Những bức thư đó không nhất thiết lịch sự. Một số cực kỳ tiêu cực; những bức khác lại ủng hộ mạnh mẽ lập trường của ông. Và như vậy cuộc tranh luận bắt đầu, cuối cùng kéo dài khoảng một thập kỷ.

Cuối cùng, tranh luận cũng lắng xuống. Lý do rất đơn giản: Dijkstra đã thắng. Khi các ngôn ngữ máy tính phát triển, câu lệnh `goto` dần bị đẩy ra ngoài, cho đến khi gần như biến mất. Hầu hết ngôn ngữ hiện đại không có `goto`, và LISP thì chưa bao giờ có.

Ngày nay chúng ta đều lập trình có cấu trúc, dù không phải do lựa chọn. Ngôn ngữ của chúng ta đơn giản là không cho phép tùy tiện chuyển giao quyền điều khiển trực tiếp.

Một số người có thể xem các lệnh `break` có nhãn trong Java hoặc ngoại lệ là tương tự `goto`. Thực tế, những cấu trúc này không phải kiểu chuyển giao quyền điều khiển hoàn toàn không giới hạn từng có trong các ngôn ngữ cũ như Fortran hay COBOL. Ngay cả ngôn ngữ vẫn hỗ trợ từ khóa `goto` thường cũng giới hạn đích nhảy trong phạm vi hàm hiện tại.

## Phân tách chức năng

Lập trình có cấu trúc cho phép các mô-đun được phân tách đệ quy thành các đơn vị có thể chứng minh, mà lần lượt có nghĩa là các mô-đun có thể được phân tách theo chức năng. Đó là, bạn có thể lấy một bài toán quy mô lớn và phân tách nó thành các hàm cấp cao. Mỗi hàm đó sau đó có thể được phân tách thành các hàm cấp thấp hơn, vô tận. Hơn nữa, mỗi hàm đã phân tách đó có thể được biểu diễn bằng các cấu trúc điều khiển bị hạn chế của lập trình có cấu trúc.

Trên nền tảng này, các phương pháp như phân tích có cấu trúc và thiết kế có cấu trúc trở nên phổ biến vào cuối thập niên 1970 và suốt thập niên 1980. Ed Yourdon, Larry Constantine, Tom DeMarco và Meilir Page-Jones đã quảng bá các kỹ thuật ấy. Nhờ áp dụng chúng, lập trình viên có thể chia các hệ thống lớn thành mô-đun và thành phần, rồi tiếp tục chia nhỏ thành những hàm có thể chứng minh.

## Không có chứng minh hình thức

Nhưng các chứng minh ấy không bao giờ thành hiện thực. Hệ thống phân cấp định lý kiểu Euclid không được xây dựng. Lập trình viên nói chung cũng không thấy lợi ích của việc kiên nhẫn chứng minh hình thức từng hàm nhỏ một. Cuối cùng, giấc mơ của Dijkstra phai nhạt rồi tan biến. Ngày nay, ít lập trình viên tin rằng chứng minh hình thức là cách thích hợp để tạo ra phần mềm chất lượng cao.

Tất nhiên, chứng minh toán học kiểu Euclid chính thức không phải là chiến lược duy nhất để chứng minh điều gì đó đúng. Một chiến lược rất thành công khác là phương pháp khoa học.

## Khoa học giải nguy

Khoa học khác căn bản với toán học ở chỗ các lý thuyết và định luật khoa học không thể được chứng minh là đúng. Tôi không thể chứng minh rằng định luật chuyển động thứ hai của Newton, $F=ma$, hay định luật vạn vật hấp dẫn, $F=Gm_1m_2/r^2$, là đúng. Tôi có thể trình bày các định luật này và đo đạc để xác nhận chúng đến nhiều chữ số thập phân, nhưng không thể chứng minh chúng theo nghĩa toán học. Dù tiến hành bao nhiêu thí nghiệm hay thu thập bao nhiêu bằng chứng thực nghiệm, vẫn luôn có khả năng một thí nghiệm nào đó cho thấy các định luật ấy sai.

Đó là bản chất của lý thuyết và định luật khoa học: chúng có thể bị bác bỏ, nhưng không thể chứng minh là đúng.

Vậy mà mỗi ngày chúng ta đều đặt mạng sống của mình vào những định luật ấy. Mỗi lần lên xe, bạn tin rằng $F=ma$ mô tả đáng tin cậy cách thế giới vận hành. Mỗi bước đi đều đặt sức khỏe và an toàn của bạn vào giả định rằng $F=Gm_1m_2/r^2$ là đúng.

Khoa học không chứng minh các mệnh đề là đúng; thay vào đó, nó cố chứng minh chúng là sai. Sau nhiều nỗ lực mà vẫn không bác bỏ được một mệnh đề, ta xem nó là đủ đúng cho mục đích của mình.

Tất nhiên, không phải mệnh đề nào cũng có thể chứng minh. Câu "Đây là một lời nói dối" không đúng cũng không sai. Đây là một trong những ví dụ đơn giản nhất về mệnh đề không thể chứng minh.

Cuối cùng, có thể nói toán học là ngành chứng minh các mệnh đề có thể chứng minh là đúng. Ngược lại, khoa học là ngành cố chứng minh các mệnh đề có thể chứng minh là sai.

## Kiểm thử

Dijkstra từng nói: "Kiểm thử cho thấy lỗi có tồn tại, chứ không chứng minh được lỗi không tồn tại." Nói cách khác, một bài kiểm thử có thể chứng minh chương trình sai, nhưng không thể chứng minh chương trình đúng. Sau khi kiểm thử đủ nhiều, ta chỉ có thể xem chương trình là đủ đúng cho mục đích của mình.

Hàm ý của điều này rất đáng kể. Phát triển phần mềm không phải một hoạt động toán học, dù có vẻ như nó thao tác với các cấu trúc toán học. Thay vào đó, phát triển phần mềm giống khoa học hơn: ta xác nhận tính đúng đắn bằng cách cố hết sức mà vẫn không chứng minh được chương trình sai.

Chỉ có thể cố chứng minh một chương trình sai nếu chương trình đó có thể chứng minh được. Một chương trình không thể chứng minh được, chẳng hạn do dùng `goto` không kiểm soát, sẽ không thể được xem là đúng, cho dù ta kiểm thử bao nhiêu lần.

Lập trình có cấu trúc buộc chúng ta phân tách đệ quy một chương trình thành một tập hợp các hàm nhỏ có thể chứng minh. Sau đó chúng ta có thể dùng bài kiểm thử để thử chứng minh những hàm nhỏ có thể chứng minh đó là sai. Nếu những bài kiểm thử đó không thể chứng minh sự sai, thì chúng ta coi các hàm đó là đủ đúng cho mục đích của mình.

## Kết luận

Chính khả năng chia chương trình thành những đơn vị có thể kiểm chứng và bác bỏ khiến lập trình có cấu trúc vẫn có giá trị ngày nay. Đó là lý do ngôn ngữ hiện đại thường không hỗ trợ câu lệnh `goto` không kiểm soát. Ở cấp độ kiến trúc, đó cũng là lý do ta vẫn xem phân tách chức năng là một trong những thực hành tốt nhất.

Ở mọi cấp độ, từ hàm nhỏ nhất đến thành phần lớn nhất, phần mềm vận hành như khoa học và vì vậy dựa trên khả năng bác bỏ. Kiến trúc sư phần mềm cố gắng định nghĩa các mô-đun, thành phần và dịch vụ có thể dễ dàng kiểm thử để phát hiện sai sót. Để làm vậy, họ dùng những kỷ luật hạn chế tương tự lập trình có cấu trúc, nhưng ở cấp độ cao hơn nhiều.

Chính những kỷ luật hạn chế ấy là những gì chúng ta sẽ nghiên cứu chi tiết ở các chương tiếp theo.