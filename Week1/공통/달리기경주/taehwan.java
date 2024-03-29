package Week1.공통.달리기경주;
import java.util.*;
public class taehwan {
    class Solution {
        public String[] solution(String[] players, String[] callings) {
            String[] answer = new String[players.length];
            HashMap<String, Integer> playerList = new HashMap<>();
            for(int i = 0; i < players.length; i++){
                playerList.put(players[i],i);
            }

            for(int i = 0; i < callings.length; i++){
                int index = playerList.get(callings[i]);

                if(index > 0){
                    String temp = players[index - 1];
                    players[index - 1] = players[index];
                    players[index] = temp;
                }
                playerList.put(players[index],index);
                playerList.put(players[index-1],index-1);
            }
            return players;
        }
    }
}
