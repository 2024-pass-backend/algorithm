package Week4.공통.숫자짝꿍;

public class suhyun1 {
    public String solution(String X, String Y) {
        StringBuilder sb = new StringBuilder();
        int[] x = {0,0,0,0,0,0,0,0,0,0};
        int[] y = {0,0,0,0,0,0,0,0,0,0};

        for(int i=0; i<X.length(); i++){
            int z = X.charAt(i) - '0';
            x[z] += 1;
        }

        for(int i=0; i<Y.length(); i++){
            int z = Y.charAt(i) - '0';
            y[z] += 1;
        }

        for(int i=9; i>-1; i--){
            if(x[i] > 0 && y[i] > 0){
                for(int j=0; j<Math.min(x[i], y[i]); j++){
                    sb.append(String.valueOf(i));
                }
            }
        }

        if("".equals(sb.toString())){
            return "-1";
        } else if(sb.length() > 0 && sb.toString().charAt(0) == '0'){
            return "0";
        } else {
            return sb.toString();
        }
    }
}
