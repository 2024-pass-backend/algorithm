package Week7.공통.다른비트_2개이하로;

import java.util.*;
public class suhyun {
    public static long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        for(int i=0; i<numbers.length; i++){
            if(numbers[i] % 2 == 0){
                answer[i] = numbers[i] + 1;
            } else{
                String temp = "0" + Long.toBinaryString(numbers[i]);
                int rightIdx = temp.lastIndexOf('0');
                char[] tempArray = temp.toCharArray();

                tempArray[rightIdx] = '1';
                tempArray[rightIdx + 1] = '0';

                String tempStr = new String(tempArray);

                answer[i] = (Long.parseLong(tempStr, 2));
            }
        }
        return answer;
    }

     public static void main(String[] args){
         long[] ans = {(long)7};
         System.out.println(solution(ans));
     }
}

