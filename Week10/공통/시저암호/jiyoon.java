package Week10.공통.시저암호;

public class jiyoon {
  class Solution {
    public String solution(String s, int n) {
      String answer = "";

      for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);

        if (c == ' ') {
          answer += " ";
          continue;
        }

        if (Character.isUpperCase(c)) {
          c = (char)((c - 'A' + n) % 26 + 'A');
        } else {
          c = (char)((c - 'a' + n) % 26 + 'a');
        }
        answer += c;
      }

      return answer;
    }
  }
}
