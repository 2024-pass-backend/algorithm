package Week11.방문길이;

public class jiyoon {
  class Solution {
    static int x, y, count;
    static char direction;
    static int[] dx = {0, 1, -1, 0}, dy = {1, 0, 0, -1};
    static boolean[][][] visited;

    public int solution(String dirs) {
      visited = new boolean[11][11][4];

      x = 5;
      y = 5;

      for (int i = 0; i < dirs.length(); i++) {
        direction = dirs.charAt(i);
        int k = 0;

        if (direction == 'U') k = 0;          // ↑
        else if (direction == 'R') k = 1;     // →
        else if (direction == 'L') k = 2;     // ←
        else if (direction == 'D') k = 3;     // ↓

        int nx = x + dx[k];
        int ny = y + dy[k];

        // 범위 밖이라면 이동 불가
        if (nx < 0 || ny < 0 || nx > 10 || ny > 10) continue;

        // k 방향으로 방문한 적이 없다면
        if (!visited[x][y][k] && !visited[nx][ny][3 - k]) {
          count++;                        // 처음 걸어본 길의 길이 + 1
          visited[x][y][k] = true;        // 방문 표시
          visited[nx][ny][3 - k] = true;  // 방문 표시
        }

        x = nx;
        y = ny;
      }

      return count;
    }
  }
}
