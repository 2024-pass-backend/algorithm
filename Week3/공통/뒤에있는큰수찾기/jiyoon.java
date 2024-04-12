package Week3.공통.뒤에있는큰수찾기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int[] numbers) {
      int[] answer = new int[numbers.length];
      Arrays.fill(answer, -1);
      Stack<Integer> stack = new Stack<>();

      for (int i = 0; i < numbers.length; i++) {
        while (!stack.isEmpty() && numbers[stack.peek()] < numbers[i]) {
          answer[stack.pop()] = numbers[i];
        }
        stack.push(i);
      }
      return answer;
    }
  }
}
