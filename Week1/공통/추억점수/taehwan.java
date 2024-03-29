package Week1.공통.추억점수;
import java.util.*;
public class taehwan {
    class Solution {
        public int[] solution(String[] name, int[] yearning, String[][] photo) {
            int[] answer = new int[photo.length];
            HashMap<String,Integer> map = new HashMap<>();
            for(int i = 0; i < name.length; i++){
                map.put(name[i],yearning[i]);
            }
            for(int i = 0; i < photo.length; i++){
                int point = 0;
                for(int j = 0; j < photo[i].length; j++){
                    if(map.containsKey(photo[i][j])) {
                        point += map.getOrDefault(photo[i][j], 0);
                    }

                }
                answer[i] += point;
            }
            return answer;
        }
    }
}
