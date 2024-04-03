package Week2.공통.둘만의암호;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// 자바는 1차원배열에서는 indexOf를 지원하지 않는다.
// indexOf는 ArrayList에서 지원가능하다.
// List<Character> alpha = Arrays.asList(리스트);
public class suhyun {

    static List<Character> alpha = Arrays.asList('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
    public static String solution(String s, String skip, int index) {
        String answer = "";
        for(int i=0; i<s.length(); i++){
            int count = 0;
            int start = alpha.indexOf(s.charAt(i));
            int idx = start;
            boolean cont = false;
            while(count < index){
                idx += 1;
                if(idx > 25){
                    idx %= 26;
                }
                cont = false;
                for(int j=0; j<skip.length(); j++){
                    if(skip.charAt(j) == alpha.get(idx)){
                        cont = true;
                    }
                }
                if (!cont) {
                    count += 1;
                }
//                System.out.print(idx + " ");
            }
//            System.out.println();
            answer += alpha.get(idx);
        }
        return answer;
    }

    public static void main(String[] args){
        String s = "aukks";
        String skip = "wbqd";
        int index = 5;
        System.out.println(solution(s, skip, index));
    }
}
