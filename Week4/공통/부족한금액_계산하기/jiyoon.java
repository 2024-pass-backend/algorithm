package Week4.공통.부족한금액_계산하기;

public class jiyoon {
  class Solution {
    public long solution(int price, int money, int count) {
      long answer = 0;
      long sum = 0;

      // count번 타는 동안의 요금
      for (int i = 1; i <= count; i++) {
        sum += (price * i);
      }

      // 요금이 보유한 금액보다 높다면, answer = sum - money;
      if (sum > money) answer = sum - money;

      return answer;
    }
  }
}
