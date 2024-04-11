package Week3.공통.숫자변환하기;

//8:21 ~ 8:56
//x를 y로 변환하기 위해 필요한 최소연산횟수
//아.. 이건 뭐냐; -> BFS문제라고? (힌트)

import java.util.LinkedList;
import java.util.Queue;

public class suhyun {
    public int solution(int x, int y, int n) {
        int answer = -1;

        if(x != y){
            Queue<Integer> q = new LinkedList<Integer>();
            int[] visited = new int[1000001];
            q.offer(x);
            while(!q.isEmpty()){
                int xx = q.poll();
                if(xx == y){
                    break;
                }
                for(int i=0; i<3; i++){
                    int nx = 0;
                    if(i==0){
                        nx = xx + n;
                    } else if(i==1){
                        nx = xx * 2;
                    } else {
                        nx = xx * 3;
                    }

                    if(nx <= 0 || nx >= 1000001){
                        continue;
                    }

                    if(visited[nx] == 0){
                        q.offer(nx);
                        visited[nx] = visited[xx] + 1;
                    }
                }
            }
            return (visited[y] == 0)? -1 : visited[y];
        } else {
            return 0;
        }
    }
}
