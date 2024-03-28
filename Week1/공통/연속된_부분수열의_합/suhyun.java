package Week1.공통.연속된_부분수열의_합;

public class suhyun {
    public int[] solution(int[] sequence, int k) {
        int R = 0, sum = 0, first = 0, second = 0, ans = Integer.MAX_VALUE;

        for(int L=0; L < sequence.length; L++){
            while(sum < k && R < sequence.length){
                sum += sequence[R++];
            }

            if(sum >= k){
                if(sum == k && ans > (R - L)){
                    first = L;
                    second = R - 1;
                }
                sum -= sequence[L];
                ans = Math.min(ans, R - L);
            }
        }

        int[] answer = {first, second};
        return answer;
    }
}
