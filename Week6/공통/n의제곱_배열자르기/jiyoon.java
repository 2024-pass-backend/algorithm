package Week6.공통.n의제곱_배열자르기;
import java.util.*;

public class jiyoon {
  class Solution {
    public List<Long> solution(int n, long left, long right) {
      List<Long> list = new ArrayList<>();

      for (long l = left; l <= right; l++) {
        list.add(Math.max(l / n, l % n) + 1);
      }

      return list;
    }
  }
}
