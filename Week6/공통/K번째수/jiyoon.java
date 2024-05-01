package Week6.공통.K번째수;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int[] array, int[][] commands) {
      int[] answer = new int[commands.length];

      // 잘라낸 배열의 정보를 저장할 ArrayList 생성
      ArrayList<Integer> list = new ArrayList<>();
      for (int i = 0; i < commands.length; i++) {

        // 배열 자르기
        for (int j = commands[i][0] - 1; j <= commands[i][1] - 1; j++) {
          list.add(array[j]);
        }

        // list 정렬하기
        Collections.sort(list);

        // k번째에 있는 수 찾기
        answer[i] = list.get(commands[i][2] - 1);

        // list 초기화
        list.clear();
      }

      return answer;
    }
  }
}
