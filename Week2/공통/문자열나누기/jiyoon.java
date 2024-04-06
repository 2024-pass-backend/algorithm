class Solution {
  public int solution(String s) {
    int answer = 0;
    char x = '0';
    int countX = 0;     // x 등장 수
    int countO = 0;     // x와 다른 문자 등장 수

    for (int i = 0; i < s.length(); i++) {
      if (x == '0') x = s.charAt(i);

      if (s.charAt(i) == x) {             // x와 동일한 문자가 나왔다면,
        countX++;
      } else if (s.charAt(i) != x) {      // x와 다른 문자가 나왔다면,
        countO++;
      }

      if (countX == countO) {
        answer++;       // 문자열 분할 개수 추가
        x = '0';        // 문자열 초기화
      }
    }

    if ((countX - countO) != 0) answer++;   // 더 이상 읽을 문자열이 없다면 문자열 분할 개수 추가
    return answer;
  }
}