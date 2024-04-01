package Week1.개인.더하기123;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class suhyun {

    static int t, n;
    static int[] d = new int[12];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());

        d[1] = 1;
        d[2] = 2;
        d[3] = 4;

        for(int i=4; i<d.length; i++){
            d[i] = d[i-1] + d[i-2] + d[i-3];
        }

        for(int i=0; i<t; i++){
            n = Integer.parseInt(br.readLine());
            System.out.println(d[n]);
        }
    }
}
