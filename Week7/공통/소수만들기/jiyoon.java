package Week7.공통.소수만들기;

public class jiyoon {
  class Solution {
    public int solution(int[] nums) {
      int answer = 0;

      for (int i = 0; i < nums.length - 2; i++) {
        for (int j = i + 1; j < nums.length - 1; j++) {
          for (int k = j + 1; k < nums.length; k++) {
            int sum = nums[i] + nums[j] + nums[k];
            boolean check = false;

            // 약수 찾기
            for (int a = 2; a <= Math.sqrt(sum); a++) {
              if (sum % a == 0) {     // 약수가 존재하면
                check = true;       // check = true;
                break;              // 순회 종료
              }
            }
            if (!check) answer++;       // check = false라면 약수가 존재하지 않으므로 answer++;
          }
        }
      }
      return answer;
    }
  }
}
