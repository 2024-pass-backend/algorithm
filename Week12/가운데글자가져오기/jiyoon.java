package Week12.가운데글자가져오기;

public class jiyoon {
  class Solution {
    public String solution(String s) {
      String answer = "";

      if (s.length() % 2 == 0) {
        answer = s.substring(s.length() / 2 - 1, s.length() / 2 + 1);
      } else {
        answer = String.valueOf(s.charAt(s.length() / 2));
      }

      return answer;
    }
  }
}
