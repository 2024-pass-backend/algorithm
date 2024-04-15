package Week4.공통.나머지가_1이되는_수찾기;

public class taehwan {
    public int solution(int n) {

        int answer = 0;

        for (int i = 2; i < n; i++) {

            if(n%i == 1) {
                answer = i;
                break;
            }

        }

        return answer;
    }
}
