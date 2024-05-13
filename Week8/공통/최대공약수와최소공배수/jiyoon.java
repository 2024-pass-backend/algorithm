package Week8.공통.최대공약수와최소공배수;

public class jiyoon {
  class Solution {
    public int[] solution(int n, int m) {
      int[] answer = new int[2];
      answer[0] = gcd(n, m);
      answer[1] = lcm(n, m);
      return answer;
    }

    // 최대 공약수
    public static int gcd(int a, int b) {
      if (a % b == 0) return b;
      return gcd(b, a % b);
    }

    // 최소 공배수
    public static int lcm(int a, int b) {
      return a * b / gcd(a, b);
    }
  }
}
