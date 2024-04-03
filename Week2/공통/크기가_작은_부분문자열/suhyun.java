package Week2.공통.크기가_작은_부분문자열;

public class suhyun {
    public static int solution(String t, String p) {
        int answer = 0;
        for(int i=0; i<t.length() - p.length() + 1; i++){
            String s = "";
            s = t.substring(i, i+p.length());
            if(Long.parseLong(s) <= Long.parseLong(p)){
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
