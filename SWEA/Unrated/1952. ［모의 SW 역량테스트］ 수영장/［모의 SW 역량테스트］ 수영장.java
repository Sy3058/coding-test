import java.io.*;

public class Solution {
    static int [] price;
    static int [] plan;
    static int minValue;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            price = new int [4];
            plan = new int [12];
            // 입력
            String [] s1 = br.readLine().split(" "); // 띄어쓰기 기준으로 배열로 받기
            String [] s2 = br.readLine().split(" ");
            for (int i = 0; i < s1.length; i++) // 0 : 1일권, 1 : 1개월 이용권, 2 : 3개월 이용권, 3 : 1년 이용권
                price[i] = Integer.parseInt(s1[i]);
            for (int i = 0; i < s2.length; i++)
                plan[i] = Integer.parseInt(s2[i]);
            
            // 초기조건
            minValue = price[3]; // 1년 이용권을 최소 가격으로 설정
            backtrack(0, 0);
            System.out.println("#" + tc + " " + minValue);
        }
    }

    public static void backtrack(int month, int cost) {
        if (month >= 12) { // 0부터 시작하므로 12 이상으로 검사
            minValue = Math.min(minValue, cost);
            return;
        }

        if (plan[month] == 0)
            backtrack(month + 1, cost); // 가격 그대로 다음달로 패스
        
        // 1일권
        backtrack(month + 1, cost + plan[month] * price[0]);

        // 1개월권
        backtrack(month + 1, cost + price[1]);

        // 3개월권
        backtrack(month + 3, cost + price[2]);
    }
}