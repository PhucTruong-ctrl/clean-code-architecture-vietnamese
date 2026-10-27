# Chương 19: Chính sách và cấp độ

Hệ thống phần mềm là những tuyên bố về chính sách. Thực ra, cốt lõi của chương trình máy tính chỉ có vậy. Một chương trình máy tính mô tả chi tiết chính sách dùng để chuyển đổi đầu vào thành đầu ra.

Trong hầu hết các hệ thống không tầm thường, chính sách có thể được chia thành nhiều chính sách nhỏ hơn. Một số mô tả cách tính các quy tắc nghiệp vụ cụ thể. Số khác mô tả cách định dạng báo cáo. Những chính sách khác nữa quy định cách xác thực dữ liệu đầu vào.

Một phần nghệ thuật xây dựng kiến trúc phần mềm là tách các chính sách đó một cách cẩn thận, rồi nhóm lại theo cách chúng thay đổi. Những chính sách thay đổi vì cùng lý do và cùng thời điểm thuộc cùng cấp độ, nên được đặt chung trong một thành phần. Những chính sách thay đổi vì lý do khác nhau hoặc vào thời điểm khác nhau thuộc các cấp độ khác nhau, nên cần được tách thành các thành phần riêng.

Nghệ thuật kiến trúc thường bao gồm việc tổ chức lại các thành phần thành một đồ thị có hướng không chu trình. Các nút của đồ thị là những thành phần chứa các chính sách cùng cấp độ. Các cạnh có hướng biểu thị quan hệ phụ thuộc giữa những thành phần đó, nối các thành phần ở những cấp độ khác nhau.

Đó là các phụ thuộc mã nguồn, tức phụ thuộc lúc biên dịch. Trong Java, chúng là các câu lệnh `import`. Trong C#, chúng là các câu lệnh `using`. Trong Ruby, chúng là các câu lệnh `require`. Đây là những phụ thuộc cần thiết để trình biên dịch hoạt động.

Trong một kiến trúc tốt, hướng của các phụ thuộc dựa trên cấp độ của những thành phần mà chúng nối với nhau. Trong mọi trường hợp, thành phần cấp thấp được thiết kế để phụ thuộc vào thành phần cấp cao.

## Cấp độ

Định nghĩa chặt chẽ của “cấp độ” là “khoảng cách đến đầu vào và đầu ra”. Một chính sách càng cách xa cả đầu vào lẫn đầu ra của hệ thống thì cấp độ của nó càng cao. Các chính sách quản lý đầu vào và đầu ra là những chính sách cấp thấp nhất trong hệ thống.

Sơ đồ luồng dữ liệu ở Hình 19.1 mô tả một chương trình mã hóa đơn giản: chương trình đọc ký tự từ thiết bị đầu vào, dùng một bảng để chuyển đổi ký tự, rồi ghi ký tự đã chuyển đổi ra thiết bị đầu ra. Luồng dữ liệu được biểu diễn bằng các mũi tên liền cong. Các phụ thuộc mã nguồn được thiết kế đúng được biểu diễn bằng những đường nét đứt thẳng.

**Hình 19.1** Một chương trình mã hóa đơn giản

Thành phần `Translate` là thành phần cấp cao nhất trong hệ thống này vì nó nằm xa đầu vào và đầu ra nhất.[^1]

Lưu ý rằng luồng dữ liệu và phụ thuộc mã nguồn không phải lúc nào cũng cùng hướng. Đây cũng là một phần của nghệ thuật kiến trúc phần mềm. Chúng ta muốn tách phụ thuộc mã nguồn khỏi luồng dữ liệu và gắn chúng với cấp độ.

Sẽ rất dễ tạo ra một kiến trúc sai nếu viết chương trình mã hóa như sau:

```
function encrypt() {
    while (true)
        writeChar(translate(readChar()));
}
```

Đây là kiến trúc sai vì hàm cấp cao `encrypt` phụ thuộc vào các hàm cấp thấp `readChar` và `writeChar`.

Một kiến trúc tốt hơn cho hệ thống này được thể hiện trong sơ đồ lớp ở Hình 19.2. Hãy chú ý đường viền nét đứt bao quanh lớp `Encrypt` và các giao diện `CharWriter` và `CharReader`. Mọi phụ thuộc đi qua đường viền đều hướng vào trong. Đây là đơn vị cấp cao nhất của hệ thống.

**Hình 19.2** Sơ đồ lớp thể hiện kiến trúc tốt hơn cho hệ thống

Ở đây, `ConsoleReader` và `ConsoleWriter` được thể hiện dưới dạng các lớp. Chúng ở cấp thấp vì nằm gần đầu vào và đầu ra.

Cấu trúc này tách chính sách mã hóa cấp cao khỏi các chính sách đầu vào/đầu ra cấp thấp. Nhờ đó, chính sách mã hóa có thể được dùng trong nhiều bối cảnh khác nhau. Khi các chính sách đầu vào và đầu ra thay đổi, chính sách mã hóa ít có khả năng bị ảnh hưởng.

Hãy nhớ rằng các chính sách được nhóm thành thành phần dựa trên cách chúng thay đổi. SRP và CCP nhóm chung những chính sách thay đổi vì cùng lý do và cùng thời điểm. Các chính sách cấp cao, tức những chính sách xa đầu vào và đầu ra nhất, thường thay đổi ít thường xuyên hơn và vì những lý do quan trọng hơn so với chính sách cấp thấp. Các chính sách cấp thấp, tức những chính sách gần đầu vào và đầu ra nhất, thường thay đổi thường xuyên và cấp bách hơn, nhưng vì những lý do ít quan trọng hơn.

Chẳng hạn, ngay cả trong ví dụ đơn giản về chương trình mã hóa, thiết bị IO có khả năng thay đổi cao hơn nhiều so với thuật toán mã hóa. Nếu thuật toán mã hóa thay đổi, nguyên nhân thường sẽ quan trọng hơn việc thay đổi một thiết bị IO.

Giữ các chính sách này tách biệt, với mọi phụ thuộc mã nguồn hướng về các chính sách cấp cao hơn, sẽ giảm ảnh hưởng của thay đổi. Những thay đổi nhỏ nhưng cấp bách ở các cấp thấp nhất của hệ thống ít hoặc không ảnh hưởng đến các cấp cao hơn, quan trọng hơn.

Một cách khác để nhìn nhận vấn đề này là xem các thành phần cấp thấp như plugin của thành phần cấp cao. Sơ đồ thành phần ở Hình 19.3 thể hiện cách bố trí đó. Thành phần `Encryption` không biết gì về thành phần `IODevices`; thành phần `IODevices` phụ thuộc vào `Encryption`.

**Hình 19.3** Các thành phần cấp thấp nên cắm vào thành phần cấp cao

## Kết luận

Cho đến đây, phần thảo luận về chính sách đã kết hợp nhiều nguyên tắc: Nguyên tắc Trách nhiệm Đơn nhất, Nguyên tắc Đóng-Mở, Nguyên tắc Đóng chung, Nguyên tắc Đảo ngược Phụ thuộc, Nguyên tắc Phụ thuộc Ổn định và Nguyên tắc Trừu tượng Ổn định. Hãy nhìn lại và thử xác định mỗi nguyên tắc được dùng ở đâu và vì sao.

[^1]: Meilir Page-Jones gọi thành phần này là “Central Transform” trong cuốn *The Practical Guide to Structured Systems Design*, ấn bản thứ hai (Yourdon Press, 1988).