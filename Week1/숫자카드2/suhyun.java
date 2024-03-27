package Week1.숫자카드2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/*
자바, HashMap
put(키, value)
getOrDefault(키, 기본값)
출력시, StringBuilder를 통해 시간단축가능
 */
public class suhyun {

    static int n, m;
    static StringTokenizer st;
    static Map<Integer, Integer> nums = new HashMap<Integer, Integer>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        for(int i=0; i<n; i++){
            int x = Integer.parseInt(st.nextToken());
            nums.put(x, (nums.getOrDefault(x, 0) + 1));
        }
        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<m; i++){
            int x = Integer.parseInt(st.nextToken());
            if (nums.containsKey(x)){
                sb.append(nums.get(x) + " ");
            } else {
                sb.append(0 + " ");
            }
        }
        System.out.println(sb);
    }
}
