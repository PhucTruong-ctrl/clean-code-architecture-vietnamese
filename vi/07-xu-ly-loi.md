# Chương 7: Xử lý lỗi

> Tác giả: Michael Feathers

Có vẻ lạ khi một cuốn sách về mã sạch lại có một mục bàn về xử lý lỗi. Xử lý lỗi chỉ là một trong những việc ai cũng phải làm khi lập trình. Đầu vào có thể bất thường và thiết bị có thể hỏng. Nói ngắn gọn, mọi thứ đều có thể sai, và khi sai, chúng ta, những lập trình viên, phải chịu trách nhiệm bảo đảm mã của mình vẫn làm được việc nó cần làm.

Tuy vậy, mối liên hệ với mã sạch hẳn phải rõ. Nhiều code base bị xử lý lỗi chi phối hoàn toàn. Khi nói chi phối, tôi không có ý rằng chúng chỉ làm mỗi việc xử lý lỗi. Ý tôi là gần như không thể thấy code làm gì, vì xử lý lỗi nằm rải rác khắp nơi. Xử lý lỗi quan trọng, nhưng nếu nó che khuất logic thì là sai.

Trong chương này, tôi sẽ phác ra một số kỹ thuật và điều cần cân nhắc để bạn viết được thứ code vừa sạch vừa vững chắc, thứ code xử lý lỗi một cách thanh thoát và có phong độ.

## Dùng ngoại lệ thay cho mã lỗi

Ngày trước, có nhiều ngôn ngữ không có ngoại lệ. Ở những ngôn ngữ đó, cách xử lý và báo lỗi rất hạn chế. Bạn hoặc đặt một cờ lỗi, hoặc trả về một mã lỗi để bên gọi kiểm tra. Đoạn mã 7-1 minh họa những cách làm này.

**Đoạn mã 7-1**
**DeviceController.java**

```java
public class DeviceController {
    ...
    public void sendShutDown() {
        DeviceHandle handle = getHandle(DEV1);
        // Kiểm tra trạng thái của thiết bị
        if (handle != DeviceHandle.INVALID) {
            // Lưu trạng thái thiết bị vào trường record
            retrieveDeviceRecord(handle);
            // Nếu không bị tạm dừng thì tắt
            if (record.getStatus() != DEVICE_SUSPENDED) {
                pauseDevice(handle);
                clearDeviceWorkQueue(handle);
                closeDevice(handle);
            } else {
                logger.log("Device suspended. Unable to shut down");
            }
        } else {
            logger.log("Invalid handle for: " + DEV1.toString());
        }
    }
    ...
}
```

Vấn đề của những cách này là chúng làm rối bên gọi. Bên gọi phải kiểm tra lỗi ngay sau lời gọi. Đáng tiếc, quên thì rất dễ. Vì thế, tốt hơn là ném ngoại lệ khi gặp lỗi. Mã gọi sẽ sạch hơn. Logic của nó không bị xử lý lỗi che khuất.

Đoạn mã 7-2 cho thấy code sau khi chúng ta chọn ném ngoại lệ trong những phương thức có thể phát hiện lỗi.

**Đoạn mã 7-2**
**DeviceController.java (có ngoại lệ)**

```java
public class DeviceController {
    ...

    public void sendShutDown() {
        try {
            tryToShutDown();
        } catch (DeviceShutDownError e) {
            logger.log(e);
        }
    }
```

**Đoạn mã 7-2 (tiếp theo)**
**DeviceController.java (có ngoại lệ)**

```java
    private void tryToShutDown() throws DeviceShutDownError {
        DeviceHandle handle = getHandle(DEV1);
        DeviceRecord record = retrieveDeviceRecord(handle);

        pauseDevice(handle);
        clearDeviceWorkQueue(handle);
        closeDevice(handle);
    }

    private DeviceHandle getHandle(DeviceID id) {
        ...
        throw new DeviceShutDownError("Invalid handle for: " + id.toString());
        ...
    }

    ...
}
```

Hãy để ý nó sạch hơn bao nhiêu. Đây không chỉ là chuyện thẩm mỹ. Mã tốt hơn vì hai mối bận tâm từng quấn vào nhau, thuật toán tắt thiết bị và xử lý lỗi, giờ đã tách ra. Bạn có thể nhìn từng mối bận tâm và hiểu chúng độc lập.

## Viết câu lệnh try-catch-finally trước

Một trong những điều thú vị nhất ở ngoại lệ là chúng định nghĩa một phạm vi trong chương trình của bạn. Khi chạy code trong phần try của câu lệnh try-catch-finally, bạn đang tuyên bố rằng việc thực thi có thể dừng ở bất kỳ điểm nào rồi tiếp tục ở catch.

Theo một nghĩa nào đó, khối try giống như giao dịch. Khối catch phải để chương trình ở trạng thái nhất quán, bất kể điều gì xảy ra trong try. Vì vậy, khi viết code có thể ném ngoại lệ, bạn nên bắt đầu bằng một câu lệnh try-catch-finally. Cách này giúp bạn định nghĩa điều người dùng code đó nên kỳ vọng, bất kể code chạy trong try gặp trục trặc gì.

Hãy xem một ví dụ. Chúng ta cần viết đoạn code truy cập một tệp và đọc vài đối tượng đã được tuần tự hóa.

Chúng ta bắt đầu bằng một bài kiểm thử đơn vị cho thấy sẽ nhận được ngoại lệ khi tệp không tồn tại:

```java
@Test(expected = StorageException.class)
public void retrieveSectionShouldThrowOnInvalidFileName() {
    sectionStore.retrieveSection("invalid - file");
}
```

Bài kiểm thử dẫn chúng ta tới việc tạo đoạn khung này:

```java
public List<RecordedGrip> retrieveSection(String sectionName) {
    // trả về tạm cho đến khi có cài đặt thật
    return new ArrayList<RecordedGrip>();
}
```

Bài kiểm thử thất bại vì code không ném ngoại lệ. Tiếp theo, chúng ta sửa phần cài đặt để nó thử truy cập một tệp không hợp lệ. Thao tác này ném ngoại lệ:

```java
public List<RecordedGrip> retrieveSection(String sectionName) {
    try {
        FileInputStream stream = new FileInputStream(sectionName)
    } catch (Exception e) {
        throw new StorageException("retrieval error", e);
    }
    return new ArrayList<RecordedGrip>();
}
```

Giờ bài kiểm thử đã qua vì chúng ta đã bắt ngoại lệ. Đến đây, ta có thể tái cấu trúc. Ta có thể thu hẹp kiểu ngoại lệ được bắt cho khớp với kiểu thật sự được ném ra từ hàm dựng FileInputStream: FileNotFoundException.

```java
public List<RecordedGrip> retrieveSection(String sectionName) {
    try {
        FileInputStream stream = new FileInputStream(sectionName);
        stream.close();
    } catch (FileNotFoundException e) {
        throw new StorageException("retrieval error", e);
    }
    return new ArrayList<RecordedGrip>();
}
```

Giờ đã định nghĩa phạm vi bằng cấu trúc try-catch, ta có thể dùng TDD để xây phần logic còn lại. Logic đó sẽ được thêm vào giữa lúc tạo FileInputStream và lúc close, và có thể giả định rằng không có gì sai.

Hãy thử viết những bài kiểm thử buộc ngoại lệ phải xảy ra, rồi thêm hành vi vào phần xử lý để làm hài lòng các bài kiểm thử đó. Việc này khiến bạn xây dựng phạm vi giao dịch của khối try trước, và giúp bạn giữ được tính giao dịch của phạm vi ấy.

## Dùng ngoại lệ không kiểm tra

Cuộc tranh luận đã kết thúc. Nhiều năm qua, giới lập trình Java tranh cãi về lợi ích và cái giá của ngoại lệ có kiểm tra (checked exception). Khi mới xuất hiện trong phiên bản đầu tiên của Java, chúng có vẻ là một ý hay. Chữ ký của mỗi phương thức sẽ liệt kê mọi ngoại lệ mà phương thức có thể chuyển cho bên gọi. Hơn nữa, những ngoại lệ này là một phần trong kiểu của phương thức. Code của bạn đơn giản là không biên dịch được nếu chữ ký không khớp với những gì code có thể làm.

Vào thời đó, chúng tôi cho rằng ngoại lệ có kiểm tra là một ý hay; và đúng, chúng có thể mang lại vài lợi ích. Tuy vậy, giờ đã rõ là chúng không cần thiết để tạo ra phần mềm vững chắc. C# không có ngoại lệ có kiểm tra, và dù đã cố gắng hết sức, C++ cũng vậy. Python và Ruby cũng không. Thế mà vẫn có thể viết phần mềm vững chắc bằng tất cả những ngôn ngữ này. Vì thế, chúng ta phải quyết định, một cách thật sự, xem ngoại lệ có kiểm tra có đáng với cái giá của chúng không.

Cái giá nào? Cái giá của ngoại lệ có kiểm tra là sự vi phạm Nguyên tắc Open/Closed[^1]. Nếu bạn ném một ngoại lệ có kiểm tra từ một phương thức trong code và khối catch nằm ở ba tầng phía trên, bạn phải khai báo ngoại lệ đó trong chữ ký của mọi phương thức nằm giữa bạn và catch. Nghĩa là một thay đổi ở tầng thấp của phần mềm có thể buộc nhiều tầng cao hơn phải đổi chữ ký. Những module bị đổi phải build lại và triển khai lại, dù chẳng có gì chúng quan tâm bị thay đổi.

Hãy xét thứ bậc lời gọi trong một hệ thống lớn. Các hàm ở trên cùng gọi các hàm bên dưới, những hàm này lại gọi tiếp các hàm bên dưới nữa, cứ thế đến vô tận. Giả sử một hàm ở tầng thấp nhất bị sửa theo cách buộc nó phải ném ngoại lệ. Nếu ngoại lệ đó là loại có kiểm tra, chữ ký hàm phải thêm mệnh đề throws. Nhưng điều này có nghĩa mọi hàm gọi hàm vừa sửa cũng phải sửa, hoặc để bắt ngoại lệ mới, hoặc thêm mệnh đề throws thích hợp vào chữ ký. Cứ thế đến vô tận. Kết quả ròng là một chuỗi thay đổi lan từ tầng thấp nhất lên tầng cao nhất! Tính đóng gói bị phá vỡ vì mọi hàm trên đường đi của một lần ném đều phải biết chi tiết của ngoại lệ tầng thấp đó. Mục đích của ngoại lệ là cho phép bạn xử lý lỗi từ xa, nên thật đáng tiếc khi ngoại lệ có kiểm tra lại phá vỡ tính đóng gói theo cách này.

Ngoại lệ có kiểm tra đôi khi hữu ích nếu bạn viết một thư viện quan trọng: bạn buộc phải bắt chúng. Nhưng trong phát triển ứng dụng thông thường, cái giá về sự phụ thuộc lớn hơn lợi ích.

## Cung cấp ngữ cảnh qua ngoại lệ

Mỗi ngoại lệ bạn ném ra nên cung cấp đủ ngữ cảnh để xác định nguồn và vị trí của lỗi. Trong Java, bạn có thể lấy stack trace từ bất kỳ ngoại lệ nào; tuy vậy, stack trace không cho bạn biết ý định của thao tác đã thất bại.

Hãy tạo những thông báo lỗi giàu thông tin và chuyển chúng đi cùng ngoại lệ. Nêu rõ thao tác đã thất bại và kiểu thất bại. Nếu ứng dụng có ghi log, hãy chuyển đủ thông tin để có thể ghi log lỗi trong khối catch.

## Định nghĩa lớp ngoại lệ theo nhu cầu của bên gọi

Có nhiều cách phân loại lỗi. Có thể phân loại theo nguồn: lỗi đến từ thành phần này hay thành phần khác? Hoặc theo kiểu: đó là hỏng thiết bị, hỏng mạng, hay lỗi lập trình? Tuy vậy, khi định nghĩa các lớp ngoại lệ trong một ứng dụng, mối bận tâm quan trọng nhất phải là chúng được bắt như thế nào.

Hãy xem một ví dụ về phân loại ngoại lệ kém. Đây là một câu lệnh try-catch-finally cho lời gọi tới thư viện của bên thứ ba. Nó bao quát mọi ngoại lệ mà các lời gọi có thể ném ra:

```java
ACMEPort port = new ACMEPort(12);

try {
    port.open();
} catch (DeviceResponseException e) {
    reportPortError(e);
    logger.log("Device response exception", e);
} catch (ATM1212UnlockedException e) {
    reportPortError(e);
    logger.log("Unlock exception", e);
} catch (GMXError e) {
    reportPortError(e);
    logger.log("Device response exception");
} finally {
    …
}
```

Câu lệnh đó có rất nhiều trùng lặp, và điều này không có gì đáng ngạc nhiên. Trong hầu hết tình huống xử lý ngoại lệ, việc ta làm tương đối giống nhau bất kể nguyên nhân thật sự là gì. Ta phải ghi nhận một lỗi và bảo đảm mình có thể đi tiếp.

Trong trường hợp này, vì biết việc mình làm gần như giống nhau bất kể ngoại lệ nào, ta có thể đơn giản hóa code đáng kể bằng cách bọc API đang gọi và bảo đảm nó trả về một kiểu ngoại lệ chung:

```java
LocalPort port = new LocalPort(12);
try {
    port.open();
} catch (PortDeviceFailure e) {
    reportError(e);
    logger.log(e.getMessage(), e);
} finally {
    …
}
```

Lớp LocalPort của chúng ta chỉ là một lớp bọc đơn giản, bắt và chuyển dịch các ngoại lệ do lớp ACMEPort ném ra:

```java
public class LocalPort {
    private ACMEPort innerPort;

    public LocalPort(int portNumber) {
        innerPort = new ACMEPort(portNumber);
    }

    public void open() {
        try {
            innerPort.open();
        } catch (DeviceResponseException e) {
            throw new PortDeviceFailure(e);
        } catch (ATM1212UnlockedException e) {
            throw new PortDeviceFailure(e);
        } catch (GMXError e) {
            throw new PortDeviceFailure(e);
        }
    }
    …
}
```

Những lớp bọc như lớp ta định nghĩa cho ACMEPort có thể rất hữu ích. Thật ra, bọc API của bên thứ ba là một cách làm tốt nhất. Khi bọc một API bên thứ ba, bạn giảm thiểu sự phụ thuộc vào nó: sau này bạn có thể chuyển sang thư viện khác mà không phải trả giá nhiều. Việc bọc cũng giúp bạn dễ giả lập các lời gọi bên thứ ba khi kiểm thử code của mình.

Một lợi ích cuối cùng của việc bọc là bạn không bị trói vào những lựa chọn thiết kế API của một nhà cung cấp cụ thể. Bạn có thể định nghĩa một API mà mình thấy thoải mái. Trong ví dụ trên, chúng ta định nghĩa một kiểu ngoại lệ duy nhất cho lỗi thiết bị cổng và thấy rằng mình có thể viết code sạch hơn nhiều.

Thường thì một lớp ngoại lệ duy nhất là đủ cho một vùng code cụ thể. Thông tin gửi kèm ngoại lệ có thể phân biệt các lỗi. Chỉ dùng các lớp khác nhau khi có lúc bạn muốn bắt một ngoại lệ và để ngoại lệ kia đi qua.

## Định nghĩa luồng bình thường

![Định nghĩa luồng bình thường](assets/illustrations/07-define-the-normal-flow.png){w=181}

Nếu làm theo lời khuyên ở các mục trên, bạn sẽ tách được khá rõ logic nghiệp vụ và phần xử lý lỗi. Phần lớn code của bạn sẽ bắt đầu giống một thuật toán sạch, không trang trí. Tuy vậy, quá trình này đẩy việc phát hiện lỗi ra rìa chương trình. Bạn bọc các API bên ngoài để có thể ném ngoại lệ của riêng mình, và định nghĩa một bộ xử lý phía trên code để giải quyết mọi phép tính bị hủy giữa chừng. Hầu hết thời gian, đây là cách làm hay, nhưng có những lúc bạn có thể không muốn hủy.

Hãy xem một ví dụ. Đây là đoạn code khá vụng về để tính tổng chi phí trong một ứng dụng xuất hóa đơn:

```java
try {
    MealExpenses expenses = expenseReportDAO.getMeals(employee.getID());
    m_total += expenses.getTotal();
} catch(MealExpensesNotFound e) {
    m_total += getMealPerDiem();
}
```

Trong nghiệp vụ này, nếu bữa ăn được tính vào chi phí thì chúng trở thành một phần của tổng. Nếu không, nhân viên nhận một khoản phụ cấp ăn trưa cho ngày hôm đó. Ngoại lệ làm rối logic. Chẳng phải tốt hơn sao nếu ta không phải xử lý trường hợp đặc biệt? Nếu không phải xử lý, code sẽ trông đơn giản hơn nhiều. Nó sẽ như thế này:

```java
MealExpenses expenses = expenseReportDAO.getMeals(employee.getID());
m_total += expenses.getTotal();
```

Liệu ta có thể làm code đơn giản đến thế không? Hóa ra là có. Ta có thể sửa ExpenseReportDAO để nó luôn trả về một đối tượng MealExpense. Nếu không có chi phí bữa ăn nào, nó trả về một đối tượng MealExpense mà tổng của nó là khoản phụ cấp:

```java
public class PerDiemMealExpenses implements MealExpenses {
    public int getTotal() {
        // trả về mức phụ cấp mặc định
    }
}
```

Đây được gọi là SPECIAL CASE PATTERN [Fowler]. Bạn tạo một lớp hoặc cấu hình một đối tượng để nó xử lý trường hợp đặc biệt thay bạn. Khi làm vậy, code phía client không phải xử lý hành vi ngoại lệ. Hành vi đó được đóng gói trong đối tượng trường hợp đặc biệt.

## Đừng trả về null

Tôi nghĩ mọi cuộc thảo luận về xử lý lỗi đều nên nhắc đến những việc ta làm để rước lỗi vào mình. Đứng đầu danh sách là trả về null. Tôi không thể đếm nổi số ứng dụng mình từng thấy mà gần như dòng nào cũng có một phép kiểm tra null. Đây là một đoạn code ví dụ:

```java
public void registerItem(Item item) {
    if (item != null) {
        ItemRegistry registry = peristentStore.getItemRegistry();
        if (registry != null) {
            Item existing = registry.getItem(item.getID());
            if (existing.getBillingPeriod().hasRetailOwner()) {
                existing.register(item);
            }
        }
    }
}
```

Nếu bạn làm việc trong một code base có kiểu code như thế này, nó có thể trông không đến nỗi tệ với bạn, nhưng nó tệ thật! Khi trả về null, thật ra ta đang tự tạo việc cho mình và đẩy rắc rối về phía bên gọi. Chỉ cần một phép kiểm tra null bị thiếu là đủ khiến ứng dụng quay cuồng mất kiểm soát.

Bạn có để ý rằng dòng thứ hai của câu lệnh if lồng nhau đó không có phép kiểm tra null không? Điều gì sẽ xảy ra lúc chạy nếu persistentStore là null? Chúng ta sẽ nhận một NullPointerException lúc chạy, và hoặc có ai đó bắt NullPointerException ở tầng cao nhất, hoặc không. Kiểu nào cũng tệ. Chính xác thì bạn nên làm gì khi nhận một NullPointerException ném ra từ sâu trong ứng dụng của mình?

Thật dễ nói rằng vấn đề của đoạn code trên là thiếu một phép kiểm tra null, nhưng thật ra vấn đề là nó có quá nhiều phép kiểm tra. Nếu bạn thấy muốn trả về null từ một phương thức, hãy cân nhắc ném ngoại lệ hoặc trả về một đối tượng SPECIAL CASE thay vào đó. Nếu bạn đang gọi một phương thức trả về null từ API của bên thứ ba, hãy cân nhắc bọc phương thức đó bằng một phương thức khác, phương thức này hoặc ném ngoại lệ, hoặc trả về một đối tượng trường hợp đặc biệt.

Trong nhiều trường hợp, đối tượng trường hợp đặc biệt là một cách khắc phục dễ dàng. Hãy tưởng tượng bạn có đoạn code như thế này:

```java
List<Employee> employees = getEmployees();
if (employees != null) {
    for(Employee e : employees) {
        totalPay += e.getPay();
    }
}
```

Hiện tại, getEmployees có thể trả về null, nhưng nó có buộc phải thế không? Nếu sửa getEmployee để nó trả về một danh sách rỗng, ta có thể dọn gọn code:

```java
List<Employee> employees = getEmployees();
for(Employee e : employees) {
    totalPay += e.getPay();
}
```

May thay, Java có Collections.emptyList(), và nó trả về một danh sách bất biến định sẵn mà ta có thể dùng cho mục đích này:

```java
public List<Employee> getEmployees() {
    if( .. there are no employees .. )
        return Collections.emptyList();
}
```

Nếu viết code theo cách này, bạn sẽ giảm thiểu khả năng gặp NullPointerException và code của bạn sẽ sạch hơn.

## Đừng truyền null

Trả về null từ phương thức là xấu, nhưng truyền null vào phương thức còn tệ hơn. Trừ khi bạn làm việc với một API mong đợi bạn truyền null, bạn nên tránh truyền null trong code của mình bất cứ khi nào có thể.

Hãy xem một ví dụ để thấy vì sao. Đây là một phương thức đơn giản tính một đại lượng cho hai điểm:

```java
public class MetricsCalculator
{
    public double xProjection(Point p1, Point p2) {
        return (p2.x - p1.x) * 1.5;
    }
    …
}
```

Điều gì xảy ra khi có người truyền null làm đối số?

```java
calculator.xProjection(null, new Point(12, 13));
```

Tất nhiên, chúng ta sẽ nhận một NullPointerException.

Làm sao sửa được? Ta có thể tạo một kiểu ngoại lệ mới và ném nó:

```java
public class MetricsCalculator
{
    public double xProjection(Point p1, Point p2) {
        if (p1 == null || p2 == null) {
            throw InvalidArgumentException(
                "Invalid argument for MetricsCalculator.xProjection");
        }
        return (p2.x - p1.x) * 1.5;
    }
}
```

Cách này có tốt hơn không? Nó có thể tốt hơn một chút so với null pointer exception, nhưng hãy nhớ, ta phải định nghĩa một bộ xử lý cho InvalidArgumentException. Bộ xử lý đó nên làm gì? Có hành động nào hợp lý để làm không?

Còn một lựa chọn khác. Ta có thể dùng một tập các phép khẳng định:

```java
public class MetricsCalculator
{
    public double xProjection(Point p1, Point p2) {
        assert p1 != null : "p1 should not be null";
        assert p2 != null : "p2 should not be null";
        return (p2.x - p1.x) * 1.5;
    }
}
```

Đó là tài liệu tốt, nhưng nó không giải quyết vấn đề. Nếu có người truyền null, ta vẫn gặp lỗi lúc chạy.

Trong hầu hết ngôn ngữ lập trình, không có cách nào tốt để xử lý một giá trị null do bên gọi vô tình truyền vào. Vì thế, cách làm hợp lý là mặc định cấm truyền null. Khi làm vậy, bạn có thể viết code với hiểu biết rằng một null trong danh sách đối số là dấu hiệu của trục trặc, và rốt cuộc mắc ít lỗi bất cẩn hơn nhiều.

## Kết luận

Mã sạch phải đọc được, nhưng cũng phải vững chắc. Hai mục tiêu này không xung đột. Ta có thể viết mã sạch vững chắc nếu xem xử lý lỗi là một mối bận tâm riêng, một thứ có thể nhìn độc lập với logic chính. Làm được đến đâu, ta có thể lý luận về nó độc lập đến đó, và tiến xa đến đó trong khả năng bảo trì code.

[^1]: [Martin].

## Tài liệu tham khảo

\[Martin\]: Agile Software Development: Principles, Patterns, and Practices, Robert C. Martin, Prentice Hall, 2002.
