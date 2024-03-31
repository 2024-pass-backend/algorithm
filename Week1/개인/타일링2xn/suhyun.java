package Week1.개인.타일링2xn;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class suhyun {

    static int n;
    static int[] d = new int[1001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        d[1] = 1;
        d[2] = 2;
        d[3] = 3;
        for(int i=4; i<d.length; i++){
            d[i] = d[i - 2] + d[i - 1];
        }
        System.out.println(d[n] % 1007);
    }
}
