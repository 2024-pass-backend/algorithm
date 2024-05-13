package Week7.개인.q1;

import java.util.*;
class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        List<String> st = new ArrayList<String>();
        for(int i=0; i<s.length(); i++){
            st.add(s.charAt(i) + "");
        }

        while(true){
            boolean flag = false;
            for(int i=0; i<st.size()-1; i++){
                if(st.get(i).equals(st.get(i+1))){
                    st.remove(i);
                    st.remove(i);
                    flag = true;
                    break;
                }
            }

            if(!flag){
                break;
            }
        }

        if(st.size() == 0){
            answer = 1;
        } else {
            answer = 0;
        }
        return answer;
    }
}
