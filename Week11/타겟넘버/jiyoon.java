package Week11.타겟넘버;

public class jiyoon {
  class Solution {
    int answer = 0;

    public int solution(int[] numbers, int target) {
      dfs(numbers, 0, target, 0);

      return answer;
    }

    public void dfs(int[] numbers, int depth, int target, int sum) {
      if (depth == numbers.length) {
        if (target == sum) answer++;
      } else {
        dfs(numbers, depth + 1, target, sum + numbers[depth]);  // 해당 노드의 값을 더하고 다음 깊이 탐색
        dfs(numbers, depth + 1, target, sum - numbers[depth]);  // 해당 노드의 값을 배고 다음 깊이 탐색
      }
    }
  }
}
