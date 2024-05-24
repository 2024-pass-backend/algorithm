package Week9.공통.삼각달팽이;

public class jiyoon_re {
  class Solution {
    public int[] solution(int n) {
      int[][] arr = new int[n + 1][n + 1];

      int num = 1;
      int x = -1, y = 0;
      for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
          if (i % 3 == 0) {
            x++;
          } else if (i % 3 == 1) {
            y++;
          } else if (i % 3 == 2) {
            x--;
            y--;
          }

          arr[x][y] = num;
          num++;
        }
      }

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
