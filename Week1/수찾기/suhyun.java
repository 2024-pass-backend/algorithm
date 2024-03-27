package Week1.수찾기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class suhyun {

    static int n, m;
    static int[] a, b;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        n = Integer.parseInt(br.readLine());
        a = new int[n];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<n; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }
        m = Integer.parseInt(br.readLine());
        b = new int[m];
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<m; i++){
            b[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);
        for(int i=0; i<b.length; i++){
            System.out.println(binary_search(0, a.length - 1, b[i]) ? 1 : 0);
        }
    }

    static boolean binary_search(int L, int R, int x){
        while(L <= R){
            int mid = (L + R) / 2;
            if (a[mid] < x){
                L = mid + 1;
            } else if(a[mid] > x){
                R = mid - 1;
            } else{
                return true;
            }
        }
        return false;
    }
}
