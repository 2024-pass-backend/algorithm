package Week4.개인.미로탈출;

import java.util.LinkedList;
import java.util.Queue;

// 자바에서 삼항연산자는 if예약어를 사용하지 않는다.
// 조건문 ? 참 : 거짓
// 파이썬은 참 if 조건문 else 거짓
public class suhyun {

    static int sx = 0, sy = 0, lx = 0, ly = 0, ex = 0, ey = 0;

    static class Node{
        int x, y, cnt;

        public Node(int x, int y, int cnt){
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    static int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    public static int bfs(int startX, int startY, int endX, int endY, String[] maps){
        boolean[][] visited = new boolean[maps.length][maps[0].length()];
        Queue<Node> q = new LinkedList<Node>();
        q.offer(new Node(startX, startY, 0));
        visited[startX][startY] = true;
        while(!q.isEmpty()){
            Node n = q.poll();
            int xx = n.x;
            int yy = n.y;
            if(xx == endX && yy == endY){
                return n.cnt;
            }

            for(int i=0; i<dir.length; i++){
                int nx = xx + dir[i][0];
                int ny = yy + dir[i][1];
                if(nx < 0 || ny < 0 || nx >= maps.length || ny >= maps[0].length()){
                    continue;
                }

                if(maps[nx].charAt(ny) == 'X'){
                    continue;
                }

                if(!visited[nx][ny]){
                    q.offer(new Node(nx, ny, n.cnt + 1));
                    visited[nx][ny] = true;
                }
            }
        }
        return 0;
    }
    public static int solution(String[] maps) {
        int answer = 0;

        for(int i=0; i<maps.length; i++){
            for(int j=0; j<maps[i].length(); j++){
                if(maps[i].charAt(j) == 'S'){
                    sx = i;
                    sy = j;
                } else if(maps[i].charAt(j) == 'L'){
                    lx = i;
                    ly = j;
                } else if(maps[i].charAt(j) == 'E'){
                    ex = i;
                    ey = j;
                }
            }
        }

        int a = bfs(sx, sy, lx, ly, maps);
//        System.out.println("a = " + a);

        int b = bfs(lx, ly, ex, ey, maps);
//        System.out.println("b = " + b);

        return (a == 0 || b == 0) ? -1 : a + b;
    }

    public static void main(String[] args){
        String[] maps = {"LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"};
        System.out.println(solution(maps));
    }
}
