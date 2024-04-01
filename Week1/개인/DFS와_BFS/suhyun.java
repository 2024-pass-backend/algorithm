package Week1.개인.DFS와_BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class suhyun {

    static StringTokenizer st;
    static int n,m,v,a,b;
    static boolean[] visited = new boolean[1001];
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        for(int i=0; i<n+1; i++){
            graph.add(new ArrayList<Integer>());
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine(), " ");
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        for(int i=1; i<=n; i++){
            Collections.sort(graph.get(i));
        }

        dfs(v);
        visited = new boolean[1001];
        System.out.println();
        bfs(v);
    }

    static void dfs(int x){
        visited[x] = true;
        System.out.print(x + " ");
        for(int i=0; i<graph.get(x).size(); i++){
            if(!visited[graph.get(x).get(i)]){
                dfs(graph.get(x).get(i));
            }
        }
    }

    static void bfs(int x){
        Queue<Integer> q = new LinkedList<Integer>();
        q.add(x);
        visited[x] = true;
        while(!q.isEmpty()){
            int y = q.poll();
            System.out.print(y + " ");
            for(int i=0; i<graph.get(y).size(); i++){
                if(!visited[graph.get(y).get(i)]){
                    visited[graph.get(y).get(i)] = true;
                    q.offer(graph.get(y).get(i));
                }
            }
        }
    }
}
