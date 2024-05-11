package Week7.공통.모음사전;
import java.util.*;

public class jiyoon_review01 {
  class Solution {
    public static String[] words = {"A", "E", "I", "O", "U"};

    public int solution(String word) {
      int answer = 0;

      ArrayList<String> list = new ArrayList<>();

      for (int i = 0; i < words.length; i++) {
        dfs(list, words[i]);
      }

      for (int i = 0; i < list.size(); i++) {
        if (list.get(i).equals(word)) {
          answer = i + 1;
          break;
        }
      }

      return answer;
    }

    void dfs(List list, String s) {
      if (s.length() > 5) return;

      if (!list.contains(s)) list.add(s);

      for (int i = 0; i < words.length; i++) {
        dfs(list, s + words[i]);
      }
    }
  }
}
