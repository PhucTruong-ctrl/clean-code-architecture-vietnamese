# Chương 3: Tổng quan về các mô hình lập trình

![Minh họa](assets/illustrations/03-paradigm-overview.png){w=260}

Ba mô hình lập trình (paradigm) trong chương tổng quan này là lập trình có cấu trúc, lập trình hướng đối tượng và lập trình hàm.

## Lập trình có cấu trúc

Mô hình đầu tiên được áp dụng, dù không phải mô hình đầu tiên được phát minh, là lập trình có cấu trúc. Edsger Wybe Dijkstra khám phá ra mô hình này năm 1968. Ông chỉ ra rằng việc dùng các lệnh nhảy tùy tiện (câu lệnh `goto`) gây hại cho cấu trúc chương trình. Như sẽ thấy trong các chương sau, Dijkstra thay những lệnh nhảy đó bằng các cấu trúc quen thuộc hơn như `if/then/else` và `do/while/until`.

Chúng ta có thể tóm tắt mô hình lập trình có cấu trúc như sau:
> **Lập trình có cấu trúc áp đặt kỷ luật lên việc chuyển giao quyền điều khiển trực tiếp.**

## Lập trình hướng đối tượng

Mô hình thứ hai được áp dụng, nhưng thực ra đã được khám phá sớm hơn hai năm, vào năm 1966, bởi Ole Johan Dahl và Kristen Nygaard. Hai lập trình viên này nhận ra rằng khung ngăn xếp lời gọi hàm trong ngôn ngữ ALGOL có thể được chuyển sang heap, nhờ đó các biến cục bộ do hàm khai báo vẫn tồn tại lâu sau khi hàm trả về. Hàm trở thành hàm tạo của lớp, biến cục bộ trở thành biến thể hiện, còn hàm lồng nhau trở thành phương thức. Từ đó dẫn đến việc khám phá ra tính đa hình thông qua cách dùng con trỏ hàm có kỷ luật.

Chúng ta có thể tóm tắt mô hình lập trình hướng đối tượng như sau:
> **Lập trình hướng đối tượng áp đặt kỷ luật lên việc chuyển giao quyền điều khiển gián tiếp.**

## Lập trình hàm

Mô hình thứ ba chỉ mới bắt đầu được áp dụng gần đây, nhưng lại là mô hình đầu tiên được phát minh. Thực ra, nó ra đời trước cả lập trình máy tính. Lập trình hàm bắt nguồn trực tiếp từ công trình của Alonzo Church. Năm 1936, trong lúc theo đuổi cùng vấn đề toán học đã thu hút Alan Turing, Church phát minh ra λ-calculus (lambda calculus). λ-calculus là nền tảng của ngôn ngữ LISP, do John McCarthy phát minh năm 1958. Một khái niệm nền tảng của λ-calculus là tính bất biến (immutability), nghĩa là giá trị các ký hiệu không thay đổi. Do đó, ngôn ngữ hàm không có câu lệnh gán (assignment statement). Trên thực tế, hầu hết ngôn ngữ hàm đều có cách thay đổi giá trị biến, nhưng chỉ cho phép làm vậy theo những quy tắc rất chặt chẽ.

Chúng ta có thể tóm tắt mô hình lập trình hàm như sau:
> **Lập trình hàm áp đặt kỷ luật lên việc gán giá trị.**

## Điều đáng suy ngẫm

Hãy nhận ra quy luật mà tôi đã cố ý thiết lập khi giới thiệu ba mô hình lập trình này: Mỗi mô hình lập trình đều **loại bỏ** khả năng khỏi người lập trình. **Không cái nào thêm khả năng mới.** Mỗi cái đều áp đặt một loại kỷ luật hạn chế. Các mô hình lập trình nói cho chúng ta biết những gì **không được làm**, nhiều hơn là nói những gì **nên làm**.

Một cách nhìn khác về vấn đề này là nhận ra rằng mỗi mô hình lập trình lấy đi của chúng ta một thứ gì đó. Ba mô hình lập trình cùng nhau loại bỏ câu lệnh `goto`, con trỏ hàm và câu lệnh gán. Vậy còn lại gì để lấy đi nữa?

Có lẽ không. Do đó ba mô hình lập trình này rất có thể là ba mô hình duy nhất chúng ta sẽ thấy, ít nhất là ba mô hình mang tính "tiêu cực" như thế. Bằng chứng khác cho thấy không còn mô hình nào như vậy là chúng đã được khám phá hết trong khoảng mười năm từ 1958 đến 1968. Trong nhiều thập kỷ sau đó, không có mô hình mới nào được thêm vào.

## Kết luận

Bài học lịch sử về các mô hình lập trình này có liên quan gì đến kiến trúc? **Mọi thứ.** Chúng ta dùng tính đa hình làm cơ chế để vượt qua ranh giới kiến trúc; dùng lập trình hàm để áp đặt kỷ luật lên vị trí và cách truy cập dữ liệu; và dùng lập trình có cấu trúc làm nền tảng thuật toán cho các mô-đun của mình.

Hãy nhận ra quy luật tôi cố ý đưa vào khi giới thiệu ba mô hình này: mô hình nào cũng tước bớt khả năng của lập trình viên. Không mô hình nào bổ sung khả năng mới. Mỗi mô hình đặt ra một kỷ luật nhằm hạn chế. Chúng chủ yếu cho ta biết không nên làm gì, hơn là nên làm gì.