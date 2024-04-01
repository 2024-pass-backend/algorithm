import java.io.*;
import java.util.*;

class Solution {
  public int solution(int[][] targets) {
    int answer = 1;     // 최소한 한 개의 구간이 존재하면서 다른 어떤 구간과도 겹치지 않는 경우가 적어도 하나는 존재
    Arrays.sort(targets, (x, y) -> x[0] - y[0]);        // targets배열 정렬

    int preStart = targets[0][0];
    int preEnd = targets[0][1];

    for (int[] target : targets) {
      int curStart = target[0];
      int curEnd = target[1];

      // 폭격 미사일의 위치가 겹친다면,
      // 겹치는 구간으로 업데이트
      if (curStart >= preStart && curStart < preEnd) {
        preStart = Math.max(preStart, curStart);
        preEnd = Math.min(preEnd, curEnd);

      } else {    // 현재 구간과 이전 구간이 겹치지 않는다면 새로운 겹치지 않는 구간이 시작된 것
        answer++;

        // 현재의 구간으로 업데이트
        preStart = curStart;
        preEnd = curEnd;
      }
    }
    return answer;
  }
}