package Week9.공통.정수제곱근판별;

public class jiyoon {
  class Solution {
    public long solution(long n) {
      for (long i = 1; i * i <= n; i++) {
        if (i * i == n) return (long)(i + 1) * (i + 1);
      }
      return -1;
    }
  }
}
