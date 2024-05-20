package Week9.공통.제일작은수제거하기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int[] arr) {
      ArrayList<Integer> list = new ArrayList<>();

      int min = Integer.MAX_VALUE;
      for (int i = 0; i < arr.length; i++) {
        if (min > arr[i]) min = arr[i];
      }

      for (int i : arr) {
        if (min != i) {
          list.add(i);
        }
      }

      if (list.size() == 0) list.add(-1);

      int[] answer = new int[list.size()];
      for (int i = 0; i < list.size(); i++) {
        answer[i] = list.get(i);
      }

      return answer;
    }
  }
}
