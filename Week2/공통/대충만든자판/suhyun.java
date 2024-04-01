package Week2.공통.대충만든자판;

public class suhyun {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        int idx = 0;
        for(int i=0; i<targets.length; i++){
            int sum = 0;
            for(int j=0; j<targets[i].length(); j++){
                int cnt = 101;
                for(int k=0; k<keymap.length; k++){
                    if(keymap[k].indexOf(targets[i].charAt(j)) != -1){
                        cnt = Math.min(cnt, keymap[k].indexOf(targets[i].charAt(j)));
                        // System.out.println(cnt);
                    }
                }
                if(cnt == 101){
                    sum = -1;
                    break;
                } else {
                    sum += (cnt + 1);
                }
            }
            answer[idx++] = sum;
        }
        return answer;
    }
}
