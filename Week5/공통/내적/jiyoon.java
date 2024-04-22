package Week5.공통.내적;

public class jiyoon {
  class Solution {
    public int solution(int[] a, int[] b) {
      int answer = 0;
      for (int i = 0; i < a.length; i++) {
        answer += a[i] * b[i];      // 내적을 answer에 더하기
      }

      return answer;
    }
  }
}
