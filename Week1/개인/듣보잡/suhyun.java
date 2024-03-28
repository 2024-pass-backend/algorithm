package Week1.개인.듣보잡;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class suhyun {

    static int n,m;
    static List<String> ans;
    static StringTokenizer st;
    static Set<String> a = new HashSet<String>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        for(int i=0; i<n; i++){
            a.add(br.readLine());
        }
        ans = new ArrayList<String>();
        for(int i=0; i<m; i++){
            String x = br.readLine();
            if(a.contains(x)){
                ans.add(x);
            }
        }
        Collections.sort(ans);
        System.out.println(ans.size());
        for(int x = 0; x < ans.size(); x++){
            System.out.println(ans.get(x));
        }
    }
}
