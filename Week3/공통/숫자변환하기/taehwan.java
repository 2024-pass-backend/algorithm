package Week3.공통.숫자변환하기;
import java.util.*;
public class taehwan {

    class Solution {

        public int solution(int x, int y, int n) {
            int count = 0;
            Queue<Integer> queue = new LinkedList<>();
            queue.add(x);
            while (!queue.isEmpty()) {
                int size = queue.size();
                for (int i = 0; i < size; i++) {
                    int cur = queue.poll();
                    if (cur == y) {
                        return count;
                    }
                    if (cur + n <= y) {
                        queue.add(cur + n);
                    }
                    if (cur * 2 <= y) {
                        queue.add(cur * 2);
                    }
                    if (cur * 3 <= y) {
                        queue.add(cur * 3);
                    }
                }
                count++;
            }
            return -1;
        }
    }
}
