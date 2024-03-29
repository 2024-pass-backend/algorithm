package Week1.공통.공원산책;

public class suhyun {

    static int[][] dir = {{0,1}, {1,0}, {0, -1}, {-1,0}};
    public int[] solution(String[] park, String[] routes) {

        //처음위치 찾기
        int startX = 0, startY = 0;
        for(int i=0; i<park.length; i++){
            for(int j=0; j<park[i].length(); j++){
                if(park[i].charAt(j) == 'S'){
                    startX = i;
                    startY = j;
                }
            }
        }

        for(int i=0; i<routes.length; i++){
            String[] a = routes[i].split(" ");
            int move_cnt = Integer.parseInt(a[1]);
            int currentX = startX, currentY = startY;
            for(int j=0; j<move_cnt; j++){
                int nx = 0, ny = 0;
                if(a[0].equals("E")){
                    System.out.println("dir[0][0]" + dir[0][0]);
                    nx = startX + dir[0][0];
                    ny = startY + dir[0][1];
                } else if(a[0].equals("S")){
                    nx = startX + dir[1][0];
                    ny = startY + dir[1][1];
                } else if(a[0].equals("W")){
                    nx = startX + dir[2][0];
                    ny = startY + dir[2][1];
                } else{
                    nx = startX + dir[3][0];
                    ny = startY + dir[3][1];
                }

                if(nx < 0 || ny < 0 || nx >= park.length || ny >= park[0].length() || park[nx].charAt(ny) == 'X'){
                    startX = currentX;
                    startY = currentY;
                    break;
                } else {
                    startX = nx;
                    startY = ny;
                }
            }
        }

        int[] answer = {startX, startY};
        return answer;
    }
}
