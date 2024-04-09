package Week3.개인.광물캐기;

import java.util.ArrayList;
import java.util.List;

//https://g4daclom.tistory.com/164 풀이 코드
/*
예제2
picks [0, 1, 1] [dia, iron, stone] -> pickList [0, 1, 2]
["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]

예제1
picks [1, 3, 2] -> pickList [0, 1, 1, 1, 2]
["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

Math.ceil(10.0) -> 10.0
Math.ceil(10.1) -> 11.0
자바 = Math.ceil(소수) => 소수점 뒤에 1이상의 숫자가 있다면 올린다.
 */

public class suhyun1 {

    static int depth;
    static int min = Integer.MAX_VALUE;
    static int calc = 0;
    static boolean[] visit;

    public int solution(int[] picks, String[] minerals) {

        int ea = 0;
        List<Integer> pickList = new ArrayList<>();
        for(int i=0; i<picks.length; i++){
            for(int j=0; j<picks[i]; j++){
                if(picks[i] > 0){
                    pickList.add(i);
                    ea++;
                }
            }
        }

        depth = Math.min((int) Math.ceil((double) minerals.length / 5), ea);
        visit = new boolean[pickList.size()];
        dfs(0, pickList, minerals);

        return min;
    }
    //picks [1, 3, 2] -> [0, 1, 1, 1, 2]
    public static void dfs(int idx, List<Integer> pickList, String[] minerals){

        //계산 도중, min이상이 되면 종료 (즉, 이미 피로도가 예를 들어, 25라고 하자. 그런데 30이 되어버리면. 종료조건이 가능함)
        if(calc >= min){
            return;
        }

        if(idx == depth){
            min = Math.min(min, calc);
            return;
        }

        for(int i=0; i<pickList.size(); i++){
            if(!visit[i]){
                int tmp = fatigue(pickList.get(i), idx, minerals);
                visit[i] = true;
                calc += tmp;
                dfs(idx + 1, pickList, minerals);
                visit[i] = false;
                calc -= tmp;
            }
        }
    }

    public static int fatigue(int num, int st, String[] minerals){
        /*
        st = 시작인덱스
        range = 시작인덱스 + 5 or 광물 마지막 인덱스
         */
        st = st * 5;
        int range = Math.min(st + 5, minerals.length); // 5의 배수로 떨어지지 않는경우를 대비하기 위해 Math.min사용
        int sum = 0;

        for(int i=st; i<range; i++){
            switch (minerals[i]){
                case "diamond":
                    sum += num == 0 ? 1 : num == 1 ? 5 : 25;
                    break;
                case "iron":
                    sum += num == 0 ? 1 : num == 1 ? 1 : 5;
                    break;
                case "stone":
                    sum += 1;
                    break;
            }
        }
        return sum;
    }
}
