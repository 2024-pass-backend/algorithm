package Week5.공통.약수의_개수와_덧셈;

public class jiyoon {
  class Solution {
    public int solution(int left, int right) {
      int answer = 0;

      for (int i = left; i <= right; i++) {
        int count = 0;      // 약수의 개수
        for (int j = 1; j <= i; j++) {
          if (i % j == 0) {       // 약수를 찾으면
            count++;            // 약수의 개수 증가
          }
        }

        if (count % 2 == 0) answer += i;
        else answer -= i;
      }
      return answer;
    }
  }
}
