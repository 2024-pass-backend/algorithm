package Week11.문자열내p와y의개수;

public class jiyoon {
  class Solution {
    boolean solution(String s) {
      s = s.toLowerCase();

      int countP = 0;
      int countY = 0;

      for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == 'p') countP++;
        else if (s.charAt(i) == 'y') countY++;
      }

      return countP == countY ? true : false;
    }
  }
}
