package Week11.문자열내마음대로정렬하기;
import java.util.*;

public class jiyoon {
  class Solution {
    public String[] solution(String[] strings, int n) {
      String[] answer = new String[strings.length];

      ArrayList<String> list = new ArrayList<>();
      for (int i = 0; i < strings.length; i++) {
        // 맨 앞에 n번째 문자를 추가 후, 문자열 추가
        list.add(strings[i].charAt(n) + strings[i]);
      }

      // list 정렬
      Collections.sort(list);

      for (int i = 0; i < answer.length; i++) {
        // 맨 앞에 추가했던 문자를 제거 후, answer 배열에 삽입
        answer[i] = list.get(i).substring(1);
      }

      return answer;
    }
  }
}
