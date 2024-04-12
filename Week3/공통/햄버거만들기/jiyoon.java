package Week3.공통.햄버거만들기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int[] ingredient) {
      int answer = 0;
      ArrayList<Integer> list = new ArrayList<>();        // ingredient[]을 담을 ArrayList

      for (int i = 0; i < ingredient.length; i++) {
        list.add(ingredient[i]);
        int size = list.size() - 1;
        if (size >= 3) {                // list의 사이즈가 4 이상이라면(size정의할 때 -1했음)
          if (list.get(size - 3) == 1 && list.get(size - 2) == 2
                  && list.get(size - 1) == 3 && list.get(size) == 1) {    // 1 - 2 - 3 - 1이라면
            answer++;                   // answer++;
            list.remove(size);          // 햄버거 구간 삭제
            list.remove(size - 1);
            list.remove(size - 2);
            list.remove(size - 3);
          }
        }
      }
      return answer;
    }
  }
}
