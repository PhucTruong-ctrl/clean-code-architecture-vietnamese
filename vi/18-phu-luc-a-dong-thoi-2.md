# Phụ lục A: Xử lý đồng thời II

> Tác giả: Brett L. Schuchert

Phụ lục này bổ sung và mở rộng chương Xử lý đồng thời ở trang 177. Nội dung được chia thành các chủ đề độc lập, nhìn chung bạn có thể đọc theo thứ tự bất kỳ. Một số phần có nội dung trùng lặp để phù hợp với cách đọc đó.

## Ví dụ client/server

Hãy hình dung một ứng dụng client/server đơn giản. Server chờ kết nối của client trên một socket. Client kết nối rồi gửi yêu cầu.

### Server

Đây là phiên bản rút gọn của một ứng dụng server. Toàn bộ mã nguồn của ví dụ này có từ trang 343, mục Client/server không dùng luồng.

```java
ServerSocket serverSocket = new ServerSocket(8009);
while (keepProcessing) {
    try {
        Socket socket = serverSocket.accept();
        process(socket);
    } catch (Exception e) {
        handle(e);
    }
}
```

Ứng dụng đơn giản này chờ kết nối, xử lý thông điệp đến rồi tiếp tục chờ yêu cầu tiếp theo từ client. Đây là mã phía client kết nối với server:

```java
private void connectSendReceive(int i) {
    try {
        Socket socket = new Socket("localhost", PORT);
        MessageUtils.sendMessage(socket, Integer.toString(i));
        MessageUtils.getMessage(socket);
        socket.close();
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

Cặp client/server này hoạt động tốt đến đâu? Làm thế nào mô tả chính xác hiệu năng của nó? Đây là một kiểm thử khẳng định hiệu năng ở mức “chấp nhận được”:

```java
@Test(timeout = 10000)
public void shouldRunInUnder10Seconds() throws Exception {
    Thread[] threads = createThreads();
    startAllThreadsw(threads);
    waitForAllThreadsToFinish(threads);
}
```
Phần thiết lập được lược đi để ví dụ đơn giản hơn (xem “ClientTest.java” ở trang 344). Kiểm thử này khẳng định chương trình phải hoàn tất trong vòng 10.000 mili giây.

Đây là ví dụ kinh điển về kiểm tra thông lượng của một hệ thống. Hệ thống phải xử lý xong một loạt yêu cầu client trong mười giây. Chỉ cần server xử lý kịp từng yêu cầu riêng lẻ thì kiểm thử sẽ đạt.

Nếu kiểm thử thất bại thì sao? Nếu không xây dựng một vòng lặp thăm dò sự kiện, trong một luồng đơn lẻ ta không thể làm gì nhiều để tăng tốc đoạn mã này. Dùng nhiều luồng có giải quyết được vấn đề không? Có thể, nhưng trước hết ta cần biết thời gian đang tiêu tốn vào đâu. Có hai khả năng:

- I/O: dùng socket, kết nối cơ sở dữ liệu, chờ bộ nhớ ảo hoán đổi, v.v.
- Bộ xử lý: tính toán số học, xử lý biểu thức chính quy, thu gom rác, v.v.

Hệ thống thường có cả hai loại công việc, nhưng với mỗi thao tác thường sẽ có một loại chiếm ưu thế. Nếu mã bị giới hạn bởi bộ xử lý, bổ sung phần cứng xử lý có thể tăng thông lượng và giúp kiểm thử đạt. Nhưng số chu kỳ CPU luôn có giới hạn, nên thêm luồng vào một vấn đề bị giới hạn bởi bộ xử lý sẽ không làm nó nhanh hơn.

Ngược lại, nếu tiến trình bị giới hạn bởi I/O thì xử lý đồng thời có thể tăng hiệu quả. Khi một phần của hệ thống chờ I/O, phần khác có thể tận dụng thời gian chờ đó để xử lý việc khác, nhờ vậy sử dụng CPU hiệu quả hơn.

### Thêm luồng

Tạm giả sử kiểm thử hiệu năng thất bại. Ta có thể tăng thông lượng để kiểm thử đạt bằng cách nào? Nếu phương thức `process` của server bị giới hạn bởi I/O, có thể cho server dùng luồng như sau (chỉ cần thay đổi `processMessage`):

```java
void process(final Socket socket) {
    if (socket == null)
        return;
    Runnable clientHandler = new Runnable() {
        public void run() {
            try {
                String message = MessageUtils.getMessage(socket);
                MessageUtils.sendMessage(socket, "Processed: " + message);
                closeIgnoringException(socket);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    };

    Thread clientConnection = new Thread(clientHandler);
    clientConnection.start();
}
```
Giả sử thay đổi này giúp kiểm thử đạt.¹ Mã đã hoàn chỉnh, đúng chưa?

### Nhận xét về server

Server đã cập nhật hoàn tất kiểm thử chỉ trong hơn một giây. Tiếc là giải pháp này hơi ngây thơ và nảy sinh một số vấn đề mới.

Server có thể tạo bao nhiêu luồng? Mã không đặt giới hạn, nên ta có thể chạm đến giới hạn của Máy ảo Java (JVM). Với nhiều hệ thống đơn giản, như vậy có thể đủ dùng. Nhưng nếu hệ thống phải hỗ trợ nhiều người dùng trên mạng công cộng thì sao? Quá nhiều người kết nối cùng lúc có thể khiến hệ thống đình trệ.

Tạm gác vấn đề hành vi đó sang một bên. Giải pháp trên còn có vấn đề về độ sạch và cấu trúc. Mã server đang đảm nhận bao nhiêu trách nhiệm?

- Quản lý kết nối socket
- Xử lý client
- Chính sách về luồng
- Chính sách tắt server

Đáng tiếc là tất cả trách nhiệm này đều nằm trong hàm `process`. Ngoài ra, đoạn mã còn đan xen nhiều cấp độ trừu tượng. Vì vậy, dù hàm `process` nhỏ, ta vẫn cần chia lại nó.

¹ Bạn có thể tự kiểm chứng bằng cách chạy thử mã trước và sau khi thay đổi. Xem mã không dùng luồng bắt đầu ở trang 343, và mã có dùng luồng bắt đầu ở trang 346.

Server có nhiều lý do để thay đổi, vì thế nó vi phạm Nguyên tắc Trách nhiệm Đơn lẻ. Để giữ cho hệ thống đồng thời sạch sẽ, việc quản lý luồng nên được gom vào một vài nơi có kiểm soát chặt chẽ. Hơn nữa, mọi mã quản lý luồng chỉ nên làm đúng việc quản lý luồng. Vì sao? Chỉ riêng việc lần tìm lỗi xử lý đồng thời đã đủ khó, không cần phải đồng thời tháo gỡ những vấn đề không liên quan khác.

Nếu tạo một lớp riêng cho từng trách nhiệm liệt kê ở trên, kể cả trách nhiệm quản lý luồng, thì khi thay đổi chiến lược quản lý luồng, phạm vi mã bị ảnh hưởng sẽ nhỏ hơn và không làm nhiễm bẩn các trách nhiệm khác. Cách này cũng giúp kiểm thử những trách nhiệm còn lại dễ hơn nhiều mà không phải bận tâm đến luồng. Đây là phiên bản cập nhật thực hiện điều đó:

```java
public void run() {
    while (keepProcessing) {
        try {
            ClientConnection clientConnection = connectionManager.awaitClient();
            ClientRequestProcessor requestProcessor
                = new ClientRequestProcessor(clientConnection);
            clientScheduler.schedule(requestProcessor);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    connectionManager.shutdown();
}
```

Giờ đây, mọi việc liên quan đến luồng đều tập trung ở một nơi: `clientScheduler`. Nếu có vấn đề về xử lý đồng thời, ta chỉ cần tìm ở một chỗ:

```java
public interface ClientScheduler {
    void schedule(ClientRequestProcessor requestProcessor);
}
```
Chính sách hiện tại rất dễ triển khai:

```java
public class ThreadPerRequestScheduler implements ClientScheduler {
    public void schedule(final ClientRequestProcessor requestProcessor) {
        Runnable runnable = new Runnable() {
            public void run() {
                requestProcessor.process();
            }
        };

        Thread thread = new Thread(runnable);
        thread.start();
    }
}
```

Khi đã tách toàn bộ việc quản lý luồng vào một nơi, việc thay đổi cách kiểm soát luồng trở nên dễ dàng hơn nhiều. Chẳng hạn, chuyển sang framework Executor của Java 5 chỉ cần viết một lớp mới rồi gắn nó vào (Đoạn mã A-1).

**Đoạn mã A-1**
**ExecutorClientScheduler.java**

```java
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

public class ExecutorClientScheduler implements ClientScheduler {
    Executor executor;

    public ExecutorClientScheduler(int availableThreads) {
        executor = Executors.newFixedThreadPool(availableThreads);
    }
    public void schedule(final ClientRequestProcessor requestProcessor) {
        Runnable runnable = new Runnable() {
            public void run() {
                requestProcessor.process();
            }
        };
        executor.execute(runnable);
    }
}
```

### Kết luận

Đưa xử lý đồng thời vào ví dụ cụ thể này cho thấy một cách tăng thông lượng hệ thống và một cách kiểm tra thông lượng đó bằng framework kiểm thử. Gom toàn bộ mã xử lý đồng thời vào một số ít lớp là một ví dụ áp dụng Nguyên tắc Trách nhiệm Đơn lẻ. Điều này đặc biệt quan trọng trong lập trình đồng thời vì độ phức tạp của nó.

## Các đường thực thi khả dĩ

Xem phương thức `incrementValue`, một phương thức Java chỉ có một dòng, không có vòng lặp hay rẽ nhánh:

```java
public class IdGenerator {
    int lastIdUsed;

    public int incrementValue() {
        return ++lastIdUsed;
    }
}
```

Bỏ qua tràn số nguyên và giả sử chỉ có một luồng truy cập một thực thể `IdGenerator`. Khi đó chỉ có một đường thực thi và một kết quả được đảm bảo:

- Giá trị trả về bằng với giá trị của `lastIdUsed`; cả hai đều lớn hơn một đơn vị so với ngay trước khi gọi phương thức.

Nếu dùng hai luồng mà không đổi phương thức thì sao? Mỗi luồng gọi `incrementValue` một lần, những kết quả nào có thể xảy ra? Có bao nhiêu đường thực thi khả dĩ? Trước hết là các kết quả (giả sử ban đầu `lastIdUsed` có giá trị 93):

- Luồng 1 nhận giá trị 94, luồng 2 nhận giá trị 95, và `lastIdUsed` lúc này là 95.
- Luồng 1 nhận giá trị 95, luồng 2 nhận giá trị 94, và `lastIdUsed` lúc này là 95.
- Luồng 1 nhận giá trị 94, luồng 2 cũng nhận giá trị 94, và `lastIdUsed` lúc này là 94.

Kết quả cuối cùng tuy bất ngờ nhưng hoàn toàn có thể xảy ra. Để hiểu vì sao có những kết quả khác nhau, ta cần biết số lượng đường thực thi khả dĩ và cách Máy ảo Java thực thi chúng.

### Số lượng đường thực thi

Để tính số đường thực thi khả dĩ, ta bắt đầu từ mã bytecode được tạo ra. Một dòng Java (`return ++lastIdUsed;`) trở thành tám chỉ thị bytecode. Hai luồng có thể đan xen việc thực thi tám chỉ thị này như người chia bài đan các lá bài khi xáo một bộ bài.² Ngay cả khi mỗi tay chỉ có tám lá, số kết quả xáo trộn vẫn rất lớn.

Với trường hợp đơn giản gồm N chỉ thị theo một chuỗi, không có vòng lặp hay điều kiện, và T luồng, tổng số đường thực thi khả dĩ bằng:

$$\frac{(N T)!}{(N!)^T}$$

#### Tính số thứ tự khả dĩ

Phần giải thích này trích từ email của Uncle Bob gửi Brett:

> Với N bước và T luồng, tổng cộng có T * N bước. Trước mỗi bước, một lần chuyển ngữ cảnh sẽ chọn một trong T luồng. Vì thế, mỗi đường đi có thể biểu diễn bằng một chuỗi chữ số cho biết các lần chuyển ngữ cảnh. Với các bước A và B cùng hai luồng 1 và 2, sáu đường đi khả dĩ là 1122, 1212, 1221, 2112, 2121 và 2211. Nếu biểu diễn theo bước thì lần lượt là A1B1A2B2, A1A2B1B2, A1A2B2B1, A2A1B1B2, A2A1B2B1 và A2B2A1B1. Với ba luồng, chuỗi có thể là 112233, 112323, 113223, 113232, 112233, 121233, 121323, 121332, 123132, 123123, . . . .
>
> Một đặc điểm của các chuỗi này là luôn phải có N lần xuất hiện của mỗi T. Vì vậy chuỗi 111111 không hợp lệ, vì nó có sáu số 1 và không có số 2 hay 3 nào.

² Đây là một sự đơn giản hóa. Tuy nhiên, để phục vụ phần thảo luận này, ta có thể dùng mô hình đơn giản hóa đó.

#### Tính số thứ tự khả dĩ (tiếp theo)

Ta cần tìm các hoán vị của N số 1, N số 2, . . . và N số T. Thực chất đây là các hoán vị của N * T phần tử lấy đủ N * T phần tử, tức (N * T)!, nhưng phải loại bỏ mọi phần tử trùng lặp. Do đó, ta cần đếm số trường hợp trùng rồi chia (N * T)! cho số đó.

Với hai bước và hai luồng, có bao nhiêu trường hợp trùng? Mỗi chuỗi bốn chữ số có hai số 1 và hai số 2. Có thể đổi chỗ từng cặp mà không làm thay đổi ý nghĩa chuỗi. Ta có thể đổi chỗ các số 1, các số 2, cả hai cặp hoặc không đổi cặp nào. Vì thế mỗi chuỗi có bốn dạng tương đương, tức ba dạng trùng. Ba trong bốn lựa chọn là trùng; nói cách khác, một phần tư số hoán vị KHÔNG trùng. 4! * .25 = 6. Có vẻ cách tính này đúng.

Có bao nhiêu trường hợp trùng? Khi N = 2 và T = 2, ta có thể đổi chỗ các số 1, các số 2 hoặc cả hai. Khi N = 2 và T = 3, ta có thể đổi chỗ các số 1, các số 2, các số 3, các số 1 và 2, các số 1 và 3, hoặc các số 2 và 3. Việc đổi chỗ chính là các hoán vị của N. Giả sử có P hoán vị của N. Số cách khác nhau để sắp xếp các hoán vị đó là P**T.

Vậy số dạng tương đương là N!**T. Số đường đi là (T*N)!/(N!**T). Với trường hợp T = 2, N = 2, ta lại được 6 (24/4).

Với N = 2 và T = 3, ta có 720/8 = 90.

Với N = 3 và T = 3, ta có 9!/6^3 = 1680.

Trong trường hợp đơn giản của một dòng mã Java, tương đương tám dòng bytecode, và hai luồng, tổng số đường thực thi khả dĩ là 12.870. Nếu kiểu của `lastIdUsed` là `long`, mỗi lần đọc/ghi trở thành hai thao tác thay vì một, và số thứ tự khả dĩ tăng thành 2.704.156.

Điều gì xảy ra nếu ta thay đổi phương thức này một chút?

```java
public synchronized void incrementValue() {
    ++lastIdUsed;
}
```

Với hai luồng, số đường thực thi khả dĩ giảm còn hai; trong trường hợp tổng quát, con số đó là N!.

### Tìm hiểu sâu hơn

Còn kết quả đáng ngạc nhiên rằng hai luồng có thể gọi phương thức một lần (trước khi thêm `synchronized`) và nhận cùng một kết quả số thì sao? Điều đó có thể xảy ra như thế nào? Trước hết, hãy bắt đầu từ cơ bản.

Thao tác nguyên tử là gì? Có thể định nghĩa thao tác nguyên tử là thao tác không thể bị ngắt quãng. Chẳng hạn, trong đoạn mã sau, dòng 5 gán 0 cho `lastId` là thao tác nguyên tử vì theo mô hình bộ nhớ Java, phép gán giá trị 32 bit không thể bị ngắt quãng.

```java
01: public class Example {
02:    int lastId;
03:
04:    public void resetId() {
05:        value = 0;
06:    }
07:
08:    public int getNextId() {
09:        ++value;
10:    }
11:}
```

Nếu đổi kiểu của `lastId` từ `int` sang `long` thì sao? Dòng 5 còn là thao tác nguyên tử không? Theo đặc tả JVM thì không. Trên một bộ xử lý cụ thể, thao tác đó có thể nguyên tử, nhưng đặc tả JVM quy định phép gán mọi giá trị 64 bit cần hai phép gán 32 bit. Điều này có nghĩa là giữa lần gán 32 bit thứ nhất và thứ hai, một luồng khác có thể chen vào và thay đổi một trong các giá trị.

Còn toán tử tăng trước `++` ở dòng 9 thì sao? Toán tử tăng trước có thể bị ngắt quãng nên không nguyên tử. Để hiểu điều này, hãy xem chi tiết bytecode của cả hai phương thức.

Trước khi tiếp tục, đây là ba định nghĩa quan trọng:

- Khung (frame): Mỗi lần gọi phương thức cần một khung. Khung chứa địa chỉ trả về, các tham số được truyền vào phương thức và các biến cục bộ được định nghĩa trong phương thức. Đây là kỹ thuật tiêu chuẩn để mô tả ngăn xếp lời gọi, được các ngôn ngữ hiện đại dùng cho việc gọi hàm/phương thức cơ bản và gọi đệ quy.
- Biến cục bộ: Mọi biến được định nghĩa trong phạm vi của phương thức. Tất cả phương thức không tĩnh đều có ít nhất một biến là `this`, đại diện cho đối tượng hiện tại, tức đối tượng nhận thông điệp gần nhất (trong luồng hiện tại) khiến phương thức được gọi.
- Ngăn xếp toán hạng: Nhiều chỉ thị trong Máy ảo Java nhận tham số. Các tham số đó được đặt trên ngăn xếp toán hạng. Ngăn xếp là cấu trúc dữ liệu vào sau ra trước (LIFO) tiêu chuẩn.

Đây là bytecode được tạo ra cho `resetId()`:

| Mã lệnh | Mô tả | Ngăn xếp toán hạng sau lệnh |
|---|---|---|
| ALOAD 0 | Nạp biến thứ 0 lên ngăn xếp toán hạng. Biến thứ 0 là `this`, đối tượng hiện tại. Khi phương thức được gọi, đối tượng nhận thông điệp, một thực thể của `Example`, được đưa vào mảng biến cục bộ của khung tạo ra cho lần gọi phương thức. Đây luôn là biến đầu tiên được đưa vào mọi phương thức thực thể. | this |
| ICONST_0 | Đưa giá trị hằng 0 lên ngăn xếp toán hạng. | this, 0 |
| PUTFIELD lastId | Lưu giá trị trên cùng của ngăn xếp (0) vào trường `value` của đối tượng được tham chiếu bởi tham chiếu đối tượng nằm ngay dưới cùng, tức `this`. | <empty> |

Ba chỉ thị này được đảm bảo là nguyên tử vì dù luồng đang thực thi có thể bị ngắt sau bất kỳ chỉ thị nào, một luồng khác không thể chạm tới thông tin của chỉ thị `PUTFIELD` (giá trị hằng 0 trên đỉnh ngăn xếp, tham chiếu `this` ngay bên dưới, cùng giá trị trường). Vì vậy, khi phép gán diễn ra, ta được đảm bảo giá trị 0 sẽ được lưu vào trường. Thao tác này là nguyên tử. Các toán hạng đều xử lý thông tin cục bộ của phương thức nên nhiều luồng không can thiệp lẫn nhau.

Nếu mười luồng thực thi ba chỉ thị này thì có 4.38679733629e+24 thứ tự khả dĩ. Tuy nhiên, chỉ có một kết quả có thể xảy ra, nên các thứ tự khác nhau không quan trọng. Trong trường hợp này, kết quả tương tự cũng được đảm bảo với `long`. Vì sao? Cả mười luồng đều gán một giá trị hằng. Dù chúng đan xen với nhau, kết quả cuối cùng vẫn như nhau.

Với phép toán `++` trong phương thức `getNextId`, vấn đề sẽ nảy sinh. Giả sử lúc bắt đầu phương thức, `lastId` có giá trị 42. Đây là bytecode của phương thức mới:

| Mã lệnh | Mô tả | Ngăn xếp toán hạng sau lệnh |
|---|---|---|
| ALOAD 0 | Đưa `this` lên ngăn xếp toán hạng. | this |
| DUP | Sao chép phần tử trên cùng của ngăn xếp. Lúc này trên ngăn xếp có hai bản sao của `this`. | this, this |
| GETFIELD lastId | Lấy giá trị trường `lastId` từ đối tượng được phần tử trên cùng (`this`) trỏ tới rồi đưa giá trị đó trở lại ngăn xếp. | this, 42 |
| ICONST_1 | Đưa hằng số nguyên 1 lên ngăn xếp. | this, 42, 1 |
| IADD | Cộng hai giá trị trên cùng của ngăn xếp toán hạng rồi đưa kết quả trở lại ngăn xếp. | this, 43 |
| DUP_X1 | Sao chép giá trị 43 và đặt nó trước `this`. | 43, this, 43 |
| PUTFIELD value | Lưu giá trị 43 trên cùng của ngăn xếp vào trường `value` của đối tượng hiện tại, được đại diện bởi giá trị kế trên ngăn xếp là `this`. | 43 |
| IRETURN | Trả về phần tử duy nhất trên cùng của ngăn xếp. | <empty> |

Hãy hình dung luồng thứ nhất thực hiện xong ba chỉ thị đầu, đến hết `GETFIELD`, rồi bị ngắt. Luồng thứ hai tiếp quản và thực hiện toàn bộ phương thức, tăng `lastId` thêm một đơn vị; nó nhận về 43. Sau đó luồng thứ nhất tiếp tục từ chỗ dừng. Trên ngăn xếp toán hạng vẫn là 42, vì đó là giá trị của `lastId` khi nó thực thi `GETFIELD`. Luồng này cộng thêm một thành 43 rồi lưu kết quả. Luồng thứ nhất cũng nhận về 43. Một lần tăng bị mất vì luồng thứ nhất ghi đè kết quả của luồng thứ hai sau khi luồng thứ hai đã chen ngang và hoàn tất.

Đặt phương thức `getNexId()` thành `synchronized` sẽ khắc phục vấn đề này.

### Kết luận

Không cần hiểu sâu bytecode mới biết các luồng có thể giẫm lên việc của nhau như thế nào. Nếu hiểu được ví dụ này, bạn sẽ thấy các luồng có thể can thiệp lẫn nhau, và chỉ cần biết đến khả năng đó là đủ.

Dù vậy, ví dụ đơn giản này cho thấy ta cần hiểu mô hình bộ nhớ đủ để biết điều gì an toàn, điều gì không. Nhiều người lầm tưởng toán tử `++` (tăng trước hoặc tăng sau) là nguyên tử, nhưng rõ ràng không phải vậy. Vì thế, bạn cần biết:

- Những đối tượng/giá trị nào được chia sẻ
- Đoạn mã nào có thể gây ra vấn đề đọc/cập nhật đồng thời
- Cách ngăn những vấn đề đồng thời đó xảy ra

## Hiểu thư viện của bạn

### Framework Executor

Như đã minh họa trong `ExecutorClientScheduler.java` ở trang 321, framework Executor được giới thiệu trong Java 5 cho phép thực thi linh hoạt bằng nhóm luồng. Đây là một lớp trong gói `java.util.concurrent`.

Nếu bạn đang tạo luồng mà không dùng nhóm luồng, hoặc tự viết một nhóm luồng, hãy cân nhắc dùng Executor. Mã sẽ sạch hơn, dễ theo dõi hơn và ngắn hơn.

Framework Executor gom luồng vào nhóm, tự động điều chỉnh kích thước và tạo lại luồng khi cần. Nó cũng hỗ trợ future, một cấu trúc lập trình đồng thời phổ biến. Framework Executor hoạt động với các lớp cài đặt `Runnable` và cả những lớp cài đặt giao diện `Callable`. `Callable` trông giống `Runnable`, nhưng có thể trả về kết quả, một nhu cầu thường gặp trong các giải pháp đa luồng.

Future rất hữu ích khi mã cần thực hiện nhiều thao tác độc lập rồi chờ tất cả hoàn tất:

```java
public String processRequest(String message) throws Exception {
    Callable<String> makeExternalCall = new Callable<String>() {
        public String call() throws Exception {
            String result = "";
            // thực hiện yêu cầu bên ngoài
            return result;
        }
    };

    Future<String> result = executorService.submit(makeExternalCall);
    String partialResult = doSomeLocalProcessing();
    return result.get() + partialResult;
}
```

Trong ví dụ này, phương thức bắt đầu thực thi đối tượng `makeExternalCall` rồi tiếp tục xử lý việc khác. Dòng cuối gọi `result.get()`, lệnh này chặn cho đến khi future hoàn tất.

### Giải pháp không chặn

Máy ảo Java 5 tận dụng thiết kế bộ xử lý hiện đại, hỗ trợ cập nhật không chặn đáng tin cậy. Chẳng hạn, hãy xét một lớp dùng đồng bộ hóa (và do đó có chặn) để cập nhật giá trị an toàn với luồng:

```java
public class ObjectWithValue {
    private int value;
    public void synchronized incrementValue() { ++value; }
    public int getValue() { return value; }
}
```
Java 5 có một loạt lớp mới cho những tình huống như vậy, chẳng hạn `AtomicBoolean`, `AtomicInteger` và `AtomicReference`, cùng nhiều lớp khác. Ta có thể viết lại đoạn mã trên theo cách không chặn như sau:

```java
public class ObjectWithValue {
    private AtomicInteger value = new AtomicInteger(0);

    public void incrementValue() {
        value.incrementAndGet();
    }
    public int getValue() {
        return value.get();
    }
}
```

Dù phiên bản này dùng một đối tượng thay vì kiểu nguyên thủy và gọi phương thức như `incrementAndGet()` thay cho `++`, hiệu năng của lớp hầu như luôn tốt hơn phiên bản trước. Trong một số trường hợp nó chỉ nhanh hơn đôi chút, còn trường hợp chậm hơn gần như không có.

Điều này có thể xảy ra thế nào? Bộ xử lý hiện đại thường có một thao tác gọi là Compare and Swap (CAS). Thao tác này tương tự khóa lạc quan trong cơ sở dữ liệu, còn phiên bản `synchronized` tương tự khóa bi quan.

Từ khóa `synchronized` luôn lấy khóa, kể cả khi không có luồng thứ hai nào định cập nhật cùng giá trị. Dù hiệu năng của khóa nội tại đã được cải thiện qua từng phiên bản, chúng vẫn tốn kém.

Phiên bản không chặn giả định rằng nhiều luồng thường không sửa cùng một giá trị đủ thường xuyên để gây ra vấn đề. Thay vào đó, nó phát hiện hiệu quả xem tình huống đó có xảy ra hay không và thử lại cho đến khi cập nhật thành công. Chi phí phát hiện này hầu như luôn thấp hơn chi phí lấy khóa, kể cả khi mức tranh chấp từ vừa đến cao.

Máy ảo thực hiện việc này như thế nào? Thao tác CAS là nguyên tử. Xét về logic, CAS có thể hình dung như sau:

```java
int variableBeingSet;

void simulateNonBlockingSet(int newValue) {
    int currentValue;
    do {
        currentValue = variableBeingSet
    } while(currentValue != compareAndSwap(currentValue, newValue));
}
int synchronized compareAndSwap(int currentValue, int newValue) {
    if(variableBeingSet == currentValue) {
        variableBeingSet = newValue;
        return currentValue;
    }
    return variableBeingSet;
}
```

Khi một phương thức định cập nhật biến được chia sẻ, thao tác CAS xác minh biến sắp được gán vẫn có giá trị đã biết gần nhất hay không. Nếu đúng, biến sẽ được thay đổi. Nếu không, biến không được gán vì một luồng khác đã chen vào. Phương thức đang thử cập nhật bằng CAS nhận ra thay đổi chưa diễn ra và thử lại.

### Các lớp không an toàn với luồng

Có một số lớp vốn không an toàn với luồng. Sau đây là vài ví dụ:

- `SimpleDateFormat`
- Kết nối cơ sở dữ liệu
- Các lớp chứa trong `java.util`
- Servlet

Lưu ý rằng một số lớp collection có những phương thức riêng lẻ an toàn với luồng. Tuy nhiên, thao tác gọi nhiều hơn một phương thức thì không. Ví dụ, nếu không muốn thay thế một phần tử trong `HashTable` khi phần tử đó đã có sẵn, ta có thể viết:

```java
if(!hashTable.containsKey(someKey)) {
    hashTable.put(someKey, new SomeValue());
}
```
Mỗi phương thức riêng lẻ đều an toàn với luồng. Tuy nhiên, một luồng khác có thể thêm giá trị vào giữa lần gọi `containsKey` và `put`. Có một số cách khắc phục:

- Khóa `HashTable` trước và đảm bảo mọi nơi dùng nó đều làm như vậy, tức khóa phía client:

```java
synchronized(map) {
    if(!map.conainsKey(key))
        map.put(key,value);
}
```
- Bọc `HashTable` trong đối tượng riêng và dùng API khác, tức khóa phía server bằng một ADAPTER:

```java
public class WrappedHashtable<K, V> {
    private Map<K, V> map = new Hashtable<K, V>();

    public synchronized void putIfAbsent(K key, V value) {
        if (map.containsKey(key))
            map.put(key, value);
    }
}
```
- Dùng các collection an toàn với luồng:

```java
ConcurrentHashMap<Integer, String> map = new ConcurrentHashMap<Integer,
String>();
map.putIfAbsent(key, value);
```

Các collection trong `java.util.concurrent` có những thao tác như `putIfAbsent()` để hỗ trợ loại thao tác này.

## Phụ thuộc giữa các phương thức có thể làm hỏng mã đồng thời

Đây là ví dụ đơn giản về cách tạo ra sự phụ thuộc giữa các phương thức:

```java
public class IntegerIterator implements Iterator<Integer>
    private Integer nextValue = 0;

    public synchronized boolean hasNext() {
        return nextValue < 100000;
    }
    public synchronized Integer next() {
        if (nextValue == 100000)
            throw new IteratorPastEndException();
        return nextValue++;
    }
    public synchronized Integer getNextValue() {
        return nextValue;
    }
}
```
Đây là đoạn mã dùng `IntegerIterator`:

```java
IntegerIterator iterator = new IntegerIterator();
while(iterator.hasNext()) {
    int nextValue = iterator.next();
    // xử lý nextValue
}
```

Nếu chỉ có một luồng thực thi đoạn mã này thì không có vấn đề. Nhưng điều gì xảy ra nếu hai luồng cùng dùng một thực thể `IngeterIterator`, mỗi luồng xử lý các giá trị mình nhận được và mỗi phần tử trong danh sách chỉ được xử lý một lần? Hầu hết thời gian, chẳng có gì xấu xảy ra; hai luồng vui vẻ chia sẻ danh sách, xử lý các phần tử iterator đưa ra rồi dừng khi iterator chạy hết. Tuy nhiên, có một xác suất nhỏ là ở cuối vòng lặp, hai luồng can thiệp lẫn nhau, khiến một luồng vượt quá cuối iterator và ném ngoại lệ.

Vấn đề nằm ở đây: Luồng 1 gọi `hasNext()`, nhận về `true`. Luồng 1 bị tạm dừng, rồi Luồng 2 cũng gọi câu hỏi đó và vẫn nhận về `true`. Luồng 2 gọi `next()`, nhận được một giá trị như dự kiến, nhưng đồng thời làm cho `hasNext()` trả về `false`. Luồng 1 chạy tiếp, vẫn nghĩ `hasNext()` là `true`, rồi gọi `next()`. Dù từng phương thức riêng lẻ đều được đồng bộ hóa, phía client lại gọi hai phương thức.

Đây là vấn đề có thật, cũng là kiểu vấn đề thường xuất hiện trong mã đồng thời. Trong tình huống này, nó đặc biệt tinh vi vì chỉ gây lỗi khi xảy ra ở vòng lặp cuối cùng. Nếu các luồng ngắt quãng đúng vào lúc đó, một luồng có thể vượt quá cuối iterator. Đây là kiểu lỗi chỉ xuất hiện rất lâu sau khi hệ thống đã đưa vào vận hành, và rất khó lần ra.

Bạn có ba lựa chọn:

- Chấp nhận lỗi.
- Thay đổi client để giải quyết vấn đề: khóa phía client.
- Thay đổi server, đồng thời cũng thay đổi client để giải quyết vấn đề: khóa phía server.

### Chấp nhận lỗi

Đôi khi có thể sắp đặt mọi thứ sao cho lỗi xảy ra mà không gây hại. Chẳng hạn, client ở trên có thể bắt ngoại lệ rồi dọn dẹp. Thành thật mà nói, cách này hơi cẩu thả, chẳng khác nào xử lý rò rỉ bộ nhớ bằng cách khởi động lại máy vào lúc nửa đêm.

### Khóa phía máy khách

Để `IntegerIterator` hoạt động đúng với nhiều luồng, hãy sửa máy khách này (và mọi máy khách khác) như sau:

```java
IntegerIterator iterator = new IntegerIterator();

while (true) {
    int nextValue;

    synchronized (iterator) {
        if (!iterator.hasNext())
            break;
        nextValue = iterator.next();
    }
    doSometingWith(nextValue);
}
```

Mỗi máy khách tự khóa bằng từ khóa `synchronized`. Việc lặp lại này vi phạm nguyên tắc DRY, nhưng có thể cần thiết nếu mã sử dụng các công cụ bên thứ ba không an toàn với luồng.

Cách này rủi ro vì mọi lập trình viên dùng máy chủ đều phải nhớ khóa nó trước khi sử dụng và mở khóa khi xong. Nhiều, rất nhiều năm trước, tôi từng làm việc trên một hệ thống dùng kiểu khóa phía máy khách cho một tài nguyên dùng chung. Tài nguyên đó được sử dụng ở hàng trăm chỗ khác nhau trong mã. Một lập trình viên đáng thương đã quên khóa tài nguyên ở một trong những chỗ ấy.

Hệ thống là một máy tính chia sẻ thời gian, nhiều thiết bị đầu cuối, chạy phần mềm kế toán cho Local 705 thuộc công đoàn tài xế xe tải. Máy tính đặt trong phòng có sàn nâng, điều hòa nhiệt độ, cách trụ sở Local 705 khoảng 50 dặm về phía bắc. Tại trụ sở, hàng chục nhân viên nhập liệu gõ các khoản đóng công đoàn vào thiết bị đầu cuối. Các thiết bị kết nối với máy tính qua đường dây điện thoại riêng và modem bán song công 600 bps. (Chuyện này đã lâu lắm rồi.)

Khoảng mỗi ngày một lần, một thiết bị đầu cuối lại “đứng máy”. Chẳng có quy luật gì cả. Tình trạng này không ưu tiên thiết bị nào hay thời điểm nào. Cứ như có ai đó gieo xúc xắc để chọn thời điểm và thiết bị sẽ đứng máy. Đôi khi nhiều thiết bị cùng đứng. Có khi vài ngày liền chẳng có chiếc nào bị.

Ban đầu, giải pháp duy nhất là khởi động lại. Nhưng việc khởi động lại rất khó phối hợp. Chúng tôi phải gọi cho trụ sở, yêu cầu mọi người dừng công việc đang làm trên tất cả thiết bị đầu cuối. Sau đó mới có thể tắt rồi khởi động lại máy. Nếu ai đó đang làm việc quan trọng cần một, hai giờ, thiết bị bị treo đành phải nằm đó.

Sau vài tuần gỡ lỗi, chúng tôi phát hiện nguyên nhân là bộ đếm của một bộ đệm vòng bị lệch so với con trỏ. Bộ đệm này điều khiển đầu ra tới thiết bị đầu cuối. Giá trị con trỏ cho biết bộ đệm trống, nhưng bộ đếm lại nói nó đã đầy. Vì trống nên chẳng có gì để hiển thị, còn vì cũng đang đầy nên không thể thêm gì vào bộ đệm để hiện lên màn hình.

Vậy là chúng tôi biết vì sao các thiết bị bị treo, nhưng chưa biết vì sao bộ đệm vòng lại lệch trạng thái. Chúng tôi bèn thêm một đoạn vá để né vấn đề. Máy tính có thể đọc được các công tắc trên bảng điều khiển phía trước. (Chuyện này còn lâu hơn nữa.) Chúng tôi viết một hàm bẫy nhỏ, phát hiện khi một công tắc bị gạt rồi tìm bộ đệm vòng nào vừa trống vừa đầy. Nếu tìm thấy, hàm đặt lại bộ đệm về trạng thái trống. Thế là các thiết bị đầu cuối bị treo lại hiển thị được.

Giờ thì chúng tôi không cần khởi động lại hệ thống khi thiết bị đầu cuối bị treo. Người của Local chỉ cần gọi báo, rồi chúng tôi đi vào phòng máy tính và gạt một công tắc.

Dĩ nhiên đôi khi họ làm việc vào cuối tuần, còn chúng tôi thì không. Vì vậy, chúng tôi bổ sung một hàm vào bộ lập lịch để kiểm tra tất cả bộ đệm vòng mỗi phút và đặt lại mọi bộ đệm vừa trống vừa đầy. Màn hình được khơi thông trước cả khi Local kịp gọi điện.

Chúng tôi mất thêm vài tuần dò từng trang mã hợp ngữ nguyên khối mới tìm ra thủ phạm. Chúng tôi tính toán và nhận thấy tần suất bị treo phù hợp với việc có một lần dùng bộ đệm vòng mà không khóa. Chỉ cần tìm ra chỗ dùng sai đó. Tiếc là chuyện xảy ra từ quá lâu rồi, chúng tôi không có công cụ tìm kiếm, tham chiếu chéo hay bất kỳ trợ giúp tự động nào khác. Chúng tôi chỉ còn cách dò từng danh sách mã.

Tôi đã học được một bài học quan trọng trong mùa đông lạnh giá ở Chicago năm 1971. Khóa phía máy khách thật tệ.

### Khóa phía máy chủ

Có thể bỏ phần mã lặp bằng cách thay đổi `IntegerIterator` như sau:

```java
public class IntegerIteratorServerLocked {
    private Integer nextValue = 0;
    public synchronized Integer getNextOrNull() {
        if (nextValue < 100000)
            return nextValue++;
        else
            return null;
    }
}
```

Mã máy khách cũng thay đổi:

```java
while (true) {
    Integer nextValue = iterator.getNextOrNull();
    if (next == null)
        break;
    // làm gì đó với nextValue
}
```

Trong trường hợp này, chúng ta thực sự thay đổi API của lớp để hỗ trợ xử lý đồng thời.³ Máy khách cần kiểm tra `null` thay vì gọi `hasNext()`.

Nói chung, nên ưu tiên khóa phía máy chủ vì những lý do sau:

- Giảm mã lặp: khóa phía máy khách buộc mỗi máy khách phải khóa máy chủ đúng cách. Khi đưa mã khóa vào máy chủ, máy khách có thể dùng đối tượng mà không phải viết thêm mã khóa.
- Cho hiệu năng tốt hơn: khi triển khai đơn luồng, bạn có thể thay máy chủ an toàn với luồng bằng máy chủ không an toàn với luồng để tránh mọi chi phí phụ trội.
- Giảm khả năng xảy ra lỗi: chỉ cần một lập trình viên quên khóa đúng cách là đủ.
- Áp dụng một chính sách duy nhất: chính sách nằm ở một nơi, trong máy chủ, thay vì rải rác ở nhiều nơi, trong từng máy khách.
- Thu hẹp phạm vi biến dùng chung: máy khách không biết đến chúng hay cách khóa chúng. Tất cả đều được giấu trong máy chủ. Khi có sự cố, số chỗ cần kiểm tra cũng ít hơn.

Nếu bạn không sở hữu mã máy chủ thì sao?

- Dùng một ADAPTER để đổi API và thêm khóa:

```java
public class ThreadSafeIntegerIterator {
    private IntegerIterator iterator = new IntegerIterator();

    public synchronized Integer getNextOrNull() {
        if(iterator.hasNext())
            return iterator.next();
        return null;
    }
}
```

- Hoặc tốt hơn, dùng các collection an toàn với luồng có giao diện mở rộng.

³ Thực ra, giao diện `Iterator` vốn không an toàn với luồng. Nó chưa bao giờ được thiết kế để nhiều luồng cùng sử dụng, nên điều này chẳng có gì đáng ngạc nhiên.

## Tăng thông lượng

Giả sử chúng ta muốn truy cập mạng và đọc nội dung một nhóm trang từ một danh sách URL. Mỗi khi đọc xong một trang, ta sẽ phân tích trang đó để tích lũy một số thống kê. Sau khi đọc hết các trang, ta sẽ in báo cáo tổng hợp.

Lớp sau trả về nội dung của một trang khi nhận URL:

```java
public class PageReader {
    //...
    public String getPageFor(String url) {
        HttpMethod method = new GetMethod(url);
        try {
            httpClient.executeMethod(method);
            String response = method.getResponseBodyAsString();
            return response;
        } catch (Exception e) {
            handle(e);
        } finally {
            method.releaseConnection();
        }
    }
}
```

Lớp tiếp theo là bộ lặp cung cấp nội dung các trang dựa trên một bộ lặp URL:

```java
public class PageIterator {
    private PageReader reader;
    private URLIterator urls;

    public PageIterator(PageReader reader, URLIterator urls) {
        this.urls = urls;
        this.reader = reader;
    }

    public synchronized String getNextPageOrNull() {
        if (urls.hasNext())
            getPageFor(urls.next());
        else
            return null;
    }

    public String getPageFor(String url) {
        return reader.getPageFor(url);
    }
}
```

Có thể chia sẻ một thể hiện của `PageIterator` giữa nhiều luồng khác nhau, mỗi luồng dùng thể hiện `PageReader` riêng để đọc và phân tích các trang nhận được từ bộ lặp.

Hãy để ý khối `synchronized` rất nhỏ. Nó chỉ chứa đoạn then chốt bên trong `PageIterator`. Luôn nên đồng bộ hóa ít nhất có thể thay vì nhiều nhất có thể.

### Tính thông lượng khi tính toán bằng một luồng

Giờ ta thử tính toán đơn giản. Để tiện lập luận, giả sử:

- Thời gian I/O để lấy một trang (trung bình): 1 giây
- Thời gian xử lý để phân tích trang (trung bình): 0,5 giây
- I/O cần 0% CPU, còn xử lý cần 100% CPU.

Với N trang được xử lý bởi một luồng, tổng thời gian thực thi là 1,5 giây * N. Hình A-1 cho thấy ảnh chụp 13 trang, tương đương khoảng 19,5 giây.

**Hình A-1**

Một luồng

### Tính thông lượng khi dùng nhiều luồng

Nếu có thể lấy các trang theo thứ tự bất kỳ và xử lý độc lập, ta có thể dùng nhiều luồng để tăng thông lượng. Điều gì xảy ra nếu dùng ba luồng? Trong cùng khoảng thời gian, ta lấy được bao nhiêu trang?

Như Hình A-2 cho thấy, giải pháp đa luồng cho phép việc phân tích bị giới hạn bởi xử lý chồng lấp với việc đọc trang bị giới hạn bởi I/O. Trong một thế giới lý tưởng, bộ xử lý được tận dụng tối đa. Mỗi lần đọc trang kéo dài một giây được chồng lấp với hai lần phân tích. Như vậy, ta xử lý được hai trang mỗi giây, gấp ba lần thông lượng của giải pháp đơn luồng.

**Hình A-2**

Ba luồng chạy đồng thời

## Bế tắc

Hãy hình dung một ứng dụng Web có hai nhóm tài nguyên dùng chung, mỗi nhóm có số lượng hữu hạn:

- Nhóm kết nối cơ sở dữ liệu để lưu trữ cục bộ công việc đang xử lý
- Nhóm kết nối MQ tới kho lưu trữ chính

Giả sử ứng dụng có hai thao tác: tạo mới và cập nhật.

- Tạo mới: lấy kết nối tới kho lưu trữ chính và cơ sở dữ liệu. Giao tiếp với dịch vụ kho lưu trữ chính, sau đó lưu công việc vào cơ sở dữ liệu xử lý cục bộ.
- Cập nhật: lấy kết nối cơ sở dữ liệu rồi tới kho lưu trữ chính. Đọc từ cơ sở dữ liệu xử lý công việc rồi gửi tới kho lưu trữ chính.

Điều gì xảy ra khi số người dùng nhiều hơn số kết nối trong nhóm? Giả sử mỗi nhóm có mười kết nối.

- Mười người dùng thực hiện thao tác tạo mới, lấy hết mười kết nối cơ sở dữ liệu. Mỗi luồng bị ngắt sau khi lấy kết nối cơ sở dữ liệu nhưng trước khi lấy kết nối tới kho lưu trữ chính.
- Mười người dùng thực hiện thao tác cập nhật, lấy hết mười kết nối tới kho lưu trữ chính. Mỗi luồng bị ngắt sau khi lấy kết nối tới kho lưu trữ chính nhưng trước khi lấy kết nối cơ sở dữ liệu.
- Giờ mười luồng “tạo mới” phải chờ kết nối tới kho lưu trữ chính, còn mười luồng “cập nhật” phải chờ kết nối cơ sở dữ liệu.
- Bế tắc. Hệ thống không bao giờ tự phục hồi.

Tình huống này nghe có vẻ khó xảy ra, nhưng ai muốn một hệ thống cứ cách tuần lại đóng băng một lần? Ai muốn gỡ lỗi một hệ thống có triệu chứng khó tái hiện đến thế? Đây là kiểu vấn đề xuất hiện trong thực tế rồi mất hàng tuần mới giải quyết được.

Một “giải pháp” thường thấy là thêm các câu lệnh gỡ lỗi để tìm hiểu chuyện gì đang xảy ra. Dĩ nhiên, các câu lệnh gỡ lỗi làm thay đổi mã đủ nhiều để bế tắc xảy ra trong tình huống khác và phải mất hàng tháng mới tái diễn.⁴

Muốn thực sự giải quyết bế tắc, ta cần hiểu nguyên nhân gây ra nó. Bế tắc cần đủ bốn điều kiện sau:

- Loại trừ tương hỗ
- Khóa và chờ
- Không thể thu hồi
- Chờ vòng tròn

### Loại trừ tương hỗ

Loại trừ tương hỗ xảy ra khi nhiều luồng cần dùng cùng một tài nguyên, nhưng tài nguyên đó:

- Không thể được nhiều luồng sử dụng cùng lúc.
- Có số lượng giới hạn.

Ví dụ thường gặp về loại tài nguyên này là kết nối cơ sở dữ liệu, tệp đang mở để ghi, khóa bản ghi hoặc semaphore.

### Khóa và chờ

Sau khi lấy được một tài nguyên, luồng sẽ không giải phóng nó cho đến khi đã lấy được mọi tài nguyên khác cần dùng và hoàn thành công việc.

### Không thể thu hồi

Một luồng không thể lấy tài nguyên khỏi luồng khác. Khi một luồng đang giữ tài nguyên, cách duy nhất để luồng khác lấy được nó là chờ luồng đang giữ giải phóng.

### Chờ vòng tròn

Hiện tượng này còn được gọi là vòng ôm chết người. Hãy hình dung hai luồng T1 và T2 cùng hai tài nguyên R1 và R2. T1 giữ R1, T2 giữ R2. T1 cũng cần R2, còn T2 cũng cần R1. Tình huống sẽ giống Hình A-3:

**Hình A-3**

Cả bốn điều kiện này phải đồng thời tồn tại thì mới có thể xảy ra bế tắc. Phá vỡ bất kỳ điều kiện nào cũng khiến bế tắc không thể xảy ra.

### Phá vỡ điều kiện loại trừ tương hỗ

Một cách tránh bế tắc là né điều kiện loại trừ tương hỗ. Bạn có thể làm vậy bằng cách:

- Dùng tài nguyên cho phép nhiều bên sử dụng đồng thời, chẳng hạn `AtomicInteger`.
- Tăng số lượng tài nguyên để bằng hoặc vượt số luồng tranh dùng.
- Kiểm tra tất cả tài nguyên đều rảnh trước khi chiếm lấy bất kỳ tài nguyên nào.

Tiếc là hầu hết tài nguyên đều có số lượng giới hạn và không cho phép dùng đồng thời. Cũng không hiếm trường hợp danh tính của tài nguyên thứ hai phụ thuộc vào kết quả thao tác trên tài nguyên thứ nhất. Nhưng đừng nản, vẫn còn ba điều kiện nữa.

⁴ Chẳng hạn, có người thêm đầu ra gỡ lỗi rồi vấn đề “biến mất”. Mã gỡ lỗi đã “sửa” vấn đề, khiến nó vẫn còn trong hệ thống.

### Phá vỡ điều kiện khóa và chờ

Bạn cũng có thể loại bỏ bế tắc bằng cách không chờ. Hãy kiểm tra từng tài nguyên trước khi chiếm lấy nó; nếu gặp tài nguyên đang bận, giải phóng mọi tài nguyên rồi bắt đầu lại.

Cách này có thể dẫn đến một số vấn đề:

- Đói tài nguyên: một luồng liên tục không lấy được tài nguyên cần thiết (có thể do nó cần một tổ hợp tài nguyên riêng hiếm khi cùng rảnh).
- Livelock: nhiều luồng có thể rơi vào cùng nhịp, mỗi luồng lấy một tài nguyên rồi lại nhả ra, lặp đi lặp lại. Điều này đặc biệt dễ xảy ra với các thuật toán lập lịch CPU đơn giản (hãy nghĩ đến thiết bị nhúng hoặc thuật toán cân bằng luồng tự viết đơn giản).

Cả hai vấn đề đều có thể làm thông lượng kém. Vấn đề thứ nhất khiến CPU ít được sử dụng, còn vấn đề thứ hai khiến CPU hoạt động nhiều nhưng vô ích.

Cách này kém hiệu quả thật, nhưng vẫn hơn không có gì. Ưu điểm là hầu như lúc nào cũng có thể triển khai nếu mọi cách khác đều thất bại.

### Phá vỡ điều kiện không thể thu hồi

Một cách khác để tránh bế tắc là cho phép các luồng lấy tài nguyên khỏi luồng khác. Việc này thường thực hiện qua một cơ chế yêu cầu đơn giản. Khi phát hiện tài nguyên đang bận, một luồng yêu cầu chủ sở hữu giải phóng nó. Nếu chủ sở hữu cũng đang chờ tài nguyên khác, nó giải phóng tất cả rồi bắt đầu lại.

Cách này tương tự cách trước nhưng có ưu điểm là luồng vẫn được phép chờ tài nguyên. Nhờ đó, số lần phải bắt đầu lại giảm xuống. Tuy nhiên, hãy lưu ý rằng quản lý tất cả các yêu cầu ấy có thể rất phức tạp.

### Phá vỡ điều kiện chờ vòng tròn

Đây là cách phổ biến nhất để ngăn bế tắc. Với hầu hết hệ thống, chỉ cần mọi bên thống nhất một quy ước đơn giản.

Trong ví dụ trên, Luồng 1 cần cả Tài nguyên 1 và Tài nguyên 2, còn Luồng 2 cần Tài nguyên 2 rồi Tài nguyên 1. Chỉ cần buộc cả hai luồng cấp phát tài nguyên theo cùng thứ tự là không thể xảy ra chờ vòng tròn.

Tổng quát hơn, nếu mọi luồng thống nhất được thứ tự toàn cục của các tài nguyên và đều cấp phát theo thứ tự ấy thì bế tắc không thể xảy ra. Cũng như các chiến lược khác, cách này có thể gây ra vấn đề:

- Thứ tự lấy tài nguyên có thể không khớp với thứ tự sử dụng, nên tài nguyên lấy từ đầu có thể đến cuối mới được dùng. Khi ấy tài nguyên có thể bị khóa lâu hơn mức cần thiết.
- Đôi khi không thể áp đặt thứ tự lấy tài nguyên. Nếu mã định danh của tài nguyên thứ hai được xác định bởi thao tác thực hiện trên tài nguyên thứ nhất thì không thể sắp thứ tự.

Có nhiều cách tránh bế tắc. Một số dẫn đến đói tài nguyên, số khác dùng CPU nhiều và làm giảm khả năng phản hồi. TANSTAAFL!⁵

Tách riêng phần liên quan đến luồng trong giải pháp để có thể điều chỉnh và thử nghiệm là cách hữu hiệu giúp hiểu rõ hơn, từ đó xác định chiến lược phù hợp nhất.

## Kiểm thử mã đa luồng

Làm thế nào viết một kiểm thử để chứng minh đoạn mã sau bị lỗi?

**Đoạn mã A-2**

```java
01: public class ClassWithThreadingProblem {
02:    int nextId;
03:
04:    public int takeNextId() {
05:        return nextId++;
06:    }
07:}
```

Sau đây là mô tả một kiểm thử sẽ chứng minh mã bị lỗi:

- Ghi nhớ giá trị hiện tại của `nextId`.
- Tạo hai luồng, cả hai đều gọi `takeNextId()` một lần.
- Xác minh `nextId` lớn hơn giá trị ban đầu hai đơn vị.
- Chạy cho đến khi chứng minh được `nextId` chỉ tăng một thay vì hai.

Đoạn mã A-2 cho thấy một kiểm thử như vậy:

**Đoạn mã A-2**
**ClassWithThreadingProblemTest.java**

```java
01: package example;
02:
03: import static org.junit.Assert.fail;
04:
05: import org.junit.Test;
06:
07: public class ClassWithThreadingProblemTest {
08:     @Test
09:     public void twoThreadsShouldFailEventually() throws Exception {
10:         final ClassWithThreadingProblem classWithThreadingProblem
                      = new ClassWithThreadingProblem();
11:
12:         Runnable runnable = new Runnable() {
13:             public void run() {
14:                 classWithThreadingProblem.takeNextId();
15:             }
16:         };
17:
18:         for (int i = 0; i < 50000; ++i) {
19:             int startingId = classWithThreadingProblem.lastId;
20:             int expectedResult = 2 + startingId;
21:
22:             Thread t1 = new Thread(runnable);
23:             Thread t2 = new Thread(runnable);
24:             t1.start();
25:             t2.start();
26:             t1.join();
27:             t2.join();
28:
29:             int endingId = classWithThreadingProblem.lastId;
30:
31:             if (endingId != expectedResult)
32:                 return;
33:         }
34:
35:         fail("Should have exposed a threading issue but it did not.");
36:     }
37: }
```

| Dòng | Mô tả |
|---|---|
| 10 | Tạo một thể hiện duy nhất của `ClassWithThreadingProblem`. Lưu ý, ta phải dùng từ khóa `final` vì sẽ sử dụng nó bên dưới trong một lớp bên trong vô danh. |
| 12–16 | Tạo một lớp bên trong vô danh sử dụng thể hiện duy nhất của `ClassWithThreadingProblem`. |
| 18 | Chạy đoạn mã “đủ nhiều” lần để chứng minh mã thất bại, nhưng không nhiều đến mức kiểm thử “chạy quá lâu”. Đây là một phép cân bằng; ta không muốn chờ quá lâu mới thấy lỗi. Chọn con số này rất khó, dù sau này ta sẽ thấy có thể giảm đáng kể con số đó. |
| 19 | Ghi nhớ giá trị ban đầu. Kiểm thử này nhằm chứng minh mã trong `ClassWithThreadingProblem` bị lỗi. Nếu kiểm thử vượt qua, nó đã chứng minh mã bị lỗi. Nếu kiểm thử thất bại, nó chưa chứng minh được mã bị lỗi. |
| 20 | Ta kỳ vọng giá trị cuối cùng lớn hơn giá trị hiện tại hai đơn vị. |
| 22–23 | Tạo hai luồng, cả hai đều dùng đối tượng ta tạo ở các dòng 12–16. Như vậy, hai luồng có thể cùng cố dùng một thể hiện `ClassWithThreadingProblem` và gây nhiễu lẫn nhau. |
| 24–25 | Cho phép hai luồng có thể chạy. |
| 26–27 | Chờ cả hai luồng chạy xong rồi mới kiểm tra kết quả. |
| 29 | Ghi lại giá trị cuối cùng thực tế. |
| 31–32 | `endingId` có khác giá trị ta mong đợi không? Nếu có, kết thúc kiểm thử, ta đã chứng minh mã bị lỗi. Nếu không, thử lại. |
| 35 | Nếu chạy đến đây, kiểm thử chưa chứng minh được mã sản phẩm bị lỗi trong khoảng thời gian “hợp lý”; kiểm thử đã thất bại. Hoặc mã không lỗi, hoặc ta chưa chạy đủ số vòng lặp để điều kiện lỗi xảy ra. |

Kiểm thử này chắc chắn tạo ra các điều kiện để xảy ra vấn đề cập nhật đồng thời. Tuy nhiên, vấn đề hiếm khi xảy ra nên phần lớn lần chạy, kiểm thử sẽ không phát hiện được.

Thật vậy, để phát hiện vấn đề, ta cần đặt số vòng lặp vượt quá một triệu. Ngay cả vậy, trong mười lần chạy với một triệu vòng lặp, vấn đề chỉ xuất hiện một lần. Điều đó có nghĩa là có lẽ ta phải đặt số vòng lặp cao hơn nhiều so với một trăm triệu để có thể tin cậy phát hiện lỗi. Ta sẵn sàng chờ bao lâu?

Ngay cả khi điều chỉnh kiểm thử để phát hiện lỗi ổn định trên một máy, có lẽ ta sẽ phải điều chỉnh lại với các giá trị khác để chứng minh lỗi trên máy, hệ điều hành hoặc phiên bản JVM khác.

Đây là một vấn đề đơn giản. Nếu không dễ chứng minh mã lỗi với vấn đề này, làm sao ta phát hiện được những vấn đề thực sự phức tạp?

Vậy có thể dùng cách nào để chứng minh lỗi đơn giản này? Quan trọng hơn, làm thế nào viết kiểm thử chứng minh được lỗi trong mã phức tạp hơn? Làm sao phát hiện lỗi trong mã khi không biết phải tìm ở đâu?

Sau đây là vài ý tưởng:

- Kiểm thử Monte Carlo. Viết kiểm thử linh hoạt để có thể điều chỉnh. Sau đó chạy đi chạy lại, chẳng hạn trên máy chủ kiểm thử, đồng thời thay đổi ngẫu nhiên các giá trị điều chỉnh. Nếu kiểm thử thất bại lần nào thì mã có lỗi. Hãy bắt đầu viết những kiểm thử này sớm để máy chủ tích hợp liên tục sớm bắt đầu chạy chúng. Nhân tiện, hãy ghi nhật ký cẩn thận các điều kiện khiến kiểm thử thất bại.
- Chạy kiểm thử trên từng nền tảng triển khai mục tiêu. Lặp đi lặp lại. Liên tục. Kiểm thử chạy càng lâu mà không thất bại thì càng có khả năng:
  - Mã sản phẩm đúng, hoặc
  - Kiểm thử chưa đủ để phát hiện vấn đề.
- Chạy kiểm thử trên máy có tải thay đổi. Nếu có thể mô phỏng tải gần với môi trường sản xuất thì hãy làm.

Tuy vậy, ngay cả khi làm tất cả những việc này, khả năng phát hiện vấn đề luồng trong mã vẫn không cao. Những vấn đề khó chịu nhất là loại có xác suất cực thấp, chỉ xảy ra một lần trong một tỷ cơ hội. Chúng là nỗi kinh hoàng của các hệ thống phức tạp.

## Công cụ hỗ trợ kiểm thử mã dựa trên luồng

IBM đã tạo ra một công cụ tên là ConTest.⁶ Công cụ này bổ sung mã đo đạc vào các lớp để tăng khả năng mã không an toàn với luồng bộc lộ lỗi.

Chúng tôi không có quan hệ trực tiếp nào với IBM hay nhóm phát triển ConTest. Một đồng nghiệp đã giới thiệu công cụ này. Chúng tôi nhận thấy khả năng tìm ra vấn đề luồng cải thiện rõ rệt chỉ sau vài phút sử dụng.

Sau đây là các bước sử dụng ConTest:

- Viết kiểm thử và mã sản phẩm, bảo đảm có những kiểm thử được thiết kế riêng để mô phỏng nhiều người dùng dưới tải thay đổi, như đã nói ở trên.
- Bổ sung mã đo đạc cho mã kiểm thử và mã sản phẩm bằng ConTest.
- Chạy kiểm thử.

Khi bổ sung mã đo đạc bằng ConTest, tỷ lệ phát hiện lỗi của chúng tôi tăng từ khoảng một lần trong mười triệu vòng lặp lên khoảng một lần trong ba mươi vòng lặp. Sau đây là số vòng lặp của vài lần chạy kiểm thử sau khi bổ sung mã đo đạc: 13, 23, 0, 54, 16, 14, 6, 69, 107, 49, 2. Rõ ràng, các lớp đã được bổ sung mã đo đạc thất bại sớm hơn nhiều và đáng tin cậy hơn hẳn.

## Kết luận

Chương này chỉ là một chuyến đi rất ngắn qua vùng đất rộng lớn và hiểm trở của lập trình đồng thời. Chúng tôi mới chỉ chạm đến bề mặt. Ở đây, chúng tôi tập trung vào các nguyên tắc giúp giữ mã xử lý đồng thời sạch sẽ, nhưng nếu định viết các hệ thống xử lý đồng thời thì bạn còn nhiều điều phải học. Chúng tôi khuyên bạn bắt đầu với cuốn sách tuyệt vời của Doug Lea, *Concurrent Programming in Java: Design Principles and Patterns*.⁷

Trong chương này, chúng tôi nói về cập nhật đồng thời, cùng các nguyên tắc đồng bộ hóa và khóa sạch giúp ngăn chặn vấn đề đó. Chúng tôi nói về cách luồng có thể tăng thông lượng của hệ thống bị giới hạn bởi I/O, đồng thời trình bày những kỹ thuật sạch để đạt được cải thiện ấy. Chúng tôi nói về bế tắc và các nguyên tắc ngăn chặn nó một cách sạch sẽ. Cuối cùng, chúng tôi nói về các chiến lược phát hiện vấn đề đồng thời bằng cách bổ sung mã đo đạc vào mã của bạn.

⁵ Không có bữa trưa nào miễn phí.

⁶ http://www.haifa.ibm.com/projects/veriﬁcation/contest/index.html
⁷ Xem [Lea99], trang 191.

## Hướng dẫn: Ví dụ mã đầy đủ

### Máy khách/máy chủ không dùng luồng

**Đoạn mã A-3**
**Server.java**

```java
package com.objectmentor.clientserver.nonthreaded;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;

import common.MessageUtils;
public class Server implements Runnable {
    ServerSocket serverSocket;
    volatile boolean keepProcessing = true;

    public Server(int port, int millisecondsTimeout) throws IOException {
        serverSocket = new ServerSocket(port);
        serverSocket.setSoTimeout(millisecondsTimeout);
    }

    public void run() {
        System.out.printf("Server Starting\n");
        while (keepProcessing) {
            try {
                System.out.printf("accepting client\n");
                Socket socket = serverSocket.accept();
                System.out.printf("got client\n");
                process(socket);
            } catch (Exception e) {
                handle(e);
            }
        }
    }
    private void handle(Exception e) {
        if (!(e instanceof SocketException)) {
            e.printStackTrace();
        }
    }

    public void stopProcessing() {
        keepProcessing = false;
        closeIgnoringException(serverSocket);
    }
```

**Đoạn mã A-3 (tiếp theo)**
**Server.java**

```java
    void process(Socket socket) {
        if (socket == null)
            return;

        try {
            System.out.printf("Server: getting message\n");
            String message = MessageUtils.getMessage(socket);
            System.out.printf("Server: got message: %s\n", message);
            Thread.sleep(1000);
            System.out.printf("Server: sending reply: %s\n", message);
            MessageUtils.sendMessage(socket, "Processed: " + message);
            System.out.printf("Server: sent\n");
            closeIgnoringException(socket);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    private void closeIgnoringException(Socket socket) {
        if (socket != null)
            try {
                socket.close();
            } catch (IOException ignore) {
            }
    }

    private void closeIgnoringException(ServerSocket serverSocket) {
        if (serverSocket != null)
            try {
                serverSocket.close();
            } catch (IOException ignore) {
            }
    }
}
```

**Đoạn mã A-4**
**ClientTest.java**

```java
package com.objectmentor.clientserver.nonthreaded;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;

import common.MessageUtils;

public class Server implements Runnable {
    ServerSocket serverSocket;
    volatile boolean keepProcessing = true;
```

**Đoạn mã A-4 (tiếp theo)**
**ClientTest.java**

```java
    public Server(int port, int millisecondsTimeout) throws IOException {
        serverSocket = new ServerSocket(port);
        serverSocket.setSoTimeout(millisecondsTimeout);
    }

    public void run() {
        System.out.printf("Server Starting\n");

        while (keepProcessing) {
            try {
                System.out.printf("accepting client\n");
                Socket socket = serverSocket.accept();
                System.out.printf("got client\n");
                process(socket);
            } catch (Exception e) {
                handle(e);
            }
        }
    }

    private void handle(Exception e) {
        if (!(e instanceof SocketException)) {
            e.printStackTrace();
        }
    }

    public void stopProcessing() {
        keepProcessing = false;
        closeIgnoringException(serverSocket);
    }

    void process(Socket socket) {
        if (socket == null)
            return;

        try {
            System.out.printf("Server: getting message\n");
            String message = MessageUtils.getMessage(socket);
            System.out.printf("Server: got message: %s\n", message);
            Thread.sleep(1000);
            System.out.printf("Server: sending reply: %s\n", message);
            MessageUtils.sendMessage(socket, "Processed: " + message);
            System.out.printf("Server: sent\n");
            closeIgnoringException(socket);
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    private void closeIgnoringException(Socket socket) {
        if (socket != null)
            try {
                socket.close();
            } catch (IOException ignore) {
            }
    }
    private void closeIgnoringException(ServerSocket serverSocket) {
        if (serverSocket != null)
            try {
                serverSocket.close();
            } catch (IOException ignore) {
            }
    }
}
```

**Đoạn mã A-5**
**MessageUtils.java**

```java
package common;

import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.net.Socket;
public class MessageUtils {
    public static void sendMessage(Socket socket, String message)
            throws IOException {
        OutputStream stream = socket.getOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(stream);
        oos.writeUTF(message);
        oos.flush();
    }

    public static String getMessage(Socket socket) throws IOException {
        InputStream stream = socket.getInputStream();
        ObjectInputStream ois = new ObjectInputStream(stream);
        return ois.readUTF();
    }
}
```

### Máy khách/máy chủ dùng luồng

Chuyển server sang dùng luồng chỉ cần thay đổi phương thức xử lý thông điệp (các dòng mới được in đậm để dễ nhận ra):

```java
void process(final Socket socket) {
    if (socket == null)
        return;

    Runnable clientHandler = new Runnable() {
        public void run() {
            try {
                System.out.printf("Server: getting message\n");
                String message = MessageUtils.getMessage(socket);
                System.out.printf("Server: got message: %s\n", message);
                Thread.sleep(1000);
                System.out.printf("Server: sending reply: %s\n", message);
                MessageUtils.sendMessage(socket, "Processed: " + message);
                System.out.printf("Server: sent\n");
                closeIgnoringException(socket);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    };

    Thread clientConnection = new Thread(clientHandler);
    clientConnection.start();
}
```
