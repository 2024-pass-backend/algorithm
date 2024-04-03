package Week2.공통.카드뭉치;

import java.util.*;

public class jiyoon {
  class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
      boolean check = true;      // 문자열 완성 확인용

      Queue<String> q1 = new LinkedList<>();      // card1의 문자열을 담을 배열
      Queue<String> q2 = new LinkedList<>();      // card2의 문자열을 담을 배열

      // 각각의 Queue에 cards1과 cards2 담기
      for (int i = 0; i < cards1.length; i++) q1.add(cards1[i]);
      for (int i = 0; i < cards2.length; i++) q2.add(cards2[i]);

      for (int i = 0; i < goal.length; i++) {
        String find = goal[i];

        // q1에서 goal[i]를 가져올 수 있는지 확인
        if (q1.peek() != null && q1.peek().equals(find)) {
          q1.remove();
          continue;
        }

        // q2에서 goal[i]를 가져올 수 있는지 확인
        if (q2.peek() != null && q2.peek().equals(find)) {
          q2.remove();
          continue;
        }

        // goal[i]를 가져올 수 없다면 check = false;
        check = false;
      }
      return check ? "Yes" : "No";
    }
  }
}
