import java.util.*;
import java.io.*;

public class Solution {

    static class Edge implements Comparable<Edge> {
        int to;
        int cost;

        public Edge(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.cost, other.cost);
        }
        
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            // 인접 리스트 그래프 생성 및 초기화
            List<Edge>[] graph = new ArrayList[V + 1];
            for (int i = 1; i <= V; i++) {
                graph[i] = new ArrayList<>();
            }

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                // A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있음
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                int C = Integer.parseInt(st.nextToken());
                
                graph[A].add(new Edge(B, C));
                graph[B].add(new Edge(A, C)); // 무향 그래프이므로 둘 다 추가
            }

            // 프림 알고리즘
            boolean [] visited = new boolean[V + 1];
            PriorityQueue<Edge> nv = new PriorityQueue<>();
            nv.add(new Edge(1, 0)); // 1번 정점을 임의의 시작점으로 지정
            long totalCost = 0;
            int cnt = 0;

            // cnt가 V가 되면 종료
            while (!nv.isEmpty() && cnt < V) {
                Edge cur = nv.poll();
                if (visited[cur.to]) continue;

                visited[cur.to] = true;
                totalCost += cur.cost;
                cnt++;

                for (Edge nxt : graph[cur.to]) {
                    if (!visited[nxt.to]) {
                        nv.add(nxt);
                    }
                }
            }
            sb.append("#").append(tc).append(" ").append(totalCost).append("\n");
        }
        System.out.print(sb);
    }
}
