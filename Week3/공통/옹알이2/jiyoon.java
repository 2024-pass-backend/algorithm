package Week3.공통.옹알이2;

public class jiyoon {
  class Solution {
    public int solution(String[] babbling) {
      int answer = 0;

      for (int i = 0; i < babbling.length; i++) {
        // 연속해서 옹알이 한다면, 건너뛰기
        if (babbling[i].contains("ayaaya") || babbling[i].contains("yeye") ||
                babbling[i].contains("woowoo") || babbling[i].contains("mama")) continue;

        babbling[i] = babbling[i].replace("aya", " ");   // "aya"발음 제거
        babbling[i] = babbling[i].replace("ye", " ");    // "ye"발음 제거
        babbling[i] = babbling[i].replace("woo", " ");   // "woo"발음 제거
        babbling[i] = babbling[i].replace("ma", " ");    // "ma"발음 제거
        babbling[i] = babbling[i].replace(" ", "");

        if (babbling[i].length() == 0) answer++;        // 옹알이 길이가 0이라면, 발음할 수 있으므로 answer++;
      }

      return answer;
    }
  }
}
