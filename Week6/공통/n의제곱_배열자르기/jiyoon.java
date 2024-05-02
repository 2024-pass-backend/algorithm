package Week6.공통.n의제곱_배열자르기;
import java.util.*;

public class jiyoon {
  class Solution {
    public int[] solution(int n, long left, long right) {
      // n^2 배열 생성하기
      int[][] arr = new int[n][n];
      for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
          if (i == j) {
            arr[i][j] = i + 1;
          } else {
            arr[i][j] = j + 1;
            arr[j][i] = j + 1;
          }
        }
      }

      // 생성한 배열을 ArrayList로 변환
      ArrayList<Integer> list = new ArrayList<>();
      for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
          list.add(arr[i][j]);
        }
      }

      // left~right 사이 배열 값 저장
      int[] answer = new int[(int)(right - left + 1)];
      for (int i = 0; i < answer.length; i++) {
        answer[i] = list.get((int)left + i);
      }

      return answer;
    }
  }
}
