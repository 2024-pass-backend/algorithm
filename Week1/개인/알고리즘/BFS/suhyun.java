package Week1.개인.알고리즘.BFS;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;

public class suhyun {

    static boolean visited[] = new boolean[9];
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    static void bfs(int x){
        Queue<Integer> q = new LinkedList<>();
        q.offer(x);
        visited[x] = true;
        while(!q.isEmpty()){
            int y = q.poll();
            System.out.print(y + " ");
            for(int i=0; i<graph.get(y).size(); i++){
                int z = graph.get(y).get(i);
                if(!visited[z]){
                    q.offer(z);
                    visited[z] = true;
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
