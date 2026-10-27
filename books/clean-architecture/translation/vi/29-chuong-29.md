# Chương 29: Kiến trúc nhúng sạch
![Minh họa](assets/illustrations/29-chuong-29-opener.png){w=300}
> James Grenning

Một thời gian trước, tôi đọc bài viết “The Growing Importance of Sustaining Software for the DoD”[^1] trên blog của Doug Schmidt. Doug đưa ra nhận định sau:

> “Phần mềm không hao mòn, nhưng firmware và phần cứng sẽ lỗi thời, khiến phần mềm phải được sửa đổi.”

Đó là khoảnh khắc giúp tôi hiểu rõ vấn đề. Doug nhắc đến hai thuật ngữ mà tôi tưởng là hiển nhiên, nhưng có lẽ không phải vậy. Phần mềm có thể hữu ích trong thời gian dài, còn firmware sẽ lỗi thời khi phần cứng phát triển. Nếu từng tham gia phát triển hệ thống nhúng, bạn biết phần cứng luôn được cải tiến. Đồng thời, các tính năng mới được thêm vào “phần mềm”, khiến nó ngày càng phức tạp.

Tôi muốn bổ sung vào nhận định của Doug:

> Dù phần mềm không hao mòn, các phụ thuộc không được quản lý vào firmware và phần cứng có thể phá hủy nó từ bên trong.

Phần mềm nhúng không hiếm khi bị tước mất khả năng tồn tại lâu dài vì bị nhiễm các phụ thuộc vào phần cứng.

Tôi thích định nghĩa firmware của Doug, nhưng hãy xem còn định nghĩa nào khác. Tôi tìm thấy những cách diễn đạt sau:

- “Firmware được lưu trong các thiết bị nhớ không mất dữ liệu như ROM, EPROM hoặc bộ nhớ flash.” (https://en.wikipedia.org/wiki/Firmware)
- “Firmware là một chương trình phần mềm hoặc tập hợp chỉ thị được lập trình vào một thiết bị phần cứng.” (https://techterms.com/definition/firmware)
- “Firmware là phần mềm được nhúng trong một thiết bị phần cứng.” (https://www.lifewire.com/what-is-firmware-2625881)
- Firmware là “phần mềm, gồm chương trình hoặc dữ liệu, được ghi vào bộ nhớ chỉ đọc (ROM).” (http://www.webopedia.com/TERM/F/firmware.html)

Nhận định của Doug khiến tôi nhận ra rằng các định nghĩa firmware được chấp nhận này sai, hoặc ít nhất đã lỗi thời. Firmware không có nghĩa là mã nằm trong ROM. Mã không phải firmware vì nơi lưu trữ của nó, mà vì nó phụ thuộc vào điều gì và khó thay đổi ra sao khi phần cứng phát triển. Phần cứng thực sự phát triển, chỉ cần dừng lại nhìn chiếc điện thoại của bạn là thấy. Vì vậy, ta nên cấu trúc mã nhúng dựa trên thực tế đó.

Tôi không có gì phản đối firmware hay các kỹ sư firmware. Chính tôi cũng từng viết firmware. Nhưng điều chúng ta thực sự cần là ít firmware hơn và nhiều phần mềm hơn. Thực ra, tôi thất vọng khi thấy các kỹ sư firmware viết quá nhiều firmware!

Các kỹ sư không làm hệ thống nhúng cũng viết firmware! Lập trình viên không chuyên nhúng vẫn viết firmware mỗi khi chôn câu lệnh SQL vào mã hoặc rải phụ thuộc nền tảng khắp nơi. Lập trình viên ứng dụng Android viết firmware khi không tách logic nghiệp vụ khỏi API Android.

Tôi từng tham gia nhiều dự án mà ranh giới giữa mã sản phẩm, tức phần mềm, và mã giao tiếp với phần cứng sản phẩm, tức firmware, mờ đến mức gần như không tồn tại. Chẳng hạn, cuối những năm 1990, tôi tham gia thiết kế lại một hệ thống truyền thông đang chuyển từ ghép kênh phân chia theo thời gian (TDM) sang thoại qua IP (VOIP). VOIP là cách làm phổ biến hiện nay, còn TDM từng được xem là công nghệ tiên tiến trong những năm 1950 và 1960, rồi được triển khai rộng rãi trong thập niên 1980 và 1990.

Mỗi khi hỏi kỹ sư hệ thống một cuộc gọi nên phản ứng thế nào trong một tình huống cụ thể, anh ấy lại biến mất rồi lát sau trở ra với câu trả lời rất chi tiết. “Anh lấy câu trả lời đó ở đâu?” chúng tôi hỏi. “Từ mã của sản phẩm hiện tại,” anh ấy đáp. Mã cũ rối rắm đã trở thành bản đặc tả cho sản phẩm mới! Phần triển khai hiện tại không hề tách TDM khỏi logic nghiệp vụ xử lý cuộc gọi. Toàn bộ sản phẩm phụ thuộc vào phần cứng và công nghệ từ đầu đến cuối, không thể tháo gỡ. Về cơ bản, toàn bộ sản phẩm đã trở thành firmware.

Xét một ví dụ khác. Thông điệp lệnh được gửi đến hệ thống qua cổng nối tiếp. Dĩ nhiên, có một bộ xử lý và điều phối thông điệp. Nó biết định dạng thông điệp, có thể phân tích cú pháp, rồi chuyển thông điệp đến mã xử lý yêu cầu. Không có gì bất ngờ, ngoại trừ việc bộ xử lý và điều phối thông điệp nằm cùng tệp với mã giao tiếp với phần cứng UART.[^2] Bộ xử lý thông điệp bị lẫn chi tiết UART. Nó vốn có thể là phần mềm hữu ích lâu dài, nhưng thay vào đó lại trở thành firmware. Bộ xử lý thông điệp mất cơ hội trở thành phần mềm, điều đó thật không ổn!

Tôi đã hiểu từ lâu rằng cần tách phần mềm khỏi phần cứng, nhưng lời Doug giúp tôi làm rõ cách dùng hai thuật ngữ phần mềm và firmware khi nói về mối quan hệ giữa chúng.

Thông điệp dành cho kỹ sư và lập trình viên rất rõ: hãy ngừng viết quá nhiều firmware và cho mã của bạn cơ hội hữu ích lâu dài. Dĩ nhiên, chỉ yêu cầu như vậy không khiến nó xảy ra. Hãy xem cách giữ kiến trúc phần mềm nhúng sạch để phần mềm có cơ hội tồn tại lâu dài và hữu ích.

## Bài kiểm tra App-titude

Vì sao phần lớn phần mềm nhúng có tiềm năng lại trở thành firmware? Có vẻ như phần lớn nỗ lực tập trung vào việc làm cho mã nhúng hoạt động, chứ không chú trọng cấu trúc để nó hữu ích lâu dài. Kent Beck mô tả ba hoạt động khi xây dựng phần mềm. Phần trích dẫn là lời của Kent, còn chữ in nghiêng là bình luận của tôi:

1. “Trước tiên, làm cho nó hoạt động.” Nếu không chạy được thì bạn hết cơ hội.
2. “Sau đó, làm cho nó đúng.” Tái cấu trúc mã để bạn và người khác hiểu được, đồng thời có thể phát triển nó khi nhu cầu thay đổi hoặc được hiểu rõ hơn.
3. “Cuối cùng, làm cho nó nhanh.” Tái cấu trúc mã để đạt hiệu năng “cần thiết”.

Phần lớn phần mềm nhúng tôi thấy ngoài thực tế dường như chỉ được viết với mục tiêu “Làm cho nó hoạt động”, và có lẽ còn bị ám ảnh bởi mục tiêu “Làm cho nó nhanh”, đạt được bằng cách bổ sung tối ưu hóa vi mô ở mọi cơ hội. Trong *The Mythical Man-Month*, Fred Brooks khuyên chúng ta “hãy dự tính sẽ vứt bỏ một bản”. Kent và Fred gần như đưa ra cùng một lời khuyên: tìm hiểu điều gì hiệu quả rồi tạo ra giải pháp tốt hơn.

Phần mềm nhúng cũng không đặc biệt hơn các phần mềm khác khi gặp những vấn đề này. Phần lớn ứng dụng không nhúng chỉ được xây dựng để chạy, mà ít chú ý đến việc làm cho mã đúng đắn để dùng lâu dài.

Tôi gọi việc làm cho ứng dụng hoạt động là bài kiểm tra App-titude dành cho lập trình viên. Lập trình viên, dù làm hệ thống nhúng hay không, nếu chỉ quan tâm đến việc ứng dụng chạy được thì đang gây bất lợi cho sản phẩm và người sử dụng lao động. Lập trình còn nhiều hơn việc làm cho ứng dụng chạy được.

Ví dụ về mã được tạo ra khi chỉ vượt qua bài kiểm tra App-titude là các hàm sau, nằm chung trong một tệp của hệ thống nhúng nhỏ:

```c
ISR(TIMER1_vect) { ... }
ISR(INT2_vect) { ... }
void btn_Handler(void) { ... }
float calc_RPM(void) { ... }
static char Read_RawData(void) { ... }
void Do_Average(void) { ... }
void Get_Next_Measurement(void) { ... }
void Zero_Sensor_1(void) { ... }
void Zero_Sensor_2(void) { ... }
void Dev_Control(char Activation) { ... }
char Load_FLASH_Setup(void) { ... }
void Save_FLASH_Setup(void) { ... }
void Store_DataSet(void) { ... }
float bytes2float(char bytes[4]) { ... }
void Recall_DataSet(void) { ... }
void Sensor_init(void) { ... }
void uC_Sleep(void) { ... }
```

Đây là thứ tự các hàm tôi tìm thấy trong mã nguồn. Bây giờ tôi sẽ tách chúng ra và nhóm theo mối quan tâm:

- **Các hàm chứa logic miền:**

```c
float calc_RPM(void) { ... }
void Do_Average(void) { ... }
void Get_Next_Measurement(void) { ... }
void Zero_Sensor_1(void) { ... }
void Zero_Sensor_2(void) { ... }
```

- **Các hàm thiết lập nền tảng phần cứng:**

```c
ISR(TIMER1_vect) { ... }*
ISR(INT2_vect) { ... }
void uC_Sleep(void) { ... }
```

- **Các hàm phản ứng khi nhấn nút bật/tắt:**

```c
void btn_Handler(void) { ... }
void Dev_Control(char Activation) { ... }
```

- **Hàm đọc đầu vào A/D từ phần cứng:**

```c
static char Read_RawData(void) { ... }
```

- **Các hàm lưu giá trị vào bộ nhớ bền vững:**

```c
char Load_FLASH_Setup(void) { ... }
void Save_FLASH_Setup(void) { ... }
void Store_DataSet(void) { ... }
float bytes2float(char bytes[4]) { ... }
void Recall_DataSet(void) { ... }
```

- **Hàm không làm điều mà tên của nó ngụ ý:**

```c
void Sensor_init(void) { ... }
```

Khi xem các tệp khác trong ứng dụng này, tôi thấy nhiều thứ cản trở việc hiểu mã. Tôi cũng thấy cấu trúc tệp ngụ ý rằng cách duy nhất để kiểm thử mã là trên thiết bị nhúng. Hầu như mọi đoạn mã đều biết rằng nó chạy trên một kiến trúc vi xử lý đặc biệt, dùng các cấu trúc C “mở rộng”[^3] gắn mã với một chuỗi công cụ và vi xử lý cụ thể. Mã trông như C nhưng không còn là C nữa. Mã này không thể hữu ích lâu dài nếu sản phẩm không bao giờ cần chuyển sang môi trường phần cứng khác.

Ứng dụng này hoạt động, người kỹ sư đã vượt qua bài kiểm tra App-titude. Nhưng không thể gọi đây là kiến trúc nhúng sạch.

## Nút thắt phần cứng đích

Có nhiều vấn đề đặc thù mà nhà phát triển hệ thống nhúng phải xử lý, còn người không làm nhúng thì không, chẳng hạn bộ nhớ hạn chế, ràng buộc thời gian thực và hạn chót, IO hạn chế, giao diện người dùng khác thường, cảm biến và kết nối với thế giới thực. Phần cứng thường được phát triển đồng thời với phần mềm và firmware. Khi viết mã cho loại hệ thống này, có thể bạn không có nơi nào để chạy mã. Nếu chưa đủ tệ, khi nhận được phần cứng, nhiều khả năng nó còn có lỗi riêng, khiến tiến độ phát triển phần mềm chậm hơn bình thường.

Đúng là hệ thống nhúng có những điểm đặc thù. Kỹ sư nhúng cũng có chuyên môn đặc thù. Nhưng phát triển nhúng không đặc biệt đến mức các nguyên tắc trong cuốn sách này không áp dụng được.

Một vấn đề riêng của hệ thống nhúng là nút thắt phần cứng đích. Nếu mã nhúng được cấu trúc mà không áp dụng các nguyên tắc và thực hành của Kiến trúc Sạch, bạn thường chỉ có thể kiểm thử mã trên thiết bị đích. Khi đó, thiết bị đích trở thành nút thắt làm chậm công việc.

## Kiến trúc nhúng sạch có thể kiểm thử

Hãy xem cách áp dụng một số nguyên tắc kiến trúc vào phần mềm và firmware nhúng để loại bỏ nút thắt phần cứng đích.

### Các lớp

Có nhiều cách phân lớp. Hãy bắt đầu với ba lớp như trong Hình 29.1. Phần dưới cùng là phần cứng. Như Doug cảnh báo, do tiến bộ công nghệ và Định luật Moore, phần cứng sẽ thay đổi. Linh kiện sẽ lỗi thời, còn linh kiện mới sẽ tiêu thụ ít điện hơn, hoạt động tốt hơn hoặc rẻ hơn. Dù lý do là gì, với tư cách kỹ sư nhúng, tôi không muốn phải làm nhiều việc hơn mức cần thiết khi thay đổi phần cứng không thể tránh khỏi.

**Hình 29.1** Ba lớp

Việc tách phần cứng khỏi phần còn lại của hệ thống là điều hiển nhiên, ít nhất sau khi phần cứng đã được xác định (Hình 29.2). Đây là nơi thường bắt đầu vấn đề khi cố vượt qua bài kiểm tra App-titude. Không có gì ngăn hiểu biết về phần cứng làm ô nhiễm toàn bộ mã. Nếu không cẩn thận khi sắp xếp mã và quy định điều một mô-đun được phép biết về mô-đun khác, mã sẽ rất khó thay đổi. Tôi không chỉ nói đến trường hợp phần cứng thay đổi, mà cả khi người dùng yêu cầu thay đổi hoặc cần sửa lỗi.

**Hình 29.2** Phần cứng phải được tách khỏi phần còn lại của hệ thống

Trộn lẫn phần mềm và firmware là một phản mẫu. Mã theo phản mẫu này chống lại thay đổi. Hơn nữa, thay đổi trở nên nguy hiểm và thường dẫn đến hậu quả ngoài ý muốn. Ngay cả thay đổi nhỏ cũng có thể đòi hỏi kiểm thử hồi quy toàn hệ thống. Nếu chưa tạo kiểm thử có thiết bị đo và quan sát bên ngoài, hãy chuẩn bị tinh thần chán ngấy các kiểm thử thủ công, rồi chờ báo cáo lỗi mới.

### Phần cứng là chi tiết

Ranh giới giữa phần mềm và firmware thường không rõ ràng bằng ranh giới giữa mã và phần cứng, như Hình 29.3 cho thấy.

**Hình 29.3** Ranh giới giữa phần mềm và firmware mờ hơn ranh giới giữa mã và phần cứng

Một trong những nhiệm vụ của nhà phát triển phần mềm nhúng là làm rõ ranh giới đó. Ranh giới giữa phần mềm và firmware gọi là lớp trừu tượng phần cứng (HAL), như Hình 29.4 cho thấy. Đây không phải ý tưởng mới. HAL đã có trong máy tính cá nhân từ trước thời Windows.

**Hình 29.4** Lớp trừu tượng phần cứng

HAL phục vụ phần mềm nằm bên trên nó, và API của HAL nên được thiết kế theo nhu cầu của phần mềm đó. Chẳng hạn, firmware có thể lưu byte và mảng byte vào bộ nhớ flash. Ngược lại, ứng dụng cần lưu và đọc các cặp tên/giá trị từ một cơ chế lưu trữ nào đó. Phần mềm không nên quan tâm các cặp tên/giá trị được lưu trong bộ nhớ flash, đĩa quay, đám mây hay bộ nhớ lõi. HAL cung cấp dịch vụ mà không tiết lộ cách thực hiện. Cách triển khai bằng flash là chi tiết cần được giấu khỏi phần mềm.

Ví dụ khác, đèn LED được nối với một bit GPIO. Firmware có thể cho phép truy cập trực tiếp các bit GPIO, trong khi HAL cung cấp hàm `Led_TurnOn(5)`. Đây là lớp trừu tượng phần cứng khá thấp. Hãy xem xét việc nâng mức trừu tượng từ góc nhìn phần cứng lên góc nhìn phần mềm và sản phẩm. Đèn LED biểu thị điều gì? Giả sử nó báo pin yếu. Ở một mức nào đó, firmware hoặc gói hỗ trợ bo mạch có thể cung cấp `Led_TurnOn(5)`, còn HAL cung cấp `Indicate_LowBattery()`. Có thể thấy HAL biểu đạt các dịch vụ mà ứng dụng cần. Cũng có thể thấy các lớp có thể chứa những lớp khác. Đây giống một mô hình fractal lặp lại hơn là một tập lớp được định nghĩa cố định. Các ánh xạ GPIO là chi tiết cần được giấu khỏi phần mềm.

#### Không để lộ chi tiết phần cứng cho người dùng HAL

Phần mềm trong kiến trúc nhúng sạch có thể được kiểm thử ngoài phần cứng đích. HAL thành công cung cấp đường nối hoặc tập điểm thay thế giúp kiểm thử ngoài thiết bị đích.

### Bộ xử lý là chi tiết

Khi ứng dụng nhúng dùng chuỗi công cụ chuyên biệt, nó thường cung cấp các tệp tiêu đề để *giúp bạn*.[^4] Những trình biên dịch này thường tự ý mở rộng ngôn ngữ C, thêm từ khóa mới để truy cập tính năng của bộ xử lý. Mã trông như C nhưng không còn là C.

Đôi khi, trình biên dịch C do nhà cung cấp đưa ra có những biến trông như biến toàn cục để truy cập trực tiếp thanh ghi bộ xử lý, cổng IO, bộ định thời xung nhịp, bit IO, bộ điều khiển ngắt và các chức năng khác của bộ xử lý. Truy cập dễ dàng vào những thứ này rất hữu ích, nhưng hãy nhớ rằng mã nào sử dụng các tiện ích này sẽ không còn là C nữa. Nó không thể biên dịch cho bộ xử lý khác, thậm chí có thể không biên dịch được với trình biên dịch khác dành cho cùng bộ xử lý.

Tôi không muốn nghĩ rằng nhà cung cấp chip hoặc công cụ đang cố ý ràng buộc sản phẩm của bạn với trình biên dịch. Hãy tin rằng họ thực sự muốn giúp. Nhưng giờ đến lượt bạn dùng sự trợ giúp đó sao cho không gây hại trong tương lai. Bạn phải giới hạn những tệp được phép biết về phần mở rộng của C.

Hãy xem tệp tiêu đề được thiết kế cho họ DSP ACME, đúng loại mà Wile E. Coyote sử dụng:

```c
#ifndef _ACME_STD_TYPES
#define _ACME_STD_TYPES

#if defined(_ACME_X42)
typedef unsigned int Uint_32;
typedef unsigned short Uint_16;
typedef unsigned char Uint_8;

typedef int Int_32;
typedef short Int_16;
typedef char Int_8;

#elif defined(_ACME_A42)
typedef unsigned long Uint_32;
typedef unsigned int Uint_16;
typedef unsigned char Uint_8;

typedef long Int_32;
typedef int Int_16;
typedef char Int_8;
#else
#error <acmetypes.h> is not supported for this environment
#endif

#endif
```

Không nên dùng trực tiếp tệp tiêu đề `acmetypes.h`. Nếu làm vậy, mã của bạn sẽ bị ràng buộc với một trong các DSP ACME. Bạn nói mình đang dùng DSP ACME, vậy có vấn đề gì? Bạn không thể biên dịch mã nếu không đưa tệp tiêu đề này vào. Nếu dùng tệp đó và định nghĩa `_ACME_X42` hoặc `_ACME_A42`, các số nguyên sẽ sai kích thước khi kiểm thử ngoài thiết bị đích. Tệ hơn nữa, một ngày nào đó bạn sẽ muốn chuyển ứng dụng sang bộ xử lý khác. Việc không chọn khả năng chuyển đổi và không giới hạn những tệp biết về ACME sẽ khiến công việc đó khó hơn nhiều.

Thay vì dùng `acmetypes.h`, hãy theo hướng chuẩn hóa hơn và dùng `stdint.h`. Nhưng nếu trình biên dịch của thiết bị đích không cung cấp `stdint.h` thì sao? Bạn có thể tự viết tệp tiêu đề này. Phiên bản `stdint.h` dùng cho bản build đích sẽ dùng `acmetypes.h` như sau:

```c
#ifndef _STDINT_H_
#define _STDINT_H_

#include <acmetypes.h>

typedef Uint_32 uint32_t;
typedef Uint_16 uint16_t;
typedef Uint_8 uint8_t;

typedef Int_32 int32_t;
typedef Int_16 int16_t;
typedef Int_8 int8_t;

#endif
```

Việc để phần mềm nhúng và firmware dùng `stdint.h` giúp mã sạch và dễ chuyển đổi. Tất nhiên, toàn bộ phần mềm nên độc lập với bộ xử lý, nhưng không phải firmware nào cũng có thể độc lập như vậy. Đoạn mã tiếp theo tận dụng các phần mở rộng đặc biệt của C để truy cập thiết bị ngoại vi trong vi điều khiển. Có khả năng sản phẩm của bạn dùng vi điều khiển này chính vì nó có các thiết bị ngoại vi tích hợp. Hàm sau gửi dòng chữ “hi” ra cổng nối tiếp. (Ví dụ này dựa trên mã thực tế.)

```c
void say_hi()
{
IE = 0b11000000;
SBUF0 = (0x68);
while(TI_0 == 0);
TI_0 = 0;
SBUF0 = (0x69);
while(TI_0 == 0);
TI_0 = 0;
SBUF0 = (0x0a);
while(TI_0 == 0);
TI_0 = 0;
SBUF0 = (0x0d);
while(TI_0 == 0);
TI_0 = 0;
IE = 0b11010000;
}
```

Hàm nhỏ này có nhiều vấn đề. Một điều có thể khiến bạn chú ý là sự xuất hiện của `0b11000000`. Cú pháp nhị phân này khá hay, nhưng C có hỗ trợ không? Tiếc là không. Một số vấn đề khác liên quan trực tiếp đến các phần mở rộng C tùy chỉnh:

- `IE`: các bit cho phép ngắt.
- `SBUF0`: bộ đệm đầu ra nối tiếp.
- `TI_0`: ngắt báo bộ đệm truyền nối tiếp trống. Đọc giá trị 1 nghĩa là bộ đệm trống.

Các biến viết hoa thực sự truy cập thiết bị ngoại vi tích hợp trong vi điều khiển. Nếu muốn điều khiển ngắt và xuất ký tự, bạn phải dùng các thiết bị ngoại vi này. Đúng là tiện, nhưng đây không phải C.

Kiến trúc nhúng sạch chỉ dùng trực tiếp các thanh ghi truy cập thiết bị này ở một số ít nơi và giới hạn chúng hoàn toàn trong firmware. Mọi mã biết về các thanh ghi đó đều trở thành firmware, do đó bị ràng buộc với chip. Việc ràng buộc mã với bộ xử lý sẽ gây khó khăn khi bạn muốn làm cho mã chạy trước khi phần cứng ổn định. Nó cũng gây khó khăn khi chuyển ứng dụng nhúng sang bộ xử lý mới.

Nếu dùng vi điều khiển như vậy, firmware có thể cách ly các hàm cấp thấp này bằng một dạng lớp trừu tượng bộ xử lý (PAL). Firmware nằm phía trên PAL có thể được kiểm thử ngoài thiết bị đích, nhờ đó bớt “cứng”.

### Hệ điều hành là chi tiết

HAL là cần thiết, nhưng đã đủ chưa? Trong hệ thống nhúng chạy trực tiếp trên phần cứng, HAL có thể là tất cả những gì bạn cần để mã không quá phụ thuộc vào môi trường vận hành. Nhưng các hệ thống nhúng dùng hệ điều hành thời gian thực (RTOS), hoặc phiên bản nhúng của Linux hay Windows thì sao?

Muốn phần mềm nhúng có cơ hội hữu ích lâu dài, bạn phải xem hệ điều hành là chi tiết và bảo vệ phần mềm khỏi phụ thuộc vào hệ điều hành.

Phần mềm truy cập dịch vụ của môi trường vận hành thông qua hệ điều hành. Hệ điều hành là một lớp tách phần mềm khỏi firmware (Hình 29.5). Dùng trực tiếp hệ điều hành có thể gây vấn đề. Chẳng hạn, điều gì xảy ra nếu nhà cung cấp RTOS bị một công ty khác mua lại, phí bản quyền tăng hoặc chất lượng giảm? Điều gì xảy ra nếu nhu cầu thay đổi và RTOS không còn cung cấp khả năng bạn cần? Bạn sẽ phải thay đổi nhiều mã. Những thay đổi này không chỉ là chỉnh cú pháp cho phù hợp với API của hệ điều hành mới, mà còn có thể phải điều chỉnh ngữ nghĩa để phù hợp với khả năng và cơ chế khác của hệ điều hành đó.

**Hình 29.5** Thêm hệ điều hành

Kiến trúc nhúng sạch cách ly phần mềm khỏi hệ điều hành thông qua lớp trừu tượng hệ điều hành (OSAL), như Hình 29.6 cho thấy. Trong một số trường hợp, triển khai lớp này có thể đơn giản như đổi tên một hàm. Trong trường hợp khác, nó có thể cần gói nhiều hàm lại với nhau.

**Hình 29.6** Lớp trừu tượng hệ điều hành

Nếu từng chuyển phần mềm từ RTOS này sang RTOS khác, bạn biết việc đó rất đau đầu. Nếu phần mềm phụ thuộc vào OSAL thay vì phụ thuộc trực tiếp vào hệ điều hành, phần lớn công việc sẽ là viết OSAL mới tương thích với OSAL cũ. Bạn muốn làm việc nào hơn: sửa một đống mã hiện có phức tạp, hay viết mã mới theo giao diện và hành vi đã xác định? Đây không phải câu hỏi đánh đố. Tôi chọn cách thứ hai.

Có thể đến đây bạn bắt đầu lo về mã phình to. Nhưng trên thực tế, lớp này trở thành nơi cách ly phần lớn mã trùng lặp liên quan đến việc dùng hệ điều hành. Sự trùng lặp này không nhất thiết gây nhiều chi phí phụ. Nếu định nghĩa OSAL, bạn cũng có thể khuyến khích ứng dụng có cấu trúc chung. Thay vì để mỗi luồng tự xây dựng mô hình đồng thời, bạn có thể cung cấp cơ chế truyền thông điệp.

OSAL có thể cung cấp các điểm kiểm thử để mã ứng dụng có giá trị trong lớp phần mềm được kiểm thử ngoài thiết bị và ngoài hệ điều hành. Phần mềm trong kiến trúc nhúng sạch có thể được kiểm thử mà không cần hệ điều hành đích. OSAL thành công cung cấp đường nối hoặc các điểm thay thế giúp kiểm thử ngoài thiết bị đích.

## Lập trình theo giao diện và khả năng thay thế

Ngoài việc thêm HAL và có thể cả OSAL vào các lớp chính, gồm phần mềm, hệ điều hành, firmware và phần cứng, bạn có thể và nên áp dụng các nguyên tắc được mô tả trong suốt cuốn sách này. Những nguyên tắc đó khuyến khích phân tách mối quan tâm, lập trình theo giao diện và khả năng thay thế.

Ý tưởng kiến trúc phân lớp dựa trên việc lập trình theo giao diện. Khi một mô-đun tương tác với mô-đun khác thông qua giao diện, bạn có thể thay nhà cung cấp dịch vụ này bằng nhà cung cấp khác. Nhiều độc giả hẳn từng viết phiên bản `printf` nhỏ của riêng mình để triển khai trên thiết bị đích. Miễn là giao diện `printf` của bạn giống phiên bản chuẩn, bạn có thể thay dịch vụ này bằng dịch vụ kia.

Một quy tắc kinh nghiệm cơ bản là dùng tệp header để định nghĩa giao diện. Tuy nhiên, hãy cẩn thận với nội dung trong tệp header. Chỉ đưa vào đó các khai báo hàm, cùng những hằng số và tên struct mà các hàm cần.

Đừng làm lộn xộn tệp header giao diện bằng cấu trúc dữ liệu, hằng số và typedef chỉ cần cho phần triển khai. Đây không chỉ là vấn đề lộn xộn: những nội dung đó dẫn đến các phụ thuộc không mong muốn. Hãy giới hạn khả năng nhìn thấy chi tiết triển khai. Hãy dự kiến rằng các chi tiết đó sẽ thay đổi. Càng ít vị trí trong mã biết về các chi tiết này thì càng ít nơi cần tìm và sửa.

Kiến trúc nhúng sạch có thể được kiểm thử bên trong từng lớp vì các mô-đun tương tác thông qua giao diện. Mỗi giao diện tạo ra đường nối hoặc điểm thay thế giúp kiểm thử ngoài thiết bị đích.

## Chỉ thị biên dịch có điều kiện DRY

Một cách áp dụng khả năng thay thế thường bị bỏ qua liên quan đến cách chương trình C và C++ nhúng xử lý các thiết bị đích hoặc hệ điều hành khác nhau. Người ta thường dùng biên dịch có điều kiện để bật hoặc tắt các đoạn mã. Tôi nhớ một trường hợp đặc biệt rắc rối, khi câu lệnh `#ifdef BOARD_V2` xuất hiện vài nghìn lần trong một ứng dụng viễn thông.

Việc lặp mã này vi phạm nguyên tắc Đừng Lặp Lại Chính Mình (DRY).[^5] Nếu chỉ thấy `#ifdef BOARD_V2` một lần thì chưa thật sự là vấn đề. Sáu nghìn lần thì là vấn đề nghiêm trọng. Trong hệ thống nhúng, chỉ thị biên dịch có điều kiện xác định loại phần cứng đích thường bị lặp lại. Nhưng còn cách nào khác?

Nếu có lớp trừu tượng phần cứng thì sao? Loại phần cứng sẽ trở thành chi tiết được HAL che giấu. Nếu HAL cung cấp một tập giao diện, thay vì biên dịch có điều kiện, ta có thể dùng linker hoặc một hình thức liên kết lúc chạy để nối phần mềm với phần cứng.

## Kết luận

Những người phát triển phần mềm nhúng có nhiều điều để học từ kinh nghiệm ngoài lĩnh vực phần mềm nhúng. Nếu bạn là nhà phát triển nhúng và đã cầm cuốn sách này lên đọc, bạn sẽ tìm thấy nhiều hiểu biết quý giá về phát triển phần mềm trong những lời nói và ý tưởng ở đây.

Để mọi mã trở thành firmware không tốt cho sức khỏe lâu dài của sản phẩm. Chỉ có thể kiểm thử trên phần cứng đích cũng không tốt cho sức khỏe lâu dài của sản phẩm. Kiến trúc nhúng sạch tốt cho sức khỏe lâu dài của sản phẩm.

[^1]: https://insights.sei.cmu.edu/sei_blog/2011/08/the-growing-importance-of-sustaining-software-for-thedod.html
[^2]: Thiết bị phần cứng điều khiển cổng nối tiếp.
[^3]: Một số nhà cung cấp chip thêm từ khóa vào ngôn ngữ C để dễ truy cập thanh ghi và cổng IO. Tuy nhiên, một khi làm vậy, mã không còn là C nữa.
[^4]: Câu này cố ý dùng HTML.
[^5]: Hunt và Thomas, *The Pragmatic Programmer*.