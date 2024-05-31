package Week10.공통.괄호변환;

import java.util.*;
public class jiyoon {
  class Solution {
    public String solution(String p) {
      String answer = "";

      StringBuilder sb = new StringBuilder();
      Stack<Character> stack = new Stack<>();
      ArrayList<Character> list = new ArrayList<>();
      int index = 0;

      if (p.length() == 0) {
        return p;
      }

      int length = p.length();    // 문자열 p의 길이
      int open = 0;               // '('의 개수
      int close = 0;              // ')'의 개수

      for (int i = 0; i < length; i++) {
        if (p.charAt(i) == '(') open++;
        else if (p.charAt(i) == ')') close++;

        list.add(p.charAt(i));
        stack.push(p.charAt(i));

        // 올바른 괄호 문자열 검사하기
        if (stack.size() >= 2) {
          while (true) {
            if (stack.get(stack.size() - 1) == ')' && stack.get(stack.size() - 2) == '(') {
              stack.pop();
              stack.pop();
            } else {
              break;
            }

            if (stack.size() == 0) {
              break;
            }
          }
        }

        // 균형잡힌 괄호 문자열이라면
        if (open == close) {
          index = i;

          // 올바른 괄호 문자열이 아니라면
          if (stack.size() != 0) {
            // 수정된 문자열 생성
            sb.append('(');
            // 나머지 문자열을 재귀적으로 처리
            sb.append(solution(p.substring(index + 1)));
            sb.append(')');

            // 리스트에서 첫 번째 문자와 마지막 문자 제거
            list.remove(list.size() - 1);
            list.remove(0);

            // 나머지 리스트의 괄호 방향 뒤집기
            for (int j = 0; j < list.size(); j++) {
              if (list.get(j) == '(') {
                list.set(j, ')');
              } else if (list.get(j) == ')') {
                list.set(j, '(');
              }
            }

            // 수정된 리스트의 문자를 StringBuilder에 추가
            for (char ch : list) {
              sb.append(ch);
            }

            // 생성된 문자열ㅇ르 반환
            return sb.toString();
          }

          // 유효한 문자열을 발견했으므로 루프 종료
          break;
        }
      }

      // 리스트의 유효한 문자를 StringBuilder에 추가
      for (char ch : list) {
        sb.append(ch);
      }

      // 나머지 문자열을 재귀적으로 처리하고 결과에 추가
      return sb.toString() + solution(p.substring(index + 1));
    }
  }
}
