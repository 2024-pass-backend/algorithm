package Week7.공통.모음사전;
import java.util.*;

public class jiyoon {
  class Solution {
    static final char[] words = {'A', 'E', 'I', 'O', 'U'};

    public int solution(String word) {
      int answer = 0;

      ArrayList<String> list = new ArrayList<>();     // 생성 가능한 모든 문자 조합을 저장할 ArrayList

      // dfs를 통해 가능한 모든 조합 생성
      for (int i = 0; i < words.length; i++) {
        dfs(list, String.valueOf(words[i]));
      }

      // word랑 동일한 문자열 찾기
      for (int i = 0; i < list.size(); i++) {
        if (list.get(i).equals(word)) {
          answer = i + 1;
        }
      }


      return answer;
    }

    void dfs(List list, String s) {
      if (s.length() > 5) return;     // word의 길이는 5 이하

      if (!list.contains(s)) list.add(s);     // list에 존재하지 않는 문자라면 list에 추가

      // 생성 가능한 모든 조합 dfs 실행
      for (int i = 0; i < words.length; i++) {
        dfs(list, s + words[i]);
      }
    }
  }
}
