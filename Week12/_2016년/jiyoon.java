package Week12._2016년;

public class jiyoon {
  class Solution {
    public String solution(int a, int b) {
      String answer = "";
      String[] day = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

      int[] month = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30};

      int days = 0;
      for (int i = 0; i < a; i++) days += month[i];
      days += b;

      answer = day[(days + 4) % 7];
      return answer;
    }
  }
}
