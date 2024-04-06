import java.util.*;

class Solution {
  public int[] solution(int k, int[] score) {
    int[] answer = new int[score.length];
    ArrayList<Integer> list = new ArrayList<>();        // 명예의 전당

    int min = Integer.MAX_VALUE;       // 최하위 비교용
    for (int i = 0; i < score.length; i++) {
      if (i < k) {        // k일 전이기에 모든 가수가 명예에 전당에 오름
        list.add(score[i]);

      } else {            // k일 이후라면
        int num = score[i];

        if (score[i] > min) {
          list.remove(0);       // 명예의 전당 최소값 제거
          list.add(score[i]);   // 명예의 전당 점수 추가
        }
      }

      Collections.sort(list);     // 명예의 전당 list 정렬
      min = list.get(0);          // 명예의 전당 최소값 갱신

      answer[i] = min;            // answer에 최하위 점수 추가
    }
    return answer;
  }
}