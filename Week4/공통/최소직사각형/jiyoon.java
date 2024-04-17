package Week4.공통.최소직사각형;

public class jiyoon {
  class Solution {
    public int solution(int[][] sizes) {
      int max_width = 0;
      int max_height = 0;

      for (int i = 0; i < sizes.length; i++) {
        int width = Math.min(sizes[i][0], sizes[i][1]);         // 너비를 명함의 최솟값으로 설정
        int height = Math.max(sizes[i][0], sizes[i][1]);        // 높이를 명함의 최댓값으로 설정
        max_width = Math.max(max_width, width);
        max_height = Math.max(max_height, height);
      }

      return max_width * max_height;
    }
  }
}
