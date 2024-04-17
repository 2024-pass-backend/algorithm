package Week4.공통.삼총사;

public class jiyoon {
  class Solution {
    public int solution(int[] number) {
      int answer = 0;
      for (int i = 0; i < number.length - 2; i++) {
        for (int j = i + 1; j < number.length - 1; j++) {
          for (int k = j + 1; k < number.length; k++) {
            int temp = number[i] + number[j] + number[k];       // 세 명의 학생들의 합

            if (temp == 0) answer++;        // 삼총사 조건을 만족하면 answer++;
          }
        }
      }

      return answer;
    }
  }
}
