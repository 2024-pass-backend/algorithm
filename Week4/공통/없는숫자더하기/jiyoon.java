package Week4.공통.없는숫자더하기;

public class jiyoon {
  class Solution {
    public int solution(int[] numbers) {
      int answer = 45;    // 0 ~ 9까지의 합
      for (int i : numbers) answer -= i;      // numbers에 있는 수들을 answer에서 뺄셈
      return answer;
    }
  }
}
