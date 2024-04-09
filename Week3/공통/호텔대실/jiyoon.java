package Week3.공통.호텔대실;

public class jiyoon {
  class Solution {
    public int solution(String[][] book_time) {
      int answer = 0;
      int[] fulltime = new int[24 * 60 + 10];
      int[][] time = new int[book_time.length][2];

      int index = 0;
      // 대실 시간 정보 저장
      for (String[] book : book_time) {
        time[index][0] = time(book[0]);
        time[index][1] = time(book[1]) + 10;        // 10분 : 청소 시간
        index++;
      }

      for (int[] t : time) {
        fulltime[t[0]]++;       // 대실 시작 시간
        fulltime[t[1]]--;       // 청소 종료 시간
      }

      // 누적합 알고리즘 사용
      for (int i = 1; i < fulltime.length; i++) {
        fulltime[i] += fulltime[i - 1];
        answer = Math.max(answer, fulltime[i]);     // Math.max를 사용하여 하는 객실 갯수 구하기
      }

      return answer;
    }

    public int time(String book) {
      int hour = Integer.parseInt(book.split(":")[0]) * 60;
      int min = Integer.parseInt(book.split(":")[1]);

      return hour + min;
    }

  }
}
