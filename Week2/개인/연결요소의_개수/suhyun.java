package Week2.개인.연결요소의_개수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class suhyun {

    static int n,m, a, b;
    static StringTokenizer st;
    static ArrayList<Integer>[] adj;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        adj = new ArrayList[n + 1];
        for(int i=1; i<=n; i++){
            adj[i] = new ArrayList<>();
        }
        visited = new boolean[n + 1];
        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine(), " ");
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            adj[a].add(b);
            adj[b].add(a);
        }
        int ans = 0;
        for(int i=1; i<=n; i++){
            if(!visited[i]){
                dfs(i);
                ans += 1;
            }
        }
        System.out.println(ans);
    }

    static void dfs(int x){
        visited[x] = true;
        for(int i=0; i<adj[x].size(); i++){
            if(!visited[adj[x].get(i)]){
                dfs(adj[x].get(i));
            }
        }
    }
}
