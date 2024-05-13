package Week8.공통.평균구하기;

public class jiyoon {
  class Solution {
    public double solution(int[] arr) {
      double answer = 0;
      for (int i : arr) answer += i;
      answer /= arr.length;
      return answer;
    }
  }
}
