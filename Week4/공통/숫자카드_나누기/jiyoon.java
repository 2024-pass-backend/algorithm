package Week4.공통.숫자카드_나누기;

public class jiyoon {
  class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
      int answer = 0;

      // 철수가 가진 카드들 중 모든 숫자를 나눌 수 있는 최댓값(gcdA)
      // 영희가 가진 카드들 중 모든 숫자를 나눌 수 있는 최댓값(gcdB)
      int gcdA = arrayA[0];
      int gcdB = arrayB[0];
      for (int i = 1; i < arrayA.length; i++) {       // 배열의 크기가 동일하므로 동시 진행
        gcdA = gcd(gcdA, arrayA[i]);
        gcdB = gcd(gcdB, arrayB[i]);
      }

      int A = 0;      // 조건 1.을 만족하는 양의 정수 A
      int B = 0;      // 조건 2.을 만족하는 양의 정수 A

      // 영희가 가진 카드들에서 하나도 나눌 수 없는 양의 정수인지 판별
      for (int i = 0; i < arrayA.length; i++) {
        if (gcdA != 1 && arrayB[i] % gcdA != 0) B = gcdA;
        else {
          B = 0;
          break;
        }
      }

      // 철수가 가진 카드들에서 하나도 나눌 수 없는 양의 정수인지 판별
      for (int i = 0; i < arrayB.length; i++) {
        if (gcdB != 1 && arrayA[i] % gcdB != 0) A = gcdB;
        else {
          A = 0;
          break;
        }
      }

      return Math.max(A, B);
    }

    // 최대 공약수
    public static int gcd (int a, int b) {
      if (a % b == 0) return b;
      return gcd(b, a % b);
    }
  }
}
