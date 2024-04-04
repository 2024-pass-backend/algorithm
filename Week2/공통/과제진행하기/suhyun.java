package Week2.공통.과제진행하기;
import java.util.*;
//Comparable - compareTo
public class suhyun {
    static class Plan implements Comparable<Plan>{
        String name;
        int start, time;
        public Plan(String name, int start, int time){
            this.name = name;
            this.start = start;
            this.time = time;
        }
        public int compareTo(Plan other){
            return this.start - other.start;
        }
        public String toString(){
            return "name = " + this.name;
        }
    }
    public static int change(String x){
        String[] a = x.split(":");
        return Integer.parseInt(a[0]) * 60 + Integer.parseInt(a[1]);
    }
    public static void init(Plan[] p, String[][] plans, Queue<Plan> homework){
        for(int i=0; i<plans.length; i++){
            p[i] = new Plan(plans[i][0], change(plans[i][1]), Integer.parseInt(plans[i][2]));
        }
        Arrays.sort(p);
        for(int i=0; i<p.length; i++){
            homework.offer(p[i]);
        }
    }
    public static String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        Plan[] p = new Plan[plans.length];
        Queue<Plan> homework = new LinkedList<Plan>();
        init(p, plans, homework);
        Stack<Plan> s = new Stack<Plan>();
        int idx = 0;
        while(!homework.isEmpty() || !s.isEmpty()){
            Plan current = homework.poll(); //1번 00시 10분 소요 //2번 00시 10분 10분 소요 // 3번 00시 30분 10분 소요
            int current_time = current.start;
            Plan next = null;
            if(!homework.isEmpty()){
                next = homework.peek(); //2번 ) 3번 ) 4번
            } else {
                current_time = current.start + current.time;
                answer[idx++] = current.name;
            }
            // 현재 진행중인 과제를 제 시간안에 끝내는 경우
            if(!homework.isEmpty()){
                // 00:20, 00:30
                // 00:40, 00:50
                if(current_time + current.time <= next.start){
                    answer[idx++] = current.name;
                    // 진행중이던 과제를 끝낸 경우, 멈춘 과제가 있다면, 멈춰둔 과제를 시작한다.
                    current_time += current.time; //2번을 끝낸 시각 (00:20), 3번을 끝낸 시각(00:40)
                    // 진행중이던 과제를 끝냈는데도 불구하고 아직 다음 과제까지 시간이 남은경우
                    while(!s.isEmpty()){
                        Plan h = s.pop(); //1번
                        //computer와 homework를 비교해서 computer가 제시간안에 끝낼 수 있는 경우
                        if (current_time + h.time <= next.start){
                            answer[idx++] = h.name;
                            current_time += h.time;
                        } else {
                            //00:30
                            //1번 12시 시작, 10분 소요
                            s.push(new Plan(h.name, h.start, h.time - (next.start - current_time)));
                            current_time = next.start;
                            break;
                        }
                    }
                } else {
                    // 1번 12시 시작, 20분 소요
                    s.push(new Plan(current.name, current.start, current.time - (next.start - current_time)));
                }
            } else {
                while(!s.isEmpty()){
                    Plan h = s.pop();
                    answer[idx++] = h.name;
                }
            }
        }
        return answer;
    }
    public static void main(String[] args){
        //String[][] plans = new String[][]{{"science", "12:40", "50"}, {"music", "12:20", "40"}, {"history", "14:00", "30"}, {"computer", "12:30", "100"}};
        //String[][] plans = new String[][]{{"aaa", "12:00", "20"}, {"bbb", "12:10", "30"}, {"ccc", "12:40", "10"}};
        String[][] plans = new String[][]{{"1", "00:00", "30"}, {"2", "00:10", "10"}, {"3", "00:30", "10"}, {"4", "00:50", "10"}};
        String[] ans = solution(plans);
        System.out.println(Arrays.toString(ans));
    }
}