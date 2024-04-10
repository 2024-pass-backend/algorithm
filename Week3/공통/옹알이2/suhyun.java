package Week3.공통.옹알이2;

public class suhyun {
    public static int solution(String[] babbling) {
        int answer = 0;
        String[] can = {"aya", "ye", "woo", "ma"};

        for(int i=0; i<babbling.length; i++){
            for(int j=0; j<can.length; j++){
                if(!(babbling[i].contains("ayaaya") || babbling[i].contains("yeye") || babbling[i].contains("woowoo") || babbling[i].contains("mama"))){
                    babbling[i] = babbling[i].replace(can[j], " ");
                }
            }
            babbling[i] = babbling[i].replace(" ","");

//            System.out.println("길이 = " + babbling[i].length());

            if(babbling[i].length() == 0){
                answer += 1;
            }
        }

        return answer;
    }

    public static void main(String[] args){
        String[] babbling = {"ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"};
        System.out.println(solution(babbling));
    }
}
