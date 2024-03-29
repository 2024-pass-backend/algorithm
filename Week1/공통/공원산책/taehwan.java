package Week1.공통.공원산책;

public class taehwan {
    class Solution {
        public int[] solution(String[] park, String[] routes) {
            int[] answer = new int[2];
            int robotX = -1;
            int robotY = -1;
            int height = park.length;
            int width = park[0].length();

            for(int i=0;i<park.length;i++){
                if(park[i].indexOf('S') != -1){
                    robotX = park[i].indexOf('S');
                    robotY = i;
                    break;
                }
            }

            for(int i=0;i<routes.length;i++){
                String[] temp = routes[i].split(" ");
                String vector = temp[0];
                int distance =  Integer.parseInt(temp[1]);
                int currX = robotX;
                int currY = robotY;

                if(vector.equals("E")){
                    boolean overRange = true;
                    for(int j=1;j<=distance;j++){
                        currX++;
                        if(currX >= width){
                            overRange = false;
                            break;
                        }
                        else if(park[currY].charAt(currX) =='X'){
                            overRange = false;
                            break;
                        }
                    }
                    if (overRange) {
                        robotX = currX;
                    }
                }
                else if(vector.equals("W")){
                    boolean overRange = true;
                    for(int j=1;j<=distance;j++){
                        currX--;
                        if(currX < 0){
                            overRange = false;
                            break;
                        }
                        else if(park[currY].charAt(currX) =='X'){
                            overRange = false;
                            break;
                        }
                    }
                    if (overRange) {
                        robotX = currX;
                    }
                }
                else if(vector.equals("S")){
                    boolean overRange = true;
                    for(int j=1;j<=distance;j++){
                        currY++;
                        if(currY >= height){
                            overRange = false;
                            break;
                        }
                        else if(park[currY].charAt(currX) =='X'){
                            overRange = false;
                            break;
                        }
                    }
                    if (overRange) {
                        robotY = currY;
                    }
                }
                else if(vector.equals("N")){
                    boolean overRange = true;
                    for(int j=1;j<=distance;j++){
                        currY--;
                        if(currY < 0){
                            overRange = false;
                            break;
                        }
                        else if(park[currY].charAt(currX) =='X'){
                            overRange = false;
                            break;
                        }
                    }
                    if (overRange) {
                        robotY = currY;
                    }
                }
            }

            answer[0] = robotY;
            answer[1] = robotX;

            return answer;
        }
    }

}
