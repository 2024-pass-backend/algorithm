package Week4.개인.광물캐기;

//picks = [5, 3, 2] > [dia, iron, stone]
//minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

//picks = [2, 1, 0]
//minerals = [다이아, 다이아, 다이아, 다이아, 다이아 //
//             철, 철, 철, 철, 철 //
//            다이아, 다이아, 다이아, 다이아, 다이아
//           ]
public class suhyun {

    int[] visited;
    int total = 0; //가지고 있는 곡괭이의 총갯수 > 총 3개
    int answer = Integer.MAX_VALUE;
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        visited = new int[picks.length];

        for(int pick:picks){
            total += pick;
        }

        for(int i=0; i<picks.length; i++){
            if(picks[i] == visited[i]){
                continue;
            }
            visited[i]++; // [1, 0, 0]
            dfs(1, 0, i, 0, picks, minerals);
            visited[i]--;
        }

        return answer;
    }
    //pickIdx > 내가 쥔 곡괭이
    //count > ?
    private void dfs(int count, int startMinderalsIdx, int pickIdx, int sum, int[] picks, String[] minerals){

        int add = 0;
        if(answer <= sum || startMinderalsIdx >= minerals.length){
            return;
        }

        for(int i=startMinderalsIdx; i<startMinderalsIdx+5; i++){
            // 더 이상 캘 광물이 없다면
            if(i >= minerals.length){
                break;
            }

            String mineral = minerals[i];
            if(pickIdx == 0){
                add += 1;
            } else if(pickIdx == 1){
                add += mineral.equals("diamond") ? 5 : 1;
            } else {
                if(mineral.equals("diamond")){
                    add += 25;
                } else if(mineral.equals("iron")){
                    add += 5;
                } else {
                    add += 1;
                }
            }
        }

        if(count >= total || startMinderalsIdx + 5 >= minerals.length){
            answer = Math.min(answer, sum + add);
            return;
        }

        //이건 왜 하는 걸까?
        for(int i=0; i<picks.length; i++){
            if(picks[i] == 0 || picks[i] == visited[i]){
                continue;
            }
            visited[i]++; // [2, 0, 0]
            dfs(count + 1, startMinderalsIdx + 5, i, sum + add, picks, minerals);
            visited[i]--;
        }
    }
}
