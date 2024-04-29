package Week6.공통.모의고사;
import java.util.*;

public class jiyoon {

  public int[] solution(int[] answers) {
    // 수포자들의 문제 찍는 순서
    int[] student1 = {1, 2, 3, 4, 5};
    int[] student2 = {2, 1, 2, 3, 2, 4, 2, 5};
    int[] student3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

    // 각 학생별로 맞춘 문제 수
    int c1 = 0, c2 = 0, c3 = 0;

    for (int i = 0; i < answers.length; i++) {
      if (answers[i] == student1[i % student1.length]) c1++;
      if (answers[i] == student2[i % student2.length]) c2++;
      if (answers[i] == student3[i % student3.length]) c3++;
    }

    // 문제를 가장 많이 맞춘 횟수 구하기
    int max = Math.max(c1, Math.max(c2, c3));

    // 문제를 가장 많이 맞춘 학생을 저장할 ArrayList
    ArrayList<Integer> list = new ArrayList<>();

    // 문제를 가장 많이 맞춘 횟수와 동일한 학생을 list에 추가
    if (c1 == max) list.add(1);
    if (c2 == max) list.add(2);
    if (c3 == max) list.add(3);

    // list를 answer배열로 변환
    int[] answer = new int[list.size()];
    for (int i = 0; i < list.size(); i++) {
      answer[i] = list.get(i);
    }

    return answer;
  }
}
