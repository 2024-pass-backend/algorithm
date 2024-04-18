package Week4.공통.최소직사각형;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class suhyun {
    public int solution(int[][] sizes) {

        List<Integer> w = new ArrayList<Integer>();
        List<Integer> h = new ArrayList<Integer>();

        for(int i=0; i<sizes.length; i++){
            w.add(Math.max(sizes[i][0], sizes[i][1]));
            h.add(Math.min(sizes[i][0], sizes[i][1]));
        }

        Collections.sort(w);
        Collections.sort(h);

        return w.get(w.size()-1) * h.get(h.size()-1);
    }
}
