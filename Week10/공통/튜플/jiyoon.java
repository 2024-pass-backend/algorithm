package Week10.공통.튜플;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(String s) {
      // {{, }} 괄호 제거
      s = s.substring(2, s.length() - 2);

      // "},{"를 기준으로 문자열 쪼개기
      String[] words = s.split("\\},\\{");

      // words를 문자열 길이를 기준으로 오름차순 정렬
      Arrays.sort(words, (s1, s2) -> Integer.compare(s1.length(), s2.length()));

      int[] answer = new int[words.length];

      // 튜플의 정보를 저장할 tuple set
      HashSet<Integer> tuple = new HashSet<>();

      int index = 0;
      StringTokenizer st;
      for (String word : words) {
        // ","를 기준으로 문자열 토큰화
        st = new StringTokenizer(word, ",");

        while (st.hasMoreTokens()) {      // 토큰이 남아있다면
          int num = Integer.parseInt(st.nextToken());

          if (!tuple.contains(num)) {       // set에 포함된 숫자가 아니라면
            tuple.add(num);                 // set에 추가
            answer[index] = num;          // answer에 추가
            index++;                      // answer의 index 추가

          }
        }
      }
      return answer;
    }
  }
}
