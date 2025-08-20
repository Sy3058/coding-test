import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static String [][] board;
    static int [] dx = {1, 0, -1, 0};
    static int [] dy = {0, 1, 0, -1};
    static boolean [][] visitedRG; // 적록색약인 사람이 방문했는지 확인
    static boolean [][] visited;   // 적록색약이 아닌 사람이 방문했는지 확인
    static Set<String> RG = new HashSet<>(Arrays.asList("R", "G"));
    static int rgCnt = 0; // 적록색약인 사람이 볼 때 구역의 개수
    static int cnt = 0;   // 적록색약이 아닌 사람이 볼 때 구역의 개수

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 입력
        N = Integer.parseInt(br.readLine());
        board = new String [N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim(); // trim을 이용해서 앞뒤 공백 제거
            for (int j = 0; j < N; j++) {
                board[i][j] = String.valueOf(line.charAt(j));
            }
        }

        // 초기화
        visitedRG = new boolean [N][N];
        visited = new boolean [N][N];

        // 구역 확인
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!(visitedRG[i][j])) { // 적록색약인 사람이 아직 확인하지 못한 곳이라면
                    dfsRG(i, j);
                    rgCnt += 1;
                    
                    // 적록 색약이 아닌 사람도 아직 확인하지 못한 구역
                    dfs(i, j);
                    cnt += 1;
                } else if (!(visited[i][j])) {
                    // 적록 색약인 사람은 R G를 같은 것으로 보므로 아닌 사람이 보기엔 다른 구역일 수 있음
                    dfs(i, j);
                    cnt += 1;
                }
            }
        }

        System.out.println(cnt + " " + rgCnt);
    }

    // 적록 색약인 사람이 볼 때 구간의 개수 확인
    public static void dfsRG(int x, int y) {
        Stack<int []> needVisited = new Stack<>();
        needVisited.push(new int[]{x, y}); // {{x1, y1}, {x2, y2}, ...} 형식으로 push, pop

        while (!needVisited.isEmpty()) {
            int [] cur = needVisited.pop();
            int cx = cur[0];
            int cy = cur[1];
            String startColor = board[cx][cy]; // 시작 색깔
            visitedRG[cx][cy] = true; // 방문 체크 누락 방지

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                // 범위를 벗어나는 경우
                if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                    continue;
                
                // 이미 방문 한 경우
                if (visitedRG[nx][ny])
                    continue;
                
                if ((RG.contains(startColor) && RG.contains(board[nx][ny])) || board[nx][ny].equals(startColor)) {
                    visitedRG[nx][ny] = true; // 방문 처리
                    needVisited.push(new int []{nx, ny});
                }
            }
        }
    }

    public static void dfs(int x, int y) {
        Stack<int []> needVisited = new Stack<>();
        needVisited.push(new int []{x, y});

        while (!needVisited.isEmpty()) {
            int [] cur = needVisited.pop();
            int cx = cur[0];
            int cy = cur[1];
            String startColor = board[cx][cy];
            visited[cx][cy] = true; // 방문 체크 누락 방지

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                // 범위를 벗어나는 경우
                if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                    continue;
                
                // 이미 방문 한 경우
                if (visited[nx][ny])
                    continue;

                if (board[nx][ny].equals(startColor)) {
                    visited[nx][ny] = true;
                    needVisited.push(new int []{nx, ny});
                }
            }
        }
    }
}
