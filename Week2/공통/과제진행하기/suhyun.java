package Week2.공통.과제진행하기;

/*
Arrays.sort(arr, (o1, o2) -> o1[1] - o2[1]);
 */

import java.util.Arrays;

public class suhyun {
    public String[] solution(String[][] plans) {
        String[] answer = {};

        Arrays.sort(plans, (o1, o2) -> o1[1].compareTo(o2[1]));

        return answer;
    }

    public static void main(String[] args){
        String[][] plans = new String[][]{{"science", "14:00", "50"}, {"music", "12:40", "40"}};
        for(int i=0; i<plans.length; i++)
            System.out.print(Arrays.asList(plans[i])+ " ");
    }
}
