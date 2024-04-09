package Week3.공통.뒤에있는큰수찾기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int[] numbers) {
      int[] answer = new int[numbers.length];
      Arrays.fill(answer, -1);        // answer배열을 -1로 채움

      Stack<Integer> stack = new Stack<>();

      for (int i = 0; i < numbers.length; i++) {
        // 스택이 비어있지 않으면서 현재 스택의 값보다 number의 값이 크면
        while (!stack.isEmpty() && numbers[i] > numbers[stack.peek()]) {
          // 뒤에 있는 큰 수에 해당하는 값 pop
          answer[stack.pop()] = numbers[i];
        }
        stack.push(i);
      }

      return answer;
    }
  }
}
