package Week10.공통.튜플;
import java.util.*;

public class jiyoon_re {
  class Solution {
    public int[] solution(String s) {
      s = s.substring(2, s.length() - 2);

      System.out.println(s);

      String[] arr = s.split("\\},\\{");

      Arrays.sort(arr, (s1, s2) -> Integer.compare(s1.length(), s2.length()));

      System.out.println(Arrays.toString(arr));

      int[] answer = new int[arr.length];

      HashSet<Integer> set = new HashSet<>();

      int index = 0;
      StringTokenizer st;
      for (String str : arr) {
        st = new StringTokenizer(str, ",");

        while (st.hasMoreTokens()) {
          int num = Integer.parseInt(st.nextToken());

          if (!set.contains(num)) {
            set.add(num);
            answer[index++] = num;
          }
        }
      }
      return answer;
    }
  }
}
