package Week12.오픈채팅방;
import java.util.*;

public class jiyoon {
  class Solution {
    public Object[] solution(String[] record) {
      HashMap<String, String> ID = new HashMap<>();       // Key : id, Value : nickname
      for (String s : record) {
        String[] arr = s.split(" ");

        // 첫 단어가 Leave가 아니라면 ID map 저장
        if (!arr[0].equals("Leave")) {
          ID.put(arr[1], arr[2]);
        }
      }

      // 메시지를 저장할 ArrayList 생성
      ArrayList<String> list = new ArrayList<>();
      for (String s : record) {
        String[] arr = s.split(" ");

        // 첫 단어가 Change가 아니라면 list에 추가
        if (arr[0].equals("Enter")) {
          list.add(ID.get(arr[1]) + "님이 들어왔습니다.");
        } else if (arr[0].equals("Leave")) {
          list.add(ID.get(arr[1]) + "님이 나갔습니다.");
        }
      }

      // ArrayList -> Array로 변환
      Object[] answer = list.toArray();
      return answer;
    }
  }
}
