package Week7.공통.예산;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int[] d, int budget) {
      int answer = 0;

      Arrays.sort(d);     // d를 오름차순 정렬
      for (int i = 0; i < d.length; i++) {
        budget -= d[i];         // 예산에서 i번째 부서 예산 지원
        if (budget < 0) break;  // 예산이 부족하다면, 지원 중단
        else answer++;          // 지원 가능하므로 answer++
      }
      return answer;
    }
  }
}
