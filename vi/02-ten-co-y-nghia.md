# Chương 2: Tên có ý nghĩa

> Tác giả: Tim Ottinger

## Giới thiệu

Tên xuất hiện khắp nơi trong phần mềm. Ta đặt tên cho biến, hàm, đối số, lớp và package. Tệp mã nguồn và thư mục chứa chúng cũng cần tên. Rồi còn tệp jar, war, ear. Ta cứ đặt tên mãi. Đã làm việc này nhiều đến thế, ta nên làm cho tốt. Dưới đây là vài quy tắc đơn giản để đặt tên hay.

## Dùng tên thể hiện ý định

Ai cũng có thể nói tên phải thể hiện ý định. Nhưng chúng tôi muốn bạn hiểu rằng chúng tôi thật sự nghiêm túc về chuyện này. Chọn tên tốt tốn thời gian, nhưng thời gian tiết kiệm được còn nhiều hơn. Vì vậy, hãy cân nhắc kỹ tên mình đặt và đổi tên khi tìm được tên hay hơn. Làm vậy, bất cứ ai đọc mã của bạn, kể cả chính bạn, cũng sẽ thấy dễ chịu hơn.

Tên của một biến, một hàm hay một lớp phải trả lời được những câu hỏi lớn: nó tồn tại để làm gì, nó làm gì và được dùng ra sao. Nếu phải viết chú thích mới hiểu được tên, thì cái tên ấy chưa thể hiện được ý định.

```java
int d; // thời gian trôi qua tính bằng ngày
```

Tên d chẳng nói lên điều gì. Nó không gợi đến thời gian đã trôi qua hay đến đơn vị ngày. Ta nên chọn tên cho biết đang đo điều gì và đo bằng đơn vị nào:

```java
int elapsedTimeInDays;
int daysSinceCreation;
int daysSinceModification;
int fileAgeInDays;
```

Tên thể hiện ý định giúp ta hiểu và sửa mã dễ hơn nhiều. Đoạn mã này dùng để làm gì?

```java
public List<int[]> getThem() {
    List<int[]> list1 = new ArrayList<int[]>();
    for (int[] x : theList)
        if (x[0] == 4)
            list1.add(x);
    return list1;
}
```

Vì sao khó nhận ra đoạn mã đang làm gì? Không có biểu thức phức tạp. Khoảng trắng và thụt lề đều hợp lý. Đoạn mã chỉ nhắc đến ba biến và hai hằng. Cũng chẳng có lớp cầu kỳ hay phương thức đa hình nào, chỉ có một danh sách các mảng, có vẻ vậy.

Vấn đề không nằm ở sự đơn giản của mã, mà ở tính hàm ẩn của nó, nếu cho phép chúng tôi dùng từ này: mức độ mà bối cảnh không được thể hiện rõ ngay trong mã. Đoạn mã ngầm yêu cầu ta biết câu trả lời cho những câu hỏi như:

1. theList chứa những thứ gì?
2. Chỉ số 0 của một phần tử trong theList có ý nghĩa gì?
3. Giá trị 4 có ý nghĩa gì?
4. Tôi sẽ dùng danh sách được trả về như thế nào?

Đoạn mã không trả lời những câu hỏi ấy, dù hoàn toàn có thể làm vậy. Giả sử ta đang làm một trò chơi dò mìn. Ta nhận ra bàn chơi là một danh sách các ô, hiện được gọi là theList. Hãy đổi tên nó thành gameBoard.

Mỗi ô trên bàn chơi được biểu diễn bằng một mảng đơn giản. Ta cũng nhận ra chỉ số 0 là vị trí chứa giá trị trạng thái, còn trạng thái 4 nghĩa là “đã cắm cờ”. Chỉ cần đặt tên cho những khái niệm đó, đoạn mã đã rõ ràng hơn nhiều:

```java
public List<int[]> getFlaggedCells() {
    List<int[]> flaggedCells = new ArrayList<int[]>();
    for (int[] cell : gameBoard)
        if (cell[STATUS_VALUE] == FLAGGED)
            flaggedCells.add(cell);
    return flaggedCells;
}
```

Độ đơn giản của mã không đổi. Số toán tử, số hằng và số mức lồng nhau đều giữ nguyên. Nhưng giờ mã đã tường minh hơn nhiều.

Ta còn có thể thay mảng int bằng một lớp đơn giản biểu diễn ô. Lớp đó có thể cung cấp một hàm thể hiện ý định, chẳng hạn isFlagged, để che đi các con số ma thuật. Khi ấy hàm sẽ thành:

```java
public List<Cell> getFlaggedCells() {
    List<Cell> flaggedCells = new ArrayList<Cell>();
    for (Cell cell : gameBoard)
        if (cell.isFlagged())
            flaggedCells.add(cell);
    return flaggedCells;
}
```

Chỉ đổi vài cái tên, ta đã dễ hiểu chuyện gì đang diễn ra hơn hẳn. Đó là sức mạnh của việc chọn tên tốt.

## Tránh tên gây hiểu lầm

Lập trình viên phải tránh để lại những manh mối sai khiến mã khó hiểu. Đừng dùng những từ mà nghĩa quen thuộc của chúng khác với điều ta muốn diễn đạt. Chẳng hạn, hp, aix và sco là tên biến tồi vì chúng cũng là tên các nền tảng hoặc biến thể Unix. Ngay cả khi viết mã tính cạnh huyền và thấy hp là cách viết tắt hợp lý, tên đó vẫn có thể gây hiểu lầm.

Đừng gọi một nhóm account là accountList trừ khi nó thực sự là một List. Với lập trình viên, từ list có nghĩa cụ thể. Nếu vật chứa các account không phải List, tên ấy có thể khiến người đọc hiểu sai.[^1] Dùng accountGroup, bunchOfAccounts hoặc đơn giản là accounts sẽ hợp lý hơn.

Cẩn thận với những cái tên chỉ khác nhau chút ít. Bạn mất bao lâu mới nhận ra khác biệt tinh vi giữa XYZControllerForEfficientHandlingOfStrings trong một module và XYZControllerForEfficientStorageOfStrings ở một chỗ khác? Hai cụm từ trông giống nhau đến đáng sợ.

Viết các khái niệm tương tự theo cùng một cách sẽ giúp người đọc có thêm thông tin. Viết không nhất quán lại khiến họ hiểu sai. Các môi trường Java hiện đại có tính năng tự động hoàn thành mã. Ta gõ vài ký tự của tên rồi nhấn một tổ hợp phím tắt nào đó, đôi khi chẳng cần nhấn gì, và nhận được danh sách các tên có thể hoàn thành. Danh sách sẽ hữu ích hơn nếu tên của những thứ gần giống nhau nằm cạnh nhau theo thứ tự chữ cái, còn điểm khác biệt thì dễ thấy. Nhà phát triển thường chọn đối tượng theo tên mà không đọc những chú thích dài của bạn, thậm chí không xem danh sách phương thức của lớp.

Một ví dụ tệ hại về tên gây hiểu lầm là dùng chữ l thường hoặc chữ O hoa làm tên biến, nhất là khi dùng cả hai. Chúng gần như không khác gì các hằng số 1 và 0.

```java
int a = l;
if ( O == l )
    a = O1;
else
    l = 01;
```

Có thể bạn nghĩ đây là ví dụ bịa, nhưng chúng tôi từng thấy những đoạn mã đầy những cái tên như vậy. Có lần, tác giả đề nghị đổi sang phông chữ khác để các ký tự trông khác nhau hơn. Giải pháp ấy sẽ phải được truyền lại cho mọi nhà phát triển về sau, bằng lời hoặc bằng văn bản. Đổi tên là đủ để xử lý dứt điểm vấn đề, không cần tạo thêm tài liệu hay sản phẩm nào.

## Tạo ra những khác biệt có nghĩa

Lập trình viên tự gây rắc rối khi viết mã chỉ để làm vừa lòng trình biên dịch hoặc trình thông dịch. Chẳng hạn, vì không thể dùng cùng một tên cho hai thứ khác nhau trong cùng phạm vi, ta có thể tùy tiện sửa một cái tên. Đôi khi người ta còn viết sai chính tả tên đó, dẫn đến tình huống trớ trêu: sửa lỗi chính tả xong thì mã không biên dịch được nữa.[^2]

Thêm dãy số hay từ nhiễu tuy làm trình biên dịch hài lòng, nhưng như thế chưa đủ. Nếu tên phải khác nhau thì ý nghĩa của chúng cũng phải khác nhau.

Đặt tên theo dãy số (a1, a2, .. aN) đi ngược lại việc đặt tên có chủ đích. Những tên như vậy không gây hiểu lầm, nhưng cũng chẳng cung cấp thông tin hay manh mối nào về ý định của tác giả. Xem ví dụ:

```java
public static void copyChars(char a1[], char a2[]) {
    for (int i = 0; i < a1.length; i++) {
        a2[i] = a1[i];
    }
}
```

Hàm này dễ đọc hơn nhiều nếu dùng source và destination làm tên đối số.

Từ nhiễu cũng tạo ra khác biệt vô nghĩa. Giả sử bạn có một lớp Product, rồi thêm lớp ProductInfo hoặc ProductData. Bạn đã làm tên khác nhau nhưng không làm ý nghĩa của chúng khác đi. Info và Data là những từ nhiễu mơ hồ, giống như a, an và the.

Dùng tiền tố như a và the không có gì sai nếu chúng tạo ra khác biệt có ý nghĩa. Chẳng hạn, bạn có thể dùng a cho mọi biến cục bộ và the cho mọi đối số của hàm.[^3] Vấn đề xuất hiện khi bạn gọi một biến là theZork chỉ vì đã có biến khác tên zork.

Từ nhiễu là phần thừa. Từ variable không nên xuất hiện trong tên biến, cũng như table không nên xuất hiện trong tên bảng. NameString hơn Name ở điểm nào? Name có khi nào lại là một số dấu phẩy động không? Nếu có thì cái tên ấy vi phạm quy tắc về tên gây hiểu lầm đã nói ở trên. Hãy tưởng tượng bạn gặp một lớp tên Customer và một lớp tên CustomerObject. Bạn sẽ hiểu hai lớp khác nhau ở điểm nào? Lớp nào giúp bạn tìm đến lịch sử thanh toán của khách hàng?

Có một ứng dụng chúng tôi biết minh họa rõ điều này. Chúng tôi đã đổi tên để không nêu đích danh người có lỗi, nhưng dạng lỗi thì vẫn nguyên như sau:

```java
getActiveAccount();
getActiveAccounts();
getActiveAccountInfo();
```

Làm sao lập trình viên trong dự án biết nên gọi hàm nào?

Nếu không có quy ước cụ thể, moneyAmount chẳng khác gì money, customerInfo chẳng khác gì customer, accountData chẳng khác gì account, còn theMessage chẳng khác gì message. Hãy đặt tên sao cho người đọc hiểu được sự khác biệt giữa chúng có ý nghĩa gì.

## Dùng tên đọc được

Con người giỏi xử lý từ ngữ. Một phần đáng kể bộ não dành cho khái niệm từ ngữ, mà từ ngữ thì có thể phát âm. Thật phí nếu không tận dụng phần lớn bộ não đã tiến hóa để xử lý ngôn ngữ nói. Vì vậy, hãy đặt những cái tên có thể phát âm được.

Tên khó phát âm khiến bạn khó bàn luận về nó mà không nghe như kẻ ngốc. “À, ở đằng này, trên cái bee cee arr three cee enn tee, chúng ta có một pee ess zee kyew int, thấy chưa?” Điều này quan trọng vì lập trình là hoạt động xã hội.

Có một công ty tôi biết dùng tên genymdhms (generation date, year, month, day, hour, minute, and second: ngày giờ sinh, năm, tháng, ngày, giờ, phút, giây), nên mọi người đi quanh đọc nó là “gen why emm dee aich emm ess”. Tôi có thói quen khó chịu là đọc mọi thứ đúng như cách viết, nên bắt đầu gọi nó là “gen-yah-mudda-hims”. Sau đó, nhiều nhà thiết kế và chuyên viên phân tích cũng gọi theo tôi. Nghe vẫn ngớ ngẩn, nhưng chúng tôi cùng hiểu câu đùa nên thấy vui. Dù vui hay không, chúng tôi vẫn đang chấp nhận một cách đặt tên tồi. Lập trình viên mới phải được giải thích các biến, rồi họ gọi chúng bằng những từ bịa ngớ ngẩn thay vì dùng thuật ngữ tiếng Anh đúng nghĩa. Hãy so sánh:

```java
class DtaRcrd102 {
    private Date genymdhms;
    private Date modymdhms;
    private final String pszqint = "102";
    /* ... */
};
```

với

```java
class Customer {
    private Date generationTimestamp;
    private Date modificationTimestamp;;
    private final String recordId = "102";
    /* ... */
};
```

Giờ ta có thể nói chuyện cho ra lẽ: “Này Mikey, xem bản ghi này đi! Dấu thời gian sinh lại được đặt vào ngày mai! Sao có thể thế được?”

## Dùng tên tìm kiếm được

Tên một chữ cái và hằng số có một nhược điểm: khó tìm trong một khối văn bản.

Ta có thể dễ dàng grep MAX_CLASSES_PER_STUDENT, nhưng tìm số 7 thì rắc rối hơn. Kết quả có thể cho ra chữ số đó trong tên tệp, định nghĩa các hằng khác, và đủ kiểu biểu thức dùng giá trị ấy với ý nghĩa khác. Còn tệ hơn nếu hằng là một số dài, ai đó đảo vị trí các chữ số, tạo ra lỗi mà công cụ tìm kiếm của lập trình viên không phát hiện được.

Tương tự, e là tên tồi cho một biến mà lập trình viên có thể cần tìm. Đây là chữ cái xuất hiện nhiều nhất trong tiếng Anh và có thể có mặt ở bất kỳ đoạn văn bản nào trong bất kỳ chương trình nào. Vì vậy, tên dài thường dễ tìm hơn tên ngắn, và tên nào tìm được cũng tốt hơn một hằng số viết trực tiếp trong mã.

Theo sở thích của tôi, tên một chữ cái CHỈ nên dùng cho biến cục bộ trong các phương thức ngắn. Độ dài tên nên tương ứng với kích thước phạm vi của nó [N5]. Nếu biến hay hằng có thể được thấy hoặc dùng ở nhiều chỗ trong khối mã, nhất thiết phải đặt cho nó một cái tên dễ tìm. Một lần nữa, hãy so sánh:

```java
for (int j=0; j<34; j++) {
    s += (t[j]*4)/5;
}
```

với

```java
int realDaysPerIdealDay = 4;
const int WORK_DAYS_PER_WEEK = 5;
int sum = 0;
for (int j=0; j < NUMBER_OF_TASKS; j++) {
    int realTaskDays = taskEstimate[j] * realDaysPerIdealDay;
    int realTaskWeeks = (realdays / WORK_DAYS_PER_WEEK);
    sum += realTaskWeeks;
}
```

Lưu ý, sum không phải cái tên hữu ích lắm, nhưng ít nhất có thể tìm được. Đoạn mã đặt tên có chủ đích dài hơn. Tuy nhiên, hãy nghĩ xem tìm WORK_DAYS_PER_WEEK dễ hơn bao nhiêu so với tìm mọi chỗ dùng số 5 rồi lọc ra những chỗ dùng nó đúng với ý nghĩa cần tìm.

## Tránh mã hóa trong tên

Ta đã phải xử lý đủ thứ mã hóa rồi, đừng tự tạo thêm gánh nặng. Mã hóa kiểu hoặc phạm vi vào tên chỉ khiến người đọc phải tốn công giải mã. Bắt mỗi nhân viên mới học thêm một “ngôn ngữ” mã hóa bên cạnh khối mã, thường khá lớn, mà họ phải làm việc cùng thì thật không hợp lý. Đó là gánh nặng tinh thần không cần thiết khi giải quyết vấn đề. Tên đã mã hóa thường khó phát âm và dễ gõ sai.

### Ký pháp Hungary

Ngày trước, khi làm việc với những ngôn ngữ giới hạn độ dài tên, ta đành vi phạm quy tắc này vì bắt buộc, và chẳng vui vẻ gì. Fortran buộc ta mã hóa bằng cách dùng chữ cái đầu làm ký hiệu kiểu dữ liệu. Các phiên bản BASIC đầu tiên chỉ cho phép một chữ cái cộng với một chữ số. Ký pháp Hungary (Hungarian Notation, HN) đẩy cách làm này đi xa hơn nhiều.

Thời Windows C API, HN được xem là khá quan trọng vì lúc ấy mọi thứ đều là handle kiểu integer, con trỏ long, con trỏ void, hoặc một trong vài cách hiện thực “string” với công dụng và thuộc tính khác nhau. Trình biên dịch khi đó không kiểm tra kiểu, nên lập trình viên cần một cái nạng để nhớ kiểu dữ liệu.

Ngôn ngữ hiện đại có hệ thống kiểu phong phú hơn nhiều, trình biên dịch ghi nhớ và kiểm tra kiểu. Lớp cũng có xu hướng nhỏ hơn, hàm ngắn hơn, nhờ vậy ta thường nhìn thấy chỗ khai báo của từng biến đang dùng.

Lập trình viên Java không cần mã hóa kiểu. Đối tượng có kiểu mạnh, còn môi trường soạn thảo phát hiện lỗi kiểu từ lâu trước khi bạn chạy biên dịch! Ngày nay, HN và các kiểu mã hóa dữ liệu khác chỉ cản trở công việc. Chúng khiến việc đổi tên hoặc đổi kiểu của biến, hàm hay lớp khó hơn, làm mã khó đọc hơn, và có thể khiến hệ thống mã hóa đánh lừa người đọc.

```java
PhoneNumber phoneString;
// tên không đổi khi kiểu đã đổi!
```

### Tiền tố cho biến thành viên

Bạn cũng không cần thêm tiền tố m_ vào biến thành viên nữa. Lớp và hàm nên đủ nhỏ để không cần tiền tố đó. Hãy dùng môi trường soạn thảo có thể làm nổi bật hoặc tô màu thành viên để phân biệt chúng.

```java
public class Part {
    private String m_dsc; // phần mô tả dạng văn bản
    void setName(String name) {
        m_dsc = name;
    }
}
```

---

```java
public class Part {
    String description;
    void setDescription(String description) {
        this.description = description;
    }
}
```

Hơn nữa, người ta nhanh chóng học cách bỏ qua tiền tố (hoặc hậu tố) để nhìn vào phần có nghĩa của tên. Càng đọc mã, ta càng ít để ý đến tiền tố. Rồi chúng thành đống lộn xộn vô hình và là dấu hiệu của mã cũ.

### Giao diện và lớp hiện thực

Đôi khi giao diện và lớp hiện thực cũng là một trường hợp mã hóa. Chẳng hạn, giả sử bạn đang xây dựng một ABSTRACT FACTORY để tạo hình. Factory này sẽ là giao diện, còn một lớp cụ thể sẽ hiện thực nó. Bạn nên đặt tên thế nào? IShapeFactory và ShapeFactory? Tôi thích để giao diện không có tiền tố trang trí. Chữ I ở đầu tên, vốn rất phổ biến trong những khối mã cũ ngày nay, gây xao nhãng trong trường hợp tốt nhất và thừa thông tin trong trường hợp xấu nhất. Tôi không muốn người dùng biết mình đang cung cấp cho họ một giao diện. Tôi chỉ muốn họ biết đó là ShapeFactory. Nếu buộc phải mã hóa tên giao diện hoặc lớp hiện thực, tôi sẽ chọn lớp hiện thực. Gọi nó là ShapeFactoryImp, hay thậm chí CShapeFactory đáng ghét, vẫn hơn là mã hóa giao diện.

## Tránh ánh xạ trong đầu

Người đọc không nên phải tự dịch tên bạn đặt sang những tên khác mà họ đã biết. Vấn đề thường xuất hiện khi ta chọn từ ngữ không thuộc miền bài toán lẫn miền giải pháp.

Tên biến một chữ cái là một ví dụ. Biến đếm vòng lặp có thể tên i, j hoặc k (nhưng đừng bao giờ dùng l!) nếu phạm vi của nó rất nhỏ và không xung đột với tên nào khác. Các tên một chữ cái này đã thành quy ước cho biến đếm vòng lặp. Tuy nhiên, ở hầu hết bối cảnh khác, tên một chữ cái là lựa chọn tồi: nó chỉ là chỗ trống để người đọc tự liên hệ với khái niệm thật trong đầu. Không có lý do nào tệ hơn để đặt tên c ngoài chuyện a và b đã bị dùng mất.

Nói chung, lập trình viên khá thông minh. Người thông minh đôi khi thích khoe khả năng xoay xở trong đầu. Nếu bạn có thể nhớ chắc rằng r là phiên bản viết thường của url sau khi bỏ host và scheme, hẳn bạn rất thông minh.

Lập trình viên chuyên nghiệp khác lập trình viên thông minh ở chỗ họ hiểu rằng sự rõ ràng quan trọng hơn cả. Họ dùng năng lực của mình vào việc có ích và viết mã để người khác hiểu được.

## Tên lớp

Lớp và đối tượng nên có tên là danh từ hoặc cụm danh từ, chẳng hạn Customer, WikiPage, Account và AddressParser. Tránh những từ như Manager, Processor, Data hay Info trong tên lớp. Tên lớp không nên là động từ.

## Tên phương thức

Phương thức nên có tên là động từ hoặc cụm động từ, chẳng hạn postPayment, deletePage hay save. Accessor, mutator và predicate nên được đặt tên theo giá trị của chúng, với tiền tố get, set và is theo chuẩn javabean.[^4]

```java
string name = employee.getName();
customer.setName("mike");
if (paycheck.isPosted())...
```

Khi nạp chồng hàm khởi tạo, hãy dùng các phương thức factory tĩnh có tên mô tả đối số. Ví dụ:

```java
Complex fulcrumPoint = Complex.FromRealNumber(23.0);
```

thường tốt hơn:

```java
Complex fulcrumPoint = new Complex(23.0);
```

Hãy cân nhắc buộc người dùng gọi các phương thức ấy bằng cách đặt những hàm khởi tạo tương ứng ở mức private.

## Đừng tỏ ra dí dỏm

Tên quá khéo léo chỉ dễ nhớ với những người có cùng khiếu hài hước với tác giả, và chỉ khi họ còn nhớ câu đùa. Họ có biết hàm tên HolyHandGrenade dùng để làm gì không? Đúng là nghe vui, nhưng ở đây DeleteItems có lẽ sẽ là cái tên tốt hơn. Hãy chọn sự rõ ràng thay vì tính giải trí.

Tên dí dỏm trong mã thường là tiếng lóng hoặc cách nói thông tục. Chẳng hạn, đừng dùng whack() với nghĩa kill(). Cũng đừng đưa vào những câu đùa nhỏ phụ thuộc vào văn hóa như eatMyShorts() với nghĩa abort().

Nói đúng ý mình. Giữ đúng lời mình nói.

## Mỗi khái niệm chọn một từ

Hãy chọn một từ cho mỗi khái niệm trừu tượng rồi dùng nhất quán. Chẳng hạn, thật khó hiểu nếu các lớp khác nhau có những phương thức tương đương tên fetch, retrieve và get. Làm sao bạn nhớ tên nào đi với lớp nào? Tiếc là thường phải nhớ công ty, nhóm hay cá nhân nào viết thư viện hoặc lớp đó mới biết họ dùng thuật ngữ nào. Nếu không, bạn sẽ mất nhiều thời gian xem các tệp header và những ví dụ mã cũ.

Các môi trường soạn thảo hiện đại như Eclipse và IntelliJ cung cấp gợi ý theo ngữ cảnh, chẳng hạn danh sách phương thức có thể gọi trên một đối tượng. Nhưng danh sách ấy thường không hiển thị chú thích bạn viết quanh tên hàm và danh sách tham số. May ra nó cho thấy tên tham số trong khai báo hàm. Tên hàm phải tự đứng vững và nhất quán để bạn chọn đúng phương thức mà không cần tìm hiểu thêm.

Tương tự, thật khó hiểu khi cùng một code base có controller, manager và driver. Khác biệt cốt yếu giữa DeviceManager và ProtocolController là gì? Sao cả hai không cùng là controller hoặc cùng là manager? Thật ra chúng có phải đều là Driver không? Tên gọi khiến bạn nghĩ hai đối tượng khác xa nhau về kiểu lẫn lớp.

Từ vựng nhất quán là món quà lớn dành cho những lập trình viên phải dùng mã của bạn.

## Đừng chơi chữ

Tránh dùng cùng một từ cho hai mục đích. Dùng một thuật ngữ cho hai ý tưởng khác nhau về bản chất chính là chơi chữ.

Nếu theo quy tắc “mỗi khái niệm một từ”, bạn có thể có nhiều lớp cùng có phương thức add. Chừng nào danh sách tham số và giá trị trả về của các phương thức add còn tương đương về ngữ nghĩa thì không có vấn đề gì.

Tuy nhiên, đôi khi người ta dùng từ add để tạo “tính nhất quán” dù thực chất không thêm theo cùng một nghĩa. Giả sử ta có nhiều lớp trong đó add tạo ra giá trị mới bằng cách cộng hoặc nối hai giá trị có sẵn. Giờ ta viết một lớp mới có phương thức đưa đối số duy nhất của nó vào một collection. Có nên gọi phương thức ấy là add không? Nghe có vẻ nhất quán vì đã có nhiều phương thức add, nhưng ngữ nghĩa ở đây khác. Ta nên dùng tên như insert hoặc append. Gọi phương thức mới là add sẽ thành chơi chữ.

Với tư cách tác giả, mục tiêu của chúng ta là làm cho mã dễ hiểu hết mức có thể. Ta muốn người đọc lướt qua là nắm được, không phải nghiền ngẫm. Ta nên theo cách viết sách phổ thông: tác giả có trách nhiệm diễn đạt rõ ràng, chứ không theo lối học thuật, nơi học giả phải đào bới ý nghĩa từ trang giấy.

## Dùng tên thuộc miền giải pháp

Hãy nhớ người đọc mã của bạn là lập trình viên. Vì vậy, cứ dùng thuật ngữ khoa học máy tính (CS), tên thuật toán, tên pattern, thuật ngữ toán học, vân vân. Không nên lấy mọi tên từ miền bài toán, vì ta không muốn đồng nghiệp cứ phải chạy đi hỏi khách hàng mỗi cái tên nghĩa là gì trong khi họ đã biết khái niệm ấy dưới một tên khác.

Tên AccountVisitor gợi nhiều ý nghĩa cho lập trình viên biết pattern VISITOR. Lập trình viên nào lại không biết JobQueue là gì? Lập trình viên phải làm nhiều việc mang tính kỹ thuật. Thường nên chọn tên kỹ thuật cho những việc đó.

## Dùng tên thuộc miền bài toán

Khi không có thuật ngữ lập trình phù hợp với việc đang làm, hãy dùng tên trong miền bài toán. Ít ra, lập trình viên bảo trì mã của bạn có thể hỏi chuyên gia nghiệp vụ để biết nó nghĩa là gì.

Phân biệt khái niệm thuộc miền giải pháp với khái niệm thuộc miền bài toán là một phần công việc của lập trình viên và nhà thiết kế giỏi. Đoạn mã nào gắn nhiều hơn với khái niệm miền bài toán thì nên dùng tên lấy từ miền đó.

## Thêm bối cảnh có nghĩa

Một số tên tự thân đã có nghĩa, nhưng phần lớn thì không. Hãy đặt tên vào bối cảnh để người đọc hiểu chúng, chẳng hạn bằng cách đưa chúng vào những lớp, hàm hoặc namespace có tên rõ ràng. Nếu mọi cách khác đều không hiệu quả, thêm tiền tố cho tên có thể là giải pháp cuối cùng.

Hãy tưởng tượng bạn có các biến firstName, lastName, street, houseNumber, city, state và zipcode. Đặt cạnh nhau, chúng rõ ràng tạo thành một địa chỉ. Nhưng nếu chỉ thấy biến state được dùng riêng trong một phương thức thì sao? Bạn có tự hiểu nó là một phần của địa chỉ không?

Có thể thêm bối cảnh bằng tiền tố: addrFirstName, addrLastName, addrState, vân vân. Như vậy, ít nhất người đọc biết các biến thuộc về một cấu trúc lớn hơn. Tốt hơn nữa là tạo lớp Address. Khi ấy, ngay cả trình biên dịch cũng biết các biến thuộc về một khái niệm rộng hơn.

Xem phương thức trong Đoạn mã 2-1. Các biến có cần bối cảnh rõ hơn không? Tên hàm chỉ cho biết một phần bối cảnh, phần còn lại nằm trong thuật toán. Đọc hết hàm, bạn sẽ thấy number, verb và pluralModifier là ba biến thuộc về thông điệp “thống kê phỏng đoán”. Tiếc là người đọc phải tự suy ra bối cảnh ấy. Mới nhìn vào phương thức, ý nghĩa các biến còn rất mờ nhạt.

**Đoạn mã 2-1**
**Các biến có bối cảnh không rõ ràng.**

```java
private void printGuessStatistics(char candidate, int count) {
    String number;
    String verb;
    String pluralModifier;
    if (count == 0) {
        number = "no";
        verb = "are";
        pluralModifier = "s";
    } else if (count == 1) {
        number = "1";
        verb = "is";
        pluralModifier = "";
    } else {
        number = Integer.toString(count);
        verb = "are";
        pluralModifier = "s";
    }
    String guessMessage = String.format(
        "There %s %s %s%s", verb, number, candidate, pluralModifier
    );
    print(guessMessage);
}
```

Hàm hơi dài, còn các biến được dùng xuyên suốt. Muốn tách hàm thành những phần nhỏ hơn, ta cần tạo lớp GuessStatisticsMessage rồi chuyển ba biến thành các trường của lớp. Nhờ đó, ba biến có bối cảnh rõ ràng: chúng chắc chắn thuộc về GuessStatisticsMessage. Bối cảnh rõ hơn cũng giúp ta chia thuật toán thành nhiều hàm nhỏ và làm nó gọn gàng hơn. (Xem Đoạn mã 2-2.)

**Đoạn mã 2-2**
**Các biến có bối cảnh.**

```java
public class GuessStatisticsMessage {
    private String number;
    private String verb;
    private String pluralModifier;

    public String make(char candidate, int count) {
        createPluralDependentMessageParts(count);
        return String.format(
            "There %s %s %s%s",
            verb, number, candidate, pluralModifier );
    }

    private void createPluralDependentMessageParts(int count) {
        if (count == 0) {
            thereAreNoLetters();
        } else if (count == 1) {
            thereIsOneLetter();
        } else {
            thereAreManyLetters(count);
        }
    }

    private void thereAreManyLetters(int count) {
        number = Integer.toString(count);
        verb = "are";
        pluralModifier = "s";
    }

    private void thereIsOneLetter() {
        number = "1";
        verb = "is";
        pluralModifier = "";
    }

    private void thereAreNoLetters() {
        number = "no";
        verb = "are";
        pluralModifier = "s";
    }
}
```

## Đừng thêm bối cảnh vô cớ

Trong ứng dụng tưởng tượng tên “Gas Station Deluxe”, thêm tiền tố GSD vào tên mọi lớp là một ý tồi. Nói thẳng ra, làm thế là chống lại chính công cụ của bạn. Gõ G rồi nhấn phím hoàn thành, bạn sẽ nhận một danh sách dài dằng dặc gồm mọi lớp trong hệ thống. Có khôn ngoan không? Sao lại khiến IDE khó hỗ trợ bạn hơn?

Tương tự, giả sử bạn tạo lớp MailingAddress trong module kế toán của GSD và gọi nó là GSDAccountAddress. Sau này, ứng dụng liên hệ khách hàng cần một địa chỉ gửi thư. Bạn có dùng GSDAccountAddress không? Tên đó nghe có đúng không? Mười trong số mười bảy ký tự là thừa hoặc không liên quan.

Nhìn chung, tên ngắn tốt hơn tên dài nếu vẫn rõ nghĩa. Đừng thêm bối cảnh nhiều hơn mức cần thiết.

accountAddress và customerAddress là những tên hợp lý cho các đối tượng thuộc lớp Address, nhưng có thể là tên tồi cho lớp. Address là tên lớp phù hợp. Nếu cần phân biệt địa chỉ MAC, địa chỉ cổng và địa chỉ Web, tôi có thể chọn PostalAddress, MAC và URI. Các tên này chính xác hơn, đó cũng là mục đích của việc đặt tên.

## Lời cuối

Điều khó nhất khi chọn tên hay là cần có khả năng mô tả tốt và nền tảng văn hóa chung. Đây là vấn đề dạy và học, không phải vấn đề kỹ thuật, kinh doanh hay quản lý. Vì vậy, nhiều người trong ngành không học được cách làm việc này cho tốt.

Người ta cũng ngại đổi tên vì sợ nhà phát triển khác phản đối. Chúng tôi không ngại như vậy, và thật sự biết ơn mỗi khi tên được đổi theo hướng tốt hơn. Phần lớn thời gian, ta không cần ghi nhớ tên lớp và phương thức. Công cụ hiện đại lo những chi tiết ấy, để ta tập trung xem mã có đọc như đoạn văn, câu văn, hoặc ít nhất như bảng và cấu trúc dữ liệu hay không. (Câu văn không phải lúc nào cũng là cách tốt nhất để trình bày dữ liệu.) Khi đổi tên, có lẽ bạn sẽ làm ai đó ngạc nhiên, cũng như khi thực hiện bất kỳ cải tiến mã nào khác. Đừng để chuyện đó cản bước.

Hãy thử áp dụng một vài quy tắc này để xem khả năng đọc mã có cải thiện không. Nếu đang bảo trì mã của người khác, hãy dùng công cụ tái cấu trúc để xử lý những vấn đề ấy. Công sức bỏ ra sẽ có ích trước mắt và cả về sau.

[^1]: Như sẽ thấy ở phần sau, kể cả khi vật chứa là một List, có lẽ vẫn không nên mã hóa kiểu vật chứa vào tên.

[^2]: Hãy nghĩ đến thói quen thật kinh khủng là tạo biến tên klass chỉ vì tên class đã được dùng cho thứ khác.

[^3]: Uncle Bob từng làm vậy trong C++ nhưng đã bỏ thói quen này vì các IDE hiện đại khiến nó không còn cần thiết.

[^4]: http://java.sun.com/products/javabeans/docs/spec.html
