package Week9.공통.자연수_뒤집어_배열로_만들기;

public class jiyoon {
  class Solution {
    public int[] solution(long n) {
      StringBuilder sb = new StringBuilder();

      // 자연수 뒤집기
      while (n != 0) {
        sb.append(n % 10);
        n /= 10;
      }

      // 뒤집은 자연수를 문자열로 변경
      String num = sb.toString();

      // 문자열을 배열로 변경
      int[] answer = new int[num.length()];
      for (int i = 0; i < num.length(); i++) {
        answer[i] = num.charAt(i) - '0';
      }

      return answer;
    }
  }
}
