package Week1.개인.감시피하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class suhyun {

    static int n, b;
    static char[][] map;
    static StringTokenizer st;
    static int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0,1}};
    static List<Node> teachers = new ArrayList<Node>();
    static int[][] blank; //장애물이 설치될 위치를 담는 배열
    static class Node{
        int x, y;

        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new char[n][n];
        blank = new int[n*n + 1][2];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<n; j++){
                map[i][j] = st.nextToken().charAt(0);
                if(map[i][j] == 'X'){
                    b++;
                    blank[b][0] = i;
                    blank[b][1] = j;
                } else if(map[i][j] == 'T'){
                    teachers.add(new Node(i,j));
                }
            }
        }

        pro(0, 1);
        System.out.println("NO");
    }

    //장애물이 설치될 수 있는 조합
    static void pro(int cnt, int idx){
        if(cnt == 3){
            if(dfs()){
                System.out.println("YES");
                System.exit(0);
            }
            return;
        }

        if(idx > b){
            return;
        }

        map[blank[idx][0]][blank[idx][1]] = 'O';
        pro(cnt + 1, idx + 1);
        map[blank[idx][0]][blank[idx][1]] = 'X';
        pro(cnt, idx + 1);
    }

    static boolean dfs(){
        for(int i=0; i<teachers.size(); i++){
            int x = teachers.get(i).x;
            int y = teachers.get(i).y;
            for(int k=0; k<4; k++){
                int nx = x + dir[k][0];
                int ny = y + dir[k][1];

                while(isIn(nx, ny)){
                    if(map[nx][ny] == 'S'){
                        return false;
                    }

                    if(map[nx][ny] == 'O'){
                        break;
                    }

                    nx = nx + dir[k][0];
                    ny = ny + dir[k][1];
                }
            }
        }
        return true;
    }

    static boolean isIn(int nx, int ny){
        if(nx < 0 || ny < 0 || nx >= n || ny >= n){
            return false;
        }
        return true;
    }
}
