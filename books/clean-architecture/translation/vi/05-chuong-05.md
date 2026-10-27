# Chương 5: Lập trình hướng đối tượng

![Minh họa](assets/illustrations/05-chuong-05-opener.png){w=220}


Như chúng ta sẽ thấy, nền tảng của kiến trúc tốt là hiểu và áp dụng các nguyên lý thiết kế hướng đối tượng (OO). Nhưng chính xác thì OO là gì?

Một câu trả lời cho câu hỏi này là "Sự kết hợp của dữ liệu và hàm." Mặc dù thường được trích dẫn, đây là một câu trả lời rất không thỏa mãn vì nó ngụ ý rằng `o.f()` có gì đó khác biệt so với `f(o)`. Điều này vô lý. Các lập trình viên đã truyền cấu trúc dữ liệu vào hàm từ lâu trước năm 1966, khi Dahl và Nygaard chuyển khung ngăn xếp gọi hàm lên heap và phát minh ra OO.

Một câu trả lời phổ biến khác là "Một cách mô hình hóa thế giới thực." Nói vậy vẫn lẩn tránh vấn đề. "Mô hình hóa thế giới thực" thực sự có nghĩa là gì, và tại sao ta lại muốn làm vậy? Có lẽ ý câu đó là OO giúp phần mềm dễ hiểu hơn vì gần với thế giới thực. Nhưng cách giải thích ấy vẫn lẩn tránh vấn đề và quá mơ hồ. Nó không cho ta biết OO là gì.

Một số người dựa vào ba từ thần thánh để giải thích bản chất của OO: đóng gói (encapsulation), kế thừa (inheritance), và đa hình (polymorphism). Ngụ ý là OO là sự phối trộn thích đáng của ba thứ này, hoặc ít nhất một ngôn ngữ OO phải hỗ trợ ba thứ này.

Hãy kiểm tra từng khái niệm này lần lượt.

## Đóng gói (Encapsulation)?

Người ta xem đóng gói là một phần của định nghĩa OO vì các ngôn ngữ OO giúp đóng gói dữ liệu và hàm một cách dễ dàng, hiệu quả. Nhờ đó, có thể vạch ranh giới quanh một nhóm dữ liệu và hàm gắn kết với nhau. Bên ngoài ranh giới ấy, dữ liệu được ẩn đi và chỉ một số hàm được công khai. Ta thấy cách này được dùng với các thành viên dữ liệu `private` và hàm thành viên `public` của một lớp.

Ý tưởng này không hề riêng có ở OO. Thực tế, ngôn ngữ C đã có thể đóng gói hoàn toàn. Xét chương trình C đơn giản này:

point.h

```c
struct Point;
struct Point* makePoint(double x, double y);
double distance (struct Point *p1, struct Point *p2);
```

point.c

```c
#include "point.h"
#include <stdlib.h>
#include <math.h>

struct Point {
    double x,y;
};
struct Point* makepoint(double x, double y) {
    struct Point* p = malloc(sizeof(struct Point));
    p->x = x;
    p->y = y;
    return p;
}

double distance(struct Point* p1, struct Point* p2) {
    double dx = p1->x - p2->x;
    double dy = p1->y - p2->y;
    return sqrt(dx*dx+dy*dy);
}
```

Người dùng của `point.h` không có quyền truy cập nào vào các thành viên của `struct Point`. Chúng có thể gọi hàm `makePoint()` và hàm `distance()`, nhưng chúng hoàn toàn không biết gì về việc triển khai của cấu trúc dữ liệu `Point` hoặc các hàm.

Đây là sự đóng gói hoàn hảo trong một ngôn ngữ không hướng đối tượng. Các lập trình viên C vẫn thường làm như vậy: khai báo trước các cấu trúc dữ liệu và hàm trong tệp header, rồi triển khai chúng trong các tệp mã nguồn. Người dùng không hề truy cập được các thành phần nằm trong những tệp triển khai đó.

Nhưng rồi C++ ra đời cùng với OO, và sự đóng gói hoàn hảo của C bị phá vỡ.

Bộ biên dịch C++, vì những lý do kỹ thuật,[^1] cần các biến thành viên của một lớp phải được khai báo trong tệp header của lớp đó. Vì vậy chương trình Point của chúng ta thay đổi trông như sau:

point.h

```cpp
class Point {
public:
    Point(double x, double y);
    double distance(const Point& p) const;

private:
    double x;
    double y;
};
```

point.cc

```cpp
#include "point.h"
#include <math.h>

Point::Point(double x, double y)
: x(x), y(y)
{}

double Point::distance(const Point& p) const {
    double dx = x-p.x;
    double dy = y-p.y;
    return sqrt(dx*dx + dy*dy);
}
```

Khách hàng (client) của tệp header `point.h` biết về các biến thành viên `x` và `y`! Bộ biên dịch sẽ ngăn chặn việc truy cập vào chúng, nhưng client vẫn biết chúng tồn tại. Ví dụ, nếu tên của các biến thành viên đó thay đổi, tệp `point.cc` phải được biên dịch lại! Đóng gói đã bị phá vỡ.

Thật vậy, cách sửa chữa một phần cho sự đóng gói là đưa các từ khóa `public`, `private`, và `protected` vào ngôn ngữ. Tuy nhiên, đây là một thủ thuật (hack) cần thiết do nhu cầu kỹ thuật của bộ biên dịch phải thấy những biến đó trong tệp header.

Java và C# đơn giản là loại bỏ hoàn toàn sự tách biệt header/triển khai, làm suy yếu sự đóng gói thêm nữa. Trong các ngôn ngữ này, không thể tách biệt khai báo và định nghĩa của một lớp.

Vì những lý do này, rất khó chấp nhận rằng OO phụ thuộc vào sự đóng gói mạnh. Thực tế, nhiều ngôn ngữ OO[^2] có rất ít hoặc không có sự đóng gói được ép buộc.

OO dựa vào giả định rằng lập trình viên đủ kỷ luật để không tìm cách vượt qua cơ chế đóng gói dữ liệu. Dù vậy, các ngôn ngữ tự nhận hỗ trợ OO chỉ làm suy yếu tính đóng gói hoàn hảo mà ta từng có trong C.

## Kế thừa (Inheritance)?

Nếu các ngôn ngữ OO không cho chúng ta sự đóng gói tốt hơn, chắc chắn chúng cho chúng ta kế thừa.

Cũng có phần như vậy. Kế thừa chỉ đơn giản là khai báo lại một nhóm biến và hàm trong một phạm vi bao quanh. Lập trình viên C[^3] đã có thể làm việc này bằng tay từ lâu trước khi có ngôn ngữ OO.

Xét sự bổ sung này cho chương trình `point.h` C gốc của chúng ta:

namedPoint.h

```c
struct NamedPoint;

struct NamedPoint* makeNamedPoint(double x, double y, char* name);
void setName(struct NamedPoint* np, char* name);
char* getName(struct NamedPoint* np);
```

namedPoint.c

```c
#include "namedPoint.h"
#include <stdlib.h>

struct NamedPoint {
    double x,y;
    char* name;
};

struct NamedPoint* makeNamedPoint(double x, double y, char* name) {
    struct NamedPoint* p = malloc(sizeof(struct NamedPoint));
    p->x = x;
    p->y = y;
    p->name = name;
    return p;
}

void setName(struct NamedPoint* np, char* name) {
    np->name = name;
}

char* getName(struct NamedPoint* np) {
    return np->name;
}
```

main.c

```c
#include "point.h"
#include "namedPoint.h"
#include <stdio.h>

int main(int ac, char** av) {
    struct NamedPoint* origin = makeNamedPoint(0.0, 0.0, "origin");
    struct NamedPoint* upperRight = makeNamedPoint (1.0, 1.0, "upperRight");
    printf("distance=%f\n",
    distance(
    (struct Point*) origin,
    (struct Point*) upperRight));
}
```

Nếu bạn nhìn kỹ vào chương trình chính, bạn sẽ thấy cấu trúc dữ liệu `NamedPoint` hành động như thể nó là một dẫn xuất (derivative) của cấu trúc dữ liệu `Point`. Điều này là vì thứ tự của hai trường đầu tiên trong `NamedPoint` giống với `Point`. Tóm lại, `NamedPoint` có thể ngụy trang thành `Point` vì `NamedPoint` là một siêu tập thuần túy (pure superset) của `Point` và duy trì thứ tự của các thành viên tương ứng với `Point`.

Loại thủ thuật này là một thực hành phổ biến[^4] của các lập trình viên trước kỷ nguyên ngôn ngữ OO. Thực tế, thủ thuật đó chính là cách C++ triển khai kế thừa đơn.

Vì vậy chúng ta có thể nói rằng chúng ta đã có một loại kế thừa từ lâu trước khi các ngôn ngữ OO được phát minh. Tuy nhiên phát ngôn đó không hoàn toàn đúng. Chúng ta có một thủ thuật, nhưng nó không tiện lợi như kế thừa thực sự. Hơn nữa, kế thừa đa (multiple inheritance) khó đạt được hơn nhiều bằng thủ thuật như vậy.

Lưu ý thêm rằng trong `main.c`, tôi bị buộc phải ép kiểu (cast) các đối số `NamedPoint` thành `Point`. Trong một ngôn ngữ OO thực sự, việc upcasting như vậy sẽ được ngầm hiểu (implicit).

Nói công bằng, dù ngôn ngữ OO không đem lại điều gì hoàn toàn mới, chúng khiến việc ngụy trang cấu trúc dữ liệu thuận tiện hơn đáng kể.

Tóm lại: Chúng ta không thể cho OO điểm nào cho sự đóng gói, và có lẽ nửa điểm cho kế thừa. Cho đến nay, điểm số không cao lắm.

Nhưng còn một thuộc tính nữa cần xem xét.

## Đa hình (Polymorphism)?

Chúng ta có hành vi đa hình trước các ngôn ngữ OO chứ? Tất nhiên là có. Xét chương trình sao chép (copy) C đơn giản này:

```c
#include <stdio.h>

void copy() {
    int c;
    while ((c=getchar()) != EOF)
        putchar(c);
}
```

Hàm `getchar()` đọc từ `STDIN`. Nhưng `STDIN` là thiết bị nào? Hàm `putchar()` ghi ra `STDOUT`. Nhưng thiết bị đó là gì? Hai hàm này có tính đa hình (polymorphic), nghĩa là hành vi của chúng tùy thuộc vào kiểu của `STDIN` và `STDOUT`.

Có thể xem `STDIN` và `STDOUT` như các interface kiểu Java, mỗi interface có cách triển khai cho từng thiết bị. Nhưng chương trình C này không có interface nào. Vậy lời gọi `getchar()` được chuyển đến trình điều khiển thiết bị đọc ký tự bằng cách nào?

Câu trả lời cho câu hỏi đó khá đơn giản. Hệ điều hành UNIX yêu cầu mọi trình điều khiển thiết bị IO cung cấp năm hàm chuẩn:[^5] `open`, `close`, `read`, `write`, và `seek`. Chữ ký của những hàm đó phải giống hệt nhau cho mọi trình điều khiển IO.

Cấu trúc dữ liệu `FILE` chứa năm con trỏ hàm. Trong ví dụ của chúng ta, nó có thể trông như sau:

```c
struct FILE {
    void (*open)(char* name, int mode);
    void (*close)();
    int (*read)();
    void (*write)(char);
    void (*seek)(long index, int mode);
};
```

Trình điều khiển IO của console định nghĩa các hàm đó rồi nạp địa chỉ của chúng vào một cấu trúc `FILE`, chẳng hạn như sau:

```c
#include "file.h"

void open(char* name, int mode) {/*...*/}
void close() {/*...*/};
int read() {int c;/*...*/ return c;}
void write(char c) {/*...*/}
void seek(long index, int mode) {/*...*/}

struct FILE console = {open, close, read, write, seek};
```

Bây giờ nếu `STDIN` được định nghĩa là một `FILE*`, và nếu nó trỏ đến cấu trúc dữ liệu `console`, thì `getchar()` có thể được triển khai như sau:

```c
extern struct FILE* STDIN;

int getchar() {
    return STDIN->read();
}
```

Nói cách khác, `getchar()` đơn giản gọi hàm được trỏ đến bởi con trỏ `read` của cấu trúc dữ liệu `FILE` được trỏ đến bởi `STDIN`.

Chiêu bài đơn giản này là cơ sở cho mọi đa hình trong OO. Trong C++, ví dụ, mọi hàm ảo (virtual function) trong một lớp có một con trỏ trong một bảng gọi là vtable, và mọi lời gọi hàm ảo đều đi qua bảng đó. Hàm tạo (constructor) của các lớp dẫn xuất đơn giản nạp phiên bản của chúng cho những hàm đó vào vtable của đối tượng đang được tạo.

Tóm lại, đa hình là một ứng dụng của con trỏ hàm. Các lập trình viên đã sử dụng con trỏ hàm để đạt được hành vi đa hình kể từ khi kiến trúc Von Neumann được triển khai đầu tiên vào cuối những năm 1940. Nói cách khác, OO không cung cấp gì mới.

À, nhưng điều đó không hoàn toàn đúng. Các ngôn ngữ OO có thể không cho chúng ta đa hình, nhưng chúng đã làm cho nó an toàn hơn nhiều và tiện lợi hơn nhiều.

Vấn đề với việc sử dụng tường minh con trỏ hàm để tạo hành vi đa hình là con trỏ hàm rất nguy hiểm. Việc sử dụng như vậy được điều khiển bởi một tập các quy ước thủ công. Bạn phải nhớ tuân theo quy ước để khởi tạo những con trỏ đó. Bạn phải nhớ tuân theo quy ước để gọi tất cả các hàm của bạn qua những con trỏ đó. Nếu bất kỳ lập trình viên nào không nhớ các quy ước đó, lỗi (bug) kết quả có thể cực kỳ khó để tìm ra và loại bỏ.

Các ngôn ngữ OO loại bỏ những quy ước đó và do vậy loại bỏ các nguy cơ. Với ngôn ngữ OO, việc dùng đa hình trở nên rất dễ dàng. Khả năng này đem lại sức mạnh to lớn mà các lập trình viên C trước kia chỉ có thể mơ ước. Từ đó, ta có thể kết luận rằng OO áp đặt kỷ luật lên việc chuyển giao quyền điều khiển gián tiếp.

### Sức mạnh của đa hình

Đa hình có gì hay ho? Để trải nghiệm vẻ đẹp của nó tốt hơn, hãy xem lại ví dụ chương trình sao chép (copy). Chương trình đó sẽ ra sao nếu một thiết bị IO mới được tạo ra? Giả sử chúng ta muốn dùng chương trình sao chép để sao chép dữ liệu từ một thiết bị nhận dạng chữ viết tay đến một thiết bị tổng hợp lời nói: Chúng ta cần thay đổi chương trình sao chép như thế nào để nó hoạt động với những thiết bị mới đó?

Chúng ta **không cần bất kỳ thay đổi nào**! Thực tế, chúng ta thậm chí không cần biên dịch lại chương trình sao chép. Tại sao? Vì mã nguồn của chương trình sao chép **không phụ thuộc** vào mã nguồn của các trình điều khiển IO. Miễn là các trình điều khiển IO đó triển khai năm hàm chuẩn được định nghĩa bởi `FILE`, chương trình sao chép sẽ vui vẻ sử dụng chúng.

Tóm lại, các thiết bị IO đã trở thành plugin (mô-đun mở rộng) của chương trình sao chép.

Tại sao hệ điều hành UNIX làm cho các thiết bị IO trở thành plugin? Vì chúng ta đã học, vào cuối những năm 1950, rằng chương trình của chúng ta nên độc lập thiết bị (device independent). Tại sao? Vì chúng ta đã viết nhiều chương trình phụ thuộc thiết bị, chỉ để phát hiện ra rằng chúng ta thực sự muốn những chương trình đó làm cùng một công việc nhưng dùng một thiết bị khác.

Ví dụ, chúng ta thường viết chương trình đọc dữ liệu đầu vào từ bộ thẻ (decks of cards),[^6] sau đó đục bộ thẻ mới làm đầu ra. Sau đó, khách hàng của chúng ta ngừng cho chúng ta bộ thẻ và bắt đầu cho chúng ta cuộn băng từ (reels of magnetic tape). Điều này rất bất tiện, vì nó có nghĩa là viết lại phần lớn chương trình gốc. Rất thuận tiện nếu cùng một chương trình hoạt động xen kẽ với thẻ hoặc băng.
Kiến trúc plugin được phát minh để hỗ trợ loại độc lập thiết bị IO này, và đã được triển khai trong hầu như mọi hệ điều hành kể từ khi nó được giới thiệu. Dù vậy, hầu hết các lập trình viên không mở rộng ý tưởng đó cho chương trình của chính họ, vì sử dụng con trỏ hàm rất nguy hiểm.

OO cho phép kiến trúc plugin được sử dụng ở bất cứ đâu, cho bất cứ thứ gì.

### Đảo ngược phụ thuộc (Dependency Inversion)

Hãy tưởng tượng phần mềm trông như thế nào trước khi một cơ chế đa hình an toàn và tiện lợi có sẵn. Trong cây gọi (calling tree) điển hình, hàm `main` gọi các hàm cấp cao (high-level functions), các hàm cấp cao gọi các hàm cấp trung (mid-level functions), các hàm cấp trung gọi các hàm cấp thấp (low-level functions). Trong cây gọi đó, tuy nhiên, các phụ thuộc mã nguồn (source code dependencies) không thể tránh khỏi phải theo luồng điều khiển (Hình 5.1).

**Hình 5.1** Phụ thuộc mã nguồn so với luồng điều khiển

Để `main` gọi một trong các hàm cấp cao, nó phải nhắc đến tên của mô-đun chứa hàm đó. Trong C, đây là một `#include`. Trong Java, đây là một câu lệnh `import`. Trong C#, đây là một câu lệnh `using`. Thực tế, mọi caller (hàm gọi) đều bị buộc phải nhắc đến tên của mô-đun chứa callee (hàm được gọi).

Yêu cầu này khiến kiến trúc sư phần mềm có rất ít lựa chọn, thậm chí có thể không có lựa chọn nào. Hành vi của hệ thống quyết định luồng điều khiển, còn luồng điều khiển lại quyết định các phụ thuộc mã nguồn.
Tuy nhiên, khi đưa đa hình vào, mọi chuyện có thể khác hẳn (Hình 5.2).

**Hình 5.2** Đảo ngược phụ thuộc

Trong Hình 5.2, mô-đun `HL1` gọi hàm `F()` trong mô-đun `ML1`. Việc gọi hàm qua một interface chỉ là thủ thuật ở mã nguồn. Khi chương trình chạy, interface không tồn tại. `HL1` chỉ gọi `F()` trong `ML1`.[^7]

Tuy nhiên, hãy lưu ý rằng phụ thuộc mã nguồn (mối quan hệ kế thừa) giữa `ML1` và interface `I` trỏ về hướng **ngược lại** so với luồng điều khiển. Điều này được gọi là **đảo ngược phụ thuộc (dependency inversion)**, và những hệ lụy của nó đối với kiến trúc sư phần mềm là sâu sắc.

Thực tế là các ngôn ngữ OO cung cấp đa hình an toàn và tiện lợi có nghĩa là **bất kỳ** phụ thuộc mã nguồn nào, không quan trọng nó ở đâu, đều có thể bị đảo ngược.

Hãy nhìn lại cây gọi trong Hình 5.1 cùng các phụ thuộc mã nguồn của nó. Có thể đảo chiều bất kỳ phụ thuộc nào bằng cách chèn một interface vào giữa.

Với cách này, kiến trúc sư làm việc trên hệ thống OO có thể kiểm soát hoàn toàn hướng của mọi phụ thuộc mã nguồn. Họ không cần căn chỉnh các phụ thuộc ấy theo luồng điều khiển. Bất kể mô-đun nào gọi hay được gọi, kiến trúc sư đều có thể định hướng phụ thuộc mã nguồn theo ý mình.

Đó là sức mạnh mà OO đem lại. Ít nhất từ góc nhìn của kiến trúc sư, đó mới là bản chất của OO.

Bạn có thể làm gì với quyền lực đó? Ví dụ, bạn có thể sắp xếp lại các phụ thuộc mã nguồn của hệ thống sao cho cơ sở dữ liệu (database) và giao diện người dùng (UI) phụ thuộc vào các quy tắc nghiệp vụ (business rules) (Hình 5.3), thay vì ngược lại.

**Hình 5.3** Cơ sở dữ liệu và giao diện người dùng phụ thuộc vào quy tắc nghiệp vụ

Điều này có nghĩa là UI và cơ sở dữ liệu có thể là các plugin cho các quy tắc nghiệp vụ. Nó có nghĩa là mã nguồn của các quy tắc nghiệp vụ **không bao giờ** nhắc đến UI hoặc cơ sở dữ liệu.

Như một hệ quả, các quy tắc nghiệp vụ, UI, và cơ sở dữ liệu có thể được biên dịch thành ba thành phần (component) hoặc đơn vị triển khai (deployment unit) riêng biệt (ví dụ: file jar, DLL, hoặc Gem file) có cùng các phụ thuộc như mã nguồn. Thành phần chứa các quy tắc nghiệp vụ sẽ **không** phụ thuộc vào các thành phần chứa UI và cơ sở dữ liệu.

Lại nữa, các quy tắc nghiệp vụ có thể được triển khai độc lập với UI và cơ sở dữ liệu. Thay đổi đối với UI hoặc cơ sở dữ liệu không cần có bất kỳ tác động nào lên các quy tắc nghiệp vụ. Những thành phần đó có thể được triển khai riêng biệt và độc lập.

Tóm lại, khi mã nguồn trong một thành phần thay đổi, **chỉ** thành phần đó cần được triển khai lại. Đây là **khả năng triển khai độc lập (independent deployability)**.

Nếu các mô-đun trong hệ thống của bạn có thể được triển khai độc lập, thì chúng có thể được phát triển độc lập bởi các đội khác nhau. Đó là **khả năng phát triển độc lập (independent developability)**.

## Kết luận

OO là gì? Có nhiều ý kiến và nhiều câu trả lời. Với kiến trúc sư phần mềm, câu trả lời rất rõ: OO là khả năng dùng đa hình để kiểm soát hoàn toàn mọi phụ thuộc mã nguồn trong hệ thống. Nhờ đó, kiến trúc sư có thể tạo ra kiến trúc plugin, trong đó các mô-đun chứa chính sách cấp cao không phụ thuộc vào mô-đun chứa chi tiết cấp thấp. Các chi tiết cấp thấp được tách thành những plugin có thể phát triển và triển khai độc lập với các mô-đun chứa chính sách cấp cao.

[^1]: Bộ biên dịch C++ cần biết kích thước của các instance (thể hiện) của mỗi lớp.
[^2]: Ví dụ: Smalltalk, Python, JavaScript, Lua, và Ruby.
[^3]: Không chỉ các lập trình viên C: Hầu hết các ngôn ngữ thời đó đều có khả năng ngụy trang một cấu trúc dữ liệu thành một cấu trúc khác.
[^4]: Thực tế nó vẫn là như vậy.
[^5]: Hệ thống UNIX đa dạng; đây chỉ là một ví dụ.
[^6]: Thẻ đục lỗ Hollerith của IBM, rộng 80 cột. Có lẽ nhiều bạn chưa từng thấy loại thẻ này, nhưng chúng rất phổ biến trong các thập niên 1950, 1960, thậm chí cả 1970.
[^7]: dù là gián tiếp.