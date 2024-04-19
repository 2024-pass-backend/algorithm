package Week4.공통.디펜스게임;

import java.util.PriorityQueue;

/*
[4, 2, 4, 5, 3, 3, 1] n=7
k = 무적권을 사용할 수 있는 횟수 (3)

https://school.programmers.co.kr/questions/60164
 */
public class suhyun {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=0; i<enemy.length; i++){
            //일단 무적권 사용 -> 4 2 4
            if(k > 0){
                pq.offer(enemy[i]);
            }
            //무적권을 다 사용한 경우
            else {
                int num = enemy[i];
                /*
                무적권을 사용하여 처리한 적의 수 중 가장 적은 수와
                현재 만난 적의 수를 비교하여
                현재 적이 더 많다면
                 */
                if(pq.peek() < enemy[i]){
                    //현재 적에게 무적권을 사용하도록 한다.
                    num = pq.poll();
                    pq.offer(enemy[i]);
                }

                //이때 num은 현재 만난 적이거나
                //무적권을 사용하여 처리한 적의 수 중 가장 적은 수
                //둘중에 하나가 될 수 있다.
                if(n >= num){
                   n -= num;
                }
                //병사가 없다면 종료
                else break;
            }
            answer++;
        }
        return answer;
    }
}
