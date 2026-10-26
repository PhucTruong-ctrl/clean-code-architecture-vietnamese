# Chương 11: Hệ thống

> Tác giả: TS. Kevin Dean Wampler

> “Sự phức tạp giết chết mọi thứ. Nó hút cạn sức sống của lập trình viên,
> khiến việc lập kế hoạch, xây dựng và kiểm thử sản phẩm trở nên khó khăn.”
> Ray Ozzie, CTO, Microsoft Corporation

## Bạn sẽ xây dựng một thành phố như thế nào?

Bạn có thể tự quản lý mọi chi tiết không? Có lẽ là không. Ngay cả việc quản lý một thành phố hiện có cũng quá sức với một người. Thế nhưng các thành phố vẫn vận hành, hầu hết thời gian. Chúng vận hành vì có những nhóm người phụ trách từng phần cụ thể của thành phố: hệ thống nước, hệ thống điện, giao thông, thực thi pháp luật, quy chuẩn xây dựng, vân vân. Một số người chịu trách nhiệm về bức tranh tổng thể, số khác tập trung vào chi tiết.

Thành phố còn vận hành được vì chúng đã phát triển những mức độ trừu tượng và mô-đun hóa phù hợp, cho phép mỗi cá nhân và những “thành phần” họ quản lý làm việc hiệu quả, ngay cả khi họ không hiểu bức tranh tổng thể.

Các nhóm phần mềm thường cũng được tổ chức như vậy, nhưng hệ thống mà họ làm việc thường không có sự phân tách mối quan tâm và các mức độ trừu tượng tương tự. Mã sạch giúp chúng ta đạt được điều đó ở các mức trừu tượng thấp. Trong chương này, chúng ta sẽ xem xét cách giữ cho hệ thống sạch ở các mức trừu tượng cao hơn, tức cấp hệ thống.

## Tách việc xây dựng hệ thống khỏi việc sử dụng hệ thống

Trước tiên, hãy nhớ rằng xây dựng là một quá trình rất khác với sử dụng. Khi tôi viết những dòng này, một khách sạn mới đang được xây dựng ngoài cửa sổ chỗ tôi ở tại Chicago. Hôm nay, nó chỉ là một khối bê tông trơ trụi, bên ngoài gắn cần cẩu và thang máy xây dựng. Những người bận rộn ở đó đều đội mũ bảo hộ và mặc quần áo lao động. Khoảng một năm nữa, khách sạn sẽ hoàn thành. Cần cẩu và thang máy sẽ biến mất. Tòa nhà sẽ sạch sẽ, được bao bọc bởi những vách kính và lớp sơn đẹp mắt. Những người làm việc và lưu trú ở đó cũng sẽ trông khác hẳn.

> Hệ thống phần mềm nên tách quá trình khởi động, khi các đối tượng ứng dụng được tạo ra và các phụ thuộc được “kết nối” với nhau, khỏi logic lúc chạy tiếp quản sau khi khởi động.

Quá trình khởi động là mối quan tâm mà mọi ứng dụng đều phải xử lý. Đây là mối quan tâm đầu tiên chúng ta xem xét trong chương này. Tách biệt mối quan tâm là một trong những kỹ thuật thiết kế lâu đời và quan trọng nhất trong nghề của chúng ta.

Đáng tiếc, hầu hết ứng dụng không tách biệt mối quan tâm này. Mã xử lý khởi động thường được viết tùy tiện và trộn lẫn với logic lúc chạy. Đây là một ví dụ điển hình:

```java
public Service getService() {
  if (service == null)
    service = new MyServiceImpl(...); // Mặc định này đủ tốt cho hầu hết trường hợp chứ?
  return service;
}
```

Đây là thành ngữ KHỞI TẠO/ĐÁNH GIÁ LƯỜI, và nó có một số ưu điểm. Ta không phải chịu chi phí khởi tạo cho đến khi thực sự dùng đối tượng, nhờ đó thời gian khởi động có thể nhanh hơn. Ta cũng bảo đảm không bao giờ trả về `null`.

Tuy nhiên, giờ đây ta phụ thuộc cứng vào `MyServiceImpl` và mọi thứ mà hàm tạo của nó cần (tôi đã lược bỏ phần đó). Ta không thể biên dịch nếu chưa giải quyết các phụ thuộc này, ngay cả khi lúc chạy ta không bao giờ dùng đối tượng thuộc kiểu này!

Việc kiểm thử có thể trở thành vấn đề. Nếu `MyServiceImpl` là một đối tượng nặng, ta phải bảo đảm một ĐỐI TƯỢNG KIỂM THỬ THAY THẾ¹ hoặc ĐỐI TƯỢNG GIẢ được gán cho trường `service` trước khi phương thức này được gọi trong quá trình kiểm thử đơn vị. Vì logic tạo đối tượng bị trộn với xử lý thông thường lúc chạy, ta nên kiểm thử mọi nhánh thực thi, chẳng hạn phép kiểm tra `null` và khối lệnh của nó. Phương thức đang gánh cả hai trách nhiệm, nghĩa là nó làm nhiều hơn một việc và vi phạm Nguyên tắc Trách nhiệm Đơn nhất ở mức độ nhỏ.

Có lẽ tệ nhất là ta không biết `MyServiceImpl` có phải đối tượng phù hợp trong mọi trường hợp hay không. Tôi đã ngụ ý điều đó trong chú thích. Tại sao lớp có phương thức này lại phải biết ngữ cảnh toàn cục? Liệu ta có bao giờ biết chắc đối tượng nào là đúng để dùng ở đây không? Có thể nào một kiểu đối tượng phù hợp với mọi ngữ cảnh không?

Dĩ nhiên, một chỗ dùng KHỞI TẠO LƯỜI không phải vấn đề nghiêm trọng. Nhưng ứng dụng thường có nhiều thành ngữ thiết lập nhỏ như thế. Vì vậy, chiến lược thiết lập toàn cục (nếu có) bị rải rác khắp ứng dụng, ít mô-đun hóa và thường trùng lặp đáng kể.

Nếu cẩn trọng khi xây dựng các hệ thống vững chắc, có cấu trúc tốt, ta không nên để những thành ngữ nhỏ tiện lợi làm suy yếu tính mô-đun. Việc tạo và kết nối đối tượng trong quá trình khởi động cũng không ngoại lệ. Ta nên mô-đun hóa riêng quá trình này khỏi logic thông thường lúc chạy, đồng thời bảo đảm có một chiến lược toàn cục, nhất quán để giải quyết các phụ thuộc chính.

### Tách biệt hàm main

Một cách tách việc xây dựng khỏi việc sử dụng là chuyển mọi khía cạnh của việc xây dựng sang `main`, hoặc các mô-đun được `main` gọi, rồi thiết kế phần còn lại của hệ thống với giả định mọi đối tượng đã được tạo và kết nối phù hợp. (Xem Hình 11-1.)

Luồng điều khiển rất dễ theo dõi. Hàm `main` tạo các đối tượng cần thiết cho hệ thống rồi chuyển chúng cho ứng dụng, nơi đơn giản là sử dụng chúng. Hãy chú ý hướng của các mũi tên phụ thuộc cắt qua ranh giới giữa `main` và ứng dụng. Tất cả đều hướng ra khỏi `main`. Điều này có nghĩa ứng dụng không biết gì về `main` hay quá trình xây dựng. Ứng dụng chỉ mong mọi thứ đã được tạo đúng cách.

**Hình 11-1**  
Tách việc xây dựng trong `main()`

### Factory

Dĩ nhiên, đôi khi ta cần để ứng dụng quyết định thời điểm tạo đối tượng. Chẳng hạn, trong hệ thống xử lý đơn hàng, ứng dụng phải tạo các đối tượng `LineItem` để thêm vào một `Order`. Khi đó ta có thể dùng mẫu ABSTRACT FACTORY² để ứng dụng kiểm soát thời điểm tạo `LineItem`, nhưng vẫn tách chi tiết xây dựng khỏi mã ứng dụng. (Xem Hình 11-2.)

**Hình 11-2**  
Tách biệt việc xây dựng bằng factory

Một lần nữa, hãy chú ý rằng mọi phụ thuộc đều hướng từ `main` về phía ứng dụng `OrderProcessing`. Điều này có nghĩa ứng dụng được tách rời khỏi chi tiết xây dựng `LineItem`. Khả năng đó nằm trong `LineItemFactoryImplementation`, ở phía `main` của ranh giới. Tuy vậy, ứng dụng vẫn hoàn toàn kiểm soát thời điểm tạo các đối tượng `LineItem`, thậm chí có thể cung cấp các đối số hàm tạo dành riêng cho ứng dụng.

¹. [Mezzaros07].

². [GOF].

### Tiêm phụ thuộc

Một cơ chế mạnh để tách việc xây dựng khỏi việc sử dụng là Tiêm phụ thuộc (Dependency Injection, DI), tức áp dụng Đảo ngược điều khiển (Inversion of Control, IoC) vào việc quản lý phụ thuộc.³ Đảo ngược điều khiển chuyển các trách nhiệm phụ từ một đối tượng sang những đối tượng khác được dành riêng cho mục đích đó, qua đó hỗ trợ Nguyên tắc Trách nhiệm Đơn nhất. Trong ngữ cảnh quản lý phụ thuộc, một đối tượng không nên tự chịu trách nhiệm khởi tạo các phụ thuộc của mình. Thay vào đó, nó nên giao trách nhiệm này cho một cơ chế “có thẩm quyền” khác, qua đó đảo ngược quyền điều khiển. Vì thiết lập là mối quan tâm toàn cục, cơ chế có thẩm quyền này thường là thủ tục `main` hoặc một bộ chứa chuyên dụng.

Các tra cứu JNDI là một cách triển khai DI “một phần”, trong đó một đối tượng yêu cầu máy chủ thư mục cung cấp một “dịch vụ” khớp với tên cụ thể:

```java
MyService myService = (MyService)(jndiContext.lookup("NameOfMyService"));
```

Đối tượng gọi không kiểm soát kiểu đối tượng thực sự được trả về (dĩ nhiên, miễn là đối tượng đó triển khai giao diện phù hợp), nhưng nó vẫn chủ động giải quyết phụ thuộc.

Tiêm phụ thuộc thực sự tiến thêm một bước. Lớp không thực hiện bước trực tiếp nào để giải quyết các phụ thuộc của nó, mà hoàn toàn thụ động. Thay vào đó, lớp cung cấp các phương thức setter hoặc đối số hàm tạo, hoặc cả hai, để tiêm các phụ thuộc vào. Trong quá trình xây dựng, bộ chứa DI khởi tạo các đối tượng cần thiết (thường theo yêu cầu) rồi dùng các đối số hàm tạo hoặc phương thức setter được cung cấp để kết nối các phụ thuộc. Những đối tượng phụ thuộc nào thực sự được dùng sẽ được chỉ định qua tệp cấu hình hoặc bằng mã trong một mô-đun xây dựng chuyên dụng.

Spring Framework cung cấp bộ chứa DI nổi tiếng nhất cho Java.⁴ Bạn định nghĩa các đối tượng cần kết nối trong một tệp cấu hình XML, rồi yêu cầu các đối tượng cụ thể theo tên trong mã Java. Chúng ta sẽ xem ví dụ ngay sau đây.

Thế còn ưu điểm của KHỞI TẠO LƯỜI thì sao? Thành ngữ này đôi khi vẫn hữu ích khi dùng DI. Thứ nhất, hầu hết bộ chứa DI sẽ không tạo một đối tượng cho đến khi cần. Thứ hai, nhiều bộ chứa cung cấp cơ chế gọi factory hoặc tạo proxy, có thể dùng cho ĐÁNH GIÁ LƯỜI và các tối ưu hóa tương tự.⁵

³. Ví dụ, xem [Fowler].

⁴. Xem [Spring]. Ngoài ra còn có framework Spring.NET.

⁵. Đừng quên rằng khởi tạo/đánh giá lười chỉ là một tối ưu hóa và có thể là tối ưu hóa quá sớm!

## Mở rộng quy mô

Thành phố phát triển từ thị trấn, thị trấn phát triển từ khu định cư. Ban đầu, đường sá nhỏ hẹp và gần như chưa tồn tại, rồi được trải nhựa, sau đó mở rộng dần theo thời gian. Những tòa nhà nhỏ và lô đất trống được lấp đầy bằng các tòa nhà lớn hơn, một số cuối cùng sẽ được thay bằng nhà chọc trời.

Ban đầu chưa có các dịch vụ như điện, nước, thoát nước và Internet (trời ơi!). Những dịch vụ này cũng được bổ sung khi dân số và mật độ xây dựng tăng lên.

Sự phát triển ấy không phải không có đau đớn. Đã bao lần bạn lái xe chậm rì, xe nối đuôi nhau qua một công trình “cải thiện” đường sá rồi tự hỏi: “Sao ngay từ đầu họ không xây đường rộng hơn nhỉ!?”

Nhưng không thể làm khác đi. Ai có thể biện minh cho chi phí xây một xa lộ sáu làn xuyên qua thị trấn nhỏ chỉ vì dự đoán nơi đó sẽ phát triển? Ai lại muốn có con đường như thế chạy qua thị trấn mình?

Thật hoang đường khi nghĩ rằng ta có thể làm cho hệ thống “đúng ngay từ đầu”. Thay vào đó, ta nên chỉ triển khai các câu chuyện người dùng của hôm nay, rồi tái cấu trúc và mở rộng hệ thống để triển khai những câu chuyện mới vào ngày mai. Đó là cốt lõi của phát triển linh hoạt theo vòng lặp và tăng dần. Phát triển hướng kiểm thử, tái cấu trúc và mã sạch do chúng tạo ra giúp cách làm này hiệu quả ở cấp mã.

Còn ở cấp hệ thống thì sao? Chẳng phải kiến trúc hệ thống cần được hoạch định trước ư? Nó đâu thể phát triển tăng dần từ đơn giản đến phức tạp được, phải không?

> Hệ thống phần mềm khác biệt với hệ thống vật lý. Kiến trúc của chúng có thể phát triển tăng dần nếu ta duy trì sự phân tách mối quan tâm thích hợp.

Bản chất phù du của hệ thống phần mềm khiến điều này trở nên khả thi, như chúng ta sẽ thấy. Trước hết, hãy xem một ví dụ đối lập về kiến trúc không phân tách mối quan tâm đầy đủ.

Các kiến trúc EJB1 và EJB2 ban đầu không phân tách mối quan tâm phù hợp, do đó dựng lên những rào cản không cần thiết đối với sự phát triển tự nhiên. Hãy xem xét một Entity Bean cho lớp `Bank` có dữ liệu bền vững. Entity bean là biểu diễn trong bộ nhớ của dữ liệu quan hệ, nói cách khác là một hàng trong bảng.

Trước tiên, bạn phải định nghĩa một giao diện cục bộ (trong cùng tiến trình) hoặc từ xa (JVM riêng), để các phía client sử dụng. Đoạn mã 11-1 cho thấy một giao diện cục bộ có thể có:

**Đoạn mã 11-1**  
Giao diện cục bộ EJB2 cho một EJB `Bank`

```java
package com.example.banking;
import java.util.Collections;
import javax.ejb.*;

public interface BankLocal extends java.ejb.EJBLocalObject {
  String getStreetAddr1() throws EJBException;
  String getStreetAddr2() throws EJBException;
  String getCity() throws EJBException;
  String getState() throws EJBException;
  String getZipCode() throws EJBException;
  void setStreetAddr1(String street1) throws EJBException;
  void setStreetAddr2(String street2) throws EJBException;
  void setCity(String city) throws EJBException;
  void setState(String state) throws EJBException;
}
```

**Đoạn mã 11-1 (tiếp)**  
Giao diện cục bộ EJB2 cho một EJB `Bank`

```java
void setZipCode(String zip) throws EJBException;
Collection getAccounts() throws EJBException;
void setAccounts(Collection accounts) throws EJBException;
void addAccount(AccountDTO accountDTO) throws EJBException;
}
```

Tôi đã trình bày một số thuộc tính địa chỉ của `Bank` và một tập hợp các tài khoản mà ngân hàng sở hữu. Mỗi tài khoản có dữ liệu được một EJB `Account` riêng xử lý. Đoạn mã 11-2 cho thấy lớp triển khai tương ứng cho bean `Bank`.

**Đoạn mã 11-2**  
Lớp triển khai Entity Bean EJB2 tương ứng

```java
package com.example.banking;
import java.util.Collections;
import javax.ejb.*;
public abstract class Bank implements javax.ejb.EntityBean {
  // Logic nghiệp vụ...
  public abstract String getStreetAddr1();
  public abstract String getStreetAddr2();
  public abstract String getCity();
  public abstract String getState();
  public abstract String getZipCode();
  public abstract void setStreetAddr1(String street1);
  public abstract void setStreetAddr2(String street2);
  public abstract void setCity(String city);
  public abstract void setState(String state);
  public abstract void setZipCode(String zip);
  public abstract Collection getAccounts();
  public abstract void setAccounts(Collection accounts);
  public void addAccount(AccountDTO accountDTO) {
    InitialContext context = new InitialContext();
    AccountHomeLocal accountHome = context.lookup("AccountHomeLocal");
    AccountLocal account = accountHome.create(accountDTO);
    Collection accounts = getAccounts();
    accounts.add(account);
  }
  // Logic của bộ chứa EJB
  public abstract void setId(Integer id);
  public abstract Integer getId();
  public Integer ejbCreate(Integer id) { ... }
  public void ejbPostCreate(Integer id) { ... }
  // Phần còn lại phải được triển khai nhưng thường để trống:
  public void setEntityContext(EntityContext ctx) {}
  public void unsetEntityContext() {}
  public void ejbActivate() {}
  public void ejbPassivate() {}
  public void ejbLoad() {}
  public void ejbStore() {}
  public void ejbRemove() {}
}
```

Tôi chưa trình bày giao diện `LocalHome` tương ứng, về cơ bản là một factory dùng để tạo đối tượng, cũng như bất kỳ phương thức tìm kiếm (truy vấn) `Bank` nào bạn có thể bổ sung.

Cuối cùng, bạn phải viết một hoặc nhiều bộ mô tả triển khai XML, chỉ định chi tiết ánh xạ đối tượng-quan hệ tới kho lưu trữ, hành vi giao dịch mong muốn, các ràng buộc bảo mật, vân vân.

Logic nghiệp vụ gắn chặt với “bộ chứa” ứng dụng EJB2. Bạn phải kế thừa các kiểu của bộ chứa và cung cấp nhiều phương thức vòng đời mà bộ chứa yêu cầu.

Vì gắn chặt với bộ chứa cồng kềnh này, việc kiểm thử đơn vị cô lập trở nên khó khăn. Ta phải giả lập bộ chứa, việc này rất khó, hoặc mất nhiều thời gian triển khai EJB và các kiểm thử lên máy chủ thật. Do phụ thuộc chặt chẽ, gần như không thể tái sử dụng bên ngoài kiến trúc EJB2.

Cuối cùng, ngay cả lập trình hướng đối tượng cũng bị suy yếu. Một bean không thể kế thừa từ bean khác. Hãy chú ý logic thêm một tài khoản mới. Các bean EJB2 thường định nghĩa “đối tượng truyền dữ liệu” (DTO), về cơ bản là các “struct” không có hành vi. Việc này thường dẫn đến các kiểu dữ liệu dư thừa chứa những dữ liệu gần như giống hệt nhau và buộc phải viết mã khuôn mẫu để sao chép dữ liệu từ đối tượng này sang đối tượng khác.

### Mối quan tâm cắt ngang

Kiến trúc EJB2 ở một số khía cạnh đã tiến gần đến việc phân tách mối quan tâm thực sự. Chẳng hạn, các hành vi giao dịch, bảo mật và một số hành vi lưu trữ bền vững mong muốn được khai báo trong bộ mô tả triển khai, độc lập với mã nguồn.

Lưu ý rằng những mối quan tâm như lưu trữ bền vững thường cắt ngang ranh giới đối tượng tự nhiên của một miền. Ta muốn lưu trữ mọi đối tượng theo nhìn chung cùng một chiến lược, chẳng hạn dùng một DBMS⁶ cụ thể thay vì tệp phẳng, tuân theo một số quy ước đặt tên cho bảng và cột, dùng ngữ nghĩa giao dịch nhất quán, vân vân.

Về nguyên tắc, ta có thể suy xét chiến lược lưu trữ bền vững theo cách mô-đun và đóng gói. Tuy vậy, trên thực tế, ta phải rải cùng một đoạn mã triển khai chiến lược lưu trữ bền vững khắp nhiều đối tượng. Ta gọi những mối quan tâm như vậy là mối quan tâm cắt ngang. Một lần nữa, framework lưu trữ bền vững có thể được mô-đun hóa, và logic miền của ta khi đứng riêng cũng có thể được mô-đun hóa. Vấn đề nằm ở sự giao cắt chi tiết giữa các miền này.

Thực tế, cách kiến trúc EJB xử lý việc lưu trữ bền vững, bảo mật và giao dịch đã “đi trước” lập trình hướng khía cạnh (AOP),⁷ một cách tiếp cận đa dụng nhằm khôi phục tính mô-đun cho các mối quan tâm cắt ngang.

Trong AOP, các cấu trúc mô-đun gọi là khía cạnh chỉ định những điểm trong hệ thống cần được điều chỉnh hành vi theo cách nhất quán để hỗ trợ một mối quan tâm cụ thể. Việc chỉ định này được thực hiện bằng cơ chế khai báo hoặc lập trình súc tích.

Lấy lưu trữ bền vững làm ví dụ, bạn sẽ khai báo những đối tượng và thuộc tính nào (hoặc mẫu của chúng) cần được lưu trữ, rồi giao nhiệm vụ lưu trữ cho framework lưu trữ bền vững. Framework AOP thực hiện những thay đổi hành vi đó trên mã đích mà không xâm lấn.⁸ Hãy xem ba khía cạnh hoặc cơ chế giống khía cạnh trong Java.

⁶. Hệ quản trị cơ sở dữ liệu.

⁷. Để biết thông tin tổng quát về khía cạnh, xem [AOSD]; để biết thông tin riêng về AspectJ, xem [AspectJ] và [Colyer].

## Proxy Java

Proxy Java phù hợp với các tình huống đơn giản, chẳng hạn bọc lời gọi phương thức trong từng đối tượng hoặc lớp. Tuy nhiên, các proxy động do JDK cung cấp chỉ hoạt động với giao diện. Muốn proxy lớp, bạn phải dùng thư viện thao tác bytecode như CGLIB, ASM hoặc Javassist.⁹

Đoạn mã 11-3 trình bày bộ khung proxy JDK để hỗ trợ lưu trữ bền vững cho ứng dụng `Bank`, chỉ bao gồm các phương thức lấy và thiết lập danh sách tài khoản.

**Đoạn mã 11-3**  
Ví dụ proxy JDK

```java
// Bank.java (lược bỏ tên gói...)
import java.utils.*;

// Trừu tượng hóa một ngân hàng.
public interface Bank {
  Collection<Account> getAccounts();
  void setAccounts(Collection<Account> accounts);
}
// BankImpl.java
import java.utils.*;
// “Plain Old Java Object” (POJO) triển khai phần trừu tượng.
public class BankImpl implements Bank {
  private List<Account> accounts;
    public Collection<Account> getAccounts() {
      return accounts;
    }
    public void setAccounts(Collection<Account> accounts) {
      this.accounts = new ArrayList<Account>();
      for (Account account: accounts) {
        this.accounts.add(account);
      }
    }
}

// BankProxyHandler.java
import java.lang.reflect.*;
import java.util.*;
```

**Đoạn mã 11-3 (tiếp)**  
Ví dụ proxy JDK

```java
// “InvocationHandler” bắt buộc theo API proxy.
public class BankProxyHandler implements InvocationHandler {
  private Bank bank;

    public BankHandler (Bank bank) {
      this.bank = bank;
    }

    // Phương thức được định nghĩa trong InvocationHandler
    public Object invoke(Object proxy, Method method, Object[] args)
        throws Throwable {
      String methodName = method.getName();
      if (methodName.equals("getAccounts")) {
        bank.setAccounts(getAccountsFromDatabase());
        return bank.getAccounts();
      } else if (methodName.equals("setAccounts")) {
        bank.setAccounts((Collection<Account>) args[0]);
        setAccountsToDatabase(bank.getAccounts());
        return null;
      } else {
        ...
      }
    }

    // Còn nhiều chi tiết khác:
    protected Collection<Account> getAccountsFromDatabase() { ... }
    protected void setAccountsToDatabase(Collection<Account> accounts) { ... }
}
// Ở nơi khác...

Bank bank = (Bank) Proxy.newProxyInstance(
  Bank.class.getClassLoader(),
  new Class[] { Bank.class },
  new BankProxyHandler(new BankImpl()));
```

Ta đã định nghĩa một giao diện `Bank`, sẽ được proxy bọc lại, và một Plain-Old Java Object (POJO) `BankImpl` triển khai logic nghiệp vụ. (Chúng ta sẽ quay lại POJO ngay sau đây.)

API Proxy yêu cầu một đối tượng `InvocationHandler`, đối tượng này được gọi để triển khai mọi lời gọi phương thức `Bank` thực hiện trên proxy. `BankProxyHandler` dùng API phản chiếu Java để ánh xạ các lời gọi phương thức tổng quát tới những phương thức tương ứng trong `BankImpl`, vân vân.

Có rất nhiều mã ở đây và nó tương đối phức tạp, ngay cả với trường hợp đơn giản này.¹⁰ Dùng một trong các thư viện thao tác bytecode cũng khó tương tự. Khối lượng mã và độ phức tạp là hai nhược điểm của proxy. Chúng khiến việc viết mã sạch trở nên khó khăn! Ngoài ra, proxy không cung cấp cơ chế chỉ định các “điểm” thực thi quan tâm trên toàn hệ thống, điều cần có để tạo giải pháp AOP thực sự.¹¹

⁸. Nghĩa là không cần chỉnh sửa thủ công mã nguồn đích.

⁹. Xem [CGLIB], [ASM] và [Javassist].

¹⁰. Để xem ví dụ chi tiết hơn về API Proxy và cách sử dụng, chẳng hạn xem [Goetz].

¹¹. Đôi khi người ta nhầm AOP với các kỹ thuật dùng để triển khai nó, chẳng hạn chặn phương thức và “bọc” bằng proxy. Giá trị thực sự của hệ thống AOP là khả năng chỉ định hành vi trên toàn hệ thống một cách súc tích và mô-đun.

## Framework AOP thuần Java

May mắn thay, các đoạn mã khuôn mẫu của proxy phần lớn có thể được công cụ xử lý tự động. Proxy được dùng bên trong một số framework Java, chẳng hạn Spring AOP và JBoss AOP, để triển khai khía cạnh bằng Java thuần.¹² Trong Spring, bạn viết logic nghiệp vụ dưới dạng Plain-Old Java Object. POJO chỉ tập trung vào miền của nó. Chúng không phụ thuộc vào framework doanh nghiệp (hay bất kỳ miền nào khác). Vì thế, về mặt khái niệm, chúng đơn giản hơn và dễ phát triển theo hướng kiểm thử hơn. Sự đơn giản tương đối giúp bảo đảm dễ dàng hơn rằng bạn đang triển khai đúng các câu chuyện người dùng tương ứng, đồng thời dễ bảo trì và phát triển mã để đáp ứng những câu chuyện về sau.

Bạn đưa hạ tầng ứng dụng cần thiết vào, bao gồm các mối quan tâm cắt ngang như lưu trữ bền vững, giao dịch, bảo mật, bộ nhớ đệm, chuyển đổi dự phòng, vân vân, bằng các tệp cấu hình khai báo hoặc API. Trong nhiều trường hợp, thực chất bạn đang chỉ định các khía cạnh của thư viện Spring hoặc JBoss, còn framework xử lý cơ chế sử dụng proxy Java hoặc thư viện bytecode một cách trong suốt với người dùng. Các khai báo này điều khiển bộ chứa tiêm phụ thuộc (DI), bộ chứa khởi tạo các đối tượng chính và kết nối chúng theo yêu cầu.

Đoạn mã 11-4 cho thấy một phần điển hình của tệp cấu hình Spring V2.5, `app.xml`.¹³

¹². Xem [Spring] và [JBoss]. “Java thuần” nghĩa là không dùng AspectJ.

¹³. Phỏng theo http://www.theserverside.com/tt/articles/article.tss?l=IntrotoSpring25

**Đoạn mã 11-4**  
Tệp cấu hình Spring 2.X

```xml
<beans>
  ...
  <bean id="appDataSource"
  class="org.apache.commons.dbcp.BasicDataSource"
  destroy-method="close"
  p:driverClassName="com.mysql.jdbc.Driver"
  p:url="jdbc:mysql://localhost:3306/mydb"
  p:username="me"/>
   <bean id="bankDataAccessObject"
   class="com.example.banking.persistence.BankDataAccessObject"
   p:dataSource-ref="appDataSource"/>

   <bean id="bank"
```

**Đoạn mã 11-4 (tiếp)**  
Tệp cấu hình Spring 2.X

```xml
  class="com.example.banking.model.Bank"
  p:dataAccessObject-ref="bankDataAccessObject"/>
  ...
</beans>
```

Mỗi “bean” giống như một phần của búp bê Nga lồng nhau, trong đó đối tượng miền `Bank` được một đối tượng truy cập dữ liệu (DAO) bọc (proxy), rồi chính DAO lại được một nguồn dữ liệu trình điều khiển JDBC bọc. (Xem Hình 11-3.)

**Hình 11-3**  
“Búp bê Nga” của các decorator

Phía client tưởng rằng nó đang gọi `getAccounts()` trên một đối tượng `Bank`, nhưng thực ra nó đang giao tiếp với lớp ngoài cùng trong một tập hợp các đối tượng DECORATOR¹⁴ lồng nhau, mở rộng hành vi cơ bản của POJO `Bank`. Ta có thể thêm các decorator khác cho giao dịch, bộ nhớ đệm, vân vân.

Trong ứng dụng, chỉ cần vài dòng để yêu cầu bộ chứa DI cung cấp các đối tượng cấp cao nhất của hệ thống như đã chỉ định trong tệp XML:

```java
XmlBeanFactory bf =
  new XmlBeanFactory(new ClassPathResource("app.xml", getClass()));
Bank bank = (Bank) bf.getBean("bank");
```

Vì chỉ cần rất ít dòng mã Java đặc thù của Spring, ứng dụng gần như tách biệt hoàn toàn khỏi Spring, loại bỏ mọi vấn đề phụ thuộc chặt chẽ của các hệ thống như EJB2.

Dù XML có thể dài dòng và khó đọc,¹⁵ “chính sách” được chỉ định trong những tệp cấu hình này vẫn đơn giản hơn logic proxy và khía cạnh phức tạp bị ẩn khỏi tầm mắt và được tạo tự động. Kiến trúc này hấp dẫn đến mức các framework như Spring đã dẫn tới cuộc cải tổ toàn diện tiêu chuẩn EJB ở phiên bản 3. EJB3 phần lớn đi theo mô hình Spring, hỗ trợ khai báo các mối quan tâm cắt ngang bằng tệp cấu hình XML và/hoặc chú thích Java 5.

¹⁴. [GOF].

¹⁵. Có thể đơn giản hóa ví dụ bằng các cơ chế tận dụng quy ước thay cho cấu hình và chú thích Java 5 để giảm lượng logic “kết nối” tường minh cần thiết.

Đoạn mã 11-5 cho thấy đối tượng `Bank` được viết lại bằng EJB3.¹⁶

**Đoạn mã 11-5**  
Một EJB `Bank` EJB3

```java
package com.example.banking.model;
import javax.persistence.*;
import java.util.ArrayList;
import java.util.Collection;
@Entity
@Table(name = "BANKS")
public class Bank implements java.io.Serializable {
   @Id @GeneratedValue(strategy=GenerationType.AUTO)
   private int id;

    @Embeddable // Một đối tượng được “nhúng trực tiếp” trong hàng DB của Bank
    public class Address {
       protected String streetAddr1;
       protected String streetAddr2;
       protected String city;
       protected String state;
       protected String zipCode;
    }

    @Embedded
    private Address address;

    @OneToMany(cascade = CascadeType.ALL, fetch = FetchType.EAGER,
               mappedBy="bank")
    private Collection<Account> accounts = new ArrayList<Account>();

    public int getId() {
       return id;
    }
    public void setId(int id) {
       this.id = id;
    }

    public void addAccount(Account account) {
       account.setBank(this);
       accounts.add(account);
    }

    public Collection<Account> getAccounts() {
       return accounts;
    }
```

**Đoạn mã 11-5 (tiếp)**  
Một EJB `Bank` EJB3

```java
    public void setAccounts(Collection<Account> accounts) {
       this.accounts = accounts;
    }
}
```

Mã này sạch hơn nhiều so với mã EJB2 ban đầu. Một số chi tiết thực thể vẫn còn đó, được chứa trong các chú thích. Tuy nhiên, vì không có thông tin nào nằm ngoài chú thích, mã vẫn sạch sẽ, rõ ràng và do đó dễ phát triển theo hướng kiểm thử, dễ bảo trì, vân vân.

Nếu muốn, có thể chuyển một phần hoặc toàn bộ thông tin lưu trữ bền vững trong chú thích sang bộ mô tả triển khai XML, để giữ lại một POJO thuần túy thực sự. Nếu chi tiết ánh xạ lưu trữ bền vững không thường xuyên thay đổi, nhiều nhóm có thể chọn giữ chú thích, nhưng cách này có ít nhược điểm tai hại hơn hẳn so với sự xâm lấn của EJB2.

¹⁶. Phỏng theo http://www.onjava.com/pub/a/onjava/2006/05/17/standardizing-with-ejb3-java-persistence-api.html

## Khía cạnh AspectJ

Cuối cùng, công cụ đầy đủ tính năng nhất để tách biệt mối quan tâm bằng khía cạnh là ngôn ngữ AspectJ,¹⁷ một phần mở rộng của Java hỗ trợ “hạng nhất” cho khía cạnh như cấu trúc mô-đun hóa. Các cách tiếp cận thuần Java của Spring AOP và JBoss AOP đủ dùng cho 80–90 phần trăm trường hợp khía cạnh hữu ích nhất. Tuy nhiên, AspectJ cung cấp bộ công cụ rất phong phú và mạnh mẽ để tách biệt mối quan tâm. Nhược điểm của AspectJ là phải tiếp nhận một số công cụ mới và học các cấu trúc ngôn ngữ cùng thành ngữ sử dụng mới.

Những trở ngại khi áp dụng đã phần nào được giảm nhẹ nhờ “dạng chú thích” AspectJ mới được giới thiệu gần đây, trong đó chú thích Java 5 được dùng để định nghĩa khía cạnh bằng mã Java thuần. Ngoài ra, Spring Framework có một số tính năng giúp nhóm ít kinh nghiệm với AspectJ dễ tích hợp khía cạnh dựa trên chú thích hơn.

Bàn đầy đủ về AspectJ nằm ngoài phạm vi cuốn sách này. Xem [AspectJ], [Colyer] và [Spring] để biết thêm thông tin.

¹⁷. Xem [AspectJ] và [Colyer].

## Phát triển kiến trúc hệ thống theo hướng kiểm thử

Không thể nói quá về sức mạnh của việc tách biệt mối quan tâm bằng các cách tiếp cận giống khía cạnh. Nếu bạn có thể viết logic miền của ứng dụng bằng POJO, tách khỏi mọi mối quan tâm kiến trúc ở cấp mã, thì bạn có thể thực sự phát triển kiến trúc theo hướng kiểm thử. Khi cần, bạn có thể phát triển nó từ đơn giản đến tinh vi bằng cách áp dụng công nghệ mới theo yêu cầu. Không cần thiết phải Thiết kế Lớn Ngay Từ Đầu¹⁸ (BDUF). Thực tế, BDUF còn có hại vì nó cản trở khả năng thích ứng với thay đổi, một phần do con người ngại vứt bỏ công sức đã bỏ ra, một phần do các lựa chọn kiến trúc ảnh hưởng đến suy nghĩ tiếp theo về thiết kế.

Kiến trúc sư xây dựng phải áp dụng BDUF vì không khả thi nếu thay đổi triệt để kiến trúc của một công trình vật lý lớn khi việc xây dựng đã tiến triển đáng kể.¹⁹ Dù phần mềm cũng có quy luật vật lý riêng,²⁰ việc thay đổi triệt để vẫn khả thi về mặt kinh tế nếu cấu trúc phần mềm phân tách các mối quan tâm hiệu quả.

Điều này có nghĩa ta có thể bắt đầu một dự án phần mềm với kiến trúc “đơn giản đến ngây thơ” nhưng được tách rời tốt, nhanh chóng bàn giao các câu chuyện người dùng hoạt động được, rồi bổ sung thêm hạ tầng khi mở rộng quy mô. Một số trang web lớn nhất thế giới đạt được khả năng sẵn sàng và hiệu năng rất cao nhờ bộ nhớ đệm dữ liệu, bảo mật, ảo hóa tinh vi, vân vân. Tất cả đều được thực hiện hiệu quả và linh hoạt vì các thiết kế ít phụ thuộc được giữ đơn giản phù hợp ở từng mức trừu tượng và phạm vi.

Dĩ nhiên, điều này không có nghĩa ta bước vào dự án mà “không định hướng”. Ta vẫn có những kỳ vọng về phạm vi, mục tiêu và tiến độ chung của dự án, cũng như cấu trúc tổng quát của hệ thống sẽ tạo ra. Tuy nhiên, ta phải duy trì khả năng đổi hướng để ứng phó với hoàn cảnh luôn thay đổi.

Kiến trúc EJB ban đầu chỉ là một trong nhiều API nổi tiếng được thiết kế quá mức và làm tổn hại sự phân tách mối quan tâm. Ngay cả API được thiết kế tốt cũng có thể quá mức cần thiết khi thực sự không cần đến. Phần lớn thời gian, một API tốt nên gần như biến mất khỏi tầm mắt để nhóm dành phần lớn nỗ lực sáng tạo tập trung vào các câu chuyện người dùng đang triển khai. Nếu không, các ràng buộc kiến trúc sẽ cản trở việc bàn giao giá trị tối ưu cho khách hàng một cách hiệu quả.

Tóm lại cuộc thảo luận dài này:

> Kiến trúc hệ thống tối ưu gồm các miền mối quan tâm được mô-đun hóa, mỗi miền được triển khai bằng các đối tượng Plain Old Java (hoặc ngôn ngữ khác). Các miền khác nhau được tích hợp bằng khía cạnh hoặc công cụ giống khía cạnh, ít xâm lấn nhất có thể. Kiến trúc này có thể được phát triển theo hướng kiểm thử, giống như mã.

¹⁸. Đừng nhầm với thực hành tốt là thiết kế sơ bộ. BDUF là thực hành thiết kế mọi thứ từ đầu trước khi triển khai bất cứ thứ gì.

¹⁹. Ngay cả sau khi bắt đầu xây dựng, người ta vẫn cần nhiều vòng khám phá và thảo luận chi tiết.

²⁰. Thuật ngữ “vật lý phần mềm” lần đầu được [Kolence] sử dụng.

## Tối ưu việc ra quyết định

Tính mô-đun và sự phân tách mối quan tâm giúp có thể quản lý và ra quyết định phi tập trung. Trong một hệ thống đủ lớn, dù là thành phố hay dự án phần mềm, không một người nào có thể đưa ra mọi quyết định.

Ai cũng biết tốt nhất là giao trách nhiệm cho những người đủ năng lực nhất. Ta thường quên rằng cũng tốt nhất nếu trì hoãn quyết định đến thời điểm muộn nhất có thể. Đây không phải lười biếng hay vô trách nhiệm, mà giúp ta đưa ra lựa chọn có hiểu biết dựa trên thông tin tốt nhất có thể. Một quyết định quá sớm là quyết định được đưa ra khi hiểu biết chưa tối ưu. Nếu quyết định quá sớm, ta sẽ có ít phản hồi của khách hàng hơn, ít thời gian suy ngẫm về dự án hơn và ít kinh nghiệm hơn với những lựa chọn triển khai của mình.

> Tính linh hoạt mà hệ thống POJO với các mối quan tâm được mô-đun hóa đem lại cho phép chúng ta đưa ra quyết định tối ưu, đúng lúc, dựa trên hiểu biết mới nhất. Độ phức tạp của những quyết định này cũng giảm đi.

## Dùng tiêu chuẩn một cách khôn ngoan, khi chúng đem lại giá trị rõ ràng

Xây dựng công trình là điều kỳ diệu để quan sát, vì tốc độ dựng nên những tòa nhà mới (ngay cả giữa mùa đông khắc nghiệt) và vì những thiết kế phi thường mà công nghệ ngày nay cho phép. Xây dựng là một ngành trưởng thành với các bộ phận, phương pháp và tiêu chuẩn được tối ưu hóa cao, hình thành qua áp lực suốt nhiều thế kỷ.

Nhiều nhóm đã dùng kiến trúc EJB2 chỉ vì nó là tiêu chuẩn, ngay cả khi những thiết kế nhẹ hơn và đơn giản hơn đã đủ dùng. Tôi từng thấy các nhóm bị ám ảnh bởi nhiều tiêu chuẩn được quảng bá rầm rộ và mất tập trung vào việc tạo ra giá trị cho khách hàng.

> Tiêu chuẩn giúp tái sử dụng ý tưởng và thành phần dễ dàng hơn, tuyển dụng người có kinh nghiệm phù hợp, đóng gói các ý tưởng tốt và kết nối các thành phần. Tuy nhiên, quá trình tạo ra tiêu chuẩn đôi khi mất quá nhiều thời gian để ngành công nghiệp chờ đợi, và một số tiêu chuẩn không còn đáp ứng đúng nhu cầu thực tế của những người mà chúng nhắm đến phục vụ.

## Hệ thống cần ngôn ngữ chuyên biệt cho miền

Xây dựng công trình, cũng như hầu hết các miền khác, đã phát triển một ngôn ngữ phong phú với từ vựng, thành ngữ và mẫu thiết kế²¹ truyền tải thông tin thiết yếu một cách rõ ràng, súc tích. Gần đây, người ta lại quan tâm đến việc tạo ra Ngôn ngữ chuyên biệt cho miền (Domain-Specific Language, DSL)²² trong phần mềm. Đó là những ngôn ngữ kịch bản nhỏ, tách biệt, hoặc các API trong ngôn ngữ tiêu chuẩn, cho phép viết mã dưới dạng văn xuôi có cấu trúc giống như cách chuyên gia miền có thể diễn đạt.

Một DSL tốt thu hẹp “khoảng cách giao tiếp” giữa khái niệm miền và mã triển khai khái niệm đó, cũng như các thực hành Agile tối ưu hóa giao tiếp trong nhóm và với các bên liên quan của dự án. Nếu bạn triển khai logic miền bằng cùng ngôn ngữ mà chuyên gia miền sử dụng, nguy cơ dịch sai miền sang phần triển khai sẽ thấp hơn.

Khi được sử dụng hiệu quả, DSL nâng mức trừu tượng lên cao hơn các thành ngữ mã và mẫu thiết kế. Chúng cho phép nhà phát triển thể hiện ý định của mã ở mức trừu tượng thích hợp.

> Ngôn ngữ chuyên biệt cho miền cho phép diễn đạt mọi mức trừu tượng và mọi miền trong ứng dụng dưới dạng POJO, từ chính sách cấp cao đến chi tiết cấp thấp.

²¹. Công trình của [Alexander] có ảnh hưởng đặc biệt lớn đến cộng đồng phần mềm.

²². Ví dụ, xem [DSL]. [JMock] là một ví dụ hay về API Java tạo ra DSL.

## Kết luận

Hệ thống cũng phải sạch. Một kiến trúc xâm lấn lấn át logic miền và làm suy giảm tính linh hoạt. Khi logic miền bị che khuất, chất lượng sẽ giảm vì lỗi dễ ẩn náu hơn và việc triển khai các câu chuyện người dùng trở nên khó khăn hơn. Nếu tính linh hoạt bị tổn hại, năng suất giảm và lợi ích của TDD mất đi.

Ở mọi mức trừu tượng, ý định phải rõ ràng. Điều này chỉ đạt được nếu bạn viết POJO và dùng các cơ chế giống khía cạnh để tích hợp những mối quan tâm triển khai khác mà không xâm lấn.

Dù thiết kế hệ thống hay từng mô-đun riêng lẻ, đừng bao giờ quên dùng cách đơn giản nhất có thể để giải quyết vấn đề.

## Tài liệu tham khảo

[Alexander]: Christopher Alexander, A Timeless Way of Building, Oxford University Press, New York, 1979.

[AOSD]: Aspect-Oriented Software Development port, http://aosd.net

[ASM]: ASM Home Page, http://asm.objectweb.org/

[AspectJ]: http://eclipse.org/aspectj

[CGLIB]: Code Generation Library, http://cglib.sourceforge.net/

[Colyer]: Adrian Colyer, Andy Clement, George Hurley, Mathew Webster, Eclipse AspectJ, Person Education, Inc., Upper Saddle River, NJ, 2005.

[DSL]: Ngôn ngữ lập trình chuyên biệt cho miền, http://en.wikipedia.org/wiki/Domain-specific_programming_language

[Fowler]: Inversion of Control Containers and the Dependency Injection pattern, http://martinfowler.com/articles/injection.html

[Goetz]: Brian Goetz, Java Theory and Practice: Decorating with Dynamic Proxies, http://www.ibm.com/developerworks/java/library/j-jtp08305.html

[Javassist]: Javassist Home Page, http://www.csg.is.titech.ac.jp/~chiba/javassist/

[JBoss]: JBoss Home Page, http://jboss.org

[JMock]: JMock, thư viện đối tượng giả nhẹ cho Java, http://jmock.org

[Kolence]: Kenneth W. Kolence, Software physics and computer performance measurements, Proceedings of the ACM annual conference, Volume 2, Boston, Massachusetts, pp. 1024–1040, 1972.

[Spring]: The Spring Framework, http://www.springframework.org

[Mezzaros07]: XUnit Patterns, Gerard Mezzaros, Addison-Wesley, 2007.

[GOF]: Design Patterns: Elements of Reusable Object Oriented Software, Gamma et al., Addison-Wesley, 1996.
