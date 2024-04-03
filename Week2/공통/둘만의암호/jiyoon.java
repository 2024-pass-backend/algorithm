package Week2.공통.둘만의암호;

public class jiyoon {
  class Solution {
    public String solution(String s, String skip, int index) {
      // answer만들 때 사용할 alphabet문자열(skip에 포함된 문자 제외)
      String alphabet = "abcdefghijklmnopqrstuvwxyz";

      for (int i = 0; i < skip.length(); i++) {
        char c = skip.charAt(i);

        // skip에 포함된 문자 제거
        alphabet = alphabet.replace(String.valueOf(c), "");
      }

      String answer = "";

      for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);

        // alphabet에서 s에 포함된 문자의 위치 찾기
        int position = alphabet.indexOf(String.valueOf(c));

        // 이동시킬 위치
        int total = position + index;

        // 이동시킬 위치가 alphabet을 넘어간다면('z'를 넘어간다면, 'a'부터 시작)
        while (total >= alphabet.length()) {
          total -= alphabet.length();
        }
        answer += alphabet.charAt(total);

      }

      return answer;
    }
  }
}