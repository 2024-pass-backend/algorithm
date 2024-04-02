package Week2.공통.대충만든자판;

import java.util.*;

public class jiyoon {
  public int[] solution(String[] keymap, String[] targets) {
    int[] answer = new int[targets.length];

    // 자판 정보를 담을 Map(Key : 자판, Value : 자판을 누르기 위해 눌러야 할 횟수)
    HashMap<Character, Integer> keyboard = new HashMap<>();

    for (int i = 0; i < keymap.length; i++) {       // keyboard에 자판과 횟수 입력
      for (int j = 0; j < keymap[i].length(); j++) {
        char c = keymap[i].charAt(j);
        int index = j + 1;

        if (keyboard.containsKey(c)) {
          keyboard.put(c, Math.min(index, keyboard.get(c)));
        } else {
          keyboard.put(c, index);
        }
      }
    }

    for (int i = 0; i < targets.length; i++) {
      String target = targets[i];
      boolean check = false;
      int count = 0;

      for (char c : target.toCharArray()) {   // 입력하려는 문자열로 char배열 생성
        if (keyboard.containsKey(c)) {
          count += keyboard.get(c);
        } else {
          check = true;
          break;
        }
      }

      if (check) answer[i] = -1;      // 목표 문자열 작성 불가능
      else answer[i] = count;         // 목표 문자열 작성 가능
    }

    return answer;
  }
}