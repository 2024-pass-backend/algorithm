package Week2.공통.혼자서_하는_틱택토;

import java.util.*;

public class jiyoon {
  public int solution(String[] board) {

    int o = 0;      // "O"의 등장 횟수
    int x = 0;      // "X"의 등장 횟수

    // board의 정보를 옮길 HashMap(Key : 위치, Value : board 정보)
    HashMap<Integer, Character> map = new HashMap<>();

    int temp = 0;       // HashMap 위치 지정용
    for (int i = 0; i < 3; i++) {       // 3 x 3크기
      for (int j = 0; j < 3; j++) {
        temp++;
        if (board[i].charAt(j) == 'O') {
          o++;
          map.put(temp, 'O');
        } else if (board[i].charAt(j) == 'X') {
          x++;
          map.put(temp, 'X');
        } else map.put(temp, '.');
      }
    }
    if (o < x) return 0;        // 'X'가 'O'보다 더 많이 공격할 수 없음
    if (o > x + 1) return 0;    // 'O'가 연속으로 공격할 수 없음

    int oWin = 0;   // 'O'의 틱택토 횟수
    int xWin = 0;   // 'X'의 틱택토 횟수

    // 가로 틱택토 확인
    for (int i = 0; i < 3; i++) {
      if (board[i].equals("OOO")) oWin++;         // 'O'의 틱택토 횟수 증가
      else if (board[i].equals("XXX")) xWin++;    // 'X'의 틱택토 횟수 증가
    }

    // 세로 틱택토 확인
    for (int i = 1; i <= 3; i++) {
      if (map.get(i) == map.get(i + 3) && map.get(i) == map.get(i + 6)) {
        if (map.get(i) == 'O') oWin++;          // 'O'의 틱택토 횟수 증가
        if (map.get(i) == 'X') xWin++;          // 'X'의 틱택토 횟수 증가
      }
    }

    // 대각선 틱택토 확인
    if (map.get(5) == map.get(1) && map.get(5) == map.get(9)) {
      if (map.get(5) == 'O') oWin++;
      else if (map.get(5) == 'X') xWin++;
    }

    if (map.get(5) == map.get(3) && map.get(5) == map.get(7)) {
      if (map.get(5) == 'O') oWin++;
      else if (map.get(5) == 'X') xWin++;
    }

    // 둘 다 틱택토가 있는 경우
    if (oWin > 0 && xWin > 0) return 0;

    // O가 이겼는데 게임이 진행된 경우
    if (oWin > 0 && o == x) return 0;

    // X가 이겼는데 게임이 진행된 경우
    if (xWin > 0 && o > x) return 0;

    return 1;
  }
}