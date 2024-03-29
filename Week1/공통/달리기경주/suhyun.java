package Week1.공통.달리기경주;

import java.util.HashMap;
import java.util.Map;

//9:00 ~ 9:18
public class suhyun {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];

        Map<String, Integer> rank = new HashMap<>();
        Map<Integer, String> rank2 = new HashMap<>();

        for(int i=0; i<players.length; i++){
            rank.put(players[i], i);
            rank2.put(i, players[i]);
        }

        for(int i=0; i<callings.length; i++){
            int current_rank = rank.get(callings[i]); // 3
            int update_rank = current_rank - 1;
            String current_player = rank2.get(current_rank);
            String prev_player = rank2.get(update_rank);

            rank.put(current_player, update_rank);
            rank2.put(update_rank, current_player);
            rank.put(prev_player, current_rank);
            rank2.put(current_rank, prev_player);
        }

        for(int i=0; i<players.length; i++){
            answer[i] = rank2.get(i);
        }

        return answer;
    }
}
