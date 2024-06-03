package Week11.문자열내림차순으로배치하기;
import java.util.*;

public class jiyoon {
  class Solution {
    public String solution(String s) {
      String answer = "";
      String[] arr = s.split("");
      Arrays.sort(arr, Collections.reverseOrder());

      for (String str : arr) answer += str;
      return answer;
    }
  }
}
