package Week2.공통.크기가_작은_부분문자열;

public class jiyoon {
  class Solution {
    public int solution(String t, String p) {
      int answer = 0;
      int tl = t.length();        // 문자열 t의 길이
      int pl = p.length();        // 문자열 p의 길이

      for (int i = 0; i < tl - pl + 1; i++) {
        // p의 길이가 18까지 가능하기 때문에, 이는 int의 범위를 벗어나므로 long 사용
        long num2 = Long.parseLong(t.substring(i, i + pl));
        long pnum = Long.parseLong(p);

        if (num2 <= pnum) answer++;

      }
      return answer;
    }
  }
}
