package Week2.공통.혼자서_하는_틱택토;
//7:00 ~ 7:15
public class suhyun {

    public boolean won(char[][] boards, char t){
        for(int i=0; i<boards.length; i++){
            if(boards[i][0] == t && boards[i][1] == t && boards[i][2] == t){
                return true;
            }
        }

        for(int i=0; i<boards.length; i++){
            if(boards[0][i] == t && boards[1][i] == t && boards[2][i] == t){
                return true;
            }
        }

        if(boards[0][0] == t && boards[1][1] == t && boards[2][2] == t){
            return true;
        }

        if(boards[0][2] == t && boards[1][1] == t && boards[2][0] == t){
            return true;
        }

        return false;
    }
    public int solution(String[] board) {
        int o_cnt = 0, x_cnt = 0;

        char[][] boards = new char[board.length][board[0].length()];

        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[i].length(); j++){
                boards[i][j] = board[i].charAt(j);
                if(boards[i][j] == 'O'){
                    o_cnt += 1;
                } else if(boards[i][j] == 'X'){
                    x_cnt += 1;
                }
            }
        }

        if (!(o_cnt == x_cnt + 1 || o_cnt == x_cnt)){
            return 0;
        }

        if (won(boards, 'O') && won(boards,'X')){
            return 0;
        }

        if (won(boards, 'O') && (o_cnt != x_cnt + 1)){
            return 0;
        }

        if (won(boards, 'X') && (o_cnt != x_cnt)){
            return 0;
        }

        return 1;
    }
}
