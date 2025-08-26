import java.util.*;
import java.io.*;

public class Solution {
    static int N;
    static int minDist; // 이동거리
    static List<Customer> customer = new ArrayList<>();
    static int[] office, house;

    static class Customer {
        int x, y; // 좌표

        Customer(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static void dfs (int x, int y, int cnt, int totalDist, boolean [] visited) {
        if (totalDist >= minDist) return; // 이미 totalDist보다 크면 더 탐색할 필요 없음

        // 모든 고객을 방문했으면 집까지 거리 더하기
        if (cnt == N) {
            int distToHome = Math.abs(x - house[0]) + Math.abs(y - house[1]);
            minDist = Math.min(minDist, totalDist + distToHome);
            return;
        }

        // 다음 방문할 고객 선택 (방문 순서에 따라 값이 달라지므로 모두 탐색)
        for (int i = 0; i < N; i++) {
            if (visited[i]) continue;
            int dist = Math.abs(x - customer.get(i).x) + Math.abs(y - customer.get(i).y);
            visited[i] = true;
            dfs(customer.get(i).x, customer.get(i).y, cnt + 1, totalDist + dist, visited);
            visited[i] = false;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // 회사에서 출발해서 집에 도착해야함
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine()); // 회사 좌표, 집 좌표, N명의 고객 좌표 (x, y 쌍으로 제공)
            office = new int [] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
            house = new int [] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};

            // 고객의 좌표
            customer = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                customer.add(new Customer(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
            }

            minDist = Integer.MAX_VALUE;
            boolean[] visited = new boolean[N];
            dfs(office[0], office[1], 0, 0, visited);

            sb.append("#").append(tc).append(" ").append(minDist).append("\n");
        }
        System.out.print(sb);
    }
}
