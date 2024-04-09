package Week3.개인.광물캐기;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

//8:00 ~ 8:42 (실패코드)
public class suhyun {

    int ans = Integer.MAX_VALUE;
    int[] selected;
    public int solution(int[] picks, String[] minerals) {
        init(minerals);
        pro(0, picks, minerals);
        return ans;
    }

    public void init(String[] minerals){
        if(minerals.length % 5 == 0){
            selected = new int[minerals.length / 5];
        } else {
            selected = new int[minerals.length / 5 + 1];
        }
        Arrays.fill(selected, -1);
    }
    //[-1][-1][-1]
    //[-1][1][2]
    public void print(){
        System.out.println(Arrays.toString(selected));
    }

    public void pro(int selected_idx, int[] picks, String[] minerals){
        if(selected_idx == selected.length){
            print();
            ans = Math.min(ans, calculate(minerals));
            return;
        }

        for(int i=0; i<picks.length; i++){
            // 곡괭이가 있는 경우
            if(picks[i] != 0){
                selected[selected_idx] = i;
                picks[i] -= 1;
                pro(selected_idx + 1, picks, minerals);
                picks[i] += 1;
            }
            // 곡괭이가 없는 경우
            else {
                pro(selected_idx + 1, picks, minerals);
            }
        }
    }

    public int calculate(String[] minerals){
        int answer = 0, idx = 5, start = 0;
        for(int j=0; j<selected.length; j++){
            // 다이아몬드 곡괭이
            if(selected[j] != -1 && j == 0){
                if(idx < minerals.length){
                    for(int i=start; i<idx; i++){
                        if(minerals[i].equals("diamond")){
                            answer += 1;
                        } else if(minerals[i].equals("iron")){
                            answer += 1;
                        } else {
                            answer += 1;
                        }
                    }
                }
            }
            //철 곡괭이
            else if(selected[j] != -1 && j == 1){
                if(idx < minerals.length){
                    for(int i=start; i<idx; i++){
                        if(minerals[i].equals("diamond")){
                            answer += 5;
                        } else if(minerals[i].equals("iron")){
                            answer += 1;
                        } else {
                            answer += 1;
                        }
                    }
                }
            }
            //돌 곡괭이
            else if(selected[j] != -1 && j == 2){
                if(idx < minerals.length){
                    for(int i=start; i<idx; i++){
                        if(minerals[i].equals("diamond")){
                            answer += 25;
                        } else if(minerals[i].equals("iron")){
                            answer += 5;
                        } else {
                            answer += 1;
                        }
                    }
                }
            }
            idx += 5;
        }
        return answer;
    }
}
