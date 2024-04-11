package Week3.공통.마법의엘리베이터;

public class jiyoon {
  class Solution {
    public int solution(int storey) {
      int answer = 0;

      while (storey > 0) {
        int digit = storey % 10;    // storey의 일의 자리
        storey /= 10;

        if (digit > 5) {
          answer += 10 - digit;       // 5 초과일 경우, -해주는 것이 더 빠름
          storey++;                   // - 해주었으니 +10해주어야 함
        } else if (digit < 5) {
          answer += digit;            // 5 미만일 경우, +해주는 것이 더빠름
        } else {                        // digit == 5
          if (storey % 10 >= 5) {     // 5 초과일 경우와 동일
            answer += 10 - digit;
            storey++;
          } else {                    // 5 이하일 경우와 동일
            answer += digit;
          }
        }
      }
      return answer;
    }
  }
}
