import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int [][] desserts;
    static boolean [][] visited;
    static int [] dx = {1, 1, -1, -1}; // 12시 기준 시계방향 회전
    static int [] dy = {1, -1, -1, 1};
    static int start_x, start_y;
    static int max_eaten; // 먹은 디저트의 최대값
    static Set<Integer> eaten = new HashSet<>(); // 먹은 디저트
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            // 입력
            N = Integer.parseInt(br.readLine());
            desserts = new int [N][N];
            for (int i = 0; i < N; i++) {
                String [] s = br.readLine().split(" ");
                for (int j = 0; j < N; j++) {
                    desserts[i][j] = Integer.parseInt(s[j]);
                }
            }

            // 초기화
            max_eaten = -1;
            visited = new boolean[N][N];
            eaten = new HashSet<>();

            for (int i = 0; i < N - 2; i++) {
                for (int j = 1; j < N - 1; j++) {
                    start_x = i;
                    start_y = j;
                    dfs(i, j, 0, 0); // x좌표, y좌표, rotate_idx, 이동한 횟수
                }
            }
            System.out.println("#" + tc + " " + max_eaten);
        }
    }

    public static void dfs(int x, int y, int rotate_idx, int moved) {
        // 한 바퀴 돌았고 시작점에 도착했으면 최대값 갱신
        if (rotate_idx == 4) {
            if (x == start_x && y == start_y) {
                max_eaten = Math.max(eaten.size(), max_eaten);
            }
            return;
        }

        int nx = x + dx[rotate_idx];
        int ny = y + dy[rotate_idx];

        if (0 <= nx && nx < N && 0 <= ny && ny < N && !(visited[nx][ny])) {
            if (!(eaten.contains(desserts[nx][ny]))) {
                visited[nx][ny] = true;
                eaten.add(desserts[nx][ny]);
                dfs(nx, ny, rotate_idx, moved + 1);
                visited[nx][ny] = false;
                eaten.remove(desserts[nx][ny]);
            }
        }

        if (moved >= 1) // 한 번 이상 이동했어야 다음 방향으로 진행 (다음 방향으로 갈 때는 이동 횟수 초기화)
            dfs(x, y, rotate_idx + 1, 0);
    }
}
