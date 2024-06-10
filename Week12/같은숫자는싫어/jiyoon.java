package Week12.같은숫자는싫어;
import java.util.*;

public class jiyoon {
  public class Solution {
    public int[] solution(int [] arr) {
      LinkedList<Integer> list = new LinkedList<>();
      list.add(arr[0]);

      int pre = arr[0];
      int now = 0;
      for (int i = 1; i < arr.length; i++) {
        now = arr[i];

        if (pre != now) {
          list.add(now);

          pre = now;
        }
      }

      // LinkedList를 Array로 변환
      int[] answer = list.stream().mapToInt(Integer::intValue).toArray();
      return answer;
    }
  }
}
