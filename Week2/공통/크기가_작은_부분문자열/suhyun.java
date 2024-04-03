package Week2.공통.크기가_작은_부분문자열;

public class suhyun {
    public static int solution(String t, String p) {
        int answer = 0;
        for(int i=0; i<t.length() - p.length() + 1; i++){
            String s = "";
            for(int j=i; j<i+p.length(); j++){
                s += String.valueOf(t.charAt(j));
            }
            if(Integer.parseInt(s) <= Integer.parseInt(p)){
                answer += 1;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        String t = "3141592";
        String p = "271";
        System.out.println(solution(t, p));
    }
}
