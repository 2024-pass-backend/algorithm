package Week4.공통.나머지가_1이되는_수찾기;

public class jiyoon {
  class Solution {
    public int solution(int n) {
      int answer = Integer.MAX_VALUE;     // answer의 값을 최댓값으로 설정
      for (int i = 1; i < n; i++) {
        if (n % i == 1) {                   // n % i == 1이라면
          answer = Math.min(i, answer);   // i와 answer를 비교해서 최솟값을 answer에 저장
        }
      }
      return answer;
    }
  }
}
