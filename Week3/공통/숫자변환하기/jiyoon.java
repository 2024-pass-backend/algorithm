package Week3.공통.숫자변환하기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int x, int y, int n) {
      int answer = 0;
      int[] dp = new int[y + 1];              // x를 y로 변환하기 위한 최소 연산 수를 저장 할 배열
      Arrays.fill(dp, Integer.MAX_VALUE);     // 배열을 Integer.MAX_VALUE로 채우기

      dp[x] = 0;      // dp[i] = x를 i로 변환하기 위해 필요한 최소 연산 수를 저장하기 위해
      for (int i = x; i <= y; i++) {
        if (dp[i] == Integer.MAX_VALUE) continue;

        if (i + n <= y) dp[i + n] = Math.min(dp[i + n], dp[i] + 1);     // x + n의 경우
        if (i * 2 <= y) dp[i * 2] = Math.min(dp[i * 2], dp[i] + 1);     // x * 2의 경우
        if (i * 3 <= y) dp[i * 3] = Math.min(dp[i * 3], dp[i] + 1);     // x * 3의 경우
      }

      if (dp[y] == Integer.MAX_VALUE) return -1;      // dp[y]가 Integer.MAX_VALUE라면, 만들 수 없는 것이므로 -1
      return dp[y];
    }
  }
}
