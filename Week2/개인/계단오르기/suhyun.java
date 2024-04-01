package Week2.개인.계단오르기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class suhyun {
    static int n;
    static int[] d, stairs;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        d = new int[301];
        stairs = new int[301];
        for(int i=1; i<=n; i++){
            stairs[i] = Integer.parseInt(br.readLine());
        }
        d[1] = stairs[1];
        d[2] = stairs[1] + stairs[2];
        d[3] = Math.max(stairs[2], stairs[1]) + stairs[3];

        for(int i=4; i<=n; i++){
            d[i] = Math.max(d[i-2], stairs[i-1] + d[i - 3]) + stairs[i];
        }

        System.out.println(d[n]);
    }
}
