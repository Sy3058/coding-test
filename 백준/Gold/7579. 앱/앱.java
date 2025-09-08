import java.io.*;
import java.util.*;

public class Main {
  static int N, M, total_cost;
  static int [] memories;
  static int [] costs;
  static int [] dp;
  
  public static void main (String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    memories = new int [N];
    costs = new int [N];

    StringTokenizer stm = new StringTokenizer(br.readLine());
    StringTokenizer stc = new StringTokenizer(br.readLine());

    for (int i = 0; i < N; i++) {
      memories[i] = Integer.parseInt(stm.nextToken());
      costs[i] = Integer.parseInt(stc.nextToken());
      total_cost += costs[i];
    }
    
    dp = new int [total_cost + 1];

    // 각 앱을 순회하면서 dp 테이블 갱신
    for (int i = 0; i < N; i++) {
      int m = memories[i];
      int c = costs[i];

      // 뒤에서부터 순회하며 중복 방지
      for (int j = total_cost; j >= c; j--) {
        // 현재 앱을 비활성화하는 경우와 활성화하는 경우 중 더 큰 메모리 선택
        dp[j] = Math.max(dp[j], dp[j - c] + m);
      }
    }

    // 최소 메모리 M을 만족하는 가장 작은 코스트 찾기
    for (int j = 0; j <= total_cost; j++) {
      if (dp[j] >= M) {
        System.out.println(j);
        break;
      }
    }
  }
}
