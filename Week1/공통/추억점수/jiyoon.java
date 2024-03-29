package Week1.공통.추억점수;
// 추억 점수

public class jiyoon {
  public int[] solution(String[] park, String[] routes) {
    int[] answer = new int[photo.length];

    HashMap<String, Integer> map = new HashMap<>();

    for (int i = 0; i < name.length; i++) {
      map.put(name[i], yearning[i]);
    }

    for (int i = 0; i < photo.length; i++) {
      int score = 0;
      for (int j = 0; j < photo[i].length; j++) {
        if (map.get(photo[i][j]) == null) continue;

        score += map.get(photo[i][j]);
      }
      answer[i] = score;
    }

    return answer;
  }
}
