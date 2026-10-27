# Chương 26: Thành phần Main
![Minh họa](assets/illustrations/26-chuong-26-opener.png){w=300}

Trong mọi hệ thống đều có ít nhất một thành phần tạo ra, điều phối và giám sát các thành phần khác. Tôi gọi thành phần này là `Main`.

## Chi tiết tối hậu

Thành phần `Main` là chi tiết tối hậu, chính sách cấp thấp nhất. Đây là điểm vào ban đầu của hệ thống. Không có gì ngoài hệ điều hành phụ thuộc vào nó. Nhiệm vụ của nó là tạo mọi Factory, Strategy và tiện ích toàn cục khác, rồi chuyển quyền điều khiển cho những phần trừu tượng cấp cao của hệ thống.

Chính trong thành phần `Main`, framework tiêm phụ thuộc nên đưa các phụ thuộc vào hệ thống. Sau khi được tiêm vào `Main`, các phụ thuộc nên được phân phối theo cách thông thường, không dùng framework.

Hãy xem `Main` là thành phần bẩn nhất trong tất cả các thành phần bẩn.

Dưới đây là thành phần `Main` trong một phiên bản gần đây của *Hunt the Wumpus*. Hãy chú ý cách nó nạp tất cả các chuỗi mà ta không muốn phần mã chính phải biết.

```java
public class Main implements HtwMessageReceiver {
private static HuntTheWumpus game;
private static int hitPoints = 10;
private static final List<String> caverns = new ArrayList<>();
private static final String[] environments = new String[]{
"bright",
"humid",
"dry",
"creepy",
"ugly",
"foggy",
"hot",
"cold",
"drafty",
"dreadful"
};

private static final String[] shapes = new String[] {
"round",
"square",
"oval",
"irregular",
"long",
"craggy",
"rough",
"tall",
"narrow"
};

private static final String[] cavernTypes = new String[] {
"cavern",
"room",
"chamber",
"catacomb",
"crevasse",
"cell",
"tunnel",
"passageway",
"hall",
"expanse"
};

private static final String[] adornments = new String[] {
"smelling of sulfur",
"with engravings on the walls",
"with a bumpy floor",
"",
"littered with garbage",
"spattered with guano",
"with piles of Wumpus droppings",
"with bones scattered around",
"with a corpse on the floor",
"that seems to vibrate",
"that feels stuffy",
"that fills you with dread"
};
```

Tiếp theo là hàm chính. Hãy chú ý cách nó dùng `HtwFactory` để tạo trò chơi. Nó truyền vào tên lớp `htw.game.HuntTheWumpusFacade`, vì lớp đó còn bẩn hơn cả `Main`. Nhờ vậy, thay đổi trong lớp đó không buộc `Main` phải biên dịch lại hay triển khai lại.

```java
public static void main(String[] args) throws IOException {
game = HtwFactory.makeGame("htw.game.HuntTheWumpusFacade",
new Main());
createMap();
BufferedReader br =
new BufferedReader(new InputStreamReader(System.in));
game.makeRestCommand().execute();
while (true) {
System.out.println(game.getPlayerCavern());
System.out.println("Health: " + hitPoints + " arrows: " +
game.getQuiver());
HuntTheWumpus.Command c = game.makeRestCommand();
System.out.println(">");
String command = br.readLine();
if (command.equalsIgnoreCase("e"))
c = game.makeMoveCommand(EAST);
else if (command.equalsIgnoreCase("w"))
c = game.makeMoveCommand(WEST);
else if (command.equalsIgnoreCase("n"))
c = game.makeMoveCommand(NORTH);
else if (command.equalsIgnoreCase("s"))
c = game.makeMoveCommand(SOUTH);
else if (command.equalsIgnoreCase("r"))
c = game.makeRestCommand();
else if (command.equalsIgnoreCase("sw"))
c = game.makeShootCommand(WEST);
else if (command.equalsIgnoreCase("se"))
c = game.makeShootCommand(EAST);
else if (command.equalsIgnoreCase("sn"))
c = game.makeShootCommand(NORTH);
else if (command.equalsIgnoreCase("ss"))
c = game.makeShootCommand(SOUTH);
else if (command.equalsIgnoreCase("q"))
return;

c.execute();
}
}
```

Cũng cần lưu ý rằng `main` tạo luồng đầu vào và chứa vòng lặp chính của trò chơi. Nó diễn giải các lệnh đầu vào đơn giản nhưng giao toàn bộ phần xử lý cho các thành phần cấp cao hơn.

Cuối cùng, hãy chú ý rằng `main` tạo bản đồ.

```java
private static void createMap() {
int nCaverns = (int) (Math.random() * 30.0 + 10.0);
while (nCaverns-- > 0)
caverns.add(makeName());

for (String cavern : caverns) {
maybeConnectCavern(cavern, NORTH);
maybeConnectCavern(cavern, SOUTH);
maybeConnectCavern(cavern, EAST);
maybeConnectCavern(cavern, WEST);
}

String playerCavern = anyCavern();
game.setPlayerCavern(playerCavern);
game.setWumpusCavern(anyOther(playerCavern));
game.addBatCavern(anyOther(playerCavern));
game.addBatCavern(anyOther(playerCavern));
game.addBatCavern(anyOther(playerCavern));

game.addPitCavern(anyOther(playerCavern));
game.addPitCavern(anyOther(playerCavern));
game.addPitCavern(anyOther(playerCavern));

game.setQuiver(5);
}
// much code removed…
}
```

Điểm chính là `Main` là mô-đun bẩn, cấp thấp, nằm ở vòng tròn ngoài cùng của Kiến trúc Sạch. Nó nạp mọi thứ cần thiết cho hệ thống cấp cao, rồi chuyển quyền điều khiển cho hệ thống đó.

## Kết luận

Hãy xem `Main` như một plugin của ứng dụng, plugin thiết lập các điều kiện và cấu hình ban đầu, thu thập tài nguyên bên ngoài, rồi chuyển quyền điều khiển cho chính sách cấp cao của ứng dụng. Vì là plugin, ứng dụng có thể có nhiều thành phần `Main`, mỗi thành phần dành cho một cấu hình.

Chẳng hạn, bạn có thể có một plugin `Main` cho môi trường phát triển, một plugin khác cho kiểm thử và một plugin nữa cho môi trường production. Bạn cũng có thể có một plugin `Main` cho từng quốc gia triển khai, từng khu vực pháp lý hoặc từng khách hàng.

Khi xem `Main` như thành phần plugin nằm sau một ranh giới kiến trúc, vấn đề cấu hình sẽ dễ giải quyết hơn nhiều.