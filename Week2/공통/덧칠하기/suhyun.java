package Week2.공통.덧칠하기;

public class suhyun {
    public int solution(int n, int m, int[] section) {
        int answer = 0, end_painted = 0;
        for(int i=0; i<section.length; i++){
            if (end_painted < section[i]){
                end_painted = section[i] + m - 1;
                answer += 1;
            }
        }
        return answer;
    }
}
