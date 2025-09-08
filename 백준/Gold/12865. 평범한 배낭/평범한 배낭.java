import java.io.*;
import java.util.*;

public class Main {
  static int N, K;
  static List<int[]> items;
  static int [][] dp;
  
  public static void main (String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    items = new ArrayList<>();
    items.add(new int [] {0, 0}); // 계산 편의를 위한 더미 데이터
    dp = new int [N+1][K+1];

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());
      int v = Integer.parseInt(st.nextToken()); // 부피
      int c = Integer.parseInt(st.nextToken()); // 가치
      items.add(new int[] {v, c});
    }

    for (int i = 1; i <= N; i++) { // 확인중인 item
      for (int j = 1; j <= K; j++) { // 부피 제한
        int v = items.get(i)[0];
        int c = items.get(i)[1];

        // 부피제한보다 무게가 크면 넣을 수 없음
        if (j < v) dp[i][j] = dp[i-1][j];
        // 현재 물건을 넣는것과 넣지 않는 것 중 가치가 더 높은 걸 저장
        else dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-v] + c);
      }
    }
    System.out.println(dp[N][K]);
  }
}
