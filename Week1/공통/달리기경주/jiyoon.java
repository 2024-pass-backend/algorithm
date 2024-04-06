package Week1.공통.달리기경주;
// 달리기 경주
import java.util.Arrays;
import java.util.HashMap;

class jiyoon {
    public String[] solution(String[] players, String[] callings) {

    HashMap<String, Integer> map = new HashMap<>();     // Key : 선수 이름, Value : 등수

    for (int i = 0; i < players.length; i++) map.put(players[i], i);

    for (String s : callings) {
      int ahead = map.get(s);       // 추월하는 선수
      int behind = map.get(s) - 1;  // 추월당하는 선수

      String outrun = players[ahead];
      String temp = players[behind];

      players[behind] = outrun;
      players[ahead] = temp;

      // 선수들의 등수를 변경
      map.put(outrun, behind);
      map.put(temp, ahead);
    }

    System.out.println(Arrays.toString(players));
  }
}
