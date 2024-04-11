package Week3.공통.시소짝꿍;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

//최종 물어보는 것은 몸무게 목록이 몇쌍이루어져있는지인데
//왜 answer가 long으로 선언되어있는거지?
//완탐으로 하면 시간복잡도가 100,000 * 100,000로 시간초과 될것같은데?
//[100,180,360,100,270]

/*
{100, 100} 은 서로 같은 거리에 마주보고 앉으면 균형을 이룹니다.
{180, 360} 은 각각 4(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
{180, 270} 은 각각 3(m), 2(m) 거리에 마주보고 앉으면 균형을 이룹니다.
{270, 360} 은 각각 4(m), 3(m) 거리에 마주보고 앉으면 균형을 이룹니다.

{180, 120} 2, 3
 */
public class suhyun {
    public long solution(int[] weights) {
        long answer = 0;
        Arrays.sort(weights);
        Map<Double, Integer> map = new HashMap<>();

        for(int w : weights){
            double a = w * 1.0;
            double b = (w * 2.0) / 3.0;
            double c = (w * 1.0) / 2.0;
            double d = (w * 3.0) / 4.0;

            if(map.containsKey(a)){
                answer += map.get(a);
            }
            if(map.containsKey(b)){
                answer += map.get(b);
            }
            if(map.containsKey(c)){
                answer += map.get(c);
            }
            if(map.containsKey(d)){
                answer += map.get(d);
            }

            map.put((w * 1.0), map.getOrDefault((w * 1.0), 0) + 1);
        }
        return answer;
    }
}
