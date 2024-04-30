package Week6.공통.두큐합같게만들기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int[] queue1, int[] queue2) {
      int answer = 0;

      // 큐 생성
      Queue<Integer> q1 = new LinkedList<>();
      Queue<Integer> q2 = new LinkedList<>();
      long sumQ1 = 0;      // q1에 포함된 원소들의 합
      long total = 0;      // queue1과 queue2의 포함된 모든 원소의 합

      // 큐에 값 저장하기 및 sumQ1과 total 구하기
      for (int i = 0; i < queue1.length; i++) {
        sumQ1 += queue1[i];
        total += queue1[i] + queue2[i];
        q1.add(queue1[i]);
        q2.add(queue2[i]);
      }

      // total이 홀수라면 각 큐의 원소 합을 같게 만들 수 없음
      if (total % 2 != 0) return -1;

      long target = total / 2;        // sumQ1의 기준이 될 target 생성

      // 큐 이동 시작
      while (true) {
        // 큐의 이동이 두 큐를 모두 순회하고도 끝나지 않으면 만들 수 없는 것이므로 순회 종료
        if (answer > (queue1.length + queue2.length) * 2) return -1;

        // sumQ1 == target이라면, 두 큐의 합을 동일하게 만든 것이므로 순회 종료
        if (target == sumQ1) break;

        if (target > sumQ1) {       // target > sumQ1라면, q2의 값을 q1으로 이동
          sumQ1 += q2.peek();
          q1.add(q2.poll());
        } else {                    // target < sumQ1라면, q1의 값을 q2으로 이동
          sumQ1 -= q1.peek();
          q2.add(q1.poll());
        }

        answer++;
      }

      return answer;
    }
  }
}
