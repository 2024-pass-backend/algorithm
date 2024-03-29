package Week1.개인.랜선자르기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static int n, k;
    static int[] arr;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        arr = new int[k];
        for (int i = 0; i < k; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        pro();
    }

    static void pro() {
        long L = 0, R = Integer.MAX_VALUE, ans = 0;
        while (L <= R) {
            long mid = (L + R) / 2;
            if (determination(mid)) {
                L = mid + 1;
                ans = mid;
            } else {
                R = mid - 1;
            }
        }
        System.out.println(ans);
    }

    static boolean determination(long x) {
        long sum = 0;
        for (int i = 0; i < k; i++) {
            if (arr[i] >= x) {
                sum += (arr[i] / x);
            }
        }
        return (sum >= n) ? true : false;
    }
}
