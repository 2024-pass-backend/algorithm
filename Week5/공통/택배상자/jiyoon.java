package Week5.공통.택배상자;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int[] order) {
      int answer = 0;

      Queue<Integer> queue = new LinkedList<>();      // 기존 컨테이너
      Stack<Integer> stack = new Stack<>();           // 보조 컨테이너

      for (int i = 1; i <= order.length; i++) {      // 1~5까지 기존 컨테이너에 삽입
        queue.add(i);
      }

      while (order[0] != queue.peek()) {      // 기존 컨테이너의 맨 앞에 놓인 상자가 트럭에 실어야 하는 순서가 아니라면
        stack.push(queue.poll());           // 보조 컨테이너에 삽입
      }

      answer++;
      queue.poll();

      for (int i = 1; i < order.length; i++) {
        // 컨테이너에서 꺼낸 상자가 트럭에 실어야하는 순서라면
        if (!queue.isEmpty() && order[i] == queue.peek()) {
          answer++;
          queue.poll();

          // 보조 컨테이너에서 꺼낸 상자가 트럭에 실어야하는 순서라면
        } else if (!stack.isEmpty() && order[i] == stack.peek()) {
          answer++;
          stack.pop();
        } else {        // 기존 컨테이너와 보조 컨테이너에서 꺼낼 수 없는 순서의 상자라면
          if (!queue.isEmpty() && queue.peek() < order[i]) {      // 기존 컨테이너에 들어있는 상자가 실어야 하는 순서보다 작다면
            while (order[i] != queue.peek()) {
              stack.push(queue.poll());
            }

            answer++;
            queue.poll();
          } else {        // 기존 컨테이너에 들어있는 상자가 실어야 하는 순서보다 크다면
            break;      // 더 이상 실을 수 없으므로 종료
          }
        }
      }

      return answer;
    }
  }
}
