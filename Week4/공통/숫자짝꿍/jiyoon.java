package Week4.공통.숫자짝꿍;

public class jiyoon {
  class Solution {
    public String solution(String X, String Y) {
      String answer = "";
      StringBuilder sb = new StringBuilder();
      int[] checkX = new int[10];     // X에서의 숫자 등장 확인
      int[] checkY = new int[10];     // Y에서의 숫자 등장 확인

      for (int i = 0; i < X.length(); i++) {
        int c = X.charAt(i) - '0';
        checkX[c]++;
      }

      for (int i = 0; i < Y.length(); i++) {
        int c = Y.charAt(i) - '0';
        checkY[c]++;
      }

      boolean zero = true;
      for (int i = 9; i >= 0; i--) {
        if (checkX[i] > 0 && checkY[i] > 0) {
          if (i != 0) zero = false;
          for (int j = 0; j < Math.min(checkX[i], checkY[i]); j++) {
            sb.append(i);
          }
        }
      }

      if (sb.length() != 0 && zero) answer = "0";
      else if (sb.length() == 0) answer = "-1";
      else answer = sb.toString();

      return answer;
    }
  }
}
