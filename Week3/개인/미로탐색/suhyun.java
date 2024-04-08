package Week3.개인.미로탐색;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

//11:29 ~
public class suhyun {

    static int n,m;
    static StringTokenizer st;
    static int[][] map;
    static boolean[][] visited;
    static int[][] dir = {{0,1}, {1,0}, {0,-1},{-1,0}};

    static class Node{
        int x, y;
        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        for(int i=0; i<n; i++){
            String s = br.readLine();
            for(int j=0; j<m; j++){
                map[i][j] = Integer.parseInt(s.charAt(j) + "");
            }
        }
        visited = new boolean[n][m];
        bfs(0, 0);
//        for(int i=0; i<n; i++){
//            for(int j=0; j<m; j++){
//                System.out.print(map[i][j] + " ");
//            }
//            System.out.println();
//        }
        System.out.println(map[n-1][m-1]);
    }

    static void bfs(int x, int y){
        Queue<Node> q = new LinkedList<Node>();
        q.offer(new Node(x, y));
        visited[x][y] = true;
        while(!q.isEmpty()){
            Node node = q.poll();
            for(int i=0; i<4; i++){
                int nx = node.x + dir[i][0];
                int ny = node.y + dir[i][1];
                if(nx < 0 || ny < 0 || nx >= n || ny >= m){
                    continue;
                }
                if(map[nx][ny] == 0){
                    continue;
                }

                if(!visited[nx][ny]){
                    q.offer(new Node(nx, ny));
                    visited[nx][ny] = true;
                    map[nx][ny] = map[node.x][node.y] + 1;
                }
            }
        }
    }
}
