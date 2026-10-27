# Chương 15: Bên trong JUnit

JUnit là một trong những framework Java nổi tiếng nhất. Xét theo các framework, nó đơn giản trong ý tưởng, chính xác trong định nghĩa và tao nhã trong cách triển khai. Nhưng mã nguồn trông như thế nào? Trong chương này, chúng ta sẽ phê bình một ví dụ lấy từ framework JUnit.

## Framework JUnit

JUnit có nhiều tác giả, nhưng nó bắt đầu từ Kent Beck và Eric Gamma trên một chuyến bay đến Atlanta. Kent muốn học Java, còn Eric muốn tìm hiểu framework kiểm thử Smalltalk của Kent. “Còn gì tự nhiên hơn với hai kẻ mê máy tính trong không gian chật hẹp là lấy máy tính xách tay ra và bắt đầu lập trình?”¹ Sau ba giờ làm việc ở độ cao lớn, họ đã viết xong những phần cơ bản của JUnit.

Mô-đun chúng ta sẽ xem xét là đoạn mã thông minh giúp xác định lỗi khi so sánh chuỗi. Mô-đun này có tên ComparisonCompactor. Khi được cho hai chuỗi khác nhau, chẳng hạn ABCDE và ABXDE, nó sẽ làm lộ ra điểm khác biệt bằng cách tạo chuỗi như <...B[X]D...>.

Tôi có thể giải thích thêm, nhưng các ca kiểm thử làm việc đó tốt hơn. Vậy hãy xem Đoạn mã 15-1, bạn sẽ hiểu sâu các yêu cầu của mô-đun này. Nhân tiện, hãy phê bình cấu trúc của các bài kiểm thử. Chúng có thể đơn giản hơn hoặc dễ hiểu hơn không?

**Đoạn mã 15-1**  
**ComparisonCompactorTest.java**

```java
package junit.tests.framework;

import junit.framework.ComparisonCompactor;
import junit.framework.TestCase;
public class ComparisonCompactorTest extends TestCase {

   public void testMessage() {
     String failure= new ComparisonCompactor(0, "b", "c").compact("a");
     assertTrue("a expected:<[b]> but was:<[c]>".equals(failure));
   }
   public void testStartSame() {
     String failure= new ComparisonCompactor(1, "ba", "bc").compact(null);
     assertEquals("expected:<b[a]> but was:<b[c]>", failure);
   }

   public void testEndSame() {
     String failure= new ComparisonCompactor(1, "ab", "cb").compact(null);
     assertEquals("expected:<[a]b> but was:<[c]b>", failure);
   }

   public void testSame() {
     String failure= new ComparisonCompactor(1, "ab", "ab").compact(null);
     assertEquals("expected:<ab> but was:<ab>", failure);
   }

   public void testNoContextStartAndEndSame() {
     String failure= new ComparisonCompactor(0, "abc", "adc").compact(null);
     assertEquals("expected:<...[b]...> but was:<...[d]...>", failure);
   }

   public void testStartAndEndContext() {
     String failure= new ComparisonCompactor(1, "abc", "adc").compact(null);
     assertEquals("expected:<a[b]c> but was:<a[d]c>", failure);
   }

   public void testStartAndEndContextWithEllipses() {
     String failure=
        new ComparisonCompactor(1, "abcde", "abfde").compact(null);
     assertEquals("expected:<...b[c]d...> but was:<...b[f]d...>", failure);
   }
   public void testComparisonErrorStartSameComplete() {
     String failure= new ComparisonCompactor(2, "ab", "abc").compact(null);
     assertEquals("expected:<ab[]> but was:<ab[c]>", failure);
   }

   public void testComparisonErrorEndSameComplete() {
     String failure= new ComparisonCompactor(0, "bc", "abc").compact(null);
     assertEquals("expected:<[]...> but was:<[a]...>", failure);
   }

   public void testComparisonErrorEndSameCompleteContext() {
     String failure= new ComparisonCompactor(2, "bc", "abc").compact(null);
     assertEquals("expected:<[]bc> but was:<[a]bc>", failure);
   }

   public void testComparisonErrorOverlapingMatches() {
     String failure= new ComparisonCompactor(0, "abc", "abbc").compact(null);
     assertEquals("expected:<...[]...> but was:<...[b]...>", failure);
   }

   public void testComparisonErrorOverlapingMatchesContext() {
     String failure= new ComparisonCompactor(2, "abc", "abbc").compact(null);
     assertEquals("expected:<ab[]c> but was:<ab[b]c>", failure);
   }
   public void testComparisonErrorOverlapingMatches2() {
      String failure= new ComparisonCompactor(0, "abcdde",
 "abcde").compact(null);
      assertEquals("expected:<...[d]...> but was:<...[]...>", failure);
   }
   public void testComparisonErrorOverlapingMatches2Context() {
     String failure=
        new ComparisonCompactor(2, "abcdde", "abcde").compact(null);
     assertEquals("expected:<...cd[d]e> but was:<...cd[]e>", failure);
   }

   public void testComparisonErrorWithActualNull() {
     String failure= new ComparisonCompactor(0, "a", null).compact(null);
     assertEquals("expected:<a> but was:<null>", failure);
   }

   public void testComparisonErrorWithActualNullContext() {
     String failure= new ComparisonCompactor(2, "a", null).compact(null);
     assertEquals("expected:<a> but was:<null>", failure);
   }

   public void testComparisonErrorWithExpectedNull() {
     String failure= new ComparisonCompactor(0, null, "a").compact(null);
     assertEquals("expected:<null> but was:<a>", failure);
   }

   public void testComparisonErrorWithExpectedNullContext() {
     String failure= new ComparisonCompactor(2, null, "a").compact(null);
     assertEquals("expected:<null> but was:<a>", failure);
   }

   public void testBug609972() {
     String failure= new ComparisonCompactor(10, "S&P500", "0").compact(null);
     assertEquals("expected:<[S&P50]0> but was:<[]0>", failure);
   }
}
```

¹. *JUnit Pocket Guide*, Kent Beck, O’Reilly, 2004, tr. 43.

Tôi đã chạy phân tích độ bao phủ mã trên ComparisonCompactor bằng các bài kiểm thử này. Mã được bao phủ 100 phần trăm. Mọi dòng mã, mọi câu lệnh if và vòng lặp for đều được các bài kiểm thử thực thi. Điều này khiến tôi rất tin tưởng rằng mã hoạt động đúng và rất kính trọng tay nghề của các tác giả.

Mã của ComparisonCompactor nằm trong Đoạn mã 15-2. Hãy dành chút thời gian xem qua mã này. Tôi nghĩ bạn sẽ thấy nó được phân chia khá hợp lý, diễn đạt tương đối rõ ràng và có cấu trúc đơn giản. Khi xem xong, chúng ta sẽ cùng bắt bẻ vài điểm nhỏ.

**Đoạn mã 15-2**  
**ComparisonCompactor.java (Bản gốc)**

```java
package junit.framework;
public class ComparisonCompactor {

    private static final String ELLIPSIS = "...";
    private static final String DELTA_END = "]";
    private static final String DELTA_START = "[";

    private int fContextLength;
    private String fExpected;
    private String fActual;
    private int fPrefix;
    private int fSuffix;
    public ComparisonCompactor(int contextLength,
                               String expected,
                                 String actual) {
      fContextLength = contextLength;
      fExpected = expected;
      fActual = actual;
    }
    public String compact(String message) {
      if (fExpected == null || fActual == null || areStringsEqual())
        return Assert.format(message, fExpected, fActual);

        findCommonPrefix();
        findCommonSuffix();
        String expected = compactString(fExpected);
        String actual = compactString(fActual);
        return Assert.format(message, expected, actual);
    }
    private String compactString(String source) {
      String result = DELTA_START +
                        source.substring(fPrefix, source.length() -
                          fSuffix + 1) + DELTA_END;
      if (fPrefix > 0)
        result = computeCommonPrefix() + result;
      if (fSuffix > 0)
        result = result + computeCommonSuffix();
      return result;
    }
    private void findCommonPrefix() {
      fPrefix = 0;
      int end = Math.min(fExpected.length(), fActual.length());
      for (; fPrefix < end; fPrefix++) {
        if (fExpected.charAt(fPrefix) != fActual.charAt(fPrefix))
          break;
      }
    }

    private void findCommonSuffix() {
      int expectedSuffix = fExpected.length() - 1;
      int actualSuffix = fActual.length() - 1;
      for (;
           actualSuffix >= fPrefix && expectedSuffix >= fPrefix;
            actualSuffix--, expectedSuffix--) {
        if (fExpected.charAt(expectedSuffix) != fActual.charAt(actualSuffix))
          break;
      }
      fSuffix = fExpected.length() - expectedSuffix;
    }

    private String computeCommonPrefix() {
      return (fPrefix > fContextLength ? ELLIPSIS : "") +
               fExpected.substring(Math.max(0, fPrefix - fContextLength),
                                      fPrefix);
    }

    private String computeCommonSuffix() {
      int end = Math.min(fExpected.length() - fSuffix + 1 + fContextLength,
                           fExpected.length());
      return fExpected.substring(fExpected.length() - fSuffix + 1, end) +
             (fExpected.length() - fSuffix + 1 < fExpected.length() -
              fContextLength ? ELLIPSIS : "");
    }
    private boolean areStringsEqual() {
      return fExpected.equals(fActual);
    }
}
```

Có thể bạn có vài điều phàn nàn về mô-đun này. Có một số biểu thức dài và vài chỗ +1 kỳ lạ, vân vân. Nhưng nhìn chung mô-đun này khá tốt. Dù sao thì nó cũng có thể trông như Đoạn mã 15-3.

**Đoạn mã 15-3**  
**ComparisonCompator.java (đã làm xấu mã)**

```java
package junit.framework;

public class ComparisonCompactor {
  private int ctxt;
  private String s1;
  private String s2;
  private int pfx;
  private int sfx;
    public ComparisonCompactor(int ctxt, String s1, String s2) {
      this.ctxt = ctxt;
      this.s1 = s1;
      this.s2 = s2;
    }

    public String compact(String msg) {
      if (s1 == null || s2 == null || s1.equals(s2))
        return Assert.format(msg, s1, s2);
        pfx = 0;
        for (; pfx < Math.min(s1.length(), s2.length()); pfx++) {
          if (s1.charAt(pfx) != s2.charAt(pfx))
            break;
        }
        int sfx1 = s1.length() - 1;
        int sfx2 = s2.length() - 1;
        for (; sfx2 >= pfx && sfx1 >= pfx; sfx2--, sfx1--) {
          if (s1.charAt(sfx1) != s2.charAt(sfx2))
            break;
        }
        sfx = s1.length() - sfx1;
        String cmp1 = compactString(s1);
        String cmp2 = compactString(s2);
        return Assert.format(msg, cmp1, cmp2);
    }

    private String compactString(String s) {
      String result =
        "[" + s.substring(pfx, s.length() - sfx + 1) + "]";
      if (pfx > 0)
        result = (pfx > ctxt ? "..." : "") +
          s1.substring(Math.max(0, pfx - ctxt), pfx) + result;
      if (sfx > 0) {
        int end = Math.min(s1.length() - sfx + 1 + ctxt, s1.length());
        result = result + (s1.substring(s1.length() - sfx + 1, end) +
          (s1.length() - sfx + 1 < s1.length() - ctxt ? "..." : ""));
      }
      return result;
    }

}
```

Dù các tác giả đã để mô-đun này ở trạng thái rất tốt, Quy tắc Hướng đạo sinh² nhắc chúng ta rằng nên để lại mọi thứ sạch hơn lúc tìm thấy. Vậy làm sao chúng ta có thể cải thiện mã ban đầu trong Đoạn mã 15-2?

² Xem “Quy tắc Hướng đạo sinh” ở trang 14.

Điều đầu tiên tôi không thích là tiền tố f ở các biến thành viên [N6]. Các môi trường ngày nay khiến kiểu mã hóa phạm vi này trở nên dư thừa. Vậy hãy loại bỏ mọi chữ f.

```java
private int contextLength;
private String expected;
private String actual;
private int prefix;
private int suffix;
```

Tiếp theo, ở đầu hàm compact có một điều kiện chưa được đóng gói [G28].

```java
public String compact(String message) {
  if (expected == null || actual == null || areStringsEqual())
    return Assert.format(message, expected, actual);
    findCommonPrefix();
    findCommonSuffix();
    String expected = compactString(this.expected);
    String actual = compactString(this.actual);
    return Assert.format(message, expected, actual);
}
```

Điều kiện này nên được đóng gói để làm rõ ý định của chúng ta. Vậy hãy trích xuất một phương thức giải thích điều kiện đó.

```java
public String compact(String message) {
  if (shouldNotCompact())
    return Assert.format(message, expected, actual);

    findCommonPrefix();
    findCommonSuffix();
    String expected = compactString(this.expected);
    String actual = compactString(this.actual);
    return Assert.format(message, expected, actual);
}

private boolean shouldNotCompact() {
  return expected == null || actual == null || areStringsEqual();
}
```

Tôi không thích cách viết this.expected và this.actual trong hàm compact. Điều này xảy ra khi chúng ta đổi tên fExpected thành expected. Tại sao hàm này lại có các biến trùng tên với biến thành viên? Chúng không biểu thị thứ gì khác sao [N4]? Chúng ta nên đặt tên sao cho không nhập nhằng.

```java
String compactExpected = compactString(expected);
String compactActual = compactString(actual);
```

Các ý phủ định hơi khó hiểu hơn ý khẳng định [G29]. Vậy hãy đảo ngược câu lệnh if và đảo nghĩa điều kiện.

```java
public String compact(String message) {
  if (canBeCompacted()) {
    findCommonPrefix();
    findCommonSuffix();
    String compactExpected = compactString(expected);
    String compactActual = compactString(actual);
    return Assert.format(message, compactExpected, compactActual);
  } else {
    return Assert.format(message, expected, actual);
  }
}
private boolean canBeCompacted() {
  return expected != null && actual != null && !areStringsEqual();
}
```

Tên hàm thật kỳ lạ [N7]. Dù nó có thực hiện việc rút gọn các chuỗi, trên thực tế hàm có thể không rút gọn chúng nếu canBeCompacted trả về false. Vì vậy, tên hàm compact che giấu tác dụng phụ của việc kiểm tra lỗi. Cũng cần lưu ý rằng hàm trả về một thông điệp đã định dạng, chứ không chỉ các chuỗi đã rút gọn. Vậy tên hàm thực sự nên là formatCompactedComparison. Như vậy khi đọc cùng đối số của hàm, câu lệnh sẽ dễ hiểu hơn nhiều:

```java
public String formatCompactedComparison(String message) {
```

Phần thân câu lệnh if là nơi thực sự rút gọn các chuỗi expected và actual. Chúng ta nên trích xuất phần này thành một phương thức tên là compactExpectedAndActual. Tuy nhiên, ta muốn hàm formatCompactedComparison thực hiện toàn bộ việc định dạng. Hàm compact... chỉ nên làm việc rút gọn [G30]. Vậy hãy tách như sau:

```java
...
private String compactExpected;
private String compactActual;

...

public String formatCompactedComparison(String message) {
  if (canBeCompacted()) {
    compactExpectedAndActual();
    return Assert.format(message, compactExpected, compactActual);
  } else {
    return Assert.format(message, expected, actual);
  }
}

private void compactExpectedAndActual() {
  findCommonPrefix();
  findCommonSuffix();
  compactExpected = compactString(expected);
  compactActual = compactString(actual);
}
```

Hãy chú ý rằng việc này buộc chúng ta phải nâng compactExpected và compactActual thành các biến thành viên. Tôi không thích việc hai dòng cuối của hàm mới trả về các biến, còn hai dòng đầu thì không. Chúng không tuân theo quy ước nhất quán [G11]. Vậy chúng ta nên đổi findCommonPrefix và findCommonSuffix để trả về các giá trị tiền tố và hậu tố.

```java
private void compactExpectedAndActual() {
  prefixIndex = findCommonPrefix();
  suffixIndex = findCommonSuffix();
  compactExpected = compactString(expected);
  compactActual = compactString(actual);
}

private int findCommonPrefix() {
  int prefixIndex = 0;
  int end = Math.min(expected.length(), actual.length());
  for (; prefixIndex < end; prefixIndex++) {
    if (expected.charAt(prefixIndex) != actual.charAt(prefixIndex))
      break;
  }
  return prefixIndex;
}

private int findCommonSuffix() {
  int expectedSuffix = expected.length() - 1;
  int actualSuffix = actual.length() - 1;
  for (; actualSuffix >= prefixIndex && expectedSuffix >= prefixIndex;
       actualSuffix--, expectedSuffix--) {
    if (expected.charAt(expectedSuffix) != actual.charAt(actualSuffix))
      break;
  }
  return expected.length() - expectedSuffix;
}
```

Chúng ta cũng nên đổi tên các biến thành viên cho chính xác hơn một chút [N1]; xét cho cùng, cả hai đều là chỉ số.

Quan sát kỹ findCommonSuffix cho thấy một sự phụ thuộc vào thời điểm bị che giấu [G31]; nó phụ thuộc vào việc prefixIndex được tính bởi findCommonPrefix. Nếu gọi hai hàm này sai thứ tự, việc gỡ lỗi sẽ rất khó khăn. Vậy để làm lộ sự phụ thuộc này, hãy cho findCommonSuffix nhận prefixIndex làm đối số.

```java
private void compactExpectedAndActual() {
  prefixIndex = findCommonPrefix();
  suffixIndex = findCommonSuffix(prefixIndex);
  compactExpected = compactString(expected);
  compactActual = compactString(actual);
}

private int findCommonSuffix(int prefixIndex) {
  int expectedSuffix = expected.length() - 1;
  int actualSuffix = actual.length() - 1;
  for (; actualSuffix >= prefixIndex && expectedSuffix >= prefixIndex;
       actualSuffix--, expectedSuffix--) {
    if (expected.charAt(expectedSuffix) != actual.charAt(actualSuffix))
      break;
  }
  return expected.length() - expectedSuffix;
}
```

Tôi không thực sự hài lòng với cách này. Việc truyền đối số prefixIndex hơi tùy tiện [G32]. Nó giúp xác lập thứ tự nhưng chẳng giải thích gì về sự cần thiết của thứ tự đó. Một lập trình viên khác có thể đảo ngược thay đổi của chúng ta vì không có dấu hiệu nào cho thấy tham số này thực sự cần thiết. Vậy hãy thử một hướng khác.

```java
private void compactExpectedAndActual() {
  findCommonPrefixAndSuffix();
  compactExpected = compactString(expected);
  compactActual = compactString(actual);
}

private void findCommonPrefixAndSuffix() {
  findCommonPrefix();
  int expectedSuffix = expected.length() - 1;
  int actualSuffix = actual.length() - 1;
  for (;
        actualSuffix >= prefixIndex && expectedSuffix >= prefixIndex;
        actualSuffix--, expectedSuffix--
    ) {
    if (expected.charAt(expectedSuffix) != actual.charAt(actualSuffix))
      break;
  }
  suffixIndex = expected.length() - expectedSuffix;
}

private void findCommonPrefix() {
  prefixIndex = 0;
  int end = Math.min(expected.length(), actual.length());
  for (; prefixIndex < end; prefixIndex++)
    if (expected.charAt(prefixIndex) != actual.charAt(prefixIndex))
      break;
}
```

Chúng ta đã đưa findCommonPrefix và findCommonSuffix trở lại như trước, đổi tên findCommonSuffix thành findCommonPrefixAndSuffix và cho nó gọi findCommonPrefix trước khi làm bất cứ việc gì khác. Cách này thể hiện rõ tính phụ thuộc thời điểm của hai hàm hơn hẳn giải pháp trước. Nó cũng chỉ ra findCommonPrefixAndSuffix xấu xí đến mức nào. Giờ hãy làm sạch nó.

```java
private void findCommonPrefixAndSuffix() {
  findCommonPrefix();
  int suffixLength = 1;
  for (; !suffixOverlapsPrefix(suffixLength); suffixLength++) {
    if (charFromEnd(expected, suffixLength) !=
         charFromEnd(actual, suffixLength))
      break;
  }
  suffixIndex = suffixLength;
}
private char charFromEnd(String s, int i) {
  return s.charAt(s.length()-i);}
private boolean suffixOverlapsPrefix(int suffixLength) {
  return actual.length() - suffixLength < prefixLength ||
    expected.length() - suffixLength < prefixLength;
}
```

Cách này tốt hơn nhiều. Nó cho thấy suffixIndex thực ra là độ dài của hậu tố và tên hiện tại không phù hợp. Điều tương tự cũng đúng với prefixIndex, dù trong trường hợp đó “chỉ số” và “độ dài” đồng nghĩa. Dù vậy, dùng “độ dài” sẽ nhất quán hơn. Vấn đề là biến suffixIndex không bắt đầu từ 0 mà từ 1, nên nó không phải độ dài thực sự. Đây cũng là lý do có nhiều chỗ +1 trong computeCommonSuffix [G33]. Vậy hãy sửa điều đó. Kết quả nằm trong Đoạn mã 15-4.

**Đoạn mã 15-4**  
**ComparisonCompactor.java (bản trung gian)**

```java
public class ComparisonCompactor {
...
  private int suffixLength;
...
  private void findCommonPrefixAndSuffix() {
    findCommonPrefix();
    suffixLength = 0;
    for (; !suffixOverlapsPrefix(suffixLength); suffixLength++) {
      if (charFromEnd(expected, suffixLength) !=
          charFromEnd(actual, suffixLength))
        break;
    }
  }
  private char charFromEnd(String s, int i) {
    return s.charAt(s.length() - i - 1);
  }

  private boolean suffixOverlapsPrefix(int suffixLength) {
    return actual.length() - suffixLength <= prefixLength ||
      expected.length() - suffixLength <= prefixLength;
  }

...
  private String compactString(String source) {
    String result =
      DELTA_START +
      source.substring(prefixLength, source.length() - suffixLength) +
      DELTA_END;
    if (prefixLength > 0)
      result = computeCommonPrefix() + result;
    if (suffixLength > 0)
      result = result + computeCommonSuffix();
    return result;
  }

...
  private String computeCommonSuffix() {
    int end = Math.min(expected.length() - suffixLength +
       contextLength, expected.length()
    );
    return
       expected.substring(expected.length() - suffixLength, end) +
       (expected.length() - suffixLength <
         expected.length() - contextLength ?
         ELLIPSIS : "");
  }
```

Chúng ta đã thay +1 trong computeCommonSuffix bằng -1 ở charFromEnd, nơi nó hoàn toàn hợp lý, và thay bằng hai toán tử <= trong suffixOverlapsPrefix, cũng rất hợp lý. Nhờ đó, chúng ta có thể đổi tên suffixIndex thành suffixLength, cải thiện đáng kể khả năng đọc của mã.

Tuy nhiên, có một vấn đề. Khi loại bỏ các chỗ +1, tôi nhận thấy dòng sau trong compactString:

```java
if (suffixLength > 0)
```

Hãy xem dòng này trong Đoạn mã 15-4. Theo lý, vì giờ suffixLength nhỏ hơn trước một đơn vị, tôi nên đổi toán tử > thành >=. Nhưng điều đó chẳng có nghĩa gì. Bây giờ thì lại có nghĩa! Điều này cho thấy trước đây nó không có nghĩa và có lẽ là một lỗi.

À, không hẳn là lỗi. Phân tích sâu hơn, ta thấy câu lệnh if giờ ngăn không cho nối một hậu tố có độ dài bằng không. Trước khi thay đổi, câu lệnh if không có tác dụng vì suffixIndex không bao giờ nhỏ hơn một!

Điều này khiến chúng ta phải xem xét cả hai câu lệnh if trong compactString! Có vẻ như có thể loại bỏ cả hai. Vậy hãy chú thích chúng lại rồi chạy các bài kiểm thử. Chúng đều đạt! Vậy hãy cấu trúc lại compactString để loại bỏ các câu lệnh if thừa và làm hàm đơn giản hơn nhiều [G9].

```java
private String compactString(String source) {
    return
      computeCommonPrefix() +
      DELTA_START +
      source.substring(prefixLength, source.length() - suffixLength) +
      DELTA_END +
      computeCommonSuffix();
  }
```

Cách này tốt hơn nhiều! Giờ ta thấy hàm compactString chỉ đơn thuần ghép các đoạn lại với nhau. Có lẽ chúng ta có thể làm cho nó rõ ràng hơn nữa. Thực vậy, còn nhiều chỗ nhỏ có thể dọn dẹp. Nhưng thay vì dẫn bạn qua toàn bộ những thay đổi còn lại, tôi sẽ chỉ cho bạn kết quả trong Đoạn mã 15-5.

**Đoạn mã 15-5**  
**ComparisonCompactor.java (bản cuối)**

```java
package junit.framework;

public class ComparisonCompactor {
  private static final String ELLIPSIS = "...";
  private static final String DELTA_END = "]";
  private static final String DELTA_START = "[";

  private int contextLength;
  private String expected;
  private String actual;
  private int prefixLength;
  private int suffixLength;

  public ComparisonCompactor(
    int contextLength, String expected, String actual
  ) {
    this.contextLength = contextLength;
    this.expected = expected;
    this.actual = actual;
  }
  public String formatCompactedComparison(String message) {
    String compactExpected = expected;
    String compactActual = actual;
    if (shouldBeCompacted()) {
      findCommonPrefixAndSuffix();
      compactExpected = compact(expected);
      compactActual = compact(actual);
    }
    return Assert.format(message, compactExpected, compactActual);
  }
  private boolean shouldBeCompacted() {
    return !shouldNotBeCompacted();
  }

  private boolean shouldNotBeCompacted() {
    return expected == null ||
           actual == null ||
           expected.equals(actual);
  }

  private void findCommonPrefixAndSuffix() {
    findCommonPrefix();
    suffixLength = 0;
    for (; !suffixOverlapsPrefix(); suffixLength++) {
      if (charFromEnd(expected, suffixLength) !=
          charFromEnd(actual, suffixLength)
      )
        break;
    }

    private char charFromEnd(String s, int i) {
      return s.charAt(s.length() - i - 1);
    }

    private boolean suffixOverlapsPrefix() {
      return actual.length() - suffixLength <= prefixLength ||
        expected.length() - suffixLength <= prefixLength;
    }

    private void findCommonPrefix() {
      prefixLength = 0;
      int end = Math.min(expected.length(), actual.length());
      for (; prefixLength < end; prefixLength++)
        if (expected.charAt(prefixLength) != actual.charAt(prefixLength))
          break;
    }

    private String compact(String s) {
      return new StringBuilder()
        .append(startingEllipsis())
        .append(startingContext())
        .append(DELTA_START)
        .append(delta(s))
        .append(DELTA_END)
        .append(endingContext())
        .append(endingEllipsis())
        .toString();
    }

    private String startingEllipsis() {
      return prefixLength > contextLength ? ELLIPSIS : "";
    }
    private String startingContext() {
      int contextStart = Math.max(0, prefixLength - contextLength);
      int contextEnd = prefixLength;
      return expected.substring(contextStart, contextEnd);
    }

    private String delta(String s) {
      int deltaStart = prefixLength;
      int deltaEnd = s.length() - suffixLength;
      return s.substring(deltaStart, deltaEnd);
    }

    private String endingContext() {
      int contextStart = expected.length() - suffixLength;
      int contextEnd =
        Math.min(contextStart + contextLength, expected.length());
      return expected.substring(contextStart, contextEnd);
    }

    private String endingEllipsis() {
      return (suffixLength > contextLength ? ELLIPSIS : "");
    }
}
```

Thực ra, cách này khá đẹp. Mô-đun được chia thành một nhóm hàm phân tích và một nhóm hàm tổng hợp. Chúng được sắp xếp theo cấu trúc tô pô, sao cho định nghĩa của mỗi hàm xuất hiện ngay sau chỗ nó được dùng. Tất cả các hàm phân tích xuất hiện trước, còn các hàm tổng hợp xuất hiện sau cùng.

Nếu quan sát kỹ, bạn sẽ nhận thấy tôi đã đảo ngược vài quyết định đưa ra trước đó trong chương này. Chẳng hạn, tôi đã đưa một số phương thức được trích xuất trở lại vào formatCompactedComparison và thay đổi chiều hướng của biểu thức shouldNotBeCompacted. Đây là điều điển hình. Thường thì một lần tái cấu trúc dẫn đến một lần khác, rồi lần đó lại khiến ta hoàn tác lần đầu. Tái cấu trúc là một quá trình lặp lại, đầy thử nghiệm và sai sót, tất yếu hội tụ về một thứ mà chúng ta cho là xứng đáng với một chuyên gia.

## Kết luận

Như vậy, chúng ta đã thực hiện Quy tắc Hướng đạo sinh. Chúng ta để lại mô-đun này sạch hơn đôi chút so với lúc tìm thấy. Không phải trước đó nó không sạch. Các tác giả đã làm rất tốt. Nhưng không mô-đun nào miễn nhiễm với việc cải thiện, và mỗi người chúng ta có trách nhiệm để lại mã tốt hơn một chút so với lúc mình tìm thấy.
