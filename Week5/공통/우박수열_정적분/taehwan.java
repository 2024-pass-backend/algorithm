package Week5.공통.우박수열_정적분;
import java.util.*;
public class taehwan {
    public double[] solution(int k, int[][] ranges) {

        double[] answer = new double[ranges.length];

        List<Integer> list = new ArrayList<>();

        while(k > 1){
            list.add(k);

            if(k % 2 == 0){
                k /= 2;
            }else{
                k = k * 3 + 1;
            }
        }

        list.add(k);

        for(int i = 0; i < ranges.length; i++){

            if(ranges[i][0] > ranges[i][1] + list.size() - 1){
                answer[i] = -1;
                continue;
            }else if(ranges[i][0] == ranges[i][1] + list.size() - 1){
                answer[i] = 0;
                continue;
            }

            double dimension = 0;

            for(int j = ranges[i][0]; j < ranges[i][1] + list.size() - 1; j++){
                dimension += (list.get(j) + list.get(j + 1)) / 2.0;
            }

            answer[i] = dimension;
        }

        return answer;
    }
}
