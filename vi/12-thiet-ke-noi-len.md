# Chương 12: Thiết kế nổi lên

> Tác giả: Jeff Langr

## Thiết kế sạch nhờ thiết kế nổi lên

Nếu có bốn quy tắc đơn giản mà bạn có thể làm theo để tạo ra những thiết kế tốt trong quá trình làm việc thì sao? Nếu nhờ làm theo các quy tắc đó, bạn hiểu sâu hơn về cấu trúc và thiết kế của mã, từ đó dễ áp dụng những nguyên tắc như SRP và DIP hơn thì sao? Nếu bốn quy tắc này giúp những thiết kế tốt tự hình thành thì sao?

Nhiều người trong chúng ta thấy bốn quy tắc Thiết kế Đơn giản của Kent Beck¹ rất hữu ích để tạo ra phần mềm có thiết kế tốt.

¹ [XPE].

Theo Kent, một thiết kế là “đơn giản” nếu tuân theo các quy tắc sau:

- Chạy qua tất cả các kiểm thử
- Không có trùng lặp
- Thể hiện ý định của lập trình viên
- Giảm thiểu số lượng lớp và phương thức

Các quy tắc được liệt kê theo thứ tự quan trọng.

## Quy tắc Thiết kế Đơn giản 1: Chạy qua tất cả các kiểm thử

Trước hết, thiết kế phải tạo ra một hệ thống hoạt động đúng như dự định. Trên giấy tờ, hệ thống có thể có thiết kế hoàn hảo. Nhưng nếu không có cách đơn giản nào để xác minh hệ thống thực sự hoạt động như dự định thì mọi công sức trên giấy đều đáng ngờ.

Một hệ thống được kiểm thử toàn diện và luôn vượt qua tất cả các kiểm thử là một hệ thống có thể kiểm thử được. Điều đó nghe hiển nhiên, nhưng rất quan trọng. Hệ thống không thể kiểm thử thì không thể xác minh. Có thể nói, một hệ thống không thể xác minh thì không bao giờ nên được triển khai.

May mắn thay, việc làm cho hệ thống có thể kiểm thử được sẽ thúc đẩy chúng ta hướng tới thiết kế có các lớp nhỏ, mỗi lớp chỉ đảm nhận một mục đích. Kiểm thử các lớp tuân theo SRP dễ hơn nhiều. Càng viết nhiều kiểm thử, chúng ta càng hướng tới những thứ dễ kiểm thử hơn. Vì vậy, bảo đảm hệ thống có thể được kiểm thử đầy đủ giúp chúng ta tạo ra thiết kế tốt hơn.

Sự phụ thuộc chặt chẽ khiến việc viết kiểm thử trở nên khó khăn. Do đó, tương tự như trên, càng viết nhiều kiểm thử, chúng ta càng áp dụng những nguyên tắc như DIP và các công cụ như tiêm phụ thuộc, giao diện và trừu tượng hóa để giảm thiểu sự phụ thuộc. Nhờ vậy, thiết kế của chúng ta càng được cải thiện.

Thật đáng kinh ngạc, chỉ cần làm theo một quy tắc đơn giản, hiển nhiên rằng chúng ta cần có kiểm thử và chạy chúng liên tục, hệ thống sẽ tuân thủ tốt hơn các mục tiêu OO cốt lõi: sự phụ thuộc thấp và độ gắn kết cao. Viết kiểm thử dẫn đến thiết kế tốt hơn.

## Quy tắc Thiết kế Đơn giản 2–4: Tái cấu trúc

Khi đã có kiểm thử, chúng ta có thể giữ cho mã và các lớp luôn sạch. Ta làm điều đó bằng cách tái cấu trúc mã từng bước. Cứ viết thêm vài dòng mã, ta lại dừng và suy ngẫm về thiết kế mới. Ta vừa làm thiết kế xuống cấp ư? Nếu có, ta dọn dẹp rồi chạy kiểm thử để chứng minh rằng mình chưa làm hỏng gì. Có sẵn những kiểm thử này sẽ xua tan nỗi lo rằng việc dọn dẹp mã sẽ làm hỏng nó!

Trong bước tái cấu trúc này, chúng ta có thể áp dụng mọi kiến thức về thiết kế phần mềm tốt. Ta có thể tăng độ gắn kết, giảm sự phụ thuộc, tách biệt các mối quan tâm, mô-đun hóa những mối quan tâm của hệ thống, thu nhỏ hàm và lớp, chọn tên tốt hơn, vân vân. Đây cũng là lúc áp dụng ba quy tắc cuối của thiết kế đơn giản: loại bỏ trùng lặp, bảo đảm tính biểu đạt và giảm thiểu số lượng lớp cùng phương thức.

## Không trùng lặp

Trùng lặp là kẻ thù hàng đầu của một hệ thống được thiết kế tốt. Nó tạo thêm công việc, thêm rủi ro và thêm độ phức tạp không cần thiết. Trùng lặp xuất hiện dưới nhiều hình thức. Dĩ nhiên, những dòng mã trông giống hệt nhau là trùng lặp. Những dòng mã tương tự nhau thường có thể được chỉnh sửa để trông giống nhau hơn, nhờ đó dễ tái cấu trúc hơn. Trùng lặp cũng có thể tồn tại dưới những dạng khác, chẳng hạn trùng lặp trong cách triển khai. Ví dụ, trong một lớp tập hợp, ta có thể có hai phương thức:

```java
int size() {}
boolean isEmpty() {}
```

Ta có thể triển khai riêng từng phương thức. Phương thức `isEmpty` có thể theo dõi một giá trị boolean, còn `size` theo dõi một bộ đếm. Hoặc ta có thể loại bỏ phần trùng lặp bằng cách định nghĩa `isEmpty` dựa trên `size`:

```java
boolean isEmpty() {
   return 0 == size();
}
```

Muốn tạo ra một hệ thống sạch, ta cần quyết tâm loại bỏ trùng lặp, dù chỉ là vài dòng mã. Chẳng hạn, hãy xem đoạn mã sau:

```java
public void scaleToOneDimension(
     float desiredDimension, float imageDimension) {
  if (Math.abs(desiredDimension - imageDimension) < errorThreshold)
     return;
  float scalingFactor = desiredDimension / imageDimension;
  scalingFactor = (float)(Math.floor(scalingFactor * 100) * 0.01f);

   RenderedOp newImage = ImageUtilities.getScaledImage(
      image, scalingFactor, scalingFactor);
   image.dispose();
   System.gc();
   image = newImage;
}
public synchronized void rotate(int degrees) {
  RenderedOp newImage = ImageUtilities.getRotatedImage(
     image, degrees);
  image.dispose();
  System.gc();
  image = newImage;
}
```

Để giữ hệ thống sạch, ta nên loại bỏ phần trùng lặp nhỏ giữa các phương thức `scaleToOneDimension` và `rotate`:

```java
public void scaleToOneDimension(
     float desiredDimension, float imageDimension) {
  if (Math.abs(desiredDimension - imageDimension) < errorThreshold)
     return;
  float scalingFactor = desiredDimension / imageDimension;
  scalingFactor = (float)(Math.floor(scalingFactor * 100) * 0.01f);

  replaceImage(ImageUtilities.getScaledImage(
     image, scalingFactor, scalingFactor));
}

public synchronized void rotate(int degrees) {
   replaceImage(ImageUtilities.getRotatedImage(image, degrees));
}
private void replaceImage(RenderedOp newImage) {
   image.dispose();
   System.gc();
   image = newImage;
}
```

Khi tách ra điểm chung ở mức rất nhỏ như vậy, ta bắt đầu nhận ra những vi phạm SRP. Vì thế, có thể ta sẽ chuyển phương thức vừa tách ra sang một lớp khác. Việc đó khiến phương thức dễ được nhìn thấy hơn. Một thành viên khác trong nhóm có thể nhận ra cơ hội trừu tượng hóa thêm phương thức mới và tái sử dụng nó trong một ngữ cảnh khác. Kiểu “tái sử dụng ở quy mô nhỏ” này có thể giảm đáng kể độ phức tạp của hệ thống. Hiểu cách đạt được sự tái sử dụng ở quy mô nhỏ là điều thiết yếu để đạt được sự tái sử dụng ở quy mô lớn.

Mẫu TEMPLATE METHOD² là một kỹ thuật phổ biến để loại bỏ trùng lặp ở cấp độ cao hơn. Ví dụ:

² [GOF].

```java
public class VacationPolicy {
   public void accrueUSDivisionVacation() {
      // code to calculate vacation based on hours worked to date
      // ...
      // code to ensure vacation meets US minimums
      // ...
      // code to apply vaction to payroll record
      // ...
   }

   public void accrueEUDivisionVacation() {
      // code to calculate vacation based on hours worked to date
      // ...
      // code to ensure vacation meets EU minimums
      // ...
      // code to apply vaction to payroll record
      // ...
   }
}
```

Mã trong `accrueUSDivisionVacation` và `accrueEuropeanDivisionVacation` phần lớn giống nhau, ngoại trừ phần tính các mức tối thiểu theo luật. Phần đó của thuật toán thay đổi tùy theo loại nhân viên.

Ta có thể loại bỏ phần trùng lặp rõ ràng bằng cách áp dụng mẫu TEMPLATE METHOD.

```java
abstract public class VacationPolicy {
   public void accrueVacation() {
      calculateBaseVacationHours();

      alterForLegalMinimums();
      applyToPayroll();
   }

   private void calculateBaseVacationHours() { /* ... */ };
   abstract protected void alterForLegalMinimums();
   private void applyToPayroll() { /* ... */ };
}

public class USVacationPolicy extends VacationPolicy {
   @Override protected void alterForLegalMinimums() {
      // US specific logic
   }
}
public class EUVacationPolicy extends VacationPolicy {
   @Override protected void alterForLegalMinimums() {
      // EU specific logic
   }
}
```

Các lớp con lấp vào “chỗ trống” trong thuật toán `accrueVacation`, cung cấp những phần thông tin duy nhất không bị trùng lặp.

## Biểu đạt

Hầu hết chúng ta từng trải qua cảm giác phải làm việc với mã rối rắm. Nhiều người trong chúng ta cũng từng viết ra những đoạn mã rối rắm như thế. Viết mã mà ta hiểu thì dễ, bởi lúc viết, ta đang hiểu sâu vấn đề mình tìm cách giải quyết. Những người bảo trì mã sau này sẽ không hiểu sâu đến vậy.

Phần lớn chi phí của một dự án phần mềm phát sinh trong giai đoạn bảo trì lâu dài. Để giảm thiểu nguy cơ phát sinh lỗi khi thay đổi hệ thống, chúng ta cần hiểu hệ thống làm gì. Hệ thống càng phức tạp thì nhà phát triển càng mất nhiều thời gian để hiểu, và nguy cơ hiểu sai cũng càng lớn. Vì vậy, mã phải thể hiện rõ ý định của người viết. Người viết làm cho mã càng rõ ràng thì người khác càng mất ít thời gian để hiểu. Nhờ đó, lỗi sẽ giảm và chi phí bảo trì cũng thấp hơn.

Bạn có thể thể hiện suy nghĩ của mình bằng cách chọn tên tốt. Ta muốn nghe tên một lớp hay một hàm mà không thấy bất ngờ khi phát hiện ra trách nhiệm của nó.

Bạn cũng có thể thể hiện suy nghĩ của mình bằng cách giữ cho hàm và lớp nhỏ gọn. Các lớp và hàm nhỏ thường dễ đặt tên, dễ viết và dễ hiểu.

Bạn còn có thể thể hiện suy nghĩ của mình bằng cách dùng thuật ngữ chuẩn. Chẳng hạn, các mẫu thiết kế phần lớn nhằm mục đích giao tiếp và biểu đạt. Khi dùng tên mẫu chuẩn như COMMAND hay VISITOR trong tên các lớp triển khai những mẫu đó, bạn có thể mô tả ngắn gọn thiết kế của mình với các nhà phát triển khác.

Các kiểm thử đơn vị được viết tốt cũng có tính biểu đạt. Một mục tiêu chính của kiểm thử là làm tài liệu thông qua ví dụ. Người đọc kiểm thử của chúng ta phải nhanh chóng hiểu được một lớp làm những gì.

Nhưng cách quan trọng nhất để biểu đạt là cố gắng làm điều đó. Quá thường xuyên, chúng ta làm cho mã chạy được rồi chuyển sang vấn đề tiếp theo mà không suy nghĩ đủ để giúp người kế tiếp dễ đọc mã. Hãy nhớ, người có khả năng đọc mã tiếp theo nhất chính là bạn.

Vì vậy, hãy tự hào một chút về tay nghề của mình. Dành chút thời gian cho từng hàm và lớp. Chọn tên tốt hơn, tách hàm lớn thành các hàm nhỏ hơn, và nói chung hãy chăm chút cho những gì mình tạo ra. Sự chăm chút là nguồn lực quý giá.

## Tối thiểu hóa số lớp và phương thức

Ngay cả những khái niệm nền tảng như loại bỏ trùng lặp, tính biểu đạt của mã và SRP cũng có thể bị đẩy đi quá xa. Trong nỗ lực làm cho lớp và phương thức nhỏ gọn, ta có thể tạo ra quá nhiều lớp và phương thức vụn vặt. Vì thế, quy tắc này cũng khuyên ta giữ số lượng hàm và lớp ở mức thấp.

Số lượng lớp và phương thức lớn đôi khi là kết quả của chủ nghĩa giáo điều vô ích. Chẳng hạn, hãy nghĩ đến một tiêu chuẩn lập trình yêu cầu tạo giao diện cho mọi lớp. Hoặc nghĩ đến những nhà phát triển khăng khăng rằng trường dữ liệu và hành vi luôn phải tách riêng thành các lớp dữ liệu và lớp hành vi. Ta nên chống lại giáo điều như vậy và chọn cách tiếp cận thực tế hơn.

Mục tiêu của chúng ta là giữ cho toàn bộ hệ thống nhỏ gọn, đồng thời giữ cho các hàm và lớp cũng nhỏ gọn. Tuy nhiên, hãy nhớ đây là quy tắc có mức ưu tiên thấp nhất trong bốn quy tắc Thiết kế Đơn giản. Vì vậy, dù việc giữ số lượng lớp và hàm ở mức thấp là quan trọng, có kiểm thử, loại bỏ trùng lặp và thể hiện suy nghĩ của mình còn quan trọng hơn.

## Kết luận

Có tập hợp những thực hành đơn giản nào có thể thay thế kinh nghiệm không? Rõ ràng là không. Mặt khác, những thực hành được mô tả trong chương này và trong cuốn sách này là kết tinh từ nhiều thập kỷ kinh nghiệm của các tác giả. Thực hành thiết kế đơn giản có thể và thực sự khuyến khích, giúp các nhà phát triển tuân theo những nguyên tắc và mẫu tốt mà nếu không thì phải mất nhiều năm mới học được.

## Tài liệu tham khảo

[XPE]: *Extreme Programming Explained: Embrace Change*, Kent Beck, Addison-Wesley, 1999.

[GOF]: *Design Patterns: Elements of Reusable Object Oriented Software*, Gamma et al., Addison-Wesley, 1996.
