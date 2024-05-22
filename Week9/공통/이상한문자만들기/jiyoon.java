package Week9.공통.이상한문자만들기;

public class jiyoon {
  class Solution {
    public String solution(String s) {
      String answer = "";
      int count = 0;
      String[] arr = s.split("");

      for (String word : arr) {
        if (word.equals(" ")) {
          count = 0;
        } else count++;

        if (count % 2 != 0) word = word.toUpperCase();
        else word = word.toLowerCase();

        answer += word;
      }


      return answer;
    }
  }
}
