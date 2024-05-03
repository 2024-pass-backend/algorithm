package Week6.공통.완주하지못한선수;
import java.util.*;

public class jiyoon {
  class Solution {
    public String solution(String[] participant, String[] completion) {
      String answer = "";

      // 마라톤 경기에 참여한 선수들의 이름을 HashMap에 저장
      // Key : 이름, Value : 참가 횟수(동명이인 참가 가능)
      HashMap<String, Integer> map = new HashMap<>();
      for (int i = 0; i < participant.length; i++) {
        String name = participant[i];
        map.put(name, map.getOrDefault(participant[i], 0) + 1);
      }

      // 완주한 선수의 이름을 map에서 찾고 참가 횟수 - 1;
      for (int i = 0; i < completion.length; i++) {
        String name = completion[i];
        map.put(name, map.get(name) - 1);

        if (map.get(name) == 0) {   // 완주한 선수의 참가 횟수가 0이 된다면
          map.remove(name);       // map에서 제거
        }
      }

      for (String s : map.keySet()) {     // map에 남겨진 선수의 이름을
        answer = s;                     // answer에 저장
      }

      return answer;
    }
  }
}
