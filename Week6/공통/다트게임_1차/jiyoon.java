package Week6.공통.다트게임_1차;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(String dartResult) {
      int answer = 0;

      // 제곱 정보를 저장할 HashMap 생성
      HashMap<Character, Integer> map = new HashMap<>();
      map.put('S', 1);
      map.put('D', 2);
      map.put('T', 3);

      String number = "";         // 숫자 정보를 저장할 number
      ArrayList<Integer> list = new ArrayList<>();        // 점수 정보를 저장할 list
      for (int i = 0; i < dartResult.length(); i++) {
        char c = dartResult.charAt(i);

        if (Character.isDigit(c)) {     // 숫자라면
          number += c;
        } else if (c == 'S' || c == 'D' || c == 'T') {          // S, D, T라면
          int num = Integer.parseInt(number);                 // 숫자 정보를 저장했던 문자열을 int형으로 변경
          list.add((int)Math.pow(num, map.get(c)));           // 점수를 list에 저장
          number = "";                                        // 문자열 초기화
        } else if (c == '*') {
          list.set(list.size() - 1, list.get(list.size() - 1) * 2);       // 해당 점수 2배

          if (list.size() != 1) {     // 이전 점수 2배
            list.set(list.size() - 2, list.get(list.size() - 2) * 2);
          }
        } else if (c == '#') {
          list.set(list.size() - 1, list.get(list.size() - 1) * -1);      // 해당 점수 마이너스
        }
      }

      for (int i = 0; i < list.size(); i++) {
        answer += list.get(i);
      }
      return answer;
    }
  }
}
