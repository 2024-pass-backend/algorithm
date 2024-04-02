package Week2.공통.과제진행하기;

import java.util.*;

class jiyoon {
  public String[] solution(String[][] plans) {
    Task[] arr = new Task[plans.length];

    for (int i = 0; i < plans.length; i++) {
      Task t = new Task(plans[i][0], plans[i][1], plans[i][2]);
      arr[i] = t;
    }


    Arrays.sort(arr, (o1, o2) -> {
      return o1.start - o2.start;
    });

    Stack<Task> stack = new Stack<>();      // 진행 중인 과제
    List<String> answer = new ArrayList<>();

    int curTime = -1;       // 현재 시간 초기화

    for (int i = 0; i < arr.length; i++) {

      // 진행 중인 과제가 없는 경우
      if (stack.isEmpty()) {
        stack.push(arr[i]);
        continue;
      }


      // 진행 중인 과제와 새로운 과제가 있는 경우
      Task curTask = stack.peek();      // 진행 중인 과제
      Task newTask = arr[i];            // 새로운 과제

      // 새로운 과제의 시작 시간과 진행 중 과제의 종료 시간 비교
      curTime = curTask.start;

      // 현재 과제 시작 시간 + 작업 시간이 새로운 과제 시작 시간보다 같거나 작은 경우
      if (curTime + curTask.time <= newTask.start) {
        recursivePop(stack, newTask, curTime, answer);

      } else {

        // 현재 작업 중단하고 작업한 시간 갱신 및 새 작업 시작
        curTask.time -= newTask.start - curTime;
      }

      stack.push(newTask);
    }

    // 새로운 과제가 없는 경우
    while (!stack.isEmpty()) {
      answer.add(stack.pop().name);
    }


    return answer.toArray(new String[0]);
  }

  public void recursivePop(Stack<Task> stack, Task newTask, int curTime, List<String> answer) {
    if (stack.isEmpty()) {
      return;
    }

    Task curTask = stack.peek();        // 진행 중 과제

    if (curTime + curTask.time <= newTask.start) {
      answer.add(stack.pop().name);
      recursivePop(stack, newTask, curTime + curTask.time, answer);

    } else {
      curTask.time -= newTask.start - curTime;
    }
  }

  static class Task {         // 작업을 나타내는 Task 클래스
    private String name;
    private int start;
    private int time;

    public Task(String name, String start, String time) {       // Task 객체를 초기화하는 생성자
      this.name = name;
      this.start = timeToMinute(start);
      this.time = Integer.parseInt(time);
    }

    public int timeToMinute(String start) {
      String[] arr = start.split(":");
      int hour = Integer.parseInt(arr[0]) * 60;
      int minute = Integer.parseInt(arr[1]);

      return hour + minute;
    }
  }
}