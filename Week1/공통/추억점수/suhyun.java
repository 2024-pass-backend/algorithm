package Week1.공통.추억점수;

import java.util.HashMap;
import java.util.Map;

public class suhyun {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        Map<String, Integer> grade = new HashMap<>();

        for(int i=0; i<name.length; i++){
            grade.put(name[i], yearning[i]);
        }

        for(int i=0; i<photo.length; i++){
            int sum = 0, idx = 0;
            for(int j=0; j<photo[i].length; j++){
                sum += grade.get(photo[i][j]);
            }
            answer[idx++] = sum;
        }

        return answer;
    }
}
