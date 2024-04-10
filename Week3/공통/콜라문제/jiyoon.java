package Week3.공통.콜라문제;

public class jiyoon {
  class Solution {
    public int solution(int a, int b, int n) {
      int answer = 0;     // 상빈이가 받을 수 있는 콜라 병 수

      while(n >= a) {
        answer += (n / a) * b;          // 빈병을 주고 받을 수 있는 콜라 병 수를 answer에 추가
        n = (n / a) * b + (n % a);      // 빈병 갱신
      }

      return answer;
    }
  }
}
