package Week1.개인.알고리즘.BFS;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class suhyun1 {

    static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    static boolean visited[] = new boolean[9];

    static void bfs(int start){
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(start);
        visited[start] = true;
        while(!q.isEmpty()){
            int x = q.poll();
            System.out.print(x + " ");
            for(int i=0; i<graph.get(x).size(); i++){
                int y = graph.get(x).get(i);
                if(!visited[y]){
                    q.offer(y);
                    visited[y] = true;
                }
            }
        }
    }

    public static void main(String[] args){
        for(int i=0; i<9; i++){
            graph.add(new ArrayList<Integer>());
        }

        graph.get(1).addAll(Arrays.asList(1,3,8));
        graph.get(2).addAll(Arrays.asList(1,7));
        graph.get(3).addAll(Arrays.asList(1,4,5));
        graph.get(4).addAll(Arrays.asList(3,5));
        graph.get(5).addAll(Arrays.asList(3,4));
        graph.get(6).addAll(Arrays.asList(7));
        graph.get(7).addAll(Arrays.asList(2,6,8));
        graph.get(8).addAll(Arrays.asList(1,7));

        bfs(1);
    }
}
