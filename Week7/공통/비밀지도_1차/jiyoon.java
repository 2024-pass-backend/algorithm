package Week7.공통.비밀지도_1차;
import java.util.*;

public class jiyoon {
  class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
      String[] answer = new String[n];

      String[] str1 = new String[n];      // arr1를 지도로 변환한 정보를 저장할 배열
      String[] str2 = new String[n];      // arr2를 지도로 변환한 정보를 저장할 배열

      StringBuilder sb;

      for (int i = 0; i < arr1.length; i++) {
        sb = new StringBuilder();

        // arr1[i]를 이진수 문자열로 변환
        String binaryString = Integer.toString(arr1[i], 2);

        // 5자리로 만들기 위해 앞에 0 채우기
        String formattedBinary = String.format("%" + n + "s", binaryString).replace(' ', '0');

        for (int j = 0; j < n; j++) {
          if (formattedBinary.charAt(j) == '0') sb.append(' ');
          else if (formattedBinary.charAt(j) == '1') sb.append('#');
        }
        str1[i] = sb.toString();
      }

      for (int i = 0; i < arr2.length; i++) {
        sb = new StringBuilder();

        // arr2[i]를 이진수 문자열로 변환
        String binaryString = Integer.toString(arr2[i], 2);

        // 5자리로 만들기 위해 앞에 0 채우기
        String formattedBinary = String.format("%" + n + "s", binaryString).replace(' ', '0');

        for (int j = 0; j < n; j++) {
          if (formattedBinary.charAt(j) == '0') sb.append(' ');
          else if (formattedBinary.charAt(j) == '1') sb.append('#');
        }

        str2[i] = sb.toString();
      }

      for (int i = 0; i < n; i++) {
        sb = new StringBuilder();
        // str1과 str2를 확인하여 answer 지도 완성하기
        for (int j = 0; j < n; j++) {
          if (str1[i].charAt(j) == '#' || str2[i].charAt(j) == '#') sb.append('#');
          else sb.append(' ');
        }

        answer[i] = sb.toString();
      }
      return answer;
    }
  }
}
