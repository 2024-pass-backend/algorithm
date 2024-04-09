package Week3.공통.무인도여행;
import java.util.*;

public class jiyoon {
  class Solution {
    static int day;                 // 무인도에서 머무를 수 있는 기간
    static char[][] map;            // map의 2차원 배열
    static boolean[][] visited;     // 방문 표시
    static int[] dx = {-1, 1, 0, 0}, dy = {0, 0, -1, 1};        // 상하좌우 이동

    public List<Integer> solution(String[] maps) {
      map = new char[maps.length][maps[0].length()];
      visited = new boolean[maps.length][maps[0].length()];

      // maps배열을 2차원 char배열로 변경
      for (int i = 0; i < maps.length; i++) {
        map[i] = maps[i].toCharArray();
      }

      // 섬마다 최대 며칠씩 머무를 수 있는 지 저장할 ArrayList
      ArrayList<Integer> answer = new ArrayList<>();

      for (int i = 0; i < map.length; i++) {
        for (int j = 0; j < map[0].length; j++) {
          // 해당 지점을 방문한 적이 없고, 음식이 있다면 탐색 시작
          if (!visited[i][j] && map[i][j] != 'X') {
            day = 0;
            dfs(i, j);
            answer.add(day);
          }
        }
      }

      if (answer.size() == 0) answer.add(-1);     // 무인도가 없다면 -1

      Collections.sort(answer);

      return answer;
    }

    private void dfs(int i, int j) {
      day += map[i][j] - '0';
      visited[i][j] = true;       // 방문 처리

      for (int k = 0; k < 4; k++) {
        int x = i + dx[k];
        int y = j + dy[k];

        if (x >= 0 && y >= 0 && x < map.length && y < map[0].length) {      // map의 범위 내에 있고
          if (!visited[x][y] && map[x][y] != 'X') {                       // 방문하지 않았고 식량이 있다면
            dfs(x, y);                                                  // dfs 실행
          }
        }
      }
    }
  }
}
