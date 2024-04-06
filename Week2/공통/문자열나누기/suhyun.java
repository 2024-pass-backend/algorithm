package Week2.공통.문자열나누기;

public class suhyun {
    public int solution(String s) {
        int answer = 0, cnt1 = 0, cnt2 = 0;
        char k = ' ';

        for(int i=0; i<s.length(); i++){
            if(cnt1 == cnt2){
                answer += 1;
                k = s.charAt(i);
            }

            if(k == s.charAt(i)){
                cnt1 += 1;
            } else{
                cnt2 += 1;
            }
        }

        return answer;
    }
}
