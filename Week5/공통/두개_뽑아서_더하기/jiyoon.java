package Week5.공통.두개_뽑아서_더하기;
import java.util.*;

public class jiyoon {
  class Solution {
    public ArrayList<Integer> solution(int[] numbers) {
      HashSet<Integer> set = new HashSet<>();     // HashSet은 중복 값을 허용하지 않기 때문에 사용

      for (int i = 0; i < numbers.length - 1; i++) {
        for (int j = i + 1; j < numbers.length; j++) {
          set.add(numbers[i] + numbers[j]);       // 서로 다른 인덱스에 있는 두 수의 덧셈을 set에 추가
        }
      }

      ArrayList<Integer> list = new ArrayList<>(set);     // HashSet의 값들을 ArrayList로 변환
      Collections.sort(list);     // ArrayList 오름차순 정렬
      return list;
    }
  }
}
