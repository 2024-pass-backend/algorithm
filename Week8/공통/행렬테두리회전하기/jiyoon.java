package Week8.공통.행렬테두리회전하기;

public class jiyoon {
  class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
      int[][] arr = new int[rows + 1][columns + 1];

      // 행렬 만들기
      for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= columns; j++) {
          arr[i][j] = (columns * (i - 1)) + j;
        }
      }

      // quries범위 내 테두리 회전하기
      int[] answer = new int[queries.length];
      for (int i = 0; i < queries.length; i++) {
        answer[i] = rotate(arr, queries[i]);
      }

      return answer;
    }

    public static int rotate(int[][] arr, int[] query) {
      int x1 = query[0];
      int y1 = query[1];
      int x2 = query[2];
      int y2 = query[3];
      int start = arr[x1][y2];
      int min = Integer.MAX_VALUE;

      // 위로 이동
      for (int y = y2; y > y1; y--) {
        arr[x1][y] = arr[x1][y - 1];
        min = Math.min(min, arr[x1][y]);
      }

      // 왼쪽으로 이동
      for (int x = x1; x < x2; x++) {
        arr[x][y1] = arr[x + 1][y1];
        min = Math.min(min, arr[x][y1]);
      }

      // 아래로 이동
      for (int y = y1; y < y2; y++) {
        arr[x2][y] = arr[x2][y + 1];
        min = Math.min(min, arr[x2][y]);
      }

      // 오른쪽으로 이동
      for (int x = x2; x > x1 + 1; x--) {
        arr[x][y2] = arr[x - 1][y2];
        min = Math.min(min, arr[x][y2]);
      }

      arr[x1 + 1][y2] = start;
      min = Math.min(min, start);

      return min;
    }
  }
}
