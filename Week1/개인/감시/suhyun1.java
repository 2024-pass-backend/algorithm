package Week1.개인.감시;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun1 {

    static int n, m, cnt, remain, res = Integer.MAX_VALUE;
    static int[][] map;
    static CCTV[] cctvs;
    static StringTokenizer st;
    static class CCTV{
        int type, x, y;

        CCTV(int type, int x, int y){
            this.type = type;
            this.x = x;
            this.y = y;
        }
    }

    static int[][] dir = {{0,1}, {1,0},{0,-1}, {-1,0}}; // 동, 남, 서, 북

    static int[][][] cctv = {
            {{0}},
            {{0}, {1}, {2}, {3}},
            {{0,2},{1,3}},
            {{0,3},{0,1},{1,2},{2,3}},
            {{0,3,2}, {1,2,3}, {0,1,2},{0,1,3}},
            {{0,1,2,3}}
    };


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        cctvs = new CCTV[8];
        remain = n * m;
        map = new int[n][m];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == 6){
                    remain -= 1;
                } else if(map[i][j] >= 1 && map[i][j] <= 5){
                    cctvs[cnt++] = new CCTV(map[i][j], i, j);
                }
            }
        }
        pro(0, map, remain - cnt);
        System.out.println(res);
    }

    static void pro(int idx, int[][] map, int remain){
        if(idx == cnt){
            res = Math.min(res, remain);
            return;
        }

        int[][] newMap = new int[n][m];
        copy(newMap, map);

        CCTV c = cctvs[idx];
        for(int j=0; j<cctv[c.type].length; j++){
            int count = 0;
            for(int k=0; k<cctv[c.type][j].length; k++){
                int d = cctv[c.type][j][k];
                count += observation(d, newMap, c.x, c.y);
            }
            pro(idx + 1, newMap, remain - count);
            copy(newMap, map);
        }
    }

    static int observation(int d, int[][] map, int cctvX, int cctvY){
        int obser_cnt = 0;
        int x = cctvX, y = cctvY;

        while(true){
            x += dir[d][0];
            y += dir[d][1];

            if((x < 0 || y < 0 || x >= n || y >= m || map[x][y] == 6)){
                break;
            }

            if((map[x][y] >= 1 && map[x][y] <= 5) || (map[x][y] == -1)){
                continue;
            }

            map[x][y] = -1;
            obser_cnt += 1;
        }
        return obser_cnt;
    }

    static void copy(int[][] newMap, int[][] map){
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                newMap[i][j] = map[i][j];
            }
        }
    }
}
