package Week2.공통.당구연습;

import java.util.Arrays;

public class suhyun {

    public static int solve(int startX, int startY, int x, int y, int m, int n){
        int[] dist = new int[4];
        int d = Integer.MAX_VALUE;
        //위쪽벽
        //위쪽벽에 맞을때, x가 같으면서 목표의 y가 더 큰경우 공을 먼저 맞게 된다.
        if (!(x == startX && startY < y)){
            d = (startX - x) * (startX - x) + (startY - (n + (n - y))) * (startY - (n + (n - y)));
        }
        dist[0] = d;
        //아래쪽벽
        //아래쪽벽에 맞을때, x가 같으면서 목표의 y가 더 작은 경우 공을 먼저 맞게 된다.
        if(!(x == startX && startY > y)){
            d = (startX - x) * (startX - x) + (startY - (-y)) * (startY - (-y));
        }
        dist[1] = d;
        //오른쪽벽
        //오른쪽벽에 맞을때, y가 같으면서 목표의 x가 더 큰 경우 공을 먼저 맞게 된다.
        if(!(y == startY && startX < x)){
            d = (startX - (m + (m - x))) * (startX - (m + (m - x))) + (startY - y) * (startY - y);
        }
        dist[2] = d;
        //왼쪽벽
        //왼쪽벽에 맞을때, y가 같으면서 목표의 x가 더 작은 경우 공을 먼저 맞게 된다.
        if(!(y == startY && startX > x)){
            d = (startX - (-x)) * (startX - (-x)) + (startY - y) * (startY - y);
        }
        dist[3] = d;
        Arrays.sort(dist);
        System.out.println(Arrays.toString(dist));
        return dist[0];
    }
    public static int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        int[] answer = new int[balls.length];
        for(int i=0; i<answer.length; i++){
            answer[i] = solve(startX, startY, balls[i][0], balls[i][1], m, n);
        }
        return answer;
    }

    public static void main(String[] args){
        int[][] balls = {{1, 2}};
        solution(4, 2, 1, 1, balls);
    }
}
