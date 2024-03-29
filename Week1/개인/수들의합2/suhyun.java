package Week1.개인.수들의합2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static int n,m;
    static StringTokenizer st;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine(), " ");
        arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        pro();
    }

    static void pro(){
        int R = 0, sum = 0, ans = Integer.MAX_VALUE, count = 0;
        for(int L = 0; L < n; L++){
            while(sum < m && R < n){
                sum += arr[R++];
            }

            if(sum >= m){
                if(sum == m){
                    count += 1;
                }
                ans = Math.min(ans, R - L);
                sum -= arr[L];
            }
        }
        System.out.println(count);
    }
}
