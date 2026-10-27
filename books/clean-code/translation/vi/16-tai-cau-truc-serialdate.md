# Chương 16: Tái cấu trúc SerialDate

Nếu bạn truy cập http://www.jfree.org/jcommon/index.php, bạn sẽ tìm thấy thư viện JCommon. Sâu bên trong thư viện đó có một gói tên là org.jfree.date. Trong gói này có một lớp tên là SerialDate. Chúng ta sẽ cùng tìm hiểu lớp đó.

Tác giả của SerialDate là David Gilbert. David rõ ràng là một lập trình viên giàu kinh nghiệm và có năng lực. Như ta sẽ thấy, mã của ông thể hiện tính chuyên nghiệp và kỷ luật đáng kể. Xét trên mọi phương diện, đây là “mã tốt”. Vậy mà tôi sắp mổ xẻ nó.

Đây không phải hành động ác ý. Tôi cũng không cho rằng mình giỏi hơn David đến mức có quyền phán xét mã của ông. Thật vậy, nếu bạn tìm thấy một đoạn mã nào đó của tôi, chắc chắn bạn cũng sẽ tìm ra khối điều đáng chê.

Không, đây không phải hành động xấu tính hay ngạo mạn. Điều tôi sắp làm chỉ đơn thuần là một cuộc review chuyên nghiệp. Đây là việc tất cả chúng ta nên thấy thoải mái khi thực hiện, và cũng nên đón nhận khi người khác làm với mình. Chỉ qua những lời phê bình như thế này chúng ta mới học được. Bác sĩ làm vậy. Phi công làm vậy. Luật sư làm vậy. Và lập trình viên chúng ta cũng cần học cách làm như thế.

Còn một điều nữa về David Gilbert: David không chỉ là một lập trình viên giỏi. David có đủ can đảm và thiện chí để tặng mã của mình miễn phí cho cộng đồng rộng lớn. Ông công khai mã để mọi người cùng xem, mời mọi người sử dụng và đánh giá. Ông đã làm rất tốt!

SerialDate (Đoạn mã B-1, trang 349) là một lớp biểu diễn ngày tháng trong Java. Tại sao lại cần lớp biểu diễn ngày tháng khi Java đã có java.util.Date, java.util.Calendar và những lớp khác? Tác giả viết lớp này vì một vấn đề mà chính tôi cũng thường gặp. Chú thích trong Javadoc mở đầu của ông (dòng 67) giải thích rất rõ. Ta có thể tranh luận về ý định của ông, nhưng bản thân tôi chắc chắn từng phải xử lý vấn đề này và hoan nghênh một lớp chuyên về ngày tháng thay vì thời gian.

## Trước hết, làm cho nó hoạt động

Có một số kiểm thử đơn vị trong lớp tên SerialDateTests (Đoạn mã B-2, trang 366). Tất cả đều chạy qua. Đáng tiếc, xem nhanh các kiểm thử cho thấy chúng không kiểm thử mọi thứ [T1]. Chẳng hạn, tìm kiếm “Find Usages” với phương thức MonthCodeToQuarter (dòng 334) cho thấy phương thức này không được dùng [F4]. Vì vậy, kiểm thử đơn vị không kiểm thử nó.

Tôi khởi chạy Clover để xem kiểm thử đơn vị bao phủ những gì và bỏ sót những gì. Clover báo rằng kiểm thử đơn vị chỉ thực thi 91 trong số 185 câu lệnh có thể thực thi trong SerialDate, khoảng 50 phần trăm [T2]. Bản đồ độ bao phủ trông như một tấm chăn chắp vá, với những mảng mã lớn chưa được thực thi rải khắp lớp.

Mục tiêu của tôi là hiểu hoàn toàn lớp này, đồng thời tái cấu trúc nó. Tôi không thể làm vậy nếu không tăng đáng kể độ bao phủ kiểm thử. Vì thế, tôi viết bộ kiểm thử đơn vị hoàn toàn độc lập của riêng mình (Đoạn mã B-4, trang 374).

Khi xem các kiểm thử này, bạn sẽ nhận thấy nhiều kiểm thử đã bị chú thích. Chúng không chạy qua. Chúng thể hiện hành vi mà tôi nghĩ SerialDate nên có. Vì vậy, khi tái cấu trúc SerialDate, tôi cũng sẽ tìm cách làm cho các kiểm thử này chạy qua.

Ngay cả khi một số kiểm thử vẫn bị chú thích, Clover báo rằng bộ kiểm thử đơn vị mới thực thi 170 trong số 185 câu lệnh có thể thực thi, đạt 92 phần trăm. Kết quả này khá tốt, và tôi nghĩ chúng ta còn có thể nâng con số đó lên nữa.

Một vài kiểm thử đầu tiên bị chú thích (dòng 23-63) phần nào là do tôi tự phụ. Chương trình không được thiết kế để chạy qua các kiểm thử này, nhưng với tôi, hành vi đó có vẻ hiển nhiên [G2]. Tôi không rõ tại sao phương thức testWeekdayCodeToString lại được viết ngay từ đầu, nhưng vì nó đã tồn tại nên rõ ràng nó không nên phân biệt chữ hoa chữ thường. Viết các kiểm thử này rất đơn giản [T3]. Làm cho chúng chạy qua còn dễ hơn: tôi chỉ sửa dòng 259 và 263 để dùng equalsIgnoreCase.

Tôi để các kiểm thử ở dòng 32 và dòng 45 dưới dạng chú thích vì tôi không chắc có nên hỗ trợ các dạng viết tắt “tues” và “thurs” hay không.

Các kiểm thử ở dòng 153 và dòng 154 không chạy qua. Rõ ràng chúng phải chạy qua [G2]. Ta có thể dễ dàng sửa chúng, cùng với các kiểm thử từ dòng 163 đến dòng 213, bằng cách thay đổi hàm stringToMonthCode như sau.

```java
      457          if ((result < 1) || (result > 12)) {
                       result = -1;
      458              for (int i = 0; i < monthNames.length; i++) {
      459                  if (s.equalsIgnoreCase(shortMonthNames[i])) {
      460                      result = i + 1;
      461                      break;
      462                  }
      463                  if (s.equalsIgnoreCase(monthNames[i])) {
      464                      result = i + 1;
      465                      break;
      466                  }
      467              }
      468          }
```

Kiểm thử bị chú thích ở dòng 318 làm lộ ra lỗi trong phương thức getFollowingDayOfWeek (dòng 672). Ngày 25 tháng 12 năm 2004 là thứ Bảy. Thứ Bảy tiếp theo là ngày 1 tháng 1 năm 2005. Thế nhưng khi chạy kiểm thử, ta thấy getFollowingDayOfWeek trả về ngày 25 tháng 12 như thể đó là thứ Bảy tiếp theo sau ngày 25 tháng 12. Rõ ràng điều này sai [G3],[T1]. Vấn đề nằm ở dòng 685. Đây là lỗi điều kiện biên điển hình [T5]. Dòng đó phải là:

```java
      685          if (baseDOW >= targetWeekday) {
```

Điều đáng chú ý là hàm này từng được sửa trước đó. Lịch sử thay đổi (dòng 43) cho thấy các “lỗi” đã được sửa trong getPreviousDayOfWeek, getFollowingDayOfWeek và getNearestDayOfWeek [T6].

Kiểm thử đơn vị testGetNearestDayOfWeek (dòng 329), kiểm thử phương thức getNearestDayOfWeek (dòng 705), ban đầu không dài và đầy đủ như bây giờ. Tôi đã thêm nhiều ca kiểm thử vì các ca ban đầu không phải tất cả đều chạy qua [T6]. Bạn có thể nhận ra kiểu lỗi bằng cách xem những ca kiểm thử nào bị chú thích. Kiểu đó cho ta biết nhiều điều [T7]. Nó cho thấy thuật toán thất bại nếu ngày gần nhất nằm trong tương lai. Rõ ràng có một dạng lỗi điều kiện biên nào đó [T5].

Kiểu độ bao phủ kiểm thử mà Clover báo cáo cũng đáng chú ý [T8]. Dòng 719 không bao giờ được thực thi! Điều đó có nghĩa câu lệnh if ở dòng 718 luôn sai. Quả đúng như vậy, xem mã thì thấy điều này là tất yếu. Biến adjust luôn âm, nên không thể lớn hơn hoặc bằng 4. Vậy thuật toán này đơn giản là sai.

Thuật toán đúng như sau:

```java
               int delta = targetDOW - base.getDayOfWeek();
               int positiveDelta = delta + 7;
               int adjust = positiveDelta % 7;
               if (adjust > 3)
                 adjust -= 7;
               return SerialDate.addDays(adjust, base);
```

Cuối cùng, có thể làm cho các kiểm thử ở dòng 417 và dòng 429 chạy qua chỉ bằng cách ném IllegalArgumentException thay vì trả về chuỗi lỗi từ weekInMonthToString và relativeToString.

Với những thay đổi này, tất cả kiểm thử đơn vị đều chạy qua, và tôi tin SerialDate hiện đã hoạt động. Vậy giờ là lúc làm cho nó “đúng đắn”.

## Sau đó, làm cho nó đúng đắn

Chúng ta sẽ đi từ đầu đến cuối SerialDate, cải thiện nó trên đường đi. Dù bạn không thấy điều này trong phần thảo luận, sau mỗi thay đổi tôi đều chạy toàn bộ kiểm thử đơn vị của JCommon, bao gồm cả kiểm thử đơn vị SerialDate đã cải tiến. Vì vậy, bạn có thể yên tâm rằng mọi thay đổi trình bày ở đây đều hoạt động với toàn bộ JCommon.

Bắt đầu từ dòng 1, ta thấy một loạt chú thích về giấy phép, bản quyền, tác giả và lịch sử thay đổi. Tôi thừa nhận có những vấn đề pháp lý cần giải quyết, nên thông tin bản quyền và giấy phép phải được giữ lại. Mặt khác, lịch sử thay đổi là tàn dư từ thập niên 1960. Giờ đây chúng ta có các công cụ quản lý mã nguồn để làm việc đó. Nên xóa lịch sử này [C1].

Có thể rút gọn danh sách import bắt đầu ở dòng 61 bằng cách dùng java.text.* và java.util.*. [J1]

Tôi nhăn mặt trước cách định dạng HTML trong Javadoc (dòng 67). Tôi không thích một tệp mã nguồn chứa nhiều hơn một ngôn ngữ. Chú thích này có bốn ngôn ngữ: Java, tiếng Anh, Javadoc và HTML [G1]. Dùng nhiều ngôn ngữ như vậy khiến việc giữ mọi thứ ngăn nắp trở nên khó khăn. Chẳng hạn, cách căn chỉnh đẹp ở dòng 71 và dòng 72 bị mất khi tạo Javadoc, nhưng ai lại muốn thấy <ul> và <li> trong mã nguồn? Một cách tốt hơn có thể là đặt toàn bộ chú thích bên trong <pre> để giữ nguyên định dạng thể hiện trong mã nguồn khi hiển thị trong Javadoc.[^1]

Dòng 86 là khai báo lớp. Tại sao lớp này tên là SerialDate? Từ “serial” có ý nghĩa gì? Có phải vì lớp này được kế thừa từ Serializable không? Có vẻ không phải.

[^1]: Một giải pháp còn tốt hơn là để Javadoc trình bày mọi chú thích dưới dạng văn bản định dạng sẵn, để chú thích hiển thị giống nhau trong mã nguồn và tài liệu.

Tôi sẽ không để bạn phải đoán. Tôi biết lý do (hoặc ít nhất tôi nghĩ mình biết lý do) dùng từ “serial”. Manh mối nằm ở các hằng SERIAL_LOWER_BOUND và SERIAL_UPPER_BOUND tại dòng 98 và dòng 101. Manh mối rõ hơn nữa nằm trong chú thích bắt đầu ở dòng 830. Lớp này tên SerialDate vì nó được triển khai bằng một “số sê-ri”, tức số ngày tính từ ngày 30 tháng 12 năm 1899.

Tôi có hai vấn đề với cách gọi này. Thứ nhất, thuật ngữ “số sê-ri” không thực sự chính xác. Có thể đây chỉ là chuyện bắt bẻ, nhưng cách biểu diễn này giống độ lệch tương đối hơn là số sê-ri. “Số sê-ri” thường liên quan đến mã nhận diện sản phẩm hơn là ngày tháng. Vì thế, tôi không thấy tên này mô tả rõ ràng [N1]. Một từ mô tả phù hợp hơn có thể là “ordinal”.

Vấn đề thứ hai đáng kể hơn. Tên SerialDate hàm ý một cách triển khai. Đây là lớp trừu tượng. Không cần hàm ý gì về cách triển khai cả. Thật ra, có lý do chính đáng để che giấu cách triển khai! Vì vậy, tôi cho rằng tên này không đúng mức trừu tượng [N2]. Theo tôi, tên lớp này đơn giản nên là Date.

Đáng tiếc là trong thư viện Java đã có quá nhiều lớp tên Date, nên có lẽ đây không phải lựa chọn tốt nhất. Vì lớp này nói về ngày, chứ không phải thời gian, tôi cân nhắc đặt tên Day, nhưng tên đó cũng được dùng nhiều ở nơi khác. Cuối cùng, tôi chọn DayDate làm phương án dung hòa tốt nhất.

Từ giờ trở đi trong phần thảo luận này, tôi sẽ dùng tên DayDate. Bạn cần nhớ rằng các đoạn mã đang xem vẫn dùng tên SerialDate.

Tôi hiểu vì sao DayDate kế thừa Comparable và Serializable. Nhưng tại sao nó lại kế thừa MonthConstants? Lớp MonthConstants (Đoạn mã B-3, trang 372) chỉ là một nhóm các hằng static final xác định các tháng. Kế thừa lớp chứa hằng là một mẹo cũ mà lập trình viên Java dùng để khỏi phải viết những biểu thức như MonthConstants.January, nhưng đó là ý tưởng tồi [J2]. MonthConstants thực sự nên là một enum.

```java
    public abstract class DayDate implements Comparable,
                                             Serializable {
      public static enum Month {
        JANUARY(1),
        FEBRUARY(2),
        MARCH(3),
        APRIL(4),
        MAY(5),
        JUNE(6),
        JULY(7),
        AUGUST(8),
        SEPTEMBER(9),
        OCTOBER(10),
        NOVEMBER(11),
        DECEMBER(12);

         Month(int index) {
           this.index = index;
         }

             public static Month make(int monthIndex) {
               for (Month m : Month.values()) {
                 if (m.index == monthIndex)
                   return m;
               }
               throw new IllegalArgumentException("Invalid month index " + monthIndex);
             }
             public final int index;
         }
```

Đổi MonthConstants thành enum này buộc phải sửa khá nhiều chỗ trong lớp DayDate và mọi nơi dùng nó. Tôi mất một giờ để hoàn tất. Tuy nhiên, giờ đây mọi hàm trước kia nhận số nguyên chỉ tháng đều nhận một giá trị Month. Điều đó giúp ta bỏ được phương thức isValidMonthCode (dòng 326) và mọi thao tác kiểm tra mã tháng như trong monthCodeToQuarter (dòng 356) [G5].

Tiếp theo là serialVersionUID ở dòng 91. Biến này dùng để kiểm soát việc tuần tự hóa. Nếu ta thay đổi nó, mọi DayDate được ghi bằng phiên bản phần mềm cũ sẽ không còn đọc được và gây ra InvalidClassException. Nếu không khai báo biến serialVersionUID, trình biên dịch sẽ tự động tạo một giá trị, và giá trị đó sẽ khác mỗi lần bạn thay đổi mô-đun. Tôi biết mọi tài liệu đều khuyên nên tự kiểm soát biến này, nhưng theo tôi, tự động kiểm soát việc tuần tự hóa an toàn hơn nhiều [G4]. Dù sao, tôi thà gỡ lỗi InvalidClassException còn hơn gặp hành vi kỳ quặc xảy ra nếu quên đổi serialVersionUID. Vì vậy, tôi sẽ xóa biến này, ít nhất là lúc này.[^2]

Tôi thấy chú thích ở dòng 93 thừa. Chú thích thừa chỉ là nơi tích tụ lời dối trá và thông tin sai lệch [C2]. Vì thế, tôi sẽ xóa nó cùng những chú thích tương tự.

Các chú thích ở dòng 97 và dòng 100 nói về số sê-ri, vấn đề tôi vừa bàn ở trên [C1]. Những biến này mô tả ngày sớm nhất và muộn nhất mà DayDate có thể biểu diễn. Ta có thể làm rõ hơn một chút [N1].

```java
         public static final int EARLIEST_DATE_ORDINAL = 2;     // 1/1/1900
         public static final int LATEST_DATE_ORDINAL = 2958465; // 12/31/9999
```

[^2]: Một số người phản biện văn bản này không đồng tình với quyết định đó. Họ cho rằng trong một framework mã nguồn mở, tốt hơn hết là tự kiểm soát ID tuần tự để những thay đổi nhỏ trong phần mềm không làm ngày tháng đã tuần tự hóa từ trước mất hiệu lực. Đây là ý kiến xác đáng. Tuy nhiên, ít nhất thì dù bất tiện, lỗi này có nguyên nhân rõ ràng. Ngược lại, nếu tác giả lớp quên cập nhật ID, kiểu lỗi sẽ không xác định và có thể hoàn toàn im lặng. Theo tôi, bài học thực sự là không nên kỳ vọng giải tuần tự hóa dữ liệu giữa các phiên bản.

Tôi không rõ vì sao EARLIEST_DATE_ORDINAL là 2 chứ không phải 0. Chú thích ở dòng 829 hé lộ rằng chuyện này có liên quan đến cách Microsoft Excel biểu diễn ngày tháng. Có thêm một giải thích sâu hơn trong lớp dẫn xuất DayDate tên SpreadsheetDate (Đoạn mã B-5, trang 382). Chú thích ở dòng 71 mô tả vấn đề rất rõ.

Vấn đề của tôi là chuyện này dường như liên quan đến cách triển khai SpreadsheetDate, không liên quan gì đến DayDate. Tôi kết luận rằng EARLIEST_DATE_ORDINAL và LATEST_DATE_ORDINAL thực sự không thuộc về DayDate, mà nên được chuyển sang SpreadsheetDate [G6].

Quả thật, tìm trong mã cho thấy những biến này chỉ được dùng bên trong SpreadsheetDate. Không có gì trong DayDate hay bất kỳ lớp nào khác của framework JCommon dùng chúng. Vì vậy, tôi sẽ chuyển chúng xuống SpreadsheetDate.

Các biến tiếp theo, MINIMUM_YEAR_SUPPORTED và MAXIMUM_YEAR_SUPPORTED (dòng 104 và dòng 107), đặt ra một tình thế khó xử. Nếu DayDate là lớp trừu tượng không hé lộ gì về cách triển khai, thì rõ ràng lớp này không nên cho biết năm tối thiểu hay tối đa. Một lần nữa, tôi muốn chuyển các biến này xuống SpreadsheetDate [G6]. Tuy nhiên, tìm nhanh nơi sử dụng cho thấy còn một lớp khác dùng chúng: RelativeDayOfWeekRule (Đoạn mã B-6, trang 390). Ta thấy cách sử dụng ở dòng 177 và dòng 178 trong hàm getDate, nơi chúng được dùng để kiểm tra năm truyền vào getDate có hợp lệ hay không. Tình thế khó xử ở đây là một lớp sử dụng lớp trừu tượng lại cần biết thông tin về cách triển khai của lớp đó.

Ta cần cung cấp thông tin này mà không làm ô nhiễm chính DayDate. Thông thường, ta sẽ lấy thông tin về cách triển khai từ một thực thể của lớp dẫn xuất. Nhưng hàm getDate không nhận một thực thể DayDate làm đối số. Tuy vậy, nó trả về một thực thể như thế, nghĩa là ở đâu đó nó phải tạo thực thể ấy. Các dòng từ 187 đến 205 gợi ý câu trả lời. Thực thể DayDate được tạo bởi một trong ba hàm getPreviousDayOfWeek, getNearestDayOfWeek hoặc getFollowingDayOfWeek. Nhìn lại đoạn mã DayDate, ta thấy các hàm này (dòng 638–724) đều trả về một ngày được tạo bởi addDays (dòng 571), hàm này gọi createInstance (dòng 808), và hàm đó tạo SpreadsheetDate! [G7]

Thông thường, lớp cơ sở không nên biết về các lớp dẫn xuất của nó. Để khắc phục điều này, ta nên dùng mẫu ABSTRACT FACTORY[^3] và tạo DayDateFactory. Factory này sẽ tạo các thực thể DayDate cần thiết, đồng thời có thể trả lời những câu hỏi về cách triển khai, chẳng hạn ngày tối đa và tối thiểu.

```java
    public abstract class DayDateFactory {
      private static DayDateFactory factory = new SpreadsheetDateFactory();
      public static void setInstance(DayDateFactory factory) {
        DayDateFactory.factory = factory;
      }

       protected abstract DayDate _makeDate(int ordinal);
       protected abstract DayDate _makeDate(int day, DayDate.Month month, int year);
       protected abstract DayDate _makeDate(int day, int month, int year);
       protected abstract DayDate _makeDate(java.util.Date date);
       protected abstract int _getMinimumYear();
       protected abstract int _getMaximumYear();

       public static DayDate makeDate(int ordinal) {
         return factory._makeDate(ordinal);
       }

           public static DayDate makeDate(int day, DayDate.Month month, int year) {
             return factory._makeDate(day, month, year);
           }

           public static DayDate makeDate(int day, int month, int year) {
             return factory._makeDate(day, month, year);
           }
           public static DayDate makeDate(java.util.Date date) {
             return factory._makeDate(date);
           }

           public static int getMinimumYear() {
             return factory._getMinimumYear();
           }

           public static int getMaximumYear() {
             return factory._getMaximumYear();
           }
      }
```

[^3]: [GOF].

Lớp factory này thay các phương thức createInstance bằng phương thức makeDate, cải thiện tên gọi đáng kể [N1]. Mặc định nó dùng SpreadsheetDateFactory, nhưng có thể đổi sang factory khác bất cứ lúc nào. Các phương thức static ủy quyền cho phương thức trừu tượng sử dụng kết hợp các mẫu SINGLETON,[^4] DECORATOR,[^5] và ABSTRACT FACTORY mà tôi thấy hữu ích.

SpreadsheetDateFactory trông như sau.

```java
      public class SpreadsheetDateFactory extends DayDateFactory {
        public DayDate _makeDate(int ordinal) {
          return new SpreadsheetDate(ordinal);
        }
           public DayDate _makeDate(int day, DayDate.Month month, int year) {
             return new SpreadsheetDate(day, month, year);
           }
           public DayDate _makeDate(int day, int month, int year) {
             return new SpreadsheetDate(day, month, year);
           }

           public DayDate _makeDate(Date date) {
             final GregorianCalendar calendar = new GregorianCalendar();
             calendar.setTime(date);
             return new SpreadsheetDate(
               calendar.get(Calendar.DATE),
               DayDate.Month.make(calendar.get(Calendar.MONTH) + 1),
               calendar.get(Calendar.YEAR));
           }

        protected int _getMinimumYear() {
          return SpreadsheetDate.MINIMUM_YEAR_SUPPORTED;
        }

        protected int _getMaximumYear() {
          return SpreadsheetDate.MAXIMUM_YEAR_SUPPORTED;
        }
    }
```

[^4]: Như trên.
[^5]: Như trên.

Như bạn thấy, tôi đã chuyển các biến MINIMUM_YEAR_SUPPORTED và MAXIMUM_YEAR_SUPPORTED vào SpreadsheetDate, nơi chúng thuộc về [G6].

Vấn đề tiếp theo trong DayDate là các hằng ngày bắt đầu từ dòng 109. Thực ra, chúng nên là một enum khác [J3]. Ta đã thấy kiểu này trước đây, nên tôi sẽ không nhắc lại. Bạn sẽ thấy nó trong các đoạn mã cuối.

Tiếp theo là một loạt bảng, bắt đầu với LAST_DAY_OF_MONTH ở dòng 140. Vấn đề đầu tiên của tôi với các bảng này là những chú thích mô tả chúng bị thừa [C3]. Tên đã đủ rõ. Vì vậy, tôi sẽ xóa các chú thích.

Không có lý do chính đáng nào để bảng này không phải private [G8], vì đã có hàm static lastDayOfMonth cung cấp cùng dữ liệu.

Bảng tiếp theo, AGGREGATE_DAYS_TO_END_OF_MONTH, khó hiểu hơn một chút vì không được dùng ở đâu trong framework JCommon [G9]. Vì vậy, tôi đã xóa nó.

LEAP_YEAR_AGGREGATE_DAYS_TO_END_OF_MONTH cũng vậy.

Bảng tiếp theo, AGGREGATE_DAYS_TO_END_OF_PRECEDING_MONTH, chỉ được dùng trong SpreadsheetDate (dòng 434 và dòng 473). Điều này đặt ra câu hỏi liệu có nên chuyển nó sang SpreadsheetDate hay không. Lý do không chuyển là bảng này không đặc thù cho một cách triển khai nào [G6]. Mặt khác, ngoài SpreadsheetDate ra thì chẳng có cách triển khai nào khác tồn tại, nên cần chuyển bảng đến gần nơi sử dụng nó hơn [G10].

Điều khiến tôi quyết định là để nhất quán [G11], ta nên đặt bảng thành private và cung cấp nó qua một hàm như julianDateOfLastDayOfMonth. Dường như không ai cần hàm như vậy. Hơn nữa, nếu một cách triển khai DayDate mới cần đến bảng này, ta có thể dễ dàng chuyển nó trở lại DayDate. Vì vậy, tôi đã chuyển nó đi.

Bảng LEAP_YEAR_AGGREGATE_DAYS_TO_END_OF_MONTH cũng tương tự.

Tiếp theo, ta thấy ba nhóm hằng có thể chuyển thành enum (dòng 162–205). Nhóm đầu tiên chọn một tuần trong tháng. Tôi đổi nó thành enum tên WeekInMonth.

```java
    public enum WeekInMonth {
        FIRST(1), SECOND(2), THIRD(3), FOURTH(4), LAST(0);
        public final int index;

            WeekInMonth(int index) {
              this.index = index;
            }
        }
```

Nhóm hằng thứ hai (dòng 177–187) khó hiểu hơn một chút. Các hằng INCLUDE_NONE, INCLUDE_FIRST, INCLUDE_SECOND và INCLUDE_BOTH dùng để mô tả các ngày ở hai đầu mút xác định một phạm vi có được tính vào phạm vi đó hay không. Trong toán học, người ta mô tả điều này bằng các thuật ngữ “khoảng mở”, “khoảng nửa mở” và “khoảng đóng”. Tôi nghĩ dùng thuật ngữ toán học sẽ rõ hơn [N3], nên đổi chúng thành enum tên DateInterval với các giá trị CLOSED, CLOSED_LEFT, CLOSED_RIGHT và OPEN.

Nhóm hằng thứ ba (dòng 18–205) mô tả việc tìm một ngày trong tuần cụ thể sẽ trả về lần xuất hiện trước, sau hay gần nhất. Tìm tên phù hợp thật không dễ. Cuối cùng, tôi chọn WeekdayRange với các giá trị LAST, NEXT và NEAREST.

Có thể bạn không đồng ý với những tên tôi chọn. Chúng hợp lý với tôi, nhưng có thể không hợp với bạn. Điểm quan trọng là giờ đây chúng ở dạng dễ thay đổi [J3]. Chúng không còn được truyền dưới dạng số nguyên mà là các ký hiệu. Tôi có thể dùng chức năng “change name” trong IDE để đổi tên hoặc kiểu mà không lo bỏ sót một số -1 hay 2 nào đó trong mã, hoặc để lại khai báo đối số int được mô tả kém.

Trường description ở dòng 208 dường như không ai dùng. Tôi đã xóa nó cùng phương thức truy cập và thay đổi [G9].

Tôi cũng xóa hàm khởi tạo mặc định rỗng ở dòng 213 [G12]. Trình biên dịch sẽ tạo nó giúp ta.

Có thể bỏ qua phương thức isValidWeekdayCode (dòng 216–238) vì ta đã xóa nó khi tạo enum Day.

Tiếp theo là phương thức stringToWeekdayCode (dòng 242–270). Javadoc không bổ sung gì nhiều cho chữ ký phương thức chỉ làm mã thêm rối [C3],[G12]. Giá trị duy nhất Javadoc này cung cấp là mô tả giá trị trả về -1. Tuy nhiên, vì ta đã chuyển sang enum Day, chú thích đó thực ra sai [C2]. Giờ phương thức ném IllegalArgumentException. Vì vậy, tôi đã xóa Javadoc.

Tôi cũng xóa mọi từ khóa final trong đối số và khai báo biến. Theo những gì tôi thấy, chúng không đem lại giá trị thực sự nào mà chỉ làm mã rối hơn [G12]. Bỏ final đi ngược một số quan niệm thông thường. Chẳng hạn, Robert Simmons[^6] khuyên chúng ta mạnh mẽ rằng “. . . hãy rải final khắp mã nguồn.” Rõ ràng tôi không đồng ý. Tôi nghĩ final có một vài cách dùng tốt, chẳng hạn đôi khi dùng cho hằng, nhưng ngoài ra từ khóa này ít giá trị và làm mã rối đáng kể. Có lẽ tôi nghĩ vậy vì những lỗi mà final có thể bắt được vốn đã được các kiểm thử đơn vị tôi viết phát hiện.

Tôi không thích các câu lệnh if trùng lặp [G5] bên trong vòng lặp for (dòng 259 và dòng 263), nên nối chúng thành một câu lệnh if duy nhất bằng toán tử ||. Tôi cũng dùng enum Day để điều khiển vòng lặp for và thực hiện thêm một số thay đổi nhỏ khác.

Tôi nhận ra phương thức này thực sự không thuộc về DayDate. Nó đúng ra là hàm parse của Day. Vì vậy, tôi chuyển nó vào enum Day. Tuy nhiên, enum Day trở nên khá lớn. Vì khái niệm Day không phụ thuộc vào DayDate, tôi chuyển enum Day ra khỏi lớp DayDate, sang tệp mã nguồn riêng [G13].

[^6]: [Simmons04], trang 73.

Tôi cũng chuyển hàm tiếp theo, weekdayCodeToString (dòng 272–286), vào enum Day và gọi nó là toString.

```java
    public enum Day {
      MONDAY(Calendar.MONDAY),
      TUESDAY(Calendar.TUESDAY),
      WEDNESDAY(Calendar.WEDNESDAY),s
      THURSDAY(Calendar.THURSDAY),
      FRIDAY(Calendar.FRIDAY),
      SATURDAY(Calendar.SATURDAY),
      SUNDAY(Calendar.SUNDAY);

        public final int index;
        private static DateFormatSymbols dateSymbols = new DateFormatSymbols();

        Day(int day) {
          index = day;
        }

        public static Day make(int index) throws IllegalArgumentException {
          for (Day d : Day.values())
            if (d.index == index)
              return d;
          throw new IllegalArgumentException(
            String.format("Illegal day index: %d.", index));
        }

        public static Day parse(String s) throws IllegalArgumentException {
          String[] shortWeekdayNames =
            dateSymbols.getShortWeekdays();
          String[] weekDayNames =
            dateSymbols.getWeekdays();
            s = s.trim();
            for (Day day : Day.values()) {
              if (s.equalsIgnoreCase(shortWeekdayNames[day.index]) ||
                  s.equalsIgnoreCase(weekDayNames[day.index])) {
                return day;
              }
            }
            throw new IllegalArgumentException(
              String.format("%s is not a valid weekday string", s));
        }
        public String toString() {
          return dateSymbols.getWeekdays()[index];
        }
    }
```

Có hai hàm getMonths (dòng 288–316). Hàm đầu gọi hàm thứ hai. Không ai gọi hàm thứ hai ngoài hàm đầu. Vì vậy, tôi gộp hai hàm thành một và đơn giản hóa đáng kể [G9],[G12],[F4]. Cuối cùng, tôi đổi tên cho tự mô tả hơn [N1].

```java
        public static String[] getMonthNames() {
          return dateFormatSymbols.getMonths();
        }
```

Hàm isValidMonthCode (dòng 326–346) trở nên không cần thiết vì enum Month, nên tôi xóa nó [G9].

Hàm monthCodeToQuarter có mùi FEATURE ENVY[^7] [G14] và có lẽ thuộc về enum Month dưới dạng phương thức tên quarter. Vì vậy, tôi thay nó bằng phương thức này.

```java
            public int quarter() {
              return 1 + (index-1)/3;
            }
```

Enum Month giờ đủ lớn để nằm trong lớp riêng. Vì nhất quán với enum Day, tôi chuyển nó ra khỏi DayDate [G11],[G13].

Hai phương thức tiếp theo tên là monthCodeToString (dòng 377–426). Một lần nữa, ta thấy kiểu một phương thức gọi phương thức song sinh bằng một cờ. Truyền cờ làm đối số cho hàm thường là ý tưởng tồi, nhất là khi cờ đó chỉ chọn định dạng đầu ra [G15]. Tôi đổi tên, đơn giản hóa, sắp xếp lại các hàm này và chuyển chúng vào enum Month [N1],[N3],[C3],[G14].

[^7]: [Refactoring].

```java
        public String toString() {
          return dateFormatSymbols.getMonths()[index - 1];
        }

        public String toShortString() {
          return dateFormatSymbols.getShortMonths()[index - 1];
        }
```

Phương thức tiếp theo là stringToMonthCode (dòng 428–472). Tôi đổi tên, chuyển nó vào enum Month và đơn giản hóa [N1],[N3],[C3],[G14],[G12].

```java
        public static Month parse(String s) {
          s = s.trim();
          for (Month m : Month.values())
            if (m.matches(s))
              return m;

            try {
              return make(Integer.parseInt(s));
            }
            catch (NumberFormatException e) {}
            throw new IllegalArgumentException("Invalid month " + s);
        }

        private boolean matches(String s) {
          return s.equalsIgnoreCase(toString()) ||
                 s.equalsIgnoreCase(toShortString());
        }
```

Phương thức isLeapYear (dòng 495–517) có thể được viết biểu đạt hơn một chút [G16].

```java
        public static boolean isLeapYear(int year) {
          boolean fourth = year % 4 == 0;
          boolean hundredth = year % 100 == 0;
          boolean fourHundredth = year % 400 == 0;
          return fourth && (!hundredth || fourHundredth);
        }
```

Hàm tiếp theo, leapYearCount (dòng 519–536), thực sự không thuộc về DayDate. Không ai gọi nó ngoài hai phương thức trong SpreadsheetDate. Vì vậy, tôi chuyển nó xuống đó [G6].

Hàm lastDayOfMonth (dòng 538–560) dùng mảng LAST_DAY_OF_MONTH. Mảng này thực sự thuộc về enum Month [G17], nên tôi chuyển nó vào đó. Tôi cũng đơn giản hóa hàm và làm nó dễ hiểu hơn [G16].

```java
        public static int lastDayOfMonth(Month month, int year) {
          if (month == Month.FEBRUARY && isLeapYear(year))
            return month.lastDay() + 1;
           else
            return month.lastDay();
        }
```

Giờ mọi thứ bắt đầu thú vị hơn một chút. Hàm tiếp theo là addDays (dòng 562–576). Trước hết, vì hàm này thao tác trên các biến của DayDate nên không nên là static [G18]. Vì vậy, tôi đổi nó thành phương thức thực thể. Thứ hai, nó gọi hàm toSerial. Nên đổi tên hàm này thành toOrdinal [N1]. Cuối cùng, có thể đơn giản hóa phương thức.

```java
        public DayDate addDays(int days) {
          return DayDateFactory.makeDate(toOrdinal() + days);
        }
```

addMonths (dòng 578–602) cũng vậy. Nó nên là phương thức thực thể [G18]. Thuật toán hơi phức tạp, nên tôi dùng các BIẾN TẠM GIẢI THÍCH[^8] [G19] để làm rõ hơn. Tôi cũng đổi tên phương thức getYYY thành getYear [N1].

```java
        public DayDate addMonths(int months) {
          int thisMonthAsOrdinal = 12 * getYear() + getMonth().index - 1;
          int resultMonthAsOrdinal = thisMonthAsOrdinal + months;
          int resultYear = resultMonthAsOrdinal / 12;
          Month resultMonth = Month.make(resultMonthAsOrdinal % 12 + 1);

            int lastDayOfResultMonth = lastDayOfMonth(resultMonth, resultYear);
            int resultDay = Math.min(getDayOfMonth(), lastDayOfResultMonth);
            return DayDateFactory.makeDate(resultDay, resultMonth, resultYear);
        }
```

[^8]: [Beck97].

Hàm addYears (dòng 604–626) không có gì bất ngờ so với các hàm khác.

```java
        public DayDate plusYears(int years) {
          int resultYear = getYear() + years;
          int lastDayOfMonthInResultYear = lastDayOfMonth(getMonth(), resultYear);
          int resultDay = Math.min(getDayOfMonth(), lastDayOfMonthInResultYear);
          return DayDateFactory.makeDate(resultDay, getMonth(), resultYear);
        }
```

Trong đầu tôi có một điều cứ vướng mắc về việc đổi các phương thức này từ static sang phương thức thực thể. Biểu thức date.addDays(5) có nói rõ rằng đối tượng ngày không thay đổi và một thực thể DayDate mới được trả về hay không? Hay nó khiến người đọc hiểu nhầm rằng ta đang cộng năm ngày vào đối tượng ngày? Có thể bạn không nghĩ đó là vấn đề lớn, nhưng đoạn mã như sau rất dễ gây hiểu nhầm [G20].

```java
      DayDate date = DateFactory.makeDate(5, Month.DECEMBER, 1952);
      date.addDays(7); // tăng ngày thêm một tuần.
```

Người đọc đoạn mã này rất có thể sẽ cho rằng addDays thay đổi đối tượng ngày. Vì vậy, ta cần một tên phá vỡ sự mơ hồ này [N4]. Tôi đổi tên thành plusDays và plusMonths. Theo tôi, ý định của phương thức được thể hiện rõ trong cách viết này:

```java
      DayDate date = oldDate.plusDays(5);
```

Còn cách viết sau không trôi chảy đủ để người đọc mặc nhiên hiểu rằng đối tượng ngày bị thay đổi:

```java
      date.plusDays(5);
```

Các thuật toán tiếp tục trở nên thú vị hơn. getPreviousDayOfWeek (dòng 628–660) hoạt động nhưng hơi phức tạp. Sau khi suy nghĩ về điều thực sự đang diễn ra [G21], tôi đơn giản hóa được nó và dùng BIẾN TẠM GIẢI THÍCH [G19] để làm rõ. Tôi cũng đổi nó từ phương thức static sang phương thức thực thể [G18], đồng thời bỏ phương thức thực thể trùng lặp [G5] (dòng 997–1008).

```java
        public DayDate getPreviousDayOfWeek(Day targetDayOfWeek) {
          int offsetToTarget = targetDayOfWeek.index - getDayOfWeek().index;
          if (offsetToTarget >= 0)
            offsetToTarget -= 7;
          return plusDays(offsetToTarget);
        }
```

getFollowingDayOfWeek (dòng 662–693) được phân tích và cho kết quả y hệt.

```java
      public DayDate getFollowingDayOfWeek(Day targetDayOfWeek) {
          int offsetToTarget = targetDayOfWeek.index - getDayOfWeek().index;
          if (offsetToTarget <= 0)
             offsetToTarget += 7;
           return plusDays(offsetToTarget);
       }
```

Hàm tiếp theo là getNearestDayOfWeek (dòng 695–726), hàm mà ta đã sửa ở trang 270. Nhưng những thay đổi tôi thực hiện khi đó không nhất quán với kiểu hiện tại của hai hàm trước [G11]. Vì vậy, tôi làm cho nó nhất quán, đồng thời dùng một số BIẾN TẠM GIẢI THÍCH [G19] để làm rõ thuật toán.

```java
    public DayDate getNearestDayOfWeek(final Day targetDay) {
        int offsetToThisWeeksTarget = targetDay.index - getDayOfWeek().index;
        int offsetToFutureTarget = (offsetToThisWeeksTarget + 7) % 7;
        int offsetToPreviousTarget = offsetToFutureTarget - 7;

           if (offsetToFutureTarget > 3)
             return plusDays(offsetToPreviousTarget);
           else
             return plusDays(offsetToFutureTarget);
       }
```

Phương thức getEndOfCurrentMonth (dòng 728–740) hơi kỳ lạ vì nó là một phương thức thực thể nhưng lại có mùi [G14] lớp của chính nó khi nhận đối số DayDate. Tôi biến nó thành phương thức thực thể đúng nghĩa và làm rõ vài tên gọi.

```java
    public DayDate getEndOfMonth() {
        Month month = getMonth();
        int year = getYear();
        int lastDay = lastDayOfMonth(month, year);
        return DayDateFactory.makeDate(lastDay, month, year);
      }
```

Tái cấu trúc weekInMonthToString (dòng 742–761) quả thực rất thú vị. Trước tiên, tôi dùng công cụ tái cấu trúc trong IDE để chuyển phương thức vào enum WeekInMonth mà tôi đã tạo ở trang 275. Sau đó, tôi đổi tên phương thức thành toString. Tiếp theo, tôi đổi nó từ phương thức static thành phương thức thực thể. Tất cả kiểm thử vẫn chạy qua. (Bạn đoán được tôi định làm gì chưa?)

Tiếp đó, tôi xóa hẳn phương thức này! Năm lệnh assert thất bại (dòng 411–415, Đoạn mã B-4, trang 374). Tôi sửa những dòng đó để dùng tên các giá trị enum (FIRST, SECOND, . . .). Tất cả kiểm thử đều chạy qua. Bạn hiểu vì sao không? Bạn cũng hiểu vì sao cần từng bước này không? Công cụ tái cấu trúc đảm bảo mọi nơi gọi weekInMonthToString trước đó giờ đều gọi toString trên giá trị weekInMonth, vì mọi giá trị enum đều triển khai toString để đơn giản trả về tên của chúng. . . .

Đáng tiếc là tôi đã tỏ ra khôn khéo quá mức. Chuỗi tái cấu trúc tuyệt vời ấy có thanh nhã đến đâu, cuối cùng tôi cũng nhận ra rằng những người duy nhất dùng hàm này là các kiểm thử mà tôi vừa sửa, nên tôi đã xóa các kiểm thử đó.

Lừa tôi lần đầu là lỗi của bạn. Lừa tôi lần thứ hai là lỗi của tôi! Sau khi xác định không ai ngoài các kiểm thử gọi relativeToString (dòng 765–781), tôi chỉ việc xóa hàm và các kiểm thử của nó.

Cuối cùng, ta cũng đến các phương thức trừu tượng của lớp trừu tượng này. Phương thức đầu tiên rất phù hợp: toSerial (dòng 838–844). Ở trang 279 tôi đã đổi tên nó thành toOrdinal. Xem xét nó trong ngữ cảnh này, tôi quyết định nên đổi tên thành getOrdinalDay.

Phương thức trừu tượng tiếp theo là toDate (dòng 838–844). Nó chuyển DayDate thành java.util.Date. Tại sao phương thức này lại trừu tượng? Nếu xem phần triển khai trong SpreadsheetDate (dòng 198–207, Đoạn mã B-5, trang 382), ta thấy nó không phụ thuộc vào điều gì trong cách triển khai của lớp đó [G6]. Vì vậy, tôi chuyển nó lên lớp cha.

Các phương thức getYYYY, getMonth và getDayOfMonth được trừu tượng hóa hợp lý. Tuy nhiên, getDayOfWeek cũng là phương thức nên được chuyển lên từ SpreadSheetDate vì nó không phụ thuộc vào thứ gì không thể tìm thấy trong DayDate [G6]. Hay là có?

Nếu xem kỹ (dòng 247, Đoạn mã B-5, trang 382), bạn sẽ thấy thuật toán ngầm phụ thuộc vào điểm gốc của ngày ordinal, nói cách khác là thứ trong tuần của ngày 0. Vì vậy, dù hàm này không có phụ thuộc vật lý nào không thể chuyển sang DayDate, nó vẫn có phụ thuộc logic.

Những phụ thuộc logic như vậy khiến tôi băn khoăn [G22]. Nếu thứ gì đó về mặt logic phụ thuộc vào cách triển khai thì về mặt vật lý cũng nên như vậy. Hơn nữa, theo tôi, bản thân thuật toán có thể dùng chung, chỉ một phần nhỏ hơn nhiều phụ thuộc vào cách triển khai [G6].

Vì thế, tôi tạo một phương thức trừu tượng trong DayDate tên getDayOfWeekForOrdinalZero và triển khai nó trong SpreadsheetDate để trả về Day.SATURDAY. Sau đó, tôi chuyển phương thức getDayOfWeek lên DayDate và sửa nó để gọi getOrdinalDay cùng getDayOfWeekForOrdinalZero.

```java
      public Day getDayOfWeek() {
          Day startingDay = getDayOfWeekForOrdinalZero();
          int startingOffset = startingDay.index - Day.SUNDAY.index;
          return Day.make((getOrdinalDay() + startingOffset) % 7 + 1);
        }
```

Nhân tiện, hãy xem kỹ chú thích từ dòng 895 đến dòng 899. Có thật cần lặp lại như vậy không? Như thường lệ, tôi xóa chú thích này cùng tất cả các chú thích khác.

Phương thức tiếp theo là compare (dòng 902–913). Một lần nữa, phương thức này bị trừu tượng hóa không đúng chỗ [G6], nên tôi chuyển phần triển khai lên DayDate. Tên gọi cũng chưa truyền đạt đủ [N1]. Phương thức này thực ra trả về số ngày chênh lệch so với đối số. Vì vậy, tôi đổi tên thành daysSince. Tôi cũng nhận thấy chưa có kiểm thử nào cho phương thức này, nên đã viết kiểm thử.

Sáu hàm tiếp theo (dòng 915–980) đều là phương thức trừu tượng cần được triển khai trong DayDate. Vì vậy, tôi chuyển tất cả chúng lên từ SpreadsheetDate.

Hàm cuối cùng, isInRange (dòng 982–995), cũng cần được chuyển lên và tái cấu trúc. Câu lệnh switch hơi xấu [G23], có thể thay bằng cách chuyển các trường hợp vào enum DateInterval.

```java
    public enum DateInterval {
        OPEN {
           public boolean isIn(int d, int left, int right) {
             return d > left && d < right;
           }
        },
        CLOSED_LEFT {
           public boolean isIn(int d, int left, int right) {
             return d >= left && d < right;
           }
        },
        CLOSED_RIGHT {
           public boolean isIn(int d, int left, int right) {
             return d > left && d <= right;
           }
        },
        CLOSED {
           public boolean isIn(int d, int left, int right) {
             return d >= left && d <= right;
           }
        };
          public abstract boolean isIn(int d, int left, int right);
      }

    public boolean isInRange(DayDate d1, DayDate d2, DateInterval interval) {
        int left = Math.min(d1.getOrdinalDay(), d2.getOrdinalDay());
        int right = Math.max(d1.getOrdinalDay(), d2.getOrdinalDay());
        return interval.isIn(getOrdinalDay(), left, right);
      }
```

Vậy là kết thúc DayDate. Giờ chúng ta sẽ xem lại toàn bộ lớp thêm một lượt để xem nó trôi chảy đến đâu.

Trước hết, chú thích mở đầu đã quá lỗi thời, nên tôi rút ngắn và cải thiện nó [C2].

Tiếp theo, tôi chuyển mọi enum còn lại sang tệp riêng [G12].

Sau đó, tôi chuyển biến static (dateFormatSymbols) và ba phương thức static (getMonthNames, isLeapYear, lastDayOfMonth) vào lớp mới tên DateUtil [G6].

Tôi chuyển các phương thức trừu tượng lên đầu lớp, nơi chúng thuộc về [G24].

Tôi đổi Month.make thành Month.fromInt [N1] và làm tương tự với mọi enum khác. Tôi cũng tạo phương thức truy cập toInt() cho mọi enum và đặt trường index thành private.

Có một số đoạn trùng lặp thú vị [G5] trong plusYears và plusMonths mà tôi loại bỏ được bằng cách tách một phương thức mới tên correctLastDayOfMonth, giúp cả ba phương thức rõ ràng hơn nhiều.

Tôi bỏ số ma thuật 1 [G25], thay bằng Month.JANUARY.toInt() hoặc Day.SUNDAY.toInt() tùy trường hợp. Tôi dành một chút thời gian dọn dẹp SpreadsheetDate và cải thiện đôi chút các thuật toán. Kết quả cuối cùng nằm trong Đoạn mã B-7, trang 394, đến Đoạn mã B-16, trang 405.

Điều thú vị là độ bao phủ mã trong DayDate giảm xuống còn 84,9 phần trăm! Không phải vì có ít chức năng được kiểm thử hơn, mà vì lớp đã thu nhỏ đáng kể, khiến một vài dòng chưa được bao phủ chiếm tỷ trọng lớn hơn. Hiện DayDate có 45 trong số 53 câu lệnh có thể thực thi được kiểm thử bao phủ. Những dòng chưa được bao phủ quá đơn giản, không đáng để kiểm thử.

## Kết luận

Một lần nữa, chúng ta đã làm theo Quy tắc Hướng đạo sinh. Ta trả mã về kho trong tình trạng sạch hơn một chút so với lúc lấy ra. Việc này mất chút thời gian, nhưng đáng công. Độ bao phủ kiểm thử tăng lên, một số lỗi được sửa, mã trở nên rõ ràng và gọn hơn. Hy vọng người tiếp theo xem đoạn mã này sẽ thấy dễ xử lý hơn chúng ta. Người đó có lẽ còn có thể dọn dẹp nó thêm một chút nữa.

## Tài liệu tham khảo

[GOF]: *Design Patterns: Elements of Reusable Object Oriented Software*, Gamma et al., Addison-Wesley, 1996.

[Simmons04]: *Hardcore Java*, Robert Simmons, Jr., O’Reilly, 2004.

[Refactoring]: *Refactoring: Improving the Design of Existing Code*, Martin Fowler et al., Addison-Wesley, 1999.

[Beck97]: *Smalltalk Best Practice Patterns*, Kent Beck, Prentice Hall, 1997.
