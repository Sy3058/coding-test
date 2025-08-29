import java.util.*;
import java.io.*;

public class Solution {
    static int n, x; // 절벽 지대의 크기, 경사로의 길이
    static Way [][] wBoard; // 안에 Way를 배치한 보드
    
    static class Way {
        int ccnt; // 연속된 개수
        boolean needRunway; // 경사로 설치가 필요한 상태인지
        int height; // 높이

        Way (int height) {
            this.ccnt = 1;
            this.needRunway = false;
            this.height = height;
        }
    }
    
    static boolean check (Way before, Way cur) {
        // 높이가 이전과 동일하다면
        if (before.height == cur.height) {
            cur.ccnt = before.ccnt + 1; // 연속된 개수 추가

            // 이전에 이미 높이가 변경된 적 있다면 내려가는 경사로를 설치할 수 있는지 확인
            if (before.needRunway) {
                cur.needRunway = true; // 현재 값도 갱신

                // 경사로 설치 가능한지 확인
                if (cur.ccnt == x) {
                    cur.ccnt = 0; // 다음으로 연속되면 +1씩 하므로 0으로 갱신해야 함
                    cur.needRunway = false; // 경사로 설치 끝났으므로 false로 변경
                }
            }
        }

        // 높이가 낮아진다면
        else if (before.height - 1 == cur.height) {
            // 이전에 경사로 설치가 모두 끝났는지 확인
            if (before.needRunway) return false;

            cur.needRunway = true; // 높이가 낮아지면 경사로 설치 필요
        }

        // 높이가 높아진다면
        else if (before.height + 1 == cur.height) {
            if (before.ccnt < x) return false; // 지정된 길이를 충족하지 못했다면 설치 불가
        }

        // 높이 차이가 1 이상이라면 설치 불가
        else return false;

        // 문제가 없었다면 경사로 설치 가능
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            // 입력
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            x = Integer.parseInt(st.nextToken());

            // 초기화
            wBoard = new Way [n][n];
            int [][] board = new int [n][n];
            int cnt = 0; // 설치된 활주로의 개수

            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                    wBoard[i][j] = new Way(board[i][j]);
                }
            }

            // 가로 확인
            for (int i = 0; i < n; i++) {
                boolean flag = true; // 중단된 적 없는지 확인
                for (int j = 1; j < n; j++) {
                    Way before = wBoard[i][j-1];
                    Way cur = wBoard[i][j];

                    // false가 return되면 경사로 설치 실패한 것
                    if (!check(before, cur)) {
                        flag = false;
                        break;
                    }
                }
                // 중단된 적 없고 경사로 설치가 모두 완료된 경우
                if (flag & !wBoard[i][n-1].needRunway) cnt++;
            }

            // wBoard 초기화
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    wBoard[i][j] = new Way(board[i][j]);
                }
            }

            // 세로 확인
            for (int j = 0; j < n; j++) {
                boolean flag = true;
                for (int i = 1; i < n; i++) {
                    Way before = wBoard[i-1][j];
                    Way cur = wBoard[i][j];

                    if (!check(before, cur)) {
                        flag = false;
                        break;
                    }
                }

                if (flag & !wBoard[n-1][j].needRunway) cnt++;
            }
            sb.append("#").append(tc).append(" ").append(cnt).append("\n");
        }
        System.out.print(sb);
    }
}
