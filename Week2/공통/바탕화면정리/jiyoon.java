package Week2.공통.바탕화면정리;

public class jiyoon {
  public int[] solution(String[] wallpaper) {
    // 드래그 시작점
    int lux = Integer.MAX_VALUE;
    int luy = Integer.MAX_VALUE;

    // 드래그 끝점
    int rdx = 0;
    int rdy = 0;

    for (int i = 0; i < wallpaper.length; i++) {
      for (int j = 0; j < wallpaper[0].length(); j++) {
        if (wallpaper[i].charAt(j) == '#') {
          // 드래그 시작점 갱신
          if (lux > i) lux = i;
          if (luy > j) luy = j;

          // 드래그 끝점 갱신
          if (rdx < i) rdx = i;
          if (rdy < j) rdy = j;
        }
      }
    }

    int[] answer = {lux, luy, rdx + 1, rdy + 1};

    return answer;
  }
}