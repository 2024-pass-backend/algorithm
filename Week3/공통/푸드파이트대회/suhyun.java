package Week3.공통.푸드파이트대회;

//자바는 String str = "ABCDE";
// StringBuffer sb = new StringBuffer(str);
// String reverse = sb.reverse().toString();
// 위처럼 문자를 뒤집는다.

public class suhyun {
    public String solution(int[] food) {
        String answer = "";
        for(int i=0; i<food.length; i++){
            for(int j=0; j < food[i] / 2; j++){
                answer += String.valueOf(i);
            }
        }
        StringBuffer sb = new StringBuffer(answer);
        String a = sb.reverse().toString();
        answer += "0";
        answer += a;
        return answer;
    }
}
