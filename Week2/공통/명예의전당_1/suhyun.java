package Week2.공통.명예의전당_1;

import java.util.PriorityQueue;

public class suhyun {

    PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];

        for(int i=0; i<score.length; i++){
            if(pq.size() >= k){
                if(score[i] > pq.peek()){
                    pq.poll();
                }
            }

            if(pq.size() < k){
                pq.offer(score[i]);
            }

            answer[i] = pq.peek();
        }

        return answer;
    }
}
