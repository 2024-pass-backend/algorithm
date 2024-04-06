import java.util.*;

class Solution {
  public String[] solution(String[] players, String[] callings) {
    HashMap<String, Integer> rank = new HashMap<>();        // Key : name, Value : rank

    for (int i = 0; i < players.length; i++) rank.put(players[i], i);

    for (int i = 0; i < callings.length; i++) {
      String name = callings[i];          // 추월한 선수
      int nowIndex = rank.get(name);      // 추월한 선수의 현재 등수
      int preIndex = nowIndex - 1;        // 추월당한 선수의 현재 등수

      String preName = players[preIndex]; // 추월당한 선수

      // rank맵 수정
      rank.replace(name, preIndex);
      rank.replace(preName, nowIndex);

      // players배열 수정
      players[preIndex] = name;
      players[nowIndex] = preName;
    }

    return players;
  }
}