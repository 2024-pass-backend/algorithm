package Week12.폰켓몬;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int[] nums) {
      int answer = 0;

      // 폰켓몬의 종류와 마리 수를 저장할 HashMap
      HashMap<Integer, Integer> map = new HashMap<>();    // Key : 종류, Value : 마리 수
      for (int i : nums) {
        map.put(i, map.getOrDefault(i, 0) + 1);
      }

      // map.size()가 폰켓몬의 n마리 수 / 2보다 크다면 총 마리수의 절반 반환, 아니라면 map 크기 반환
      answer = map.size() >= nums.length / 2 ? nums.length / 2 : map.size();

      return answer;
    }
  }
}
