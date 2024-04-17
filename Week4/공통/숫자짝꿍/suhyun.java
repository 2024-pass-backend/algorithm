package Week4.공통.숫자짝꿍;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

//자바에서 숫자 3을 char형의 '3'으로 변환하려면,
//int a = 3;
//char b = (char)(a + '0')
//b -> '3'이 대입된다.

//자바에서 제네릭타입의 내림차순 정렬은 다음과 같다.
//Collections.sort(배열, Collections.reverseOrder());

//시간초과코드
public class suhyun {
    public String solution(String X, String Y) {
        String answer = "";
        List<Integer> a = new ArrayList<>();
        boolean z = false;
        for(int i=0; i<10; i++){
            int cntX = 0, cntY = 0;
            if(X.contains(String.valueOf(i)) && Y.contains(String.valueOf(i))) {
                for(int j=0; j<X.length(); j++){
                    if(X.charAt(j) == (char)(i + '0')){
                        cntX += 1;
                    }
                }
                for(int j=0; j<Y.length(); j++){
                    if(Y.charAt(j) == (char)(i + '0')){
                        cntY += 1;
                    }
                }
                if(cntX >= 1 && cntY >= 1){
                    z = true;
                    for(int l=0; l<Math.min(cntX, cntY); l++){
                        a.add(i);
                    }
                }
            }

        }

        Collections.sort(a, Collections.reverseOrder());

        for(int i=0; i<a.size(); i++){
            answer += a.get(i);
        }

        if(!z){
            answer += "-1";
        }

        if(answer.length() > 1 && answer.charAt(0) == '0'){
            answer = "0";
        }

        return answer;
    }
}
