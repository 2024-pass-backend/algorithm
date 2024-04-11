package Week3.공통.마법의엘리베이터;

public class taehwan {
    public int solution(int storey) {
        int answer = 0;

        while (storey != 0) {
            int one = storey % 10;
            int ten = (storey / 10) % 10;

            if (one > 5) {
                answer += (10 - one);
                storey += 10;
            } else if (one == 5) {
                answer += one;
                storey += (ten < 5 ? 0 : 10);
            } else {
                answer += one;
            }

            storey /= 10;
        }

        return answer;
    }
}
