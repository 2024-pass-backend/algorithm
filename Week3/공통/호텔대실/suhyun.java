package Week3.공통.호텔대실;

//배열 자체는 시작시간을 기준으로 정렬하되, 진행중인 것은 큐에 담아서 끝나는 시간을 기준으로 정렬해야하나?
//정렬전 : [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
//정렬후 : ["14:20", "15:20"], ["15:00", "17:00"], ["16:40", "18:20"], ["14:10", "19:20"], ["18:20", "21:20"] --> X

// 정렬후 : ["14:10", "19:20"], ["14:20", "15:20"], ["15:00", "17:00"], ["16:40", "18:20"], ["18:20", "21:20"]


// 객실2 ["16:40", "18:20"],
// 객실3 ["18:20", "21:20"]
// 객실1 ["14:10", "19:20"]

// 파이썬 같은 경우는 우선순위큐를 어떻게 이용해야할지 몰라 자바로 일단 ㄱㄱ -> 굿 !풀었다 !

import java.util.*;

public class suhyun {

    class Book implements Comparable<Book>{
        int start, end;

        public Book(int start, int end){
            this.start = start;
            this.end = end;
        }

        public int compareTo(Book other){
            return this.start - other.start;
        }

    }

    List<Book> list = new ArrayList<>();
    PriorityQueue<Book> pq = new PriorityQueue<Book>(new Comparator<Book>(){
        public int compare(Book b1, Book b2){
            return b1.end - b2.end;
        }
    });

    public int convert(String x){
        String[] xx = x.split(":");
        return Integer.parseInt(xx[0]) * 60 + Integer.parseInt(xx[1]);
    }

    public int solution(String[][] book_time) {
        int answer = 0;

        for(int i=0; i<book_time.length; i++){
            int start = 0, end = 0;
            start = convert(book_time[i][0]);
            end = convert(book_time[i][1]);
            list.add(new Book(start, end));
        }

        Collections.sort(list);
        pq.offer(list.get(0));
        answer += 1;

        for(int i=1; i<list.size(); i++){
            Book b = pq.peek();
            if(b.end + 10 <= list.get(i).start){
                pq.poll();
                pq.offer(list.get(i));
            } else {
                pq.offer(list.get(i));
                answer += 1;
            }
        }

        return answer;
    }
}
