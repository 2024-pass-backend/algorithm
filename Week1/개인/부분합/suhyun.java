package Week1.개인.부분합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static StringTokenizer st;
    static int n,s;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());
        arr = new int[n];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        pro();
    }

    static void pro(){
        int R = 0, sum = 0, ans = Integer.MAX_VALUE;
        for(int L=0; L < n; L++){
            while(sum < s && R < n){
                sum += arr[R++];
            }

            if(sum >= s){
                ans = Math.min(ans, R - L);
                //System.out.println("L = " + L + ", R = " + R + ", ans = " + ans + ", sum = " + sum);
                sum -= arr[L];
            }
        }

        System.out.println((ans == Integer.MAX_VALUE ? 0 : ans));
    }
}
