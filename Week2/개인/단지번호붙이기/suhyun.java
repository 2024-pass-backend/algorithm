package Week2.개인.단지번호붙이기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class suhyun {

    static int n, ans = 0;
    static char[][] graph;
    static int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    static List<Integer> houses = new ArrayList<Integer>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new char[n][n];
        for(int i=0; i<n; i++){
            String str = br.readLine();
            for(int j=0; j<n; j++){
                graph[i][j] = str.charAt(j);
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(graph[i][j] == '1'){
                    dfs(i,j);
                    houses.add(ans);
                    ans = 0;
                }
            }
        }
        System.out.println(houses.size());
        Collections.sort(houses);
        for(int i=0; i<houses.size(); i++){
            System.out.println(houses.get(i));
        }
    }

    static int dfs(int x, int y){
        ans += 1;
        graph[x][y] = '0';
        for(int i=0; i<4; i++){
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];
            if(nx < 0 || ny < 0 || nx >= n || ny >= n){
                continue;
            }
            if(graph[nx][ny] == '1'){
                dfs(nx, ny);
            }
        }
        return ans;
    }
}
