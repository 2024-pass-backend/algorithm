package Week9.공통.이진변환반복하기;

public class jiyoon {
  class Solution {
    public int[] solution(String s) {
      int[] answer = new int[2];

      int zero = 0;       // 제거된 0의 갯수
      int count = 0;      // 이진 변환 횟수
      StringBuilder sb;

      while (true) {
        sb = new StringBuilder();

        // 0을 제거한 문자열 생성하기
        for (int i = 0; i < s.length(); i++) {
          if (s.charAt(i) == '1') sb.append('1');
          else zero++;
        }

        s = sb.toString();

        // 0이 제거된 문자열을 2진수로 변환하기
        s = Integer.toString(s.length(), 2);
        count++;

        // 만약 문자열이 1이 된다면 while문 종료
        if (s.equals("1")) break;
      }

      answer[0] = count;
      answer[1] = zero;

      return answer;
    }
  }
}
