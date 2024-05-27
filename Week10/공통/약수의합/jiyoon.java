package Week10.공통.약수의합;

public class jiyoon {
  class Solution {
    public int solution(int n) {
      int sum = 0;

      for (int i = 1; i <= n; i++) {
        if (n % i == 0) sum += i;
      }
      return sum;
    }
  }
}
