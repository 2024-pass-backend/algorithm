package Week1.개인.먹을것인가_먹힐것인가;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class suhyun {

    static int[] arr;
    static int t;
    static int ans = 0;
    static int[] a, b;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for(int i=0; i<t; i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            a = new int[Integer.parseInt(st.nextToken())];
            b = new int[Integer.parseInt(st.nextToken())];
            ans = 0;
            StringTokenizer stA = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<a.length; j++){
                a[j] = Integer.parseInt(stA.nextToken());
            }
            StringTokenizer stB = new StringTokenizer(br.readLine(), " ");
            for(int j=0; j<b.length; j++){
                b[j] = Integer.parseInt(stB.nextToken());
            }
            Arrays.sort(b);
            for(int k=0; k<a.length; k++){
                ans += (binary_search(b, 0, b.length - 1 , a[k]) + 1);
            }
            System.out.println(ans);
        }


    }

    public static int binary_search(int[] b, int L, int R, int x){
        int ans = -1;
        while(L <= R){
            int mid = (L + R) / 2;
            if(b[mid] < x){
                L = mid + 1;
                ans = mid;
            } else {
                R = mid - 1;
            }
        }
        return ans;
    }
}

