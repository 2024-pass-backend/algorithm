package Week10.공통.소수찾기;

public class jiyoon {
  class Solution {
    public int solution(int n) {
      int answer = 0;

      for (int i = 2; i <= n; i++) {
        if (isPrime(i)) answer++;
      }

      return answer;
    }

    private boolean isPrime(int num) {
      for (int i = 2; i <= Math.sqrt(num); i++) {
        if (num % i == 0) {
          return false;
        }
      }

      return true;
    }
  }
}
