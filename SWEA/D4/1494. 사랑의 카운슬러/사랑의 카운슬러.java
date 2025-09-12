import java.util.*;
import java.io.*;

public class Solution {
    static int N;
    static List <Ji> jiList;
    static long result;
    static boolean [] visited;

    static class Ji { // 지렁이
        int x, y; // 위치

        Ji (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static void makePair(int idx, int cnt) {
        if (cnt == N / 2) {
            long x = 0, y = 0;
            for (int i = 0; i < N; i++) {
                if (visited[i]) {
                    x += jiList.get(i).x;
                    y += jiList.get(i).y;
                } else {
                    x -= jiList.get(i).x;
                    y -= jiList.get(i).y;
                }
            }
            result = Math.min(result, x * x + y * y);
            return;
        }
        for (int i = idx; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                makePair(i + 1, cnt + 1);
                visited[i] = false;
            }
        }
    }

    public static void main (String args[]) throws IOException {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine());

            // 초기화
            jiList = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                jiList.add(new Ji (x, y));
            }

            result = Long.MAX_VALUE;
            visited = new boolean [N];
            makePair(0, 0);
            System.out.println("#" + tc + " " + result);
        }
    }
}
