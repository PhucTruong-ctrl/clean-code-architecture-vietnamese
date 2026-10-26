# Chương 6: Đối tượng và cấu trúc dữ liệu

Có lý do để chúng ta giữ các biến của mình ở chế độ riêng tư. Chúng ta không muốn ai khác phụ thuộc vào chúng. Chúng ta muốn giữ quyền tự do thay đổi kiểu hay cách hiện thực của chúng theo ý thích hoặc theo một phút bốc đồng. Vậy tại sao nhiều lập trình viên vẫn tự động thêm getter và setter cho đối tượng của mình, phơi bày các biến riêng tư như thể chúng là công khai?

## Trừu tượng hóa dữ liệu

Hãy xét khác biệt giữa Đoạn mã 6-1 và Đoạn mã 6-2. Cả hai đều biểu diễn dữ liệu của một điểm trên mặt phẳng Descartes. Vậy mà một cái phơi bày cách hiện thực, cái còn lại che giấu hoàn toàn.

**Đoạn mã 6-1**
**Điểm cụ thể**

```java
public class Point {
  public double x;
  public double y;
}
```

**Đoạn mã 6-2**
**Điểm trừu tượng**

```java
public interface Point {
  double getX();
  double getY();
  void setCartesian(double x, double y);
  double getR();
  double getTheta();
  void setPolar(double r, double theta);
}
```

Điều tuyệt vời ở Đoạn mã 6-2 là bạn không thể nào biết được cách hiện thực dùng tọa độ vuông góc hay tọa độ cực. Có khi nó chẳng dùng cái nào cả! Vậy mà giao diện vẫn biểu diễn một cấu trúc dữ liệu không thể nhầm lẫn.

Nhưng nó biểu diễn nhiều hơn một cấu trúc dữ liệu. Các phương thức áp đặt một chính sách truy cập. Bạn có thể đọc từng tọa độ riêng lẻ, nhưng phải đặt các tọa độ cùng nhau như một thao tác nguyên tử.

Ngược lại, Đoạn mã 6-1 hiện thực rất rõ ràng bằng tọa độ vuông góc, và nó buộc chúng ta thao tác trên từng tọa độ một cách độc lập. Như thế là phơi bày cách hiện thực. Thật vậy, nó vẫn phơi bày cách hiện thực ngay cả khi các biến là riêng tư và chúng ta dùng getter, setter cho từng biến.

Che giấu cách hiện thực không chỉ là đặt một lớp hàm giữa các biến. Che giấu cách hiện thực là chuyện trừu tượng hóa! Một lớp không đơn thuần đẩy các biến của mình ra ngoài qua getter và setter. Nó phơi bày những giao diện trừu tượng cho phép người dùng thao tác trên bản chất của dữ liệu mà không cần biết cách hiện thực.

Hãy xét Đoạn mã 6-3 và Đoạn mã 6-4. Cái đầu dùng những thuật ngữ cụ thể để truyền đạt mức nhiên liệu của một xe, còn cái sau dùng trừu tượng phần trăm. Trong trường hợp cụ thể, bạn có thể khá chắc rằng đây chỉ là các accessor của biến. Trong trường hợp trừu tượng, bạn không có manh mối nào về hình thái của dữ liệu.

**Đoạn mã 6-3**
**Xe cụ thể**

```java
public interface Vehicle {
  double getFuelTankCapacityInGallons();
  double getGallonsOfGasoline();
}
```

**Đoạn mã 6-4**
**Xe trừu tượng**

```java
public interface Vehicle {
  double getPercentFuelRemaining();
}
```

Trong cả hai trường hợp trên, lựa chọn thứ hai đáng mong muốn hơn. Chúng ta không muốn phơi bày chi tiết dữ liệu của mình. Chúng ta muốn diễn đạt dữ liệu bằng những thuật ngữ trừu tượng. Điều này không chỉ đạt được bằng cách dùng giao diện và/hoặc getter, setter. Cần suy nghĩ nghiêm túc về cách tốt nhất để biểu diễn dữ liệu mà một đối tượng chứa. Lựa chọn tồi nhất là thản nhiên thêm getter và setter.

## Đối tượng và cấu trúc dữ liệu: tính phản đối xứng

Hai ví dụ này cho thấy khác biệt giữa đối tượng và cấu trúc dữ liệu. Đối tượng che giấu dữ liệu của mình sau các lớp trừu tượng và phơi bày những hàm thao tác trên dữ liệu đó. Cấu trúc dữ liệu phơi bày dữ liệu và không có hàm nào có ý nghĩa. Hãy quay lại đọc lần nữa. Hãy để ý tính bổ sung cho nhau của hai định nghĩa. Chúng gần như đối lập hoàn toàn. Khác biệt này có vẻ nhỏ nhặt, nhưng hệ quả của nó rất xa.

Hãy xét ví dụ về hình học theo lối thủ tục trong Đoạn mã 6-5. Lớp Geometry thao tác trên ba lớp hình. Các lớp hình là những cấu trúc dữ liệu đơn giản, không có hành vi nào. Toàn bộ hành vi nằm trong lớp Geometry.

**Đoạn mã 6-5**
**Hình học theo lối thủ tục**

```java
public class Square {
  public Point topLeft;
  public double side;
}
public class Rectangle {
  public Point topLeft;
  public double height;
  public double width;
}

public class Circle {
  public Point center;
  public double radius;
}

public class Geometry {
  public final double PI = 3.141592653589793;

  public double area(Object shape) throws NoSuchShapeException
  {
    if (shape instanceof Square) {
      Square s = (Square)shape;
      return s.side * s.side;
    }
    else if (shape instanceof Rectangle) {
      Rectangle r = (Rectangle)shape;
      return r.height * r.width;
    }
    else if (shape instanceof Circle) {
      Circle c = (Circle)shape;
      return PI * c.radius * c.radius;
    }
    throw new NoSuchShapeException();
  }
}
```

Những lập trình viên hướng đối tượng có thể sẽ nhăn mặt và phàn nàn rằng đây là lối thủ tục, và họ đúng. Nhưng cái nhếch mép đó có khi không có cơ sở. Hãy xét điều gì sẽ xảy ra nếu thêm một hàm perimeter() vào Geometry. Các lớp hình sẽ không bị ảnh hưởng gì! Mọi lớp khác phụ thuộc vào các hình cũng không bị ảnh hưởng! Mặt khác, nếu tôi thêm một hình mới, tôi phải sửa mọi hàm trong Geometry để xử lý nó. Lại đọc lại điều đó đi. Hãy để ý hai tình huống này đối lập nhau hoàn toàn.

Giờ hãy xét giải pháp hướng đối tượng trong Đoạn mã 6-6. Ở đây phương thức area() là đa hình. Không cần lớp Geometry. Vậy nếu tôi thêm một hình mới, không hàm hiện có nào bị ảnh hưởng, nhưng nếu tôi thêm một hàm mới thì mọi hình đều phải thay đổi![^1]

**Đoạn mã 6-6**
**Các hình đa hình**

```java
public class Square implements Shape {
  private Point topLeft;
  private double side;
  public double area() {
    return side*side;
  }
}
public class Rectangle implements Shape {
  private Point topLeft;
  private double height;
  private double width;
  public double area() {
    return height * width;
  }
}
```

**Đoạn mã 6-6 (tiếp theo)**
**Các hình đa hình**

```java
public class Circle implements Shape {
  private Point center;
  private double radius;
  public final double PI = 3.141592653589793;
  public double area() {
    return PI * radius * radius;
  }
}
```

Lại một lần nữa, ta thấy tính bổ sung của hai định nghĩa này; chúng gần như đối lập hoàn toàn! Điều này phơi bày sự phân đôi nền tảng giữa đối tượng và cấu trúc dữ liệu:

> Mã thủ tục (mã dùng cấu trúc dữ liệu) giúp dễ thêm hàm mới mà không phải thay đổi các cấu trúc dữ liệu hiện có. Ngược lại, mã OO giúp dễ thêm lớp mới mà không phải thay đổi các hàm hiện có.

Điều ngược lại cũng đúng:

> Mã thủ tục khiến việc thêm cấu trúc dữ liệu mới trở nên khó, vì mọi hàm đều phải thay đổi. Mã OO khiến việc thêm hàm mới trở nên khó, vì mọi lớp đều phải thay đổi.

Vậy những gì khó với OO thì dễ với lối thủ tục, và những gì khó với lối thủ tục thì dễ với OO!

Trong bất kỳ hệ thống phức tạp nào cũng sẽ có lúc ta muốn thêm kiểu dữ liệu mới thay vì hàm mới. Với những trường hợp đó, đối tượng và OO là thích hợp nhất. Mặt khác, cũng sẽ có lúc ta muốn thêm hàm mới thay vì kiểu dữ liệu. Khi đó mã thủ tục và cấu trúc dữ liệu sẽ thích hợp hơn.

Những lập trình viên trưởng thành biết rằng ý tưởng mọi thứ đều là đối tượng chỉ là chuyện hoang đường. Đôi khi bạn thật sự muốn những cấu trúc dữ liệu đơn giản với các thủ tục thao tác trên chúng.

## Định luật Demeter

Có một nguyên tắc kinh nghiệm nổi tiếng gọi là Định luật Demeter[^2], nói rằng một module không nên biết về bên trong của những đối tượng mà nó thao tác. Như ta thấy ở mục trước, đối tượng che giấu dữ liệu và phơi bày các thao tác. Điều này có nghĩa là một đối tượng không nên phơi bày cấu trúc bên trong của mình qua accessor, vì làm thế là phơi bày chứ không phải che giấu cấu trúc bên trong của nó.

Chính xác hơn, Định luật Demeter nói rằng một phương thức f của lớp C chỉ nên gọi các phương thức của những thứ sau:

- C
- Một đối tượng được f tạo ra
- Một đối tượng được truyền làm đối số cho f
- Một đối tượng được giữ trong biến thực thể (instance variable) của C

Phương thức không nên gọi phương thức trên những đối tượng được trả về bởi bất kỳ hàm nào trong số các hàm được phép. Nói cách khác, hãy nói chuyện với bạn bè, không nói chuyện với người lạ.

Đoạn mã sau[^3] có vẻ vi phạm Định luật Demeter (cùng với vài thứ khác) vì nó gọi hàm getScratchDir() trên giá trị trả về của getOptions(), rồi gọi getAbsolutePath() trên giá trị trả về của getScratchDir().

```java
final String outputDir = ctxt.getOptions().getScratchDir().getAbsolutePath();
```

### Tàu hỏa trật bánh

Kiểu mã này thường được gọi là tàu hỏa trật bánh vì nó trông như một đống toa tàu móc nối vào nhau. Những chuỗi gọi như thế thường bị coi là phong cách cẩu thả và nên tránh [G36]. Thường tốt nhất là tách chúng ra như sau:

```java
Options opts = ctxt.getOptions();
File scratchDir = opts.getScratchDir();
final String outputDir = scratchDir.getAbsolutePath();
```

Hai đoạn mã này có vi phạm Định luật Demeter không? Chắc chắn module chứa chúng biết rằng đối tượng ctxt chứa options, options chứa một thư mục tạm (scratch directory), và thư mục đó có một đường dẫn tuyệt đối. Đó là khối lượng kiến thức quá lớn cho một hàm. Hàm gọi biết cách đi xuyên qua rất nhiều đối tượng khác nhau.

Việc này có vi phạm Demeter hay không phụ thuộc vào việc ctxt, Options và ScratchDir là đối tượng hay cấu trúc dữ liệu. Nếu chúng là đối tượng thì cấu trúc bên trong của chúng phải được che giấu chứ không phơi bày, nên việc biết về bên trong của chúng là vi phạm rõ ràng Định luật Demeter. Ngược lại, nếu ctxt, Options và ScratchDir chỉ là cấu trúc dữ liệu không có hành vi, thì đương nhiên chúng phơi bày cấu trúc bên trong, và Demeter không áp dụng.

Việc dùng các hàm accessor làm vấn đề rối lên. Nếu đoạn mã được viết như sau, có lẽ chúng ta đã không đặt câu hỏi về vi phạm Demeter.

```java
final String outputDir = ctxt.options.scratchDir.absolutePath;
```

Vấn đề này sẽ bớt rối hơn nhiều nếu cấu trúc dữ liệu chỉ đơn giản có biến công khai và không có hàm, còn đối tượng có biến riêng tư và hàm công khai. Tuy nhiên, có những framework và chuẩn (ví dụ "beans") đòi hỏi ngay cả cấu trúc dữ liệu đơn giản cũng phải có accessor và mutator.

### Cấu trúc lai

Sự nhầm lẫn này đôi khi dẫn đến những cấu trúc lai đáng tiếc, nửa đối tượng nửa cấu trúc dữ liệu. Chúng có những hàm làm việc có ý nghĩa, đồng thời có hoặc biến công khai, hoặc accessor và mutator công khai mà trên thực tế biến các biến riêng tư thành công khai, dụ các hàm bên ngoài khác dùng những biến đó theo cách một chương trình thủ tục dùng cấu trúc dữ liệu.[^4]

Những cấu trúc lai như vậy khiến việc thêm hàm mới khó, mà thêm cấu trúc dữ liệu mới cũng khó. Chúng là cái tệ nhất của cả hai thế giới. Hãy tránh tạo ra chúng. Chúng cho thấy một thiết kế lộn xộn mà tác giả không chắc, hoặc tệ hơn là không biết, mình cần được bảo vệ khỏi hàm hay khỏi kiểu.

### Che giấu cấu trúc

Nếu ctxt, options và scratchDir là những đối tượng có hành vi thật thì sao? Khi đó, vì đối tượng phải che giấu cấu trúc bên trong, chúng ta không nên có khả năng đi xuyên qua chúng. Vậy làm sao lấy được đường dẫn tuyệt đối của thư mục tạm?

```java
ctxt.getAbsolutePathOfScratchDirectoryOption();
```

hoặc

```java
ctx.getScratchDirectoryOption().getAbsolutePath()
```

Lựa chọn đầu có thể dẫn đến bùng nổ phương thức trong đối tượng ctxt. Lựa chọn thứ hai giả định rằng getScratchDirectoryOption() trả về một cấu trúc dữ liệu, không phải một đối tượng. Cả hai lựa chọn đều không ổn.

Nếu ctxt là một đối tượng, ta nên bảo nó làm điều gì đó; không nên hỏi nó về bên trong của nó. Vậy tại sao ta lại muốn đường dẫn tuyệt đối của thư mục tạm? Ta định làm gì với nó? Hãy xét đoạn mã này, nằm (cách đó nhiều dòng) trong cùng module:

```java
String outFile = outputDir + "/" + className.replace('.', '/') + ".class";
FileOutputStream fout = new FileOutputStream(outFile);
BufferedOutputStream bos = new BufferedOutputStream(fout);
```

Việc trộn lẫn các mức chi tiết khác nhau [G34][G6] hơi đáng lo. Dấu chấm, dấu gạch chéo, phần mở rộng tệp và đối tượng File không nên bị trộn với nhau một cách cẩu thả như vậy, rồi trộn luôn vào đoạn mã bao quanh. Bỏ qua điều đó, ta thấy ý định của việc lấy đường dẫn tuyệt đối của thư mục tạm là tạo một tệp tạm với tên cho trước.

Vậy nếu ta bảo đối tượng ctxt làm việc này thì sao?

```java
BufferedOutputStream bos = ctxt.createScratchFileStream(classFileName);
```

Đó có vẻ là việc hợp lý để một đối tượng làm! Cách này cho phép ctxt che giấu bên trong và ngăn hàm hiện tại phải vi phạm Định luật Demeter bằng cách đi xuyên qua những đối tượng mà nó không nên biết.

## Đối tượng truyền dữ liệu

Hình thái tiêu biểu nhất của cấu trúc dữ liệu là một lớp có biến công khai và không có hàm. Đôi khi người ta gọi nó là đối tượng truyền dữ liệu, hay DTO. DTO là cấu trúc rất hữu ích, nhất là khi giao tiếp với cơ sở dữ liệu hoặc phân tích thông điệp từ socket, v.v. Chúng thường trở thành chặng đầu tiên trong chuỗi các chặng chuyển đổi, biến dữ liệu thô trong cơ sở dữ liệu thành đối tượng trong mã ứng dụng.

Phổ biến hơn một chút là dạng "bean" trong Đoạn mã 6-7. Bean có các biến riêng tư được điều khiển qua getter và setter. Kiểu đóng gói nửa vời của bean có vẻ làm một số người theo chủ nghĩa OO thuần túy thấy dễ chịu hơn, nhưng thường không mang lại lợi ích nào khác.

**Đoạn mã 6-7**
**address.java**

```java
public class Address {
  private String street;
  private String streetExtra;
  private String city;
  private String state;
  private String zip;

  public Address(String street, String streetExtra,
                  String city, String state, String zip) {
    this.street = street;
    this.streetExtra = streetExtra;
    this.city = city;
    this.state = state;
    this.zip = zip;
  }
  public String getStreet() {
    return street;
  }

  public String getStreetExtra() {
    return streetExtra;
  }
  public String getCity() {
    return city;
  }
  public String getState() {
    return state;
  }

  public String getZip() {
    return zip;
  }
}
```

### Active Record

Active Record là dạng đặc biệt của DTO. Chúng là cấu trúc dữ liệu với biến công khai (hoặc truy cập qua bean); nhưng chúng thường có các phương thức điều hướng như save và find. Thông thường, Active Record là bản dịch trực tiếp từ bảng cơ sở dữ liệu hoặc nguồn dữ liệu khác.

Đáng tiếc là ta thường thấy các nhà phát triển cố đối xử với những cấu trúc dữ liệu này như thể chúng là đối tượng, bằng cách đặt các phương thức quy tắc nghiệp vụ vào trong chúng. Điều này gượng gạo vì nó tạo ra một cấu trúc lai giữa cấu trúc dữ liệu và đối tượng.

Tất nhiên, giải pháp là đối xử với Active Record như một cấu trúc dữ liệu, và tạo những đối tượng riêng chứa các quy tắc nghiệp vụ, che giấu dữ liệu bên trong của chúng (mà có lẽ chỉ là các thực thể của Active Record).

## Kết luận

Đối tượng phơi bày hành vi và che giấu dữ liệu. Điều này giúp dễ thêm những loại đối tượng mới mà không phải thay đổi hành vi hiện có. Nó cũng khiến việc thêm hành vi mới vào các đối tượng hiện có trở nên khó. Cấu trúc dữ liệu phơi bày dữ liệu và không có hành vi đáng kể. Điều này giúp dễ thêm hành vi mới vào các cấu trúc dữ liệu hiện có, nhưng khiến việc thêm cấu trúc dữ liệu mới vào các hàm hiện có trở nên khó.

Trong bất kỳ hệ thống nào, có lúc ta muốn sự linh hoạt để thêm kiểu dữ liệu mới, nên ở phần đó của hệ thống ta thích đối tượng hơn. Có lúc khác ta muốn sự linh hoạt để thêm hành vi mới, nên ở phần đó ta thích kiểu dữ liệu và thủ tục hơn. Những nhà phát triển phần mềm giỏi hiểu những vấn đề này mà không thành kiến và chọn cách tiếp cận tốt nhất cho công việc trước mắt.

[^1]: Có những cách lách điều này mà các nhà thiết kế hướng đối tượng giàu kinh nghiệm đều biết: VISITOR, hay dual-dispatch, chẳng hạn. Nhưng những kỹ thuật này có cái giá riêng và thường đưa cấu trúc trở lại thành một chương trình thủ tục.

[^2]: http://en.wikipedia.org/wiki/Law_of_Demeter

[^3]: Tìm thấy đâu đó trong framework apache.

[^4]: Đôi khi người ta gọi đây là Feature Envy, theo \[Refactoring\].

## Tài liệu tham khảo

\[Refactoring\]: Refactoring: Improving the Design of Existing Code, Martin Fowler et al., Addison-Wesley, 1999.
