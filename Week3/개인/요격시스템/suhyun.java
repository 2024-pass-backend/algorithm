package Week3.개인.요격시스템;

import java.util.Arrays;

//[[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
// [1,4] [3,7] [4,5] [4,8] [5,12] [10,14] [11,13]

// [1,4] [4,5] [3,7] [4,8] [5,12] [10,14] [11,13]
public class suhyun {
    public int solution(int[][] targets) {
        int answer = 0;

        Arrays.sort(targets, (o1, o2) -> {
           return o1[1] - o2[1];
        });

        int before = targets[0][1];
        answer += 1;
        for(int i=1; i<targets.length; i++){
            if(before <= targets[i][0]){
                before = targets[i][1];
                answer += 1;
            }
        }

        return answer;
    }
}
