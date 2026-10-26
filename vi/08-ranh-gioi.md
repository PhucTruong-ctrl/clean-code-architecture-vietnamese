# Chương 8: Ranh giới

> Tác giả: James Grenning

Chúng ta hiếm khi kiểm soát được toàn bộ phần mềm trong hệ thống của mình. Đôi khi ta mua các gói phần mềm của bên thứ ba hoặc dùng phần mềm mã nguồn mở. Những lúc khác, ta phụ thuộc vào các nhóm trong chính công ty mình để tạo ra những thành phần hoặc hệ thống con. Bằng cách nào đó, ta phải tích hợp sạch sẽ đoạn mã xa lạ này với phần mềm của mình. Trong chương này, chúng ta sẽ xem xét các cách làm và kỹ thuật giúp giữ cho ranh giới của phần mềm luôn sạch.

## Dùng mã của bên thứ ba

Giữa bên cung cấp giao diện và bên sử dụng giao diện luôn có một sự căng thẳng tự nhiên. Nhà cung cấp các gói phần mềm và framework của bên thứ ba muốn sản phẩm có phạm vi ứng dụng rộng để chạy được trong nhiều môi trường và thu hút đông đảo người dùng. Ngược lại, người dùng muốn một giao diện tập trung vào nhu cầu riêng của mình. Sự căng thẳng này có thể gây ra vấn đề ở ranh giới hệ thống.

Hãy lấy `java.util.Map` làm ví dụ. Như bạn thấy khi xem Hình 8-1, `Map` có giao diện rất rộng với nhiều khả năng. Sức mạnh và tính linh hoạt đó chắc chắn hữu ích, nhưng cũng có thể trở thành gánh nặng. Chẳng hạn, ứng dụng của ta có thể tạo một `Map` rồi truyền nó đi khắp nơi. Ta có thể muốn không bên nhận nào xóa thứ gì trong `Map`. Nhưng ngay đầu danh sách đã có phương thức `clear()`. Bất kỳ ai dùng `Map` cũng có thể xóa sạch nó. Hoặc có thể quy ước thiết kế của ta chỉ cho phép lưu một số kiểu đối tượng nhất định trong `Map`, nhưng `Map` không giới hạn đáng tin cậy kiểu đối tượng được đặt vào đó. Người dùng nào quyết tâm cũng có thể thêm phần tử thuộc bất kỳ kiểu nào vào bất kỳ `Map` nào.

- `clear() void – Map`
- `containsKey(Object key) boolean – Map`
- `containsValue(Object value) boolean – Map`
- `entrySet() Set – Map`
- `equals(Object o) boolean – Map`
- `get(Object key) Object – Map`
- `getClass() Class<? extends Object> – Object`
- `hashCode() int – Map`
- `isEmpty() boolean – Map`
- `keySet() Set – Map`
- `notify() void – Object`
- `notifyAll() void – Object`
- `put(Object key, Object value) Object – Map`
- `putAll(Map t) void – Map`
- `remove(Object key) Object – Map`
- `size() int – Map`
- `toString() String – Object`
- `values() Collection – Map`
- `wait() void – Object`
- `wait(long timeout) void – Object`
- `wait(long timeout, int nanos) void – Object`

**Hình 8-1**  
Các phương thức của `Map`

Nếu ứng dụng cần một `Map` chứa `Sensor`, bạn có thể thấy các cảm biến được thiết lập như sau:

```java
Map sensors = new HashMap();
```

Sau đó, khi một phần khác của mã cần truy cập cảm biến, ta thấy đoạn mã này:

```java
Sensor s = (Sensor)sensors.get(sensorId );
```

Ta không chỉ thấy cách làm này một lần, mà lặp đi lặp lại khắp nơi trong mã. Phía gọi đoạn mã phải chịu trách nhiệm lấy một `Object` từ `Map` rồi ép kiểu sang kiểu phù hợp. Cách này chạy được, nhưng không phải mã sạch. Nó cũng chưa kể câu chuyện rõ ràng như có thể. Có thể cải thiện đáng kể khả năng đọc của đoạn mã bằng cách dùng kiểu tổng quát, như dưới đây:

```java
Map<Sensor> sensors = new HashMap<Sensor>();
...
Sensor s = sensors.get(sensorId );
```

Tuy nhiên, cách này không giải quyết được vấn đề `Map<Sensor>` cung cấp nhiều khả năng hơn điều ta cần hoặc muốn.

Truyền thoải mái một đối tượng `Map<Sensor>` khắp hệ thống đồng nghĩa với việc sẽ có nhiều nơi cần sửa nếu giao diện của `Map` thay đổi. Bạn có thể nghĩ thay đổi như vậy khó xảy ra, nhưng hãy nhớ rằng giao diện này đã thay đổi khi Java 5 bổ sung hỗ trợ kiểu tổng quát. Thật vậy, chúng tôi từng thấy những hệ thống không thể dùng kiểu tổng quát vì khối lượng thay đổi khổng lồ cần thiết để khắc phục việc dùng `Map` tràn lan.

Cách dùng `Map` sạch hơn có thể như sau. Người dùng `Sensors` sẽ chẳng bận tâm có dùng kiểu tổng quát hay không. Lựa chọn đó đã trở thành, và vốn dĩ luôn nên là, chi tiết triển khai.

```java
public class Sensors {
  private Map sensors = new HashMap();

    public Sensor getById(String id) {
      return (Sensor) sensors.get(id);
    }

    // lược bớt
}
```

Giao diện ở ranh giới (`Map`) được che giấu. Nó có thể phát triển mà hầu như không ảnh hưởng đến phần còn lại của ứng dụng. Việc dùng kiểu tổng quát không còn là vấn đề lớn, vì lớp `Sensors` xử lý việc ép kiểu và quản lý kiểu.

Giao diện này cũng được điều chỉnh và giới hạn để đáp ứng nhu cầu của ứng dụng. Nhờ đó, mã dễ hiểu hơn và khó bị dùng sai hơn. Lớp `Sensors` có thể thực thi các quy tắc thiết kế và nghiệp vụ.

Chúng tôi không khuyên bạn đóng gói mọi lần dùng `Map` theo cách này. Thay vào đó, chúng tôi khuyên bạn đừng truyền `Map` (hay bất kỳ giao diện ranh giới nào khác) khắp hệ thống. Nếu dùng một giao diện ranh giới như `Map`, hãy giữ nó bên trong lớp, hoặc một nhóm lớp liên quan gần gũi, nơi nó được sử dụng. Tránh trả nó về từ API công khai hoặc nhận nó làm đối số.

## Khám phá và tìm hiểu ranh giới

Mã của bên thứ ba giúp chúng ta bổ sung nhiều chức năng hơn trong thời gian ngắn hơn. Ta nên bắt đầu từ đâu khi muốn dùng một gói phần mềm của bên thứ ba? Kiểm thử mã của bên thứ ba không phải việc của ta, nhưng viết kiểm thử cho đoạn mã bên thứ ba mà ta sử dụng có thể mang lại lợi ích cho chính ta.

Giả sử ta chưa rõ cách dùng thư viện của bên thứ ba. Ta có thể dành một hoặc hai ngày, thậm chí lâu hơn, để đọc tài liệu và quyết định cách sử dụng. Sau đó, ta có thể viết mã dùng thư viện ấy rồi xem nó có hoạt động như mình nghĩ không. Hẳn ta sẽ không ngạc nhiên nếu bị sa lầy vào những phiên gỡ lỗi kéo dài, cố tìm hiểu xem lỗi mình gặp nằm trong mã của ta hay của họ.

Tìm hiểu mã của bên thứ ba rất khó. Tích hợp mã đó cũng khó. Làm cả hai việc cùng lúc khó gấp đôi. Nếu thử một cách tiếp cận khác thì sao? Thay vì thử nghiệm trong mã sản phẩm, ta có thể viết một số kiểm thử để khám phá xem mình hiểu mã của bên thứ ba đến đâu. Jim Newkirk gọi những kiểm thử như vậy là kiểm thử tìm hiểu.¹

¹ [BeckTDD], tr. 136–137.

Trong các kiểm thử tìm hiểu, ta gọi API của bên thứ ba theo cách dự định sử dụng trong ứng dụng. Về bản chất, ta đang làm các thí nghiệm có kiểm soát để kiểm tra hiểu biết của mình về API đó. Các kiểm thử tập trung vào những gì ta cần từ API.

## Tìm hiểu log4j

Giả sử ta muốn dùng gói `apache log4j` thay cho trình ghi nhật ký tự xây dựng. Ta tải nó về và mở trang tài liệu giới thiệu. Chỉ đọc sơ qua, ta viết ca kiểm thử đầu tiên, mong nó ghi chữ “hello” ra bảng điều khiển.

```java
@Test
public void testLogCreate() {
  Logger logger = Logger.getLogger("MyLogger");
  logger.info("hello");
}
```

Khi chạy, trình ghi nhật ký báo lỗi cho biết ta cần một thứ gọi là `Appender`. Đọc thêm một chút, ta tìm thấy `ConsoleAppender`. Vậy là ta tạo một `ConsoleAppender` để xem mình đã khám phá được bí quyết ghi ra bảng điều khiển chưa.

```java
@Test
public void testLogAddAppender() {
  Logger logger = Logger.getLogger("MyLogger");
  ConsoleAppender appender = new ConsoleAppender();
  logger.addAppender(appender);
  logger.info("hello");
}
```

Lần này ta phát hiện `Appender` không có luồng xuất. Lạ thật, cứ tưởng nó phải có chứ. Tìm trên Google một chút, ta thử đoạn sau:

```java
@Test
public void testLogAddAppender() {
  Logger logger = Logger.getLogger("MyLogger");
  logger.removeAllAppenders();
  logger.addAppender(new ConsoleAppender(
       new PatternLayout("%p %t %m%n"),
       ConsoleAppender.SYSTEM_OUT));
  logger.info("hello");
}
```

Cách này có tác dụng. Một thông báo ghi nhật ký có chữ “hello” xuất hiện trên bảng điều khiển! Thật kỳ lạ khi ta phải nói rõ với `ConsoleAppender` rằng nó ghi ra bảng điều khiển.

Điều thú vị là khi bỏ đối số `ConsoleAppender.SystemOut`, ta vẫn thấy “hello” được in ra. Nhưng nếu bỏ `PatternLayout`, nó lại phàn nàn không có luồng xuất. Hành vi này thật kỳ quặc.

Xem tài liệu kỹ hơn, ta thấy hàm khởi tạo mặc định của `ConsoleAppender` ở trạng thái “chưa cấu hình”, điều này chẳng rõ ràng hay hữu ích chút nào. Cảm giác như đây là một lỗi, hoặc ít nhất là sự thiếu nhất quán trong `log4j`.

Tìm kiếm, đọc và kiểm thử thêm một chút, cuối cùng ta có được Đoạn mã 8-1. Ta đã khám phá ra khá nhiều về cách `log4j` hoạt động, đồng thời mã hóa hiểu biết đó thành một tập hợp kiểm thử đơn vị đơn giản.

**Đoạn mã 8-1**  
**LogTest.java**

```java
public class LogTest {
    private Logger logger;

     @Before
     public void initialize() {
         logger = Logger.getLogger("logger");
         logger.removeAllAppenders();
         Logger.getRootLogger().removeAllAppenders();
     }
     @Test
     public void basicLogger() {
         BasicConfigurator.configure();
         logger.info("basicLogger");
     }

     @Test
     public void addAppenderWithStream() {
      logger.addAppender(new ConsoleAppender(
           new PatternLayout("%p %t %m%n"),
           ConsoleAppender.SYSTEM_OUT));
         logger.info("addAppenderWithStream");
     }
```

**Đoạn mã 8-1 (tiếp theo)**  
**LogTest.java**

```java
     @Test
     public void addAppenderWithoutStream() {
      logger.addAppender(new ConsoleAppender(
           new PatternLayout("%p %t %m%n")));
         logger.info("addAppenderWithoutStream");
     }
}
```

Giờ ta đã biết cách khởi tạo một trình ghi nhật ký đơn giản ra bảng điều khiển. Ta có thể đóng gói hiểu biết ấy vào lớp ghi nhật ký của riêng mình, để phần còn lại của ứng dụng được cách ly khỏi giao diện ranh giới `log4j`.

## Kiểm thử tìm hiểu có lợi hơn miễn phí

Rốt cuộc, các kiểm thử tìm hiểu chẳng tốn gì. Dù sao ta cũng phải tìm hiểu API, và viết những kiểm thử đó là cách dễ dàng, tách biệt để tích lũy hiểu biết. Đó là những thí nghiệm chính xác giúp ta hiểu rõ hơn.

Kiểm thử tìm hiểu không chỉ miễn phí mà còn đem lại lợi ích. Khi gói phần mềm bên thứ ba có phiên bản mới, ta chạy lại các kiểm thử để xem có khác biệt về hành vi không.

Kiểm thử tìm hiểu xác minh rằng các gói phần mềm của bên thứ ba mà ta dùng hoạt động đúng như mong đợi. Sau khi tích hợp, không có gì bảo đảm mã của bên thứ ba sẽ luôn tương thích với nhu cầu của ta. Các tác giả ban đầu sẽ chịu áp lực phải thay đổi mã để đáp ứng nhu cầu mới của chính họ. Họ sẽ sửa lỗi và bổ sung khả năng mới. Mỗi phiên bản phát hành đều mang theo rủi ro mới. Nếu gói phần mềm thay đổi theo cách không tương thích với các kiểm thử của ta, ta sẽ phát hiện ngay.

Dù có cần phần hiểu biết mà kiểm thử tìm hiểu mang lại hay không, một ranh giới sạch vẫn cần được hỗ trợ bởi một tập hợp kiểm thử hướng ra ngoài, thực thi giao diện theo đúng cách mã sản phẩm sử dụng. Không có những kiểm thử ranh giới này để giúp việc chuyển đổi dễ dàng, ta có thể bị cám dỗ ở lại với phiên bản cũ lâu hơn mức nên làm.

## Dùng mã chưa tồn tại

Có một kiểu ranh giới khác, ngăn cách điều đã biết với điều chưa biết. Trong mã thường có những chỗ mà kiến thức của ta dường như đột ngột chấm dứt. Đôi khi ta không thể biết được điều gì nằm bên kia ranh giới, ít nhất là vào lúc này. Đôi khi ta chọn không tìm hiểu xa hơn ranh giới.

Nhiều năm trước, tôi tham gia một nhóm phát triển phần mềm cho hệ thống liên lạc vô tuyến. Có một hệ thống con gọi là “Transmitter” mà chúng tôi biết rất ít, còn những người phụ trách hệ thống ấy chưa xác định được giao diện của nó. Chúng tôi không muốn bị chặn lại, nên bắt đầu công việc ở xa phần mã chưa biết đó.

Chúng tôi khá hiểu rõ thế giới của mình kết thúc ở đâu và thế giới mới bắt đầu từ đâu. Trong lúc làm việc, đôi khi chúng tôi chạm đến ranh giới ấy. Sương mù và mây mù của sự thiếu hiểu biết che khuất tầm nhìn về phía bên kia, nhưng công việc giúp chúng tôi nhận ra mình muốn giao diện ranh giới có dạng nào. Chúng tôi muốn có thể nói với bộ phát như sau:

> Bật bộ phát ở tần số đã cung cấp và phát ra tín hiệu tương tự biểu diễn dữ liệu đến từ luồng này.

Chúng tôi không biết phải thực hiện việc đó thế nào vì API vẫn chưa được thiết kế. Vì vậy, chúng tôi quyết định sẽ xử lý chi tiết sau.

Để không bị chặn lại, chúng tôi tự định nghĩa giao diện của mình. Chúng tôi đặt cho nó một cái tên nghe bắt tai, chẳng hạn `Transmitter`. Chúng tôi tạo một phương thức tên `transmit`, nhận tần số và luồng dữ liệu. Đó là giao diện mà chúng tôi mong mình có.

Một điều hay khi viết giao diện mình mong muốn là ta kiểm soát được nó. Nhờ vậy, mã phía gọi dễ đọc hơn và tập trung hơn vào điều nó đang cố thực hiện.

Trong Hình 8-2, bạn có thể thấy chúng tôi đã cách ly các lớp `CommunicationsController` khỏi API của bộ phát, vốn nằm ngoài quyền kiểm soát và chưa được định nghĩa. Dùng một giao diện đặc thù cho ứng dụng do mình tạo ra, chúng tôi giữ cho mã `CommunicationsController` sạch sẽ và giàu tính biểu đạt. Khi API của bộ phát được định nghĩa, chúng tôi viết `TransmitterAdapter` để bắc cầu khoảng cách. `ADAPTER`² đóng gói việc tương tác với API và cung cấp một nơi duy nhất cần thay đổi khi API phát triển.

**Hình 8-2**  
Dự đoán giao diện bộ phát

Thiết kế này còn tạo cho ta một điểm nối³ rất thuận tiện trong mã để kiểm thử. Dùng một `FakeTransmitter` phù hợp, ta có thể kiểm thử các lớp `CommunicationsController`. Ta cũng có thể viết kiểm thử ranh giới sau khi có `TransmitterAPI` để bảo đảm ta dùng API đúng cách.

² Xem mẫu Adapter trong [GOF].

³ Xem thêm về điểm nối trong [WELC].

## Ranh giới sạch

Những điều thú vị xảy ra ở ranh giới. Thay đổi là một trong số đó. Thiết kế phần mềm tốt thích ứng với thay đổi mà không đòi hỏi đầu tư khổng lồ và làm lại nhiều. Khi dùng mã nằm ngoài quyền kiểm soát, ta phải đặc biệt cẩn trọng để bảo vệ khoản đầu tư của mình và bảo đảm việc thay đổi sau này không quá tốn kém.

Mã ở ranh giới cần được tách biệt rõ ràng và có các kiểm thử xác định kỳ vọng. Ta nên tránh để quá nhiều mã của mình biết đến những chi tiết riêng của bên thứ ba. Tốt hơn hết là phụ thuộc vào thứ mình kiểm soát thay vì thứ mình không kiểm soát, kẻo cuối cùng nó lại kiểm soát ta.

Ta quản lý ranh giới với bên thứ ba bằng cách chỉ để thật ít chỗ trong mã tham chiếu đến chúng. Ta có thể bọc chúng như đã làm với `Map`, hoặc dùng một `ADAPTER` để chuyển đổi từ giao diện hoàn hảo của mình sang giao diện được cung cấp. Dù chọn cách nào, mã của ta cũng diễn đạt rõ hơn, khuyến khích cách dùng nhất quán bên trong khi qua ranh giới, và có ít điểm cần bảo trì hơn khi mã của bên thứ ba thay đổi.

## Tài liệu tham khảo

[BeckTDD]: Test Driven Development, Kent Beck, Addison-Wesley, 2003.

[GOF]: Design Patterns: Elements of Reusable Object Oriented Software, Gamma et al., Addison-Wesley, 1996.

[WELC]: Working Effectively with Legacy Code, Addison-Wesley, 2004.
