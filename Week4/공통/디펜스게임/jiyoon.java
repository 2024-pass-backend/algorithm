package Week4.공통.디펜스게임;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int n, int k, int[] enemy) {
      int answer = 0;

      // 무적권을 사용한 적의 수 저장
      PriorityQueue<Integer> pq = new PriorityQueue<>();

      for (int i = 0; i < enemy.length; i++) {
        if (k > 0) {                // 무적권의 개수만큼 일단 큐에 삽입
          pq.add(enemy[i]);
          k--;
        } else {                    // 무적권을 다 썼다면
          int num = enemy[i];     // i번째 적의 수

          if (pq.peek() < enemy[i]) {     // 우선순위 큐에서 빼낸 수보다 적의 수가 더 많다면
            num = pq.poll();
            pq.add(enemy[i]);           // 현재 적에게 무적권 사용
          }

          if (n >= num) {     // 준호가 가지고 있는 병사의 수가 무적권을 안 쓴 적보다 많을 경우
            n -= num;       // 병사의 수 - 무적권 안쓴 적
          } else break;
        }
        answer++;
      }

      return answer;
    }
  }
}
