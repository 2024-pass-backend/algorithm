package Week3.공통.시소짝꿍;
import java.util.*;

public class jiyoon {

  class Solution {
    public long solution(int[] weights) {
      long answer = 0;
      HashMap<Double, Integer> map = new HashMap<>();

      Arrays.sort(weights);       // weights 배열 정렬
      for (int i : weights) {
        double a = i * 1.0;             // Double형태로 변환
        double b = (i * 2.0) / 3.0;     // 2 : 3의 경우
        double c = (i * 2.0) / 4.0;     // 2 : 4의 경우
        double d = (i * 3.0) / 4.0;     // 3 : 4의 경우

        if (map.containsKey(a)) answer += map.get(a);
        if (map.containsKey(b)) answer += map.get(b);
        if (map.containsKey(c)) answer += map.get(c);
        if (map.containsKey(d)) answer += map.get(d);

        map.put((i * 1.0), map.getOrDefault((i * 1.0), 0) + 1);
      }

      return answer;
    }
  }
}
