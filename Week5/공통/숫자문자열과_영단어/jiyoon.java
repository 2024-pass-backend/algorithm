package Week5.공통.숫자문자열과_영단어;

public class jiyoon {
  class Solution {
    public int solution(String s) {
      int answer = 0;
      String[] words = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

      for (int i = 0; i < words.length; i++) {
        if (s.contains(words[i])) {                               // s에 영단어 문자가 있다면
          s = s.replaceAll(words[i], Integer.toString(i));        // 해당 문자열을 숫자로 변경
        }
      }

      answer = Integer.parseInt(s);

      return answer;
    }
  }
}
