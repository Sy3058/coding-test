import java.util.*;
import java.io.*;

public class Solution {
    static int [] parent;

    static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static boolean union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            parent[rootB] = rootA;
            return true;
        }
        return false;
    }

    static class Edge implements Comparable<Edge> {
        int A, B, C; // 두 노드, 간선 비용

        public Edge (int A, int B, int C) {
            this.A = A;
            this.B = B;
            this.C = C; // cost
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.C, other.C);
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

            // 초기화
            parent = new int[V+1];
            for (int i = 0; i <= V; i++)
                parent[i] = i;

            // 간선 리스트 생성
            List<Edge> edges = new ArrayList<>();

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                // A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있음
                int A = Integer.parseInt(st.nextToken());
                int B = Integer.parseInt(st.nextToken());
                int C = Integer.parseInt(st.nextToken());
                edges.add(new Edge(A, B, C));
            }

            // 간선비용 기준 정렬
            Collections.sort(edges);

            long totalCost = 0;
            int cnt = 0; // 간선 선택 개수
            for (Edge e : edges) {
                if (union(e.A, e.B)) {
                    totalCost += e.C;
                    cnt++;
                    if (cnt == V - 1)
                        break;
                }
            }
            sb.append("#").append(tc).append(" ").append(totalCost).append("\n");
        }
        System.out.print(sb);
    }
}
