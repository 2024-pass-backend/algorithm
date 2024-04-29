package Week6.공통.체육복;
import java.util.*;

public class jiyoon {
  class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
      int answer = 0;
      int[] sportWear = new int[n + 1];       // 각 학생들의 체육복 개수
      Arrays.fill(sportWear, 1);


      // 체육복 안가져온 학생
      for (int i = 0; i < lost.length; i++) {
        sportWear[lost[i]]--;
      }

      // 여벌 체육복이 있는 학생
      for (int i = 0; i < reserve.length; i++) {
        sportWear[reserve[i]]++;
      }

      // 체육복 빌려주기
      for (int i = 1; i <= n; i++) {
        // 바로 앞의 학생에게 빌려주기
        if (sportWear[i] > 1 && i > 1 && sportWear[i - 1] == 0) {
          sportWear[i - 1]++;
          sportWear[i]--;
        }

        // 바로 뒤의 학생에게 빌려주기
        if (sportWear[i] > 1 && i < n && sportWear[i + 1] == 0) {
          sportWear[i + 1]++;
          sportWear[i]--;
        }
      }

      // 체육 수업을 들을 수 있는 학생의 최댓값
      for (int i = 1; i <= n; i++) {
        if (sportWear[i] > 0) answer++;
      }

      return answer;
    }
  }
}
