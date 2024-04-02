package Week2.공통.광물캐기;

import java.util.*;

public class jiyoon {

  static class Mineral {
    private int diamond;
    private int iron;
    private int stone;

    public Mineral(int diamond, int iron, int stone) {
      this.diamond = diamond;
      this.iron = iron;
      this.stone = stone;
    }
  }

  static int[][] scoreBoard;
  static List<Mineral> list;

  public int solution(int[] picks, String[] minerals) {
    int answer = 0;

    scoreBoard = new int[][]{{1, 1, 1}, {5, 1, 1}, {25, 5, 1}};

    int total = Arrays.stream(picks).sum();
    // Arrays.stream(picks) : picks 배열을 스트림으로 변환
    // sum() : 해당 스트림의 모든 요소를 합산하여 최종 결과를 반환
    // -> picks 배열의 모든 요소를 합한 값

    list = new ArrayList<>();

    for (int i = 0; i < minerals.length; i += 5) {
      if (total == 0) break;

      int dia = 0, iron = 0, stone = 0;
      for (int j = i; j < i + 5; j++) {   // 한 번에 채굴할 수 있는 미네랄의 종류 확인
        if (j == minerals.length) break;

        String mineral = minerals[j];
        int val = mineral.equals("iron") ? 1 :
                mineral.equals("stone") ? 2 : 0;

        dia += scoreBoard[0][val];
        iron += scoreBoard[1][val];
        stone += scoreBoard[2][val];
      }

      list.add(new Mineral(dia, iron, stone));
      total--;
    }

    // 돌의 가치를 기준으로 내림차순으로 정렬(최소한의 피로도를 구하기 위해)
    Collections.sort(list, ((o1, o2) -> (o2.stone - o1.stone)));

    // 피로도 계산
    for (Mineral m : list) {
      int dia = m.diamond;
      int iron = m.iron;
      int stone = m.stone;

      if (picks[0] > 0) {
        answer += dia;
        picks[0]--;
        continue;
      }

      if (picks[1] > 0) {
        answer += iron;
        picks[1]--;
        continue;
      }

      if (picks[2] > 0) {
        answer += stone;
        picks[2]--;
        continue;
      }
    }
    return answer;
  }
}