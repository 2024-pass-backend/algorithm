package Week6.개인.LFU캐시;

import java.util.*;

//#LFU는 페이지 교체 알고리즘 중 하나로, 참조횟수가 가장 적은 페이지를 내쫓는 방식의 알고리즘이다.
public class suhyun {
    static class Cache{
        int key, value;

        public Cache(int key, int value){
            this.key = key;
            this.value = value;
        }

        public int getkey(){
            return key;
        }

        public int getValue(){
            return value;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null || getClass() != obj.getClass())
                return false;
            Cache cache = (Cache) obj;
            return key == cache.key;
        }

        @Override
        public int hashCode() {
            return Objects.hash(key);
        }

        public String toString(){
            return "{ " + key + ", " + value + "}";
        }
    }
    public static List<Integer> implementLFU(int cacheSize, List<String> queries){
        List<Integer> answer = new ArrayList<Integer>();
        //[key, value] -> value는 키에 해당하는 실제 value
        List<Cache> cache = new ArrayList<>();
        //[key, value] -> value는 키에 해당하는 사용빈도를 저장한다.
        Map<Integer, Integer> frequency = new HashMap<>();

        for(int i=0; i<queries.size(); i++){
            String[] st = queries.get(i).split(" ");
            if(st[0].equals("PUT")){
                if(cache.size() < cacheSize) {
                    cache.add(new Cache(Integer.parseInt(st[1]), Integer.parseInt(st[2])));
                    frequency.put(Integer.parseInt(st[1]), frequency.getOrDefault(Integer.parseInt(st[1]), 0) + 1);
                } else {
                    //사용빈도가 가장 적은 것을 찾기 위해 순회한다.
                    //사용빈도가 동일하다면, 가장 최근에 사용되지 않은 키가 제거된다.
                    int[] q = {100001};
                    int[] k = {0};
                    System.out.println(frequency);
                    frequency.forEach((key,value) -> {
                       if(value < q[0]){
                           q[0] = value;
                           k[0] = key;
                       }
                    });
                    System.out.println("참조횟수가 가장 적은 키 = " + k[0]);
                    frequency.remove(k[0]);
                    for(int j=0; j<cache.size(); j++){
                        if(cache.get(j).key == k[0]){
                            cache.remove(j);
                        }
                    }
                    cache.add(new Cache(Integer.parseInt(st[1]), Integer.parseInt(st[2])));
                    frequency.put(Integer.parseInt(st[1]), frequency.getOrDefault(Integer.parseInt(st[1]), 0) + 1);
                }
            } else {
                int value = -1;
                for(int j=0; j<cache.size(); j++){
                    if(cache.get(j).key == (Integer.parseInt(st[1]))){
                        frequency.put(frequency.getOrDefault(Integer.parseInt(st[1]), 0), Integer.parseInt(st[1]) + 1);
                        value = cache.get(j).getValue();
                    }
                }
                answer.add(value);
            }
        }
        return answer;
    }

    public static void main(String[] args){
        List<String> queries = new ArrayList<String>();
        queries.add("PUT 1 1");
        queries.add("PUT 2 2");
        queries.add("PUT 1 3");
        queries.add("PUT 3 4");
        queries.add("PUT 5 4");
        queries.add("GET 1");
        queries.add("GET 2");
        System.out.println(implementLFU(4, queries));
    }
}
