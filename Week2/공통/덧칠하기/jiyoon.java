package Week2.공통.덧칠하기;

public class jiyoon {
  public int solution(int n, int m, int[] section) {
    int answer = 0;

    boolean[] paint = new boolean[n + 1];       // 페인트로 칠해지는 구역 확인용

    for (int i = 0; i < section.length; i++) {
      int num = section[i];

      if (!paint[num]) {     // section의 i번째가 덧칠 되어야 하는 경우
        for (int j = 0; j < m; j++) {       // 덧칠 시작
          if (num + j < paint.length) {     // 벽에서 벗어나지 않는 범위에서
            paint[num + j] = true;
          }
        }
        answer++;
      }
    }

    return answer;
  }
}