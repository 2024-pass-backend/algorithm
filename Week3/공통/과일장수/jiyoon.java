package Week3.공통.과일장수;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int k, int m, int[] score) {
      int answer = 0;

      // int형 배열을 Integer형 배열로 변경
      Integer[] arr = Arrays.stream(score).boxed().toArray(Integer[]::new);
      // Integer형 배열을 내림차순 정렬
      Arrays.sort(arr, Collections.reverseOrder());

      // 한 상자당 m개씩 담기
      for (int i = 0; i < score.length / m; i++) {
        int min = k;        // 상자 내 최저 점수 확인용
        for (int j = 0; j < m; j++) {
          min = Math.min(arr[(i * m) + j], min);
        }
        answer += (min * m);    // 최저 점수로 m개씩 담긴 사과 상자 점수 더하기
      }
      return answer;
    }
  }
}
