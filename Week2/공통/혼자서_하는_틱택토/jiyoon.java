package Week2.공통.혼자서_하는_틱택토;

import java.util.*;

public class jiyoon
  class Solution {
    public int solution(String[] board) {

      int o = 0;      // "O"의 등장 횟수
      int x = 0;      // "X"의 등장 횟수

      HashMap<Integer, Character> map = new HashMap<>();      // board의 정보를 옮길 HashMap

      int temp = 1;       // HashMap 위치 지정용
      for (int i = 0; i < 3; i++) {       // 3 x 3크기
        for (int j = 0; j < 3; j++) {
          temp++;
          if (board[i].charAt(j) == 'O') {
            o++;
            map.put(temp, 'O');
          } else if (board[i].charAt(j) == 'X') {
            x++;
            map.put(temp, 'X');
          }
        }
      }
      if (o < x) return 0;   // 'X'가 'O'보다 더 많이 공격할 수 없음

      // 공격 횟수 3회 미만
      if (x < 3) {
        if (o == x) return 1;           // 'O'의 공격 횟수와 'X'의 공격 횟수가 같으면 가능
        if (o == (x + 1)) return 1;     // 'O'의 공격 횟수가 'X'의 공격 횟수보다 1회 더 많으면 가능
        else return 0;                  // 이 외의 상황들은 불가능
      }

      int Owin = 0;   // 'O'의 틱택토 횟수
      int Xwin = 0;   // 'X'의 틱택토 횟수

      // 공격 횟수 3회 이상(틱택토 발생 가능)
      temp = 0;
      // 가로 틱택토 확인
      for (int i = 0; i < 3; i++) {
        temp = 1 + (i * 3);
        if (map.get(temp) == map.get(temp + 1) && map.get(i) == map.get(temp + 2)) {
          if (o == x) return 0;       // 틱택토 만들었는데 O의 등장 횟수와 X의 등장 횟수가 동일하게 나올 수 없음
          if (map.get(temp) == 'X' && o > x) return 0;     // X가 이겼는데 O가 공격할 수 없음
          return 1;
        }
      }

      // 세로 틱택토 확인
      for (int i = 1; i <= 3; i++) {
        if (map.get(i) == map.get(i + 3) && map.get(i) == map.get(i + 6)) {
          if (o == x) return 0;       // 틱택토 만들었는데 O의 등장 횟수와 X의 등장 횟수가 동일하게 나올 수 없음
          if (map.get(i) == 'X' && o > x) return 0;       // X가 이겼는데 O가 공격할 수 없음
          return 1;
        }
      }

      // 대각선 틱택토 확인
      if (map.get(5) == map.get(1) && map.get(5) == map.get(9)) {
        return 1;
      }
      if (map.get(5) == map.get(3) && map.get(5) == map.get(7)) {
        return 1;
      }

      return 0;
    }
  }
}
