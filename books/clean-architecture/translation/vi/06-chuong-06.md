# Chương 6: Lập trình hàm
![Minh họa](assets/illustrations/06-chuong-06-opener.png){w=220}

Ở nhiều phương diện, các khái niệm của lập trình hàm có từ trước cả lập trình máy tính. Mô hình này dựa chủ yếu trên λ-calculus do Alonzo Church phát minh trong thập niên 1930.

## Bình phương các số nguyên (SQUARES OF INTEGERS)

Để giải thích lập trình hàm là gì, tốt nhất là xem xét một vài ví dụ. Hãy cùng tìm hiểu một bài toán đơn giản: in ra bình phương của 25 số nguyên đầu tiên.

Trong một ngôn ngữ như Java, chúng ta có thể viết như sau:

```java
public class Squint {
    public static void main(String args[]) {
        for (int i=0; i<25; i++)
            System.out.println(i*i);
    }
}
```

Trong một ngôn ngữ như Clojure, một ngôn ngữ phái sinh từ Lisp và mang tính hàm, chúng ta có thể triển khai cùng một chương trình như sau:

```clojure
(println (take 25 (map (fn [x] (* x x)) (range))))
```

Nếu bạn không biết Lisp, đoạn mã trên có thể trông hơi kỳ lạ. Hãy cùng định dạng lại một chút và thêm chú thích:

```clojure
(println ;___________________ In ra
  (take 25 ;_________________ 25 phần tử đầu
    (map (fn [x] (* x x)) ;__ bình phương
      (range)))) ;___________ của các số nguyên
```

Rõ ràng `println`, `take`, `map`, và `range` đều là các hàm. Trong Lisp, bạn gọi một hàm bằng cách đặt nó trong cặp ngoặc đơn. Ví dụ, `(range)` gọi hàm `range`.

Biểu thức `(fn [x] (* x x))` là một hàm ẩn danh gọi hàm nhân, truyền đối số đầu vào của nó hai lần. Nói cách khác, nó tính bình phương của đầu vào.

Nhìn lại toàn bộ biểu thức, tốt nhất là bắt đầu từ lời gọi hàm nằm sâu nhất bên trong.

- Hàm `range` trả về một danh sách không bao giờ kết thúc các số nguyên bắt đầu từ 0.
- Danh sách này được truyền vào hàm `map`, hàm này gọi hàm ẩn danh tính bình phương trên từng phần tử, tạo ra một danh sách mới không bao giờ kết thúc chứa tất cả các bình phương.
- Danh sách các bình phương được truyền vào hàm `take`, hàm này trả về một danh sách mới chỉ chứa 25 phần tử đầu tiên.
- Hàm `println` in ra đầu vào của nó, là một danh sách 25 bình phương đầu tiên của các số nguyên.

Nếu bạn thấy khái niệm "danh sách không bao giờ kết thúc" đáng sợ, đừng lo. Chỉ có 25 phần tử đầu tiên của những danh sách đó mới thực sự được tạo ra. Đó là vì không phần tử nào của một danh sách không bao giờ kết thúc được đánh giá cho đến khi nó được truy cập.

Nếu tất cả điều trên khiến bạn bối rối, bạn có thể mong chờ một thời gian tuyệt vời khi tìm hiểu về Clojure và lập trình hàm. Mục tiêu của tôi ở đây không phải dạy bạn về các chủ đề này.

Thay vào đó, mục tiêu của tôi là chỉ ra một điểm khác biệt rất đáng chú ý giữa chương trình Clojure và chương trình Java. Chương trình Java sử dụng một biến có thể thay đổi (mutable variable), tức là một biến thay đổi trạng thái trong khi chương trình thực thi. Biến đó là `i`, biến điều khiển vòng lặp. Không có biến có thể thay đổi nào tồn tại trong chương trình Clojure. Trong chương trình Clojure, các biến như `x` được khởi tạo, nhưng chúng không bao giờ bị sửa đổi.

Điều này dẫn chúng ta đến một phát biểu khiến người ta kinh ngạc: **Các biến trong ngôn ngữ hàm không thay đổi.**

## Bất biến và kiến trúc (IMMUTABILITY AND ARCHITECTURE)

Tại sao điểm này lại quan trọng như một cân nhắc kiến trúc? Tại sao một kiến trúc sư lại quan tâm đến tính có thể thay đổi của biến? Câu trả lời đơn giản đến mức bất ngờ: **Tất cả các điều kiện đua (race conditions), các tình trạng bế tắc (deadlock conditions), và các vấn đề cập nhật đồng thời (concurrent update problems) đều do các biến có thể thay đổi gây ra.** Bạn không thể có điều kiện đua hay vấn đề cập nhật đồng thời nếu không biến nào từng bị cập nhật. Bạn không thể có bế tắc nếu không có khóa có thể thay đổi (mutable locks).

Nói cách khác, tất cả những vấn đề mà chúng ta đối mặt trong các ứng dụng đồng thời, tất cả những vấn đề trong các ứng dụng yêu cầu nhiều luồng (thread) và nhiều bộ xử lý, đều không thể xảy ra nếu không có biến có thể thay đổi.

Là một kiến trúc sư, bạn nên rất quan tâm đến các vấn đề đồng thời. Bạn muốn đảm bảo rằng các hệ thống bạn thiết kế sẽ vững chắc khi có nhiều luồng và bộ xử lý. Câu hỏi bạn phải tự hỏi là liệu bất biến có thực tế không.

Câu trả lời cho câu hỏi đó là khẳng định, **nếu bạn có bộ nhớ vô hạn và tốc độ bộ xử lý vô hạn**. Nếu thiếu những tài nguyên vô hạn đó, câu trả lời phức tạp hơn một chút. Có, bất biến có thể thực tế được, **nếu chấp nhận một số sự thỏa hiệp**.

Hãy xem xét một vài sự thỏa hiệp đó.

## Tách biệt trạng thái có thể thay đổi (SEGREGATION OF MUTABILITY)

Một trong những sự thỏa hiệp phổ biến nhất liên quan đến bất biến là phân tách ứng dụng, hoặc các dịch vụ trong ứng dụng, thành các thành phần có thể thay đổi và bất biến. Các thành phần bất biến thực hiện nhiệm vụ của chúng theo cách hàm thuần túy, không sử dụng bất kỳ biến có thể thay đổi nào. Các thành phần bất biến giao tiếp với một hoặc nhiều thành phần khác không thuần túy theo hàm, và cho phép trạng thái của các biến bị thay đổi (Hình 6.1).

**Hình 6.1** Trạng thái biến đổi và bộ nhớ giao dịch

Vì thay đổi trạng thái làm cho các thành phần đó hứng chịu tất cả các vấn đề của đồng thời, thực hành phổ biến là sử dụng một loại bộ nhớ giao dịch (transactional memory) để bảo vệ các biến có thể thay đổi khỏi các cập nhật đồng thời và điều kiện đua.

Bộ nhớ giao dịch đơn giản chỉ xử lý các biến trong bộ nhớ theo cách tương tự như cơ sở dữ liệu xử lý các bản ghi trên đĩa.[^1] Nó bảo vệ những biến đó bằng một sơ đồ dựa trên giao dịch hoặc thử lại (retry).

Một ví dụ đơn giản về cách tiếp cận này là cơ chế `atom` của Clojure:

```clojure
(def counter (atom 0)) ; khởi tạo counter = 0
(swap! counter inc) ; tăng counter an toàn
```

Trong mã này, biến `counter` được định nghĩa là một `atom`. Trong Clojure, `atom` là một loại biến đặc biệt mà giá trị của nó được phép thay đổi dưới những điều kiện rất kỷ luật, được hàm `swap!` thực thi.

Hàm `swap!`, như trong đoạn mã trước, nhận hai đối số: `atom` sẽ bị thay đổi, và một hàm tính giá trị mới để lưu vào `atom`. Trong ví dụ của chúng ta, `atom` counter sẽ được thay đổi thành giá trị do hàm `inc` tính toán, hàm này đơn giản chỉ tăng đối số của nó.

Chiến lược mà `swap!` sử dụng là thuật toán so sánh và hoán đổi (compare and swap) truyền thống. Giá trị của `counter` được đọc và truyền cho `inc`. Khi `inc` trả về, giá trị của `counter` bị khóa và so sánh với giá trị đã truyền cho `inc`. Nếu giá trị giống nhau, giá trị do `inc` trả về được lưu vào `counter` và khóa được giải phóng. Ngược lại, khóa được giải phóng và chiến lược được thử lại từ đầu.

Cơ chế `atom` đủ cho các ứng dụng đơn giản. Thật không may, nó không thể bảo vệ hoàn toàn khỏi các cập nhật đồng thời và bế tắc khi nhiều biến phụ thuộc lẫn nhau xuất hiện. Trong những trường hợp đó, các cơ chế phức tạp hơn có thể được sử dụng.

Điểm mấu chốt là các ứng dụng được cấu trúc tốt sẽ được phân tách thành những thành phần không thay đổi biến và những thành phần làm vậy. Loại phân tách này được hỗ trợ bằng việc sử dụng các kỷ luật phù hợp để bảo vệ những biến bị thay đổi.

Kiến trúc sư sẽ khôn ngoan nếu đẩy càng nhiều xử lý càng tốt vào các thành phần bất biến, và gạt càng nhiều mã càng tốt ra khỏi những thành phần phải cho phép thay đổi.

## Nguồn sự kiện (EVENT SOURCING)

Giới hạn về bộ nhớ và sức mạnh xử lý đang nhanh chóng không còn là rào cản. Ngày nay, các bộ xử lý thực thi hàng tỷ lệnh mỗi giây và có hàng tỷ byte RAM là điều phổ biến. Càng nhiều bộ nhớ, máy móc càng nhanh, chúng ta càng ít cần trạng thái có thể thay đổi.

Lấy một ví dụ đơn giản, hãy tưởng tượng một ứng dụng ngân hàng duy trì số dư tài khoản của khách hàng. Nó thay đổi những số dư đó khi các giao dịch nạp và rút được thực thi.

Bây giờ hãy tưởng tượng thay vì lưu trữ số dư tài khoản, chúng ta chỉ lưu trữ các giao dịch. Bất cứ khi nào ai đó muốn biết số dư của một tài khoản, chúng ta đơn giản chỉ cộng tổng tất cả các giao dịch của tài khoản đó, từ đầu thời gian. Sách lược này không đòi hỏi bất kỳ biến có thể thay đổi nào.

Rõ ràng, cách tiếp cận này nghe có vẻ vô lý. Theo thời gian, số lượng giao dịch sẽ tăng không giới hạn, và sức mạnh xử lý cần thiết để tính tổng sẽ trở nên không thể chấp nhận được. Để làm cho sách lược này hoạt động mãi mãi, chúng ta sẽ cần bộ nhớ vô hạn và sức mạnh xử lý vô hạn.

Nhưng có lẽ chúng ta không cần sách lược này hoạt động mãi mãi. Và có lẽ chúng ta có đủ bộ nhớ và đủ sức mạnh xử lý để sách lược này hoạt động trong vòng đời hợp lý của ứng dụng.

Đây chính là ý tưởng đằng sau **nguồn sự kiện (event sourcing)**.[^2] Nguồn sự kiện là một chiến lược trong đó chúng ta lưu trữ các giao dịch, chứ không lưu trạng thái. Khi trạng thái được yêu cầu, chúng ta đơn giản áp dụng tất cả các giao dịch từ đầu thời gian.

Tất nhiên, chúng ta có thể lấy đường tắt. Ví dụ, chúng ta có thể tính toán và lưu trạng thái mỗi nửa đêm. Khi đó, khi thông tin trạng thái được yêu cầu, chúng ta chỉ cần tính toán các giao dịch kể từ nửa đêm.

Xét về bộ nhớ dữ liệu cần thiết cho sách lược này: chúng ta sẽ cần rất nhiều. Thực tế, bộ nhớ ngoại tuyến đã tăng trưởng nhanh đến mức chúng ta hiện coi hàng nghìn tỷ byte là nhỏ, nên chúng ta có rất nhiều.

Quan trọng hơn, **không bao giờ có thứ gì bị xóa hoặc cập nhật** từ kho dữ liệu như vậy. Hệ quả là, ứng dụng của chúng ta không phải là CRUD (Create, Read, Update, Delete); chúng chỉ là CR (Create, Read). Ngoài ra, vì không có cập nhật hay xóa xảy ra trong kho dữ liệu, không thể có bất kỳ vấn đề cập nhật đồng thời nào.

Nếu chúng ta có đủ bộ nhớ và đủ sức mạnh bộ xử lý, chúng ta có thể làm cho ứng dụng của mình hoàn toàn bất biến, và do đó, thuần túy theo kiểu hàm.

Nếu điều này vẫn nghe có vẻ vô lý, có thể sẽ giúp ích nếu bạn nhớ rằng **đúng chính cách hoạt động của hệ thống kiểm soát mã nguồn (source code control system) của bạn.**

## Kết luận (CONCLUSION)

Tóm lại:

- Lập trình có cấu trúc là kỷ luật được áp đặt lên việc chuyển giao quyền điều khiển trực tiếp.
- Lập trình hướng đối tượng là kỷ luật được áp đặt lên việc chuyển giao quyền điều khiển gián tiếp.
- Lập trình hàm là kỷ luật được áp đặt lên việc gán biến.

Mỗi mô hình lập trình trong số ba này đều đã lấy đi một thứ gì đó từ chúng ta. Mỗi cái đều hạn chế một khía cạnh nào đó của cách chúng ta viết mã. Không cái nào trong số chúng bổ sung quyền năng hay khả năng cho chúng ta.

Điều chúng ta học được trong nửa thế kỷ qua là **điều không nên làm**.

Với sự nhận thức đó, chúng ta phải đối mặt với một thực tế khó chịu: **Phần mềm không phải là một công nghệ tiến bộ nhanh chóng.** Quy tắc của phần mềm ngày nay y hệt như năm 1946, khi Alan Turing viết nên đoạn mã đầu tiên được thực thi trên một máy tính điện tử. Công cụ đã thay đổi, phần cứng đã thay đổi, nhưng bản chất của phần mềm vẫn giữ nguyên.

Phần mềm, nguyên liệu của các chương trình máy tính, bao gồm trình tự (sequence), lựa chọn (selection), lặp (iteration), và gián tiếp (indirection). Không hơn. Không kém.

[^1]: Tôi biết… đĩa là gì cơ?
[^2]: Cảm ơn Greg Young đã dạy tôi khái niệm này.