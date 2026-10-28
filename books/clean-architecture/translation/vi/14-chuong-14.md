# Chương 14: Mức độ liên kết giữa các thành phần
![Minh họa](assets/illustrations/14-chuong-14-opener.png){w=300}

Ba nguyên tắc tiếp theo liên quan đến các mối quan hệ giữa các thành phần. Ở đây chúng ta lại gặp phải sự căng thẳng giữa khả năng phát triển và thiết kế logic. Các lực tác động lên kiến trúc của một cấu trúc thành phần mang tính kỹ thuật, chính trị và biến động.

## Nguyên tắc phụ thuộc không chu trình (ADP)
**Không cho phép chu trình trong biểu đồ phụ thuộc của thành phần.**

Bạn có từng làm việc cả ngày, làm cho một số thứ chạy được, rồi về nhà, chỉ để sáng hôm sau nhận thấy những thứ đó không còn hoạt động nữa? Tại sao nó không chạy? Vì có ai đó ở lại muộn hơn bạn và thay đổi thứ mà bạn phụ thuộc vào! Tôi gọi đây là "hội chứng sáng hôm sau".

"Hội chứng sáng hôm sau" xảy ra trong các môi trường phát triển nơi nhiều nhà phát triển cùng sửa đổi các tệp nguồn giống nhau. Trong các dự án nhỏ với chỉ vài nhà phát triển, nó không quá nghiêm trọng. Nhưng khi quy mô dự án và nhóm phát triển tăng lên, những buổi sáng sau có thể trở nên kinh khủng. Không hiếm khi nhiều tuần trôi qua mà nhóm không thể build một phiên bản ổn định của dự án. Thay vào đó, mọi người cứ việc thay đổi mã của mình để làm cho nó hoạt động với những thay đổi vừa được người khác thực hiện.

Trong vài thập kỷ qua, hai giải pháp cho vấn đề này đã được phát triển, cả hai đều đến từ ngành viễn thông. Giải pháp thứ nhất là "build hàng tuần", và giải pháp thứ hai là Nguyên tắc Phụ thuộc Không chu trình (ADP).

### Build hàng tuần

Build hàng tuần từng phổ biến trong các dự án trung bình. Nó hoạt động như sau: Tất cả nhà phát triển bỏ qua nhau trong bốn ngày đầu tuần. Tất cả đều làm việc trên các bản sao riêng của mã nguồn, và không lo lắng về việc tích hợp công việc trên cơ sở tập thể. Sau đó, vào thứ Sáu, họ tích hợp tất cả các thay đổi và build hệ thống.

Cách tiếp cận này có ưu điểm tuyệt vời là cho phép các nhà phát triển sống trong một thế giới biệt lập trong bốn ngày trên năm ngày. Nhược điểm, tất nhiên, là chi phí tích hợp lớn phải trả vào thứ Sáu.

Thật không may, khi dự án lớn lên, việc hoàn thành tích hợp vào thứ Sáu trở nên kém khả thi. Gánh nặng tích hợp tăng dần và bắt đầu kéo dài sang thứ Bảy. Sau vài lần làm việc vào thứ Bảy, các nhà phát triển sẽ muốn bắt đầu tích hợp từ thứ Năm, khiến thời điểm tích hợp dần lùi về giữa tuần.

Khi tỷ lệ nhiệm vụ giữa phát triển và tích hợp giảm xuống, hiệu suất của nhóm cũng giảm theo. Cuối cùng, tình huống này trở nên chán nản đến mức các nhà phát triển, hoặc người quản lý dự án, tuyên bố rằng lịch trình nên được thay đổi thành build hai tuần một lần. Điều này đủ dùng một thời gian, nhưng thời gian tích hợp vẫn tiếp tục tăng cùng với quy mô dự án.

Cuối cùng, kịch bản này dẫn đến khủng hoảng. Để duy trì hiệu suất, lịch build phải liên tục được kéo dài, nhưng làm vậy lại tăng rủi ro cho dự án. Việc tích hợp và kiểm thử ngày càng khó khăn, còn nhóm mất đi lợi ích của phản hồi nhanh.

### Loại bỏ các chu trình phụ thuộc

Giải pháp cho vấn đề này là phân chia môi trường phát triển thành các thành phần có thể phát hành. Các thành phần trở thành các đơn vị công việc có thể là trách nhiệm của một nhà phát triển đơn lẻ, hoặc một nhóm nhà phát triển. Khi các nhà phát triển làm cho một thành phần hoạt động, họ phát hành nó để các nhà phát triển khác sử dụng. Họ gán cho nó một số phát hành và di chuyển nó vào một thư mục để các nhóm khác dùng. Sau đó họ tiếp tục sửa đổi thành phần của mình trong khu vực riêng tư. Mọi người khác sử dụng phiên bản đã phát hành.

Khi các phát hành mới của một thành phần có sẵn, các nhóm khác có thể quyết định xem họ có nên áp dụng ngay phát hành mới hay không. Nếu họ quyết định không, họ chỉ cần tiếp tục dùng phiên bản cũ. Khi họ quyết định đã sẵn sàng, họ bắt đầu dùng phát hành mới.

Nhờ đó, không nhóm nào phải chờ nhóm khác. Thay đổi ở một thành phần không nhất thiết tác động ngay đến các nhóm khác. Mỗi nhóm tự quyết định khi nào cập nhật thành phần của mình để dùng bản phát hành mới từ các thành phần khác. Hơn nữa, việc tích hợp diễn ra từng bước nhỏ. Không có một thời điểm duy nhất mà tất cả nhà phát triển phải cùng tập trung để tích hợp mọi thứ họ đang làm.

Đây là một quy trình rất đơn giản và hợp lý, và nó được sử dụng rộng rãi. Tuy nhiên, để làm cho nó thành công, bạn phải quản lý cấu trúc phụ thuộc của các thành phần. **Không được có chu trình**. Nếu có chu trình trong cấu trúc phụ thuộc, thì "hội chứng sáng hôm sau" không thể tránh khỏi.

Xét biểu đồ thành phần trong Hình 14.1. Nó cho thấy một cấu trúc điển hình của các thành phần được lắp ráp thành một ứng dụng. Chức năng của ứng dụng này không quan trọng cho mục đích của ví dụ này. Điều quan trọng là cấu trúc phụ thuộc của các thành phần. Chú ý rằng cấu trúc này là một đồ thị có hướng. Các thành phần là các nút, và các mối quan hệ phụ thuộc là các cạnh có hướng.

**Hình 14.1** Biểu đồ thành phần điển hình

Chú ý thêm một điều: Dù bạn bắt đầu từ thành phần nào, đều không thể theo dõi các mối quan hệ phụ thuộc và quay trở lại thành phần đó. Cấu trúc này không có chu trình. Nó là một đồ thị có hướng không chu trình (DAG).

Bây giờ xét điều xảy ra khi nhóm chịu trách nhiệm về Presenters tạo một phát hành mới của thành phần của họ. Dễ dàng tìm ra ai bị ảnh hưởng bởi phát hành này; bạn chỉ cần theo dõi các mũi tên phụ thuộc ngược lại. Do đó View và Main đều sẽ bị ảnh hưởng. Các nhà phát triển hiện đang làm việc trên các thành phần đó sẽ phải quyết định khi nào nên tích hợp công việc của họ với phát hành mới của Presenters.

Chú ý thêm rằng khi Main được phát hành, nó hoàn toàn không có tác động đến bất kỳ thành phần nào khác trong hệ thống. Chúng không biết về Main, và không quan tâm khi Main thay đổi. Điều này tốt. Nó có nghĩa là tác động của việc phát hành Main tương đối nhỏ.

Khi các nhà phát triển làm việc trên thành phần Presenters muốn chạy kiểm thử cho thành phần đó, họ chỉ cần build phiên bản Presenters của họ với các phiên bản của Interactors và Entities mà họ đang dùng. Không thành phần nào khác trong hệ thống cần được liên quan. Điều này tốt. Nó có nghĩa là các nhà phát triển làm việc trên Presenters có ít việc phải làm để thiết lập kiểm thử, và họ có ít biến số phải cân nhắc.

Khi đến lúc phát hành toàn bộ hệ thống, quy trình diễn ra từ dưới lên trên. Trước tiên thành phần Entities được biên dịch, kiểm thử, và phát hành. Sau đó làm tương tự cho Database và Interactors. Các thành phần này được theo sau bởi Presenters, View, Controllers, và sau đó là Authorizer. Main là cuối cùng. Quy trình này rất rõ ràng và dễ xử lý. Chúng ta biết cách build hệ thống vì chúng ta hiểu các phụ thuộc giữa các phần của nó.

### Tác động của chu trình trong biểu đồ phụ thuộc thành phần

Giả sử một yêu cầu mới ép buộc chúng ta phải thay đổi một trong các lớp trong Entities để nó sử dụng một lớp trong Authorizer. Ví dụ, hãy nói rằng lớp User trong Entities sử dụng lớp Permissions trong Authorizer. Điều này tạo ra một chu trình phụ thuộc, như được minh họa trong Hình 14.2.

Chu trình này lập tức gây ra một số vấn đề. Chẳng hạn, các nhà phát triển làm việc trên thành phần Database biết rằng để phát hành, thành phần này phải tương thích với Entities. Nhưng khi đã có chu trình, Database còn phải tương thích với Authorizer, trong khi Authorizer lại phụ thuộc vào Interactors. Vì vậy, Database trở nên khó phát hành hơn nhiều. Trên thực tế, Entities, Authorizer và Interactors đã hợp thành một thành phần lớn. Mọi nhà phát triển làm việc trên bất kỳ thành phần nào trong số đó đều có thể gặp “hội chứng sáng hôm sau”, vì họ buộc phải dùng đúng cùng một bản phát hành của các thành phần kia.

Nhưng đó mới chỉ là một phần vấn đề. Khi muốn kiểm thử thành phần Entities, thật thất vọng khi thấy chúng ta phải build và tích hợp nó với Authorizer và Interactors. Mức độ kết nối này giữa các thành phần thật đáng lo ngại, nếu không muốn nói là khó chịu.

Bạn có thể đã thắc mắc tại sao phải đưa vào nhiều thư viện khác nhau đến vậy, và nhiều mã của người khác đến vậy, chỉ để chạy một bài kiểm thử đơn vị đơn giản của một lớp của mình. Nếu bạn điều tra một chút, bạn có thể sẽ phát hiện ra rằng có chu trình trong biểu đồ phụ thuộc. Các chu trình như vậy làm cho việc tách biệt các thành phần trở nên rất khó khăn. Kiểm thử đơn vị và phát hành trở nên rất khó khăn và dễ sai sót. Ngoài ra, các vấn đề về build tăng lên theo cấp số nhân với số lượng mô-đun.

Hơn nữa, khi có chu trình trong biểu đồ phụ thuộc, có thể rất khó xác định thứ tự mà bạn phải build các thành phần. Thực tế, có lẽ không có thứ tự đúng nào. Điều này có thể dẫn đến những vấn đề rất tồi tệ trong các ngôn ngữ như Java, nơi các khai báo được đọc từ các tệp nhị phân đã biên dịch.

### Phá vỡ chu trình

Luôn có thể phá vỡ một chu trình của các thành phần và khôi phục biểu đồ phụ thuộc trở thành DAG. Có hai cơ chế chính để làm như vậy:

1. **Áp dụng Nguyên tắc Đảo ngược Phụ thuộc (DIP).** Trong trường hợp của Hình 14.3, chúng ta có thể tạo một giao diện có các phương thức mà User cần. Sau đó chúng ta đặt giao diện đó vào Entities và kế thừa nó vào Authorizer. Điều này đảo ngược phụ thuộc giữa Entities và Authorizer, từ đó phá vỡ chu trình.

**Hình 14.3** Đảo ngược phụ thuộc giữa Entities và Authorizer

2. **Tạo một thành phần mới mà cả Entities và Authorizer đều phụ thuộc vào.** Di chuyển các lớp mà chúng cùng phụ thuộc vào thành phần mới đó (Hình 14.4).

**Hình 14.4** Thành phần mới mà cả Entities và Authorizer đều phụ thuộc vào

### Sự dao động (The Jitters)

Giải pháp thứ hai ngụ ý rằng cấu trúc thành phần có tính biến động khi các yêu cầu thay đổi. Thực tế, khi ứng dụng lớn lên, cấu trúc phụ thuộc của thành phần sẽ dao động và phát triển. Do đó, cấu trúc phụ thuộc phải luôn được giám sát để tìm chu trình. Khi chu trình xuất hiện, chúng phải được phá vỡ bằng cách nào đó. Đôi khi điều này sẽ có nghĩa là tạo ra các thành phần mới, làm cho cấu trúc phụ thuộc phát triển.

## Thiết kế từ trên xuống (Top-Down Design)

Các vấn đề chúng ta đã thảo luận dẫn đến một kết luận không thể tránh khỏi: **Cấu trúc thành phần không thể được thiết kế từ trên xuống**. Nó không phải là một trong những thứ được thiết kế đầu tiên của hệ thống, mà là thứ tiến hóa khi hệ thống lớn lên và thay đổi.

Một số người đọc có thể thấy điểm này đi ngược trực giác. Chúng ta đã quen mong đợi rằng các phân chia lớn, như các thành phần, cũng sẽ là các phân chia chức năng ở cấp cao.

Khi chúng ta nhìn thấy một cấu trúc lớn như biểu đồ phụ thuộc thành phần, chúng ta tin rằng các thành phần nên đại diện cho các chức năng của hệ thống. Tuy nhiên, dường như đây không phải là một thuộc tính của các biểu đồ phụ thuộc thành phần.

Thực tế, các biểu đồ phụ thuộc thành phần có rất ít liên quan đến việc mô tả chức năng của ứng dụng. Thay vào đó, chúng là một bản đồ cho khả năng build và khả năng bảo trì của ứng dụng. Đây là lý do tại sao chúng không được thiết kế ở đầu dự án. Không có phần mềm nào để build hoặc bảo trì, nên không có nhu cầu cho một bản đồ build và bảo trì. Nhưng khi càng nhiều mô-đun tích lũy trong các giai đoạn đầu của triển khai và thiết kế, có một nhu cầu ngày càng lớn để quản lý các phụ thuộc sao cho dự án có thể được phát triển mà không gặp "hội chứng sáng hôm sau". Hơn nữa, chúng ta muốn giữ các thay đổi càng cục bộ càng tốt, nên chúng ta bắt đầu chú ý đến SRP và CCP và đặt cùng nhau các lớp có khả năng thay đổi cùng lúc.

Một trong những mối quan tâm áp đảo với cấu trúc phụ thuộc này là sự cô lập sự biến động. Chúng ta không muốn các thành phần thay đổi thường xuyên và vì những lý do ngẫu nhiên tác động đến các thành phần mà nếu không thì nên ổn định. Ví dụ, chúng ta không muốn các thay đổi về mặt thẩm mỹ của GUI tác động đến các quy tắc kinh doanh của chúng ta. Chúng ta không muốn việc thêm hoặc sửa đổi báo cáo tác động đến các chính sách ở cấp cao nhất. Do đó, biểu đồ phụ thuộc thành phần được tạo ra và định hình bởi các kiến trúc sư để bảo vệ các thành phần ổn định, giá trị cao khỏi các thành phần biến động.

Khi ứng dụng tiếp tục phát triển, chúng ta bắt đầu quan tâm đến việc tạo ra các phần tử có thể tái sử dụng. Tại thời điểm này, CRP bắt đầu ảnh hưởng đến cấu thành của các thành phần. Cuối cùng, khi chu trình xuất hiện, ADP được áp dụng và biểu đồ phụ thuộc thành phần dao động và phát triển.

Nếu chúng ta cố gắng thiết kế cấu trúc phụ thuộc thành phần trước khi thiết kế bất kỳ lớp nào, chúng ta có thể sẽ thất bại khá tệ. Chúng ta sẽ không biết nhiều về sự đóng chung, chúng ta sẽ không biết về bất kỳ phần tử có thể tái sử dụng nào, và chúng ta gần như chắc chắn sẽ tạo ra các thành phần sản sinh ra chu trình phụ thuộc. Do đó, cấu trúc phụ thuộc thành phần lớn lên và tiến hóa cùng với thiết kế logic của hệ thống.

## Nguyên tắc phụ thuộc ổn định (SDP)
**Phụ thuộc theo hướng ổn định.**

Thiết kế không thể hoàn toàn tĩnh. Một số sự biến động là cần thiết nếu thiết kế phải được bảo trì. Bằng cách tuân theo Nguyên tắc Đóng chung (CCP), chúng ta tạo ra các thành phần nhạy cảm với một số loại thay đổi nhưng miễn dịch với những loại khác. Một số thành phần trong số này được thiết kế để biến động. Chúng ta mong đợi chúng thay đổi.

Bất kỳ thành phần nào mà chúng ta mong đợi sẽ biến động **không nên** được phụ thuộc vào bởi một thành phần khó thay đổi. Nếu không, thành phần biến động cũng sẽ trở nên khó thay đổi.

Đây là sự nghịch lý của phần mềm: một mô-đun mà bạn đã thiết kế để dễ thay đổi có thể bị biến thành khó thay đổi bởi ai đó chỉ cần treo một sự phụ thuộc lên nó. Không một dòng mã nguồn nào trong mô-đun của bạn cần thay đổi, nhưng mô-đun của bạn đột ngột trở nên khó thay đổi hơn. Bằng cách tuân theo Nguyên tắc Phụ thuộc Ổn định (SDP), chúng ta đảm bảo rằng các mô-đun được dự định dễ thay đổi không bị phụ thuộc vào bởi các mô-đun khó thay đổi hơn.

### Ổn định (Stability)

"Ổn định" ở đây có nghĩa là gì? Đặt một đồng xu đứng dọc. Nó có ổn định ở tư thế đó không? Bạn có thể nói "không". Tuy nhiên, trừ khi bị xao động, nó sẽ giữ nguyên tư thế đó trong một thời gian rất dài. Do đó, sự ổn định không liên quan trực tiếp đến tần suất thay đổi. Đồng xu không thay đổi, nhưng khó mà coi nó là ổn định.

Từ điển Webster nói rằng một thứ là ổn định nếu nó "không dễ bị di chuyển". Sự ổn định liên quan đến lượng công sức cần thiết để thực hiện một thay đổi. Một mặt, đồng xu đứng dọc không ổn định vì nó cần rất ít công sức để đẩy ngã nó. Mặt khác, một chiếc bàn rất ổn định vì nó cần một lượng công sức đáng kể để lật nó ngửa.

Điều này liên quan gì đến phần mềm? Nhiều yếu tố có thể khiến một thành phần phần mềm khó thay đổi, chẳng hạn kích thước, độ phức tạp và mức độ rõ ràng. Ở đây, chúng ta sẽ bỏ qua những yếu tố đó và tập trung vào điểm khác biệt sau: **Một cách chắc chắn để khiến thành phần phần mềm khó thay đổi là làm cho nhiều thành phần khác phụ thuộc vào nó.** Thành phần có nhiều phụ thuộc đến rất ổn định, vì cần nhiều công sức phối hợp với mọi thành phần phụ thuộc trước khi thay đổi được thực hiện.

Biểu đồ trong Hình 14.5 cho thấy X, một thành phần ổn định. Ba thành phần phụ thuộc vào X, nên nó có ba lý do tốt để không thay đổi. Chúng ta nói rằng X chịu trách nhiệm đối với ba thành phần đó. Ngược lại, X không phụ thuộc vào bất cứ thứ gì, nên nó không có ảnh hưởng bên ngoài để làm nó thay đổi. Chúng ta nói nó độc lập.

**Hình 14.5** X: một thành phần ổn định

Hình 14.6 cho thấy Y, một thành phần rất không ổn định. Không thành phần nào khác phụ thuộc vào Y, nên chúng ta nói rằng nó không chịu trách nhiệm. Y cũng có ba thành phần mà nó phụ thuộc vào, nên thay đổi có thể đến từ ba nguồn bên ngoài. Chúng ta nói rằng Y phụ thuộc.

**Hình 14.6** Y: một thành phần rất không ổn định

### Các chỉ số Ổn định

Làm thế nào để đo lường sự ổn định của một thành phần? Một cách là đếm số phụ thuộc đi vào và đi ra khỏi thành phần đó. Các số đếm này sẽ cho phép chúng ta tính toán sự ổn định vị trí của thành phần.

* **Fan-in (Độ vào):** Phụ thuộc đến. Chỉ số này xác định số lượng lớp bên ngoài thành phần này mà phụ thuộc vào các lớp bên trong thành phần.
* **Fan-out (Độ ra):** Phụ thuộc đi. Chỉ số này xác định số lượng lớp bên trong thành phần này mà phụ thuộc vào các lớp bên ngoài thành phần.
* **I: Độ không ổn định (Instability):** I = Fan-out / (Fan-in + Fan-out). Chỉ số này có phạm vi [0, 1]. I = 0 chỉ ra một thành phần ổn định tối đa. I = 1 chỉ ra một thành phần không ổn định tối đa.

Các chỉ số Fan-in và Fan-out[^1] được tính bằng cách đếm số lượng các lớp bên ngoài thành phần đang xét mà có sự phụ thuộc với các lớp bên trong thành phần đang xét. Xét ví dụ trong Hình 14.7.

**Hình 14.7** Ví dụ của chúng ta

Giả sử chúng ta muốn tính sự ổn định của thành phần Cc. Chúng ta thấy có ba lớp bên ngoài Cc phụ thuộc vào các lớp trong Cc. Do đó, Fan-in = 3. Hơn nữa, có một lớp bên ngoài Cc mà các lớp trong Cc phụ thuộc vào. Do đó, Fan-out = 1 và I = 1/4.

Trong C++, các phụ thuộc này thường được biểu diễn bằng các câu lệnh #include. Thực tế, chỉ số I dễ tính nhất khi bạn tổ chức mã nguồn sao cho mỗi tệp nguồn chứa một lớp. Trong Java, chỉ số I có thể được tính bằng cách đếm các câu lệnh import và tên đủ điều kiện.

Khi chỉ số I bằng 1, điều đó có nghĩa là không thành phần nào khác phụ thuộc vào thành phần này (Fan-in = 0), và thành phần này phụ thuộc vào các thành phần khác (Fan-out > 0). Tình huống này là mức không ổn định nhất mà một thành phần có thể đạt được; nó là không chịu trách nhiệm và phụ thuộc. Sự thiếu hụt thành phần phụ thuộc của nó không cho thành phần lý do nào để không thay đổi, và các thành phần mà nó phụ thuộc vào có thể cho nó nhiều lý do để thay đổi.

Ngược lại, khi chỉ số I bằng 0, điều đó có nghĩa là thành phần được các thành phần khác phụ thuộc vào (Fan-in > 0), nhưng bản thân nó không phụ thuộc vào bất kỳ thành phần nào khác (Fan-out = 0). Thành phần như vậy là chịu trách nhiệm và độc lập. Nó ổn định nhất có thể. Các thành phần phụ thuộc của nó làm cho việc thay đổi thành phần trở nên khó khăn, và nó không có phụ thuộc nào có thể ép nó phải thay đổi.

SDP nói rằng chỉ số I của một thành phần nên lớn hơn các chỉ số I của các thành phần mà nó phụ thuộc vào. Đó là, các chỉ số I nên giảm theo hướng phụ thuộc.

### Không phải thành phần nào cũng nên ổn định

Nếu tất cả các thành phần trong một hệ thống đều ổn định tối đa, hệ thống sẽ không thể thay đổi. Đây không phải là tình huống mong muốn. Thực tế, chúng ta muốn thiết kế cấu trúc thành phần của mình sao cho một số thành phần không ổn định và một số ổn định. Biểu đồ trong Hình 14.8 cho thấy một cấu hình lý tưởng cho một hệ thống với ba thành phần.

**Hình 14.8** Cấu hình lý tưởng cho hệ thống ba thành phần

Các thành phần có thể thay đổi nằm ở trên và phụ thuộc vào thành phần ổn định ở dưới. Việc đặt các thành phần không ổn định ở trên cùng của biểu đồ là một quy ước hữu ích vì bất kỳ mũi tên nào chỉ lên trên đều vi phạm SDP (và, như chúng ta sẽ thấy sau, cả ADP).

Biểu đồ trong Hình 14.9 cho thấy SDP có thể bị vi phạm như thế nào.

**Hình 14.9** Vi phạm SDP

Flexible là một thành phần mà chúng ta đã thiết kế để dễ thay đổi. Chúng ta muốn Flexible không ổn định. Tuy nhiên, một nhà phát triển nào đó, đang làm việc trong thành phần tên là Stable, đã treo một sự phụ thuộc lên Flexible. Điều này vi phạm SDP vì chỉ số I cho Stable nhỏ hơn nhiều so với chỉ số I cho Flexible. Hệ quả là Flexible sẽ không còn dễ thay đổi nữa. Một thay đổi đối với Flexible sẽ ép buộc chúng ta phải đối phó với Stable và tất cả các thành phần phụ thuộc của nó.

Để khắc phục vấn đề này, chúng ta phải làm cách nào đó phá vỡ sự phụ thuộc của Stable vào Flexible. Tại sao sự phụ thuộc này tồn tại? Giả sử có một lớp C bên trong Flexible mà một lớp U bên trong Stable cần sử dụng (Hình 14.10).

**Hình 14.10** U trong Stable sử dụng C trong Flexible

Chúng ta có thể khắc phục bằng cách sử dụng DIP. Chúng ta tạo một lớp giao diện tên là US và đặt nó trong một thành phần tên là UServer. Chúng ta đảm bảo rằng giao diện này khai báo tất cả các phương thức mà U cần dùng. Sau đó chúng ta làm cho C triển khai giao diện này như được minh họa trong Hình 14.11. Điều này phá vỡ sự phụ thuộc của Stable vào Flexible, và ép buộc cả hai thành phần phụ thuộc vào UServer. UServer rất ổn định (I = 0), và Flexible giữ được sự không ổn định cần thiết của nó (I = 1). Tất cả các phụ thuộc bây giờ đều chảy theo hướng giảm I.

**Hình 14.11** C triển khai lớp giao diện US

### Các thành phần trừu tượng (Abstract Components)

Bạn có thể thấy lạ khi chúng ta tạo một thành phần, trong ví dụ này là UService, chỉ chứa một giao diện. Thành phần như vậy không có mã thực thi! Tuy nhiên, đây là chiến thuật phổ biến và cần thiết khi sử dụng ngôn ngữ định kiểu tĩnh như Java và C#. Những thành phần trừu tượng này rất ổn định, nên là đích phụ thuộc lý tưởng cho các thành phần kém ổn định hơn.

Trong các ngôn ngữ định kiểu động như Ruby và Python, những thành phần trừu tượng này hoàn toàn không tồn tại, cũng như các phụ thuộc vốn sẽ hướng đến chúng. Cấu trúc phụ thuộc trong các ngôn ngữ này đơn giản hơn nhiều vì đảo ngược phụ thuộc không cần khai báo hay kế thừa giao diện.

## Nguyên tắc trừu tượng ổn định (SAP)
**Một thành phần nên trừu tượng đến mức nó ổn định.**

### Chúng ta đặt chính sách cấp cao ở đâu?

Một số phần mềm trong hệ thống không nên thay đổi thường xuyên. Chúng đại diện cho các quyết định kiến trúc và chính sách cấp cao. Chúng ta không muốn những quyết định kinh doanh và kiến trúc này biến động. Vì vậy, mã nguồn đóng gói các chính sách cấp cao nên nằm trong các thành phần ổn định (I = 0). Các thành phần không ổn định (I = 1) chỉ nên chứa phần mềm có tính biến động, tức phần mềm cần được thay đổi nhanh chóng và dễ dàng.

Tuy nhiên, nếu các chính sách cấp cao được đặt vào các thành phần ổn định, thì mã nguồn đại diện cho các chính sách đó sẽ khó thay đổi. Điều này có thể làm cho kiến trúc tổng thể trở nên cứng nhắc. Làm thế nào một thành phần ổn định tối đa (I = 0) có thể đủ linh hoạt để chịu đựng được thay đổi? Câu trả lời nằm trong OCP. Nguyên tắc này nói rằng có thể và mong muốn tạo ra các lớp đủ linh hoạt để được mở rộng mà không yêu cầu sửa đổi. Loại lớp nào tuân theo nguyên tắc này? Lớp trừu tượng.

### Giới thiệu Nguyên tắc Trừu tượng Ổn định

Nguyên tắc Trừu tượng Ổn định (SAP) thiết lập một mối quan hệ giữa sự ổn định và mức độ trừu tượng. Một mặt, nó nói rằng một thành phần ổn định cũng nên là trừu tượng để sự ổn định của nó không ngăn cản nó được mở rộng. Mặt khác, nó nói rằng một thành phần không ổn định nên là cụ thể vì sự không ổn định của nó cho phép mã cụ thể bên trong nó dễ dàng được thay đổi.

Do đó, nếu một thành phần sẽ ổn định, nó nên bao gồm các giao diện và các lớp trừu tượng để có thể được mở rộng. Các thành phần ổn định có thể mở rộng là linh hoạt và không khiến kiến trúc bị ràng buộc quá chặt.

SDP và SAP kết hợp lại tương đương với DIP cho các thành phần. Điều này đúng vì SDP nói rằng các phụ thuộc nên chạy theo hướng ổn định, và SAP nói rằng ổn định ngụ ý trừu tượng. Do đó, các phụ thuộc chạy theo hướng trừu tượng.

Tuy nhiên, DIP là nguyên tắc áp dụng cho các lớp, và lớp không có vùng xám: hoặc trừu tượng, hoặc không. SDP kết hợp với SAP áp dụng cho các thành phần, nên một thành phần có thể vừa trừu tượng một phần, vừa ổn định một phần.

### Đo lường mức độ trừu tượng

Chỉ số A là một thước đo của mức độ trừu tượng của một thành phần. Giá trị của nó đơn giản là tỷ lệ giữa số giao diện và lớp trừu tượng trong một thành phần với tổng số lớp trong thành phần đó.

* **Nc:** Số lượng lớp trong thành phần.
* **Na:** Số lượng lớp trừu tượng và giao diện trong thành phần.
* **A: Mức độ trừu tượng (Abstractness).** A = Na ÷ Nc.

Chỉ số A dao động từ 0 đến 1. Giá trị 0 ngụ ý rằng thành phần không có lớp trừu tượng nào. Giá trị 1 ngụ ý rằng thành phần chỉ chứa các lớp trừu tượng.

### Dãy chính (Main Sequence)

Chúng ta hiện đang ở vị trí xác định mối quan hệ giữa sự ổn định (I) và mức độ trừu tượng (A). Để làm được điều này, chúng ta tạo một biểu đồ với A trên trục tung và I trên trục hoành (Hình 14.12). Nếu chúng ta vẽ hai loại thành phần "tốt" lên biểu đồ này, chúng ta sẽ tìm thấy các thành phần ổn định tối đa và trừu tượng tối đa ở góc trên bên trái tại (0, 1). Các thành phần không ổn định tối đa và cụ thể nằm ở góc dưới bên phải tại (1, 0).

**Hình 14.12** Biểu đồ I/A

Không phải thành phần nào cũng rơi vào một trong hai vị trí này, vì các thành phần thường có các độ trừu tượng và ổn định. Ví dụ, rất phổ biến khi một lớp trừu tượng kế thừa từ một lớp trừu tượng khác. Lớp dẫn xuất là một trừu tượng có một phụ thuộc. Do đó, dù nó trừu tượng tối đa, nó sẽ không ổn định tối đa. Phụ thuộc của nó sẽ giảm sự ổn định của nó.

Vì không thể yêu cầu mọi thành phần phải nằm tại (0, 1) hoặc (1, 0), ta cần xác định một tập hợp các điểm hợp lý trên biểu đồ A/I. Có thể tìm ra tập hợp đó bằng cách xác định những vùng mà thành phần **không** nên nằm, tức các vùng loại trừ (Hình 14.13).

**Hình 14.13** Các vùng loại trừ

#### Vùng đau khổ (Zone of Pain)

Xét một thành phần trong khu vực (0, 0). Đây là một thành phần ổn định cao và cụ thể. Thành phần như vậy không mong muốn vì nó cứng nhắc. Nó không thể được mở rộng vì nó không trừu tượng, và nó rất khó thay đổi do sự ổn định của nó. Do đó chúng ta thường không mong đợi thấy các thành phần thiết kế tốt ngồi gần (0, 0). Khu vực quanh (0, 0) là một vùng loại trừ được gọi là Vùng đau khổ.

Một số thực thể phần mềm thực sự rơi vào Vùng đau khổ. Một ví dụ là lược đồ cơ sở dữ liệu. Các lược đồ cơ sở dữ liệu nổi tiếng là biến động, cực kỳ cụ thể, và bị phụ thuộc nhiều. Đây là một lý do tại sao giao diện giữa ứng dụng hướng đối tượng và cơ sở dữ liệu rất khó quản lý, và tại sao cập nhật lược đồ thường đau đớn.

Một ví dụ khác về phần mềm ngồi gần khu vực (0, 0) là thư viện tiện ích cụ thể. Dù thư viện như vậy có chỉ số I = 1, nó thực tế có thể không biến động. Xét thành phần String, ví dụ. Dù tất cả các lớp trong nó đều cụ thể, nó được dùng phổ biến đến mức thay đổi nó sẽ tạo ra hỗn loạn. Do đó String là không biến động.

Các thành phần không biến động là vô hại trong vùng (0, 0) vì chúng không có khả năng bị thay đổi. Với lý do đó, chỉ có các thành phần phần mềm biến động mới gây vấn đề trong Vùng đau khổ. Càng biến động một thành phần trong Vùng đau khổ, nó càng "đau khổ". Thực tế, chúng ta có thể coi sự biến động là trục thứ ba của biểu đồ. Với hiểu biết này, Hình 14.13 chỉ cho thấy mặt phẳng đau khổ nhất, nơi độ biến động = 1.

#### Vùng vô dụng (Zone of Uselessness)

Xét một thành phần gần (1, 1). Vị trí này không mong muốn vì nó trừu tượng tối đa, nhưng không có thành phần phụ thuộc. Các thành phần như vậy là vô dụng. Do đó khu vực này được gọi là Vùng vô dụng.

Các thực thể phần mềm trú ngụ trong khu vực này là một loại phế liệu. Chúng thường là các lớp trừu tượng thừa không ai bao giờ triển khai. Chúng ta tìm thấy chúng trong các hệ thống từ thời gian qua, ngồi trong cơ sở mã, không được dùng.

Một thành phần có vị trí sâu bên trong Vùng vô dụng phải chứa một phần đáng kể các thực thể như vậy. Rõ ràng, sự hiện diện của các thực thể vô dụng như vậy là không mong muốn.

### Tránh các vùng loại trừ

Rõ ràng là các thành phần biến động nhất của chúng ta nên được giữ càng xa càng tốt khỏi cả hai vùng loại trừ. Tập hợp các điểm xa nhất từ mỗi vùng là đường nối (1, 0) và (0, 1). Tôi gọi đường này là Dãy chính[^2].

**Hình 14.14** Biểu đồ phân tán của các thành phần

Một thành phần ngồi trên Dãy chính không "quá trừu tượng" cho sự ổn định của nó, cũng không "quá không ổn định" cho mức độ trừu tượng của nó. Nó không vô dụng cũng không đặc biệt đau khổ. Nó bị phụ thuộc vào ở mức độ mà nó trừu tượng, và nó phụ thuộc vào người khác ở mức độ mà nó cụ thể.

Vị trí mong muốn nhất cho một thành phần là ở một trong hai đầu mút của Dãy chính. Các kiến trúc sư giỏi nỗ lực đặt phần lớn thành phần của họ ở các đầu mút đó. Tuy nhiên, theo kinh nghiệm của tôi, một phần nhỏ các thành phần trong một hệ thống lớn không hoàn toàn trừu tượng cũng không hoàn toàn ổn định. Các thành phần đó có đặc điểm tốt nhất nếu chúng ở trên, hoặc gần, Dãy chính.

### Khoảng cách từ Dãy chính

Điều này dẫn chúng ta đến chỉ số cuối cùng. Nếu các thành phần mong muốn nằm trên, hoặc gần, Dãy chính, thì chúng ta có thể tạo một chỉ số đo lường một thành phần xa đến đâu từ lý tưởng này.

* **D: Khoảng cách (Distance).** D = |A + I - 1|[^3]. Phạm vi của chỉ số là [0, 1]. Giá trị 0 cho biết thành phần nằm đúng trên Dãy chính. Giá trị 1 cho biết nó nằm xa Dãy chính nhất có thể.

Cho chỉ số này, một thiết kế có thể được phân tích cho sự tuân thủ tổng thể đối với Dãy chính. Chỉ số D cho mỗi thành phần có thể được tính. Bất kỳ thành phần nào có giá trị D không gần bằng không có thể được xem xét lại và cấu trúc lại. Phân tích thống kê của một thiết kế cũng là khả thi. Chúng ta có thể tính trung bình và phương sai của tất cả các chỉ số D cho các thành phần trong một thiết kế. Chúng ta mong đợi một thiết kế tuân thủ có trung bình và phương sai gần bằng không. Phương sai có thể được dùng để thiết lập "giới hạn kiểm soát" để nhận diện các thành phần "ngoài lệ" so với tất cả các thành phần khác.

Trong biểu đồ phân tán trong Hình 14.14, chúng ta thấy phần lớn các thành phần nằm dọc theo Dãy chính, nhưng một số trong số chúng xa hơn một độ lệch chuẩn (Z = 1) từ trung bình. Những thành phần bất thường này đáng giá xem xét kỹ hơn. Với một lý do nào đó, chúng hoặc rất trừu tượng với ít thành phần phụ thuộc, hoặc rất cụ thể với nhiều thành phần phụ thuộc.

Một cách khác để dùng các chỉ số là vẽ chỉ số D của mỗi thành phần theo thời gian. Biểu đồ trong Hình 14.15 là bản mô phỏng của một biểu đồ như vậy. Bạn có thể thấy một số phụ thuộc kỳ lạ đã từ từ len lỏi vào thành phần Payroll trong vài phát hành gần đây. Biểu đồ cho thấy ngưỡng kiểm soát tại D = 0.1. Điểm R2.1 đã vượt quá giới hạn kiểm soát này, vì vậy sẽ đáng giá để tìm hiểu tại sao thành phần này lại xa Dãy chính đến vậy.

**Hình 14.15** Biểu đồ D của một thành phần đơn lẻ theo thời gian

## Kết luận

Các chỉ số quản lý phụ thuộc được mô tả trong chương này đo lường sự tuân thủ của một thiết kế đối với một mẫu phụ thuộc và trừu tượng mà tôi nghĩ là một mẫu "tốt". Kinh nghiệm đã chỉ ra rằng một số phụ thuộc là tốt và những cái khác xấu. Mẫu này phản ánh kinh nghiệm đó. Tuy nhiên, một chỉ số không phải là thần thánh; nó chỉ là phép đo theo một tiêu chuẩn tùy ý. Các chỉ số này, ở mức tốt nhất, cũng chỉ không hoàn hảo, nhưng tôi hy vọng bạn thấy chúng hữu ích.

[^1]: Trong các xuất bản trước, tôi dùng tên Efferent và Afferent couplings (Ce và Ca) cho Fan-out và Fan-in, tương ứng. Đó chỉ là sự kiêu ngạo của tôi: tôi thích ẩn dụ về hệ thần kinh trung ương.
[^2]: Tác giả xin phép người đọc cho phép mượn một thuật ngữ quan trọng như vậy từ thiên văn học.
[^3]: Trong các xuất bản trước, tôi gọi chỉ số này là D′. Tôi không thấy lý do nào để tiếp tục thực hành đó.