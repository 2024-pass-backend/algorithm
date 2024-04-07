package Week2.공통.과제진행하기;

//10:22 ~

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class suhyun1 {

    class Plan implements Comparable<Plan> {
        String name;
        int start, time;

        public Plan(String name, int start, int time) {
            this.name = name;
            this.start = start;
            this.time = time;
        }

        public int compareTo(Plan other) {
            return this.start - other.start;
        }

        public String toString(){
            return "name = " + this.name + ", start = " + this.start + ", time = " + this.time;
        }
    }

    public void init(Plan[] p, String[][] plans, Queue<Plan> q){
        for(int i=0; i<plans.length; i++){
            p[i] = new Plan(plans[i][0], convert(plans[i][1]), Integer.parseInt(plans[i][2]));
        }
        Arrays.sort(p);

        for(int i=0; i<plans.length; i++){
            q.offer(p[i]);
        }
    }

    public int convert(String x){
        String[] xx = x.split(":");
        return Integer.parseInt(xx[0]) * 60 + Integer.parseInt(xx[1]);
    }

    public String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        int idx = 0;
        Plan[] p = new Plan[plans.length];
        Queue<Plan> q = new LinkedList<Plan>();
        init(p, plans, q);
        Stack<Plan> stack = new Stack<>();
        System.out.println(Arrays.toString(p));

        while(!q.isEmpty()){
            Plan current = q.poll();
            int current_time = 0;
            Plan next = null;
            if(!q.isEmpty()){
                next = q.peek();
            }

            if(!q.isEmpty()){
                if(current.start + current.time <= next.start){
                    current_time = current.start + current.time;
                    answer[idx++] = current.name;
                    while(!stack.isEmpty()){
                        Plan remain_job = stack.pop();
                        if(current_time + remain_job.time <= next.start){
                            answer[idx++] = remain_job.name;
                            current_time += remain_job.time;
                        } else {
                            stack.push(new Plan(remain_job.name, remain_job.start, remain_job.time - (next.start - current_time)));
                            break;
                        }
                    }
                } else {
                    stack.push(new Plan(current.name, current.start, current.time - (next.start - current.start)));
                }
            } else {
                answer[idx++] = current.name;
                while(!stack.isEmpty()){
                    Plan remain_job = stack.pop();
                    answer[idx++] = remain_job.name;
                }
            }
        }

        return answer;
    }
}
