package Week6.개인.n과m2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class suhyun {

    static int n,m;
    static StringTokenizer st;
    static int[] selected;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        selected = new int[m];
        pro(0);
        System.out.println(sb);
    }

    static void pro(int idx){
        if(idx == m){
            for(int i=0; i<selected.length; i++){
                sb.append(selected[i] + " ");
            }
            sb.append('\n');
            return;
        }

        int start;
        if(idx == 0){
            start = 1;
        } else {
            start = selected[idx-1] + 1;
        }
        for(int i=start; i<=n; i++){
            selected[idx] = i;
            pro(idx + 1);
        }
    }
}
