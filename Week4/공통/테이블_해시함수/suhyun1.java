package Week4.공통.테이블_해시함수;

import java.util.Arrays;
import java.util.Comparator;

public class suhyun1 {
    public static int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;

        Arrays.sort(data, new Comparator<int[]>(){
           public int compare(int[] o1, int[] o2){
               if(o1[col-1] == o2[col-1]){
                   return o2[0] - o1[0];
               }
               return o1[col-1] - o2[col-1];
           }
        });

        for(int i=row_begin-1; i<row_end; i++){
            int sum = 0;
            for(int j=0; j<data[i].length; j++){
                sum += (data[i][j] % (i+1));
            }
            answer = answer ^ sum;
        }

        return answer;
    }

    public static void main(String[] args){
        int[][] data = {{2,2,6},{1,5,10},{4,2,9},{3,8,3}};
        System.out.println(solution(data, 2, 2, 3));
    }
}
