package Week2.공통.바탕화면정리;

public class suhyun {
    public int[] solution(String[] wallpaper) {
        int startX = wallpaper.length, startY = wallpaper[0].length(), endX = -1, endY = -1;

        for(int i=0; i<wallpaper.length; i++){
            for(int j=0; j<wallpaper[i].length(); j++){
                if(wallpaper[i].charAt(j) == '#'){
                    startX = Math.min(startX, i);
                    startY = Math.min(startY, j);
                    endX = Math.max(endX, i);
                    endY = Math.max(endY, j);
                }
            }
        }
        return new int[]{startX, startY, endX + 1, endY + 1};
    }
}
