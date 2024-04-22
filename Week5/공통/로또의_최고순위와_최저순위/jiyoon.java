package Week5.공통.로또의_최고순위와_최저순위;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
      int[] answer = new int[2];      // answer[0] = 최고 순위, answer[1] = 최저 순위

      ArrayList<Integer> list = new ArrayList<>();
      for (int i = 0; i < lottos.length; i++) {
        list.add(lottos[i]);        // lottos배열의 값을 list에 추가
      }

      for (int i = 0; i < win_nums.length; i++) {
        // win_nums[i]의 값을 list가 가지고 있다면, win_nums[i]의 인덱스 값을 제거
        if (list.contains(win_nums[i])) list.remove(Integer.valueOf(win_nums[i]));
      }

      int temp = 0;       // list의 0의 개수 세기용
      for (int i = 0; i < list.size(); i++) {
        if (list.get(i) == 0) temp++;
      }

      answer[0] = list.size() - temp + 1;     // 최고 점수
      answer[1] = list.size() + 1;            // 최저 점수

      if (answer[0] > 6) answer[0] = 6;       // 최고 점수가 6초과라면, 6으로 변경
      if (answer[1] > 6) answer[1] = 6;       // 최저 점수가 6초과라면, 6으로 변경

      return answer;
    }
  }
}
