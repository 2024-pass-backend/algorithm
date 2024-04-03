package Week2.공통.카드뭉치;

import java.util.LinkedList;
import java.util.Queue;

public class suhyun {

    Queue<String> c1 = new LinkedList<String>();
    Queue<String> c2 = new LinkedList<String>();
    public String solution(String[] cards1, String[] cards2, String[] goal) {

        for(int i=0; i<cards1.length; i++){
            c1.add(cards1[i]);
        }

        for(int i=0; i<cards2.length; i++){
            c2.add(cards2[i]);
        }

        for(int i=0; i<goal.length; i++){
            if (!c1.isEmpty() && c1.peek().equals(goal[i])){
                c1.remove();
            } else if(!c2.isEmpty() && c2.peek().equals(goal[i])){
                c2.remove();
            } else{
                return "No";
            }
        }
        return "Yes";
    }
}
