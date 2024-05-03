package Week6.공통.실패율;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int N, int[] stages) {
      int[] answer = new int[N];

      // Key : 스테이지 번호, Value : 해당 스테이지의 플레이어 수(실패율 분모)
      HashMap<Integer, Integer> player = new HashMap<>();
      for (int i = 0; i < stages.length; i++) {
        //if (stages[i] >= N) stages[i] = N;
        player.put(stages[i], player.getOrDefault(stages[i], 0) + 1);
      }

      // 실패율 계산하기
      Double totalPlayer = (double)stages.length;
      HashMap<Integer, Double> fail = new HashMap<>();
      for (int i = 1; i <= N; i++) {
        if (player.containsKey(i)) {
          fail.put(i, player.get(i) / totalPlayer);
          totalPlayer -= player.get(i);
        } else {
          fail.put(i, 0.0);
        }
      }

      // list를 fail의 값을 기준으로 내림차순으로 정렬
      ArrayList<Integer> list = new ArrayList<>(fail.keySet());
      Collections.sort(list, (o1, o2) ->
              fail.get(o2).compareTo(fail.get(o1)));

      for (int i = 0; i < N; i++) {
        answer[i] = list.get(i);
      }
      return answer;
    }
  }
}
