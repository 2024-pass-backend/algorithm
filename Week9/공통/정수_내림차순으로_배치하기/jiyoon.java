package Week9.공통.정수_내림차순으로_배치하기;
import java.util.*;

public class jiyoon {
  class Solution {
    public long solution(long n) {
      String[] arr = String.valueOf(n).split("");     // n을 한글자씩 arr배열에 저장
      Arrays.sort(arr, Collections.reverseOrder());   // 내림차순 정렬

      StringBuilder sb = new StringBuilder();
      for (String s : arr) {      // arr을 StringBuilder에 저장
        sb.append(s);
      }

      return Long.parseLong(sb.toString());
    }
  }
}
