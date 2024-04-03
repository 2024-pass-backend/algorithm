package Week2.개인.섬의_개수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static int w, h, ans;
    static StringTokenizer st;
    static int[][] adj;
    static int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}, {-1,-1}, {-1,1},{1,1},{1,-1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            st = new StringTokenizer(br.readLine(), " ");
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());
            if(w == 0 && h == 0){
                break;
            }

            adj = new int[h][w];
            for(int i=0; i<h; i++){
                st = new StringTokenizer(br.readLine(), " ");
                for(int j=0; j<w; j++){
                    adj[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            for(int i=0; i<h; i++){
                for(int j=0; j<w; j++){
                    if(adj[i][j] == 1){
                        dfs(i,j);
                        ans += 1;
                    }
                }
            }
            System.out.println(ans);
            ans = 0;
        }
    }

    static void dfs(int x, int y){
        adj[x][y] = 0;
        for(int i=0; i<dir.length; i++){
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];
            if(nx < 0 || ny < 0 || nx >= h || ny >= w){
                continue;
            }
            if(adj[nx][ny] == 1){
                dfs(nx, ny);
            }
        }
    }
}
