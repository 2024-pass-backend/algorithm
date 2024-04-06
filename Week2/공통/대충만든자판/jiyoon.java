import java.util.*;

class Solution {
  public int[] solution(String[] keymap, String[] targets) {
    int[] answer = new int[targets.length];

    HashMap<Character, Integer> keyboard = new HashMap<>();     // 자판 정보를 담을 Map(Key : 자판, Value : 자판을 누르기 위해 눌러야 할 횟수)

    for (int i = 0; i < keymap.length; i++) {       // keyboard에 자판과 횟수 입력
      for (int j = 0; j < keymap[i].length(); j++) {
        char c = keymap[i].charAt(j);

        if (!keyboard.containsKey(c)) {     // keyboard에 c값 없으면
          keyboard.put(c, j + 1);           // keyboard에 문자 값과 문자의 위치(문자를 누르는 횟수) 저장

        } else {    // keyboard에 c값이 있다면
          int now = keyboard.get(c);        // 현재 keyboard에 저장된 c의 value값

          if (now > j + 1) {                // keyboard에 저장된 Value값보다 현재 값이 더 작으면
            keyboard.replace(c, j + 1);     // 현재 값으로 갱신
          }
        }
      }
    }

    for (int i = 0; i < targets.length; i++) {
      char[] arr = targets[i].toCharArray();    // 목표 문자열로 char배열 생성

      int count = 0;
      for (char c : arr) {
        if (keyboard.containsKey(c)) {      // keyboard에 문자가 저장되어 있다면,
          count += keyboard.get(c);         // Value값 더하기

        } else {            // keyboard에 저장되지 않은 문자라면
          count = -1;       // 목표 문자열을 작성할 수 없으므로 -1
          break;
        }
      }

      answer[i] = count;
    }

    return answer;
  }
}