package Week4.공통.디펜스게임;

import java.util.PriorityQueue;

public class suhyun1 {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int i=0; i<enemy.length; i++){
            if(k > 0){
                pq.offer(enemy[i]);
                k--;
            } else {
                //현재 적
                int num = enemy[i];

                //무적권을 사용했다고 가정한 병사의 수와 비교했을떄,
                //현재 적이 더 많다면,
                //현재 적에게 무적권을 사용하도록 수정
                if(num > pq.peek()){
                    num = pq.poll();
                    pq.offer(enemy[i]);
                }

                //이때의 num은
                //현재 적이거나
                //무적권을 사용했다고 가정한 수 중 가장 작은 원소
                //둘중 하나일 수 있다.
                if(n >= num){
                    n -= num;
                } else break;
            }
            answer++;
        }

        return answer;
    }
}
