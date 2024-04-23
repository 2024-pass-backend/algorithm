package Week5.공통.롤케이크_자르기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int[] topping) {
      int answer = 0;

      HashSet<Integer> left = new HashSet<>();                // 왼쪽 케이크 정보
      HashMap<Integer, Integer> right = new HashMap<>();      // 오른쪽 케이크 정보

      for (int i = 0; i < topping.length; i++) {
        right.put(topping[i], right.getOrDefault(topping[i], 0) + 1);
      }

      for (int i = 0; i < topping.length; i++) {
        // 케이크 자르기
        left.add(topping[i]);
        right.put(topping[i], right.get(topping[i]) - 1);

        if (right.get(topping[i]) == 0) {       // 오른쪽에 더이상 topping[i]가 없다면
          right.remove(topping[i]);           // Map에서 제거
        }

        if (left.size() == right.size()) {      // left와 right의 크기가 같다면
          answer++;                           // answer++;
        }
      }

      return answer;
    }
  }
}
