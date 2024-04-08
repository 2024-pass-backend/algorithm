package Week3.공통.기사단원의_무기;

class Solution {
  public int solution(int number, int limit, int power) {
    int answer = 0;

    for (int i = 1; i <= number; i++) {
      int count = 0;      // 약수의 개수 세기 용도
      for (int j = 1; j * j <= i; j++) {
        if (j * j == i) count++;            // 제곱으로 인해 만들어진 약수라면 +1
        else if (i % j == 0) count += 2;    // 그렇지 않다면, 약수는 쌍을 이루므로 +2
      }

      if (count > limit) {
        answer += power;
      } else {
        answer += count;
      }
    }

    return answer;
  }
}