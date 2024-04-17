package Week4.공통.테이블_해시함수;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

//https://itpro.tistory.com/136
public class suhyun {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;

        Arrays.sort(data, new Comparator<int[]>(){
            public int compare(int[] o1, int[] o2){
                if(o1[col-1] == o2[col-1]){
                    return o2[0] - o1[0];
                }
                return o1[col-1] - o2[col-1];
            }
        });

        List<Integer> a = new ArrayList<>();

        for(int i=row_begin-1; i<=row_end-1; i++){
            int sum = 0;
            for(int j=0; j<data[0].length; j++){
                sum += data[i][j] % (i+1);
            }
            a.add(sum);
        }

        for(int i=0; i<a.size(); i++){
            answer = answer ^ a.get(i);
        }

        return answer;
    }
}
