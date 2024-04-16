package Week4.공통.귤고르기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int k, int[] tangerine) {
      int answer = 0;

      HashMap<Integer, Integer> map = new HashMap<>();        // Key : 귤의 크기, Value : 등장 횟수

      for (int i = 0; i < tangerine.length; i++) {
        int num = tangerine[i];

        if (!map.containsKey(num)) map.put(num, 1);         // 처음 등장한 귤의 크기라면 map.put(크기, 1);
        else map.replace(num, map.get(num) + 1);            // 이 외의 경우 등장 횟수 + 1
      }

      Integer[] arr = new Integer[map.size()];        // 등장 횟수만 담을 배열

      int temp = 0;
      for (int i : map.keySet()) {        // map 순회
        arr[temp] = map.get(i);           // 귤의 등장 횟수를 배열에 저장
        temp++;
      }

      Arrays.sort(arr, Collections.reverseOrder());       // 내림차순 정렬

      for (int i : arr) {     // 내림차순 정렬된 배열 순회
        int num = i;
        k -= num;             // 귤의 개수만큼 빼기
        answer++;             // answer ++;
        if (k <= 0) break;    // k가 0 이하라면 순회 종료
      }

      return answer;
    }
  }
}
