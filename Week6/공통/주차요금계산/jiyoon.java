package Week6.공통.주차요금계산;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int[] fees, String[] records) {

      // 차량 입차 시간을 저장할 HashMap 생성
      HashMap<String, Integer> map = new HashMap<>();         // Key : 차량 번호, Value : 입차 시간

      // 차량 번호가 작은 자동차부터 출력해야 하므로 TreeMap 사용
      TreeMap<String, Integer> tree = new TreeMap<>();        // Key : 차량 번호, Value : 주차 시간

      StringTokenizer st;
      for (int i = 0; i < records.length; i++) {
        st = new StringTokenizer(records[i]);
        int timeRecord = time(st.nextToken());
        String car = String.format("%04d", Integer.parseInt(st.nextToken()));
        String check = st.nextToken();

        if (check.equals("IN")) {       // 입차
          map.put(car, timeRecord);
        } else {                        // 출차
          int total = timeRecord - map.get(car);      // 주차한 시간

          if (!tree.containsKey(car)) tree.put(car, total);
          else tree.put(car, tree.get(car) + total);

          map.remove(car);            // 출차되었으므로 map에서 삭제
        }
      }

      // 출차된 기록이 없다면
      for (String s : map.keySet()) {
        int total = (23 * 60 + 59) - map.get(s);        // 23:59에 출차한 것으로 간주

        if (!tree.containsKey(s)) tree.put(s, total);
        else tree.put(s, tree.get(s) + total);
      }

      int i = 0;
      int[] answer = new int[tree.size()];
      for (String s : tree.keySet()) {
        int calcTime = tree.get(s) - fees[0];
        int calcFee = fees[1];

        if (calcTime > 0) {
          int temp = calcTime / fees[2];
          if (calcTime % fees[2] != 0) temp++;
          calcFee += temp * fees[3];
        }

        answer[i] = calcFee;
        i++;
      }

      return answer;
    }

    public int time(String timeRecord) {
      int hour = Integer.parseInt(timeRecord.split(":")[0]) * 60;
      int min = Integer.parseInt(timeRecord.split(":")[1]);

      return hour + min;
    }
  }
}
