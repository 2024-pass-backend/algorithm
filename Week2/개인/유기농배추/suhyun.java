package Week2.개인.유기농배추;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static int t, m, n, k, a, b;
    static StringTokenizer st;
    static int[][] graph;
    static int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for(int i=0; i<t; i++){
            st = new StringTokenizer(br.readLine(), " ");
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            graph = new int[n][m];
            for(int j=0; j<k; j++){
                st = new StringTokenizer(br.readLine(), " ");
                a = Integer.parseInt(st.nextToken());
                b = Integer.parseInt(st.nextToken());
                graph[b][a] = 1;
            }
            int ans = 0;
            for(int x=0; x<graph.length; x++){
                for(int y=0; y<graph[x].length; y++){
                    if(graph[x][y] == 1){
                        dfs(x, y);
                        ans += 1;
                    }
                }
            }
            System.out.println(ans);
        }
    }

    static void dfs(int x, int y){
        graph[x][y] = 0;
        for(int i=0; i<4; i++){
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];
            if(nx < 0 || ny < 0 || nx >= n || ny >= m){
                continue;
            }
            if(graph[nx][ny] == 1){
                dfs(nx, ny);
            }
        }
    }
}
