package Week7.개인.qq1;

//문헌의 제목이 아닌 문헌의 번호들을 오름차순으로 쉼표로 구분해서
//나열해야함
import java.io.*;
import java.lang.*;
import java.util.*;


class Main {
    public static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
        String text = scanner.nextLine().trim(); // 수정 전 논문의 내용
        int len = text.length(); // 논문의 글자 수
        StringBuilder sb = new StringBuilder();
        Set<String> ans = new HashSet<>();
        List<String> a = new ArrayList<>();
        Map<String, Integer> aaa = new HashMap<>();
        for(int i=0; i<text.length(); i++){
            String te = "";
            if(text.charAt(i) == '['){
                int idx = i + 1;
                while(true){
                    if(text.charAt(idx) == ']'){
                        break;
                    }
                    te += text.charAt(idx) + "";
                    idx += 1;
                }
                te.trim();
                String[] s = te.split(",");
                for(int j=0; j<s.length; j++){
                    String aa = s[j].trim();
                    ans.add(aa);
                    a.add(aa);
                }
            }
        }

        int i = 1;
        for(int j=0; j<a.size(); j++){
            if(ans.contains(a.get(j))){
                sb.append("[" + i + "]" + " ");
                sb.append(a.get(j) + '\n');
                aaa.put(a.get(j), i);
                ans.remove(a.get(j));
                i += 1;
            }
        }

        StringBuilder sb1 = new StringBuilder();

        Set<String> keySet = aaa.keySet();
        for (String key : keySet) {
            text = text.replace(key, aaa.get(key) + "");
        }
        sb1.append(text + '\n');
        System.out.println(sb1.toString());
        System.out.println(sb.toString());
    }
}
