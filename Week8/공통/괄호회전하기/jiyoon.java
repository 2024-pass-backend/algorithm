package Week8.공통.괄호회전하기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(String s) {
      int answer = 0;

      // s를 회전시킬 때 사용할 ArrayList 생성
      ArrayList<Character> list = new ArrayList<>();

      // s를 문자별로 ArrayList에 삽입
      for (int i = 0; i < s.length(); i++) list.add(s.charAt(i));

      for (int i = 0; i < s.length(); i++) {
        // list 회전
        list.add(list.get(0));
        list.remove(list.get(0));

        // 올바른 괄호 문자열인지 확인할 stack
        Stack<Character> stack = new Stack<>();

        for (int j = 0; j < s.length(); j++) {
          char c = list.get(j);
          stack.add(c);

          // 여는 괄호면 다음 글자로 이동
          if (c == '(' || c == '[' || c == '{') continue;
          else {              // 닫는 괄호라면
            stack.pop();    // 닫는 괄호 스택에서 제거

            // 스택이 비어있지 않다면
            if (!stack.isEmpty()) {
              // 올바른 괄호쌍이라면 스택에서 괄호쌍 제거
              if (c == ')' && stack.peek() == '(') stack.pop();
              if (c == ']' && stack.peek() == '[') stack.pop();
              if (c == '}' && stack.peek() == '{') stack.pop();
            } else {
              break;  // 스택이 비어있다면 순환 종료
            }
          }

          // 문자열이 올바른 괄호 문자열이라면
          if (stack.size() == 0 && j == s.length() - 1) {
            answer++;
          }
        }
      }

      return answer;
    }
  }
}
