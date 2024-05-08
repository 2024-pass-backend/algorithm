package Week7.공통.x만큼_간격이_있는_n개의_숫자;

public class jiyoon {
  class Solution {
    public long[] solution(long x, int n) {
      long[] answer = new long[n];

      for (int i = 1; i <= n; i++) {
        answer[i - 1] = x * i;
      }
      return answer;
    }
  }
}
