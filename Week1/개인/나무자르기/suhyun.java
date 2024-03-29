package Week1.개인.나무자르기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static int n, m;
    static int[] arr;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        pro();
    }

    static void pro(){
        int L = 0, R = 1000000000, ans = 0;
        while(L <= R){
            int mid = (L + R) / 2;
            if(determination(mid)){
                L = mid + 1;
                ans = mid;
            } else {
                R = mid - 1;
            }
        }
        System.out.println(ans);
    }

    static boolean determination(int x){
        long sum = 0;
        for(int i=0; i<n; i++){
            if(arr[i] > x){
                sum += (arr[i] - x);
            }
        }
        return (m <= sum) ? true : false;
    }
}
