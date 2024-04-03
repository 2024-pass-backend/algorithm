package Week2.개인.양;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static int r,c,v_cnt, o_cnt, v_ans, o_ans;
    static StringTokenizer st;
    static char[][] adj;
    static boolean[][] visited;
    static int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        adj = new char[r][c];
        visited = new boolean[r][c];
        for(int i=0; i<r; i++){
            String x = br.readLine();
            for(int j=0; j<c; j++){
                adj[i][j] = x.charAt(j);
            }
        }
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(adj[i][j] != '#' && !visited[i][j]){
                    dfs(i,j);
//                    System.out.println(i + ", " + j + ", " + v_cnt + ", " + o_cnt);
                    if(v_cnt >= o_cnt){
                        if(v_cnt == 0 && o_cnt == 0){
                            continue;
                        }
                        v_ans += v_cnt;
                    } else {
                        if(v_cnt == 0 && o_cnt == 0){
                            continue;
                        }
                        o_ans += o_cnt;
                    }
                    v_cnt = 0;
                    o_cnt = 0;
                }
            }
        }
        System.out.println(o_ans + " " + v_ans);
    }

    static void dfs(int x, int y){
        visited[x][y] = true;

        if(adj[x][y] == 'v'){
            v_cnt += 1;
        } else if(adj[x][y] == 'o'){
            o_cnt += 1;
        }

        for(int i=0; i<4; i++){
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];
            if(nx < 0 || ny < 0 || nx >= r || ny >= c){
                continue;
            }
            if(!visited[nx][ny] && adj[nx][ny] != '#'){
                dfs(nx, ny);
            }
        }
    }
}
