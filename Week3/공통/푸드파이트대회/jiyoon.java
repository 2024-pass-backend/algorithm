package Week3.공통.푸드파이트대회;

public class jiyoon {
  class Solution {
    public String solution(int[] food) {
      String answer = "";
      StringBuilder sb = new StringBuilder();

      // 왼쪽 선수의 음식 배치하기
      for (int i = 1; i < food.length; i++) {
        for (int j = 0; j < food[i] / 2; j++) sb.append(i);     // i번 음식을 food[i] / 2개 배치하기
      }

      answer += sb.toString();    // 배치된 왼쪽 음식 String으로 변경하기

      // 오른쪽 선수 음식 배치하기
      sb.append("0");             // 배치된 음식에 +0
      sb.reverse();               // 배치된 음식 좌우 변경하기

      answer += sb.toString();    // 배치된 오른쪽 음식 String으로 변경한 후, 왼쪽 음식과 합치기

      return answer;
    }
  }
}
