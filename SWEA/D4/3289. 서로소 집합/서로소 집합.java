import java.util.*;
import java.io.*;

public class Solution {
    static int[] parent;

    // 루트 찾기 (경로 압축 포함)
    static int findSet(int x) {
        if (x == parent[x]) return x;
        return parent[x] = findSet(parent[x]);
    }

    // 두 집합 합치기
    static void union(int x, int y) {
        int rootX = findSet(x);
        int rootY = findSet(y);
        if (rootX != rootY) {
            parent[rootY] = rootX;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            StringBuilder sb = new StringBuilder();
            sb.append("#").append(tc).append(" ");

            int N = Integer.parseInt(st.nextToken()); // 원소 수
            int M = Integer.parseInt(st.nextToken()); // 연산 수

            // 부모 배열 초기화
            parent = new int[N + 1];
            for (int i = 1; i <= N; i++) {
                parent[i] = i; // 자기 자신을 부모로 초기화
            }

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                int command = Integer.parseInt(st.nextToken());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if (command == 0) {
                    // union 연산
                    union(a, b);
                } else if (command == 1) {
                    // find 연산
                    sb.append(findSet(a) == findSet(b) ? 1 : 0);
                }
            }

            System.out.println(sb.toString());
        }
    }
}
