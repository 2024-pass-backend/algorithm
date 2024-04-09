package Week2.공통.가장가까운_같은글자;

class jiyoon {
  public int[] solution(String s) {
    boolean[] alphabet = new boolean[26];       // 첫 등장 확인용
    int[] answer = new int[s.length()];

    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      int n = c - 'a';

      if (!alphabet[n]) {     // 첫 등장 이라면
        answer[i] = -1;
        alphabet[n] = true;
      } else {                // 첫 등장이 아니라면
        for (int j = 0; j < i ; j++) {
          if (c == s.charAt(j)) {
            answer[i] = i - j;
          }

        }
      }

    }
    return answer;
  }
}