package Week9.공통.삼각달팽이;

public class jiyoon {
  class Solution {
    public int[] solution(int n) {
      int[][] arr = new int[n + 1][n + 1];

      int x = -1, y = 0;
      int num = 1;

      // 달팽이 채우기 배열 생성
      for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
          if (i % 3 == 0) {     // 아래로 이동
            x++;
          } else if (i % 3 == 1) {        // 오른쪽으로 이동
            y++;
          } else if (i % 3 == 2) {        // 위로 이동
            x--;
            y--;
          }

          arr[x][y] = num;
          num++;
        }
      }

      // 첫 행부터 마지막 행까지 순서대로 합친 새로운 배열 생성
      int temp = 0;
      int[] answer = new int[num - 1];
      for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
          answer[temp] = arr[i][j];
          temp++;
        }
      }

      return answer;
    }
  }
}
