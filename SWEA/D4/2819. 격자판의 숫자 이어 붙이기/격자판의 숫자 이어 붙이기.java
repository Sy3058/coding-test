import java.util.*;
import java.io.*;

public class Solution {
  static String[][] board;
  static int[] dx = { 1, 0, -1, 0 };
  static int[] dy = { 0, 1, 0, -1 };
  static Set<String> numSet;

  public static void main(String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int T = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= T; tc++) {
      // 초기화
      board = new String[4][4];
      numSet = new HashSet<>();

      for (int i = 0; i < 4; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int j = 0; j < 4; j++) {
          board[i][j] = st.nextToken();
        }
      }
      for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
          backtrack(i, j, 0, board[i][j]);
        }
      }
      sb.append("#").append(tc).append(" ").append(numSet.size()).append("\n");
    }
    System.out.print(sb);
  }

  static void backtrack(int x, int y, int idx, String number) {
    if (idx == 6) {
      numSet.add(number);
      return;
    }

    for (int d = 0; d < 4; d++) {
      int nx = x + dx[d];
      int ny = y + dy[d];

      if (0 <= nx && nx < 4 && 0 <= ny && ny < 4) {
        backtrack(nx, ny, idx + 1, number + board[nx][ny]);
      }
    }
  }
}
