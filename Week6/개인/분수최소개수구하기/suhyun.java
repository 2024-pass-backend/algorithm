package Week6.개인.분수최소개수구하기;

public class suhyun {
    public static int solution(int n, int[] locations){
        int max = 0, min = 100001, count = 0;
        for(int i=0; i<locations.length; i++){
            int a = Math.max(i+1 - locations[i], 1);
            int b = Math.min(i+1 + locations[i], n);
            boolean A = false, B = false;
            if(min > a){
                min = a;
                A = true;
            }
            if(max < b){
                max = b;
                B = true;
            }
            if(A && B){
                count += 1;
            }
        }
        return count;
    }
    public static void main(String[] args){
        System.out.println(solution(3, new int[]{1,2,1}));
    }
}
