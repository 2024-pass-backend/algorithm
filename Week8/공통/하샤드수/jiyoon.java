package Week8.공통.하샤드수;

public class jiyoon {
  class Solution {
    public boolean solution(int x) {
      boolean answer = false;

      int num = x;
      int temp = 0;

      while (true) {
        temp += num % 10;
        num /= 10;

        if (num == 0) break;
      }

      if (x % temp == 0) answer = true;
      return answer;
    }
  }
}
