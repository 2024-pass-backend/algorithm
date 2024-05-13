package Week8.공통.콜라츠추측;

public class jiyoon {
  class Solution {
    public int solution(long num) {
      int answer = 0;

      while (true) {
        // 단, 조건
        if (num == 1) return 0;         // 주어진 수가 1인 경우, 0 반환
        if (answer > 500) return -1;    // 작업을 500번 반복할 때까지 1이 되지 않는다면 -1 반환

        if (num % 2 == 0) {     // 짝수라면
          num /= 2;
        } else {                // 홀수라면
          num = (num * 3) + 1;
        }

        answer++;

        if (num == 1) break;
      }
      return answer;
    }
  }
}
