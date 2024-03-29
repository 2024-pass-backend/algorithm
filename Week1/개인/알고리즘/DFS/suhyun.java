package Week1.개인.알고리즘.DFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class suhyun {

    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void dfs(int x){
        visited[x] = true;
        System.out.print(x + " ");
        for(int i=0; i<graph.get(x).size(); i++){
            int y = graph.get(x).get(i);
            if(!visited[y]){
                dfs(y);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        for(int i=0; i<9; i++){
            graph.add(new ArrayList<Integer>());
        }

        graph.get(1).addAll(Arrays.asList(2,3,8));
        graph.get(2).addAll(Arrays.asList(1,7));
        graph.get(3).addAll(Arrays.asList(1,4,5));
        graph.get(4).addAll(Arrays.asList(3,5));
        graph.get(5).addAll(Arrays.asList(3));
        graph.get(6).addAll(Arrays.asList(7));
        graph.get(7).addAll(Arrays.asList(2,6,8));
        graph.get(8).addAll(Arrays.asList(1,7));
        dfs(1);
    }
}
