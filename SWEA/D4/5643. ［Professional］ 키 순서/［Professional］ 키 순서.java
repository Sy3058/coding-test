import java.io.*;
import java.util.*;

public class Solution {
  static int N, M;
  static List<List<Integer>> sgraph;
  static List<List<Integer>> bgraph;

  static int bfs(int s, boolean isSmall) {
    boolean [] visited = new boolean[N + 1];
    Queue<Integer> nv = new ArrayDeque<>();

    int cnt = 0;
    visited[s] = true;
    nv.add(s);

    while (!nv.isEmpty()) {
      int cur = nv.poll();

      if (isSmall) { // s보다 작은 사람 탐색
        for (int nxt : bgraph.get(cur)) { // bgraph를 이용해 cur보다 작은 사람 탐색
          if (!visited[nxt]) {
            visited[nxt] = true;
            nv.add(nxt);
            cnt++;
          }
        }
      } else { // s보다 큰 사람 탐색
        for (int nxt : sgraph.get(cur)) { // sgraph를 이용해 cur보다 큰 사람 탐색
          if (!visited[nxt]) {
            visited[nxt] = true;
            nv.add(nxt);
            cnt++;
          }
        }
      }
    }
    return cnt;
  }
  public static void main (String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int T = Integer.parseInt(br.readLine());

    for (int tc = 1; tc <= T; tc++) {
      // 입력
      N = Integer.parseInt(br.readLine()); // 학생들의 수
      M = Integer.parseInt(br.readLine()); // 학생의 키를 비교한 횟수

      // 초기화
      sgraph = new ArrayList<>();
      bgraph = new ArrayList<>();

      for (int i = 0; i <= N; i++) {
        sgraph.add(new ArrayList<>());
        bgraph.add(new ArrayList<>());
      }

      for (int i = 0; i < M; i++) {
        // 번호가 a인 학생이 번호가 b인 학생보다 키가 작다 (유향그래프)
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        sgraph.get(a).add(b); // a보다 큰 학생들 리스트
        bgraph.get(b).add(a); // b보다 작은 학생들 리스트
      }

      int ans = 0;
      for (int i = 1; i <= N; i++) {
        int smaller = bfs(i, true); // i보다 작은 사람의 수
        int bigger = bfs(i, false); // i보다 큰 사람의 수

        // 둘의 합이 전체 명수에서 자기 자신을 뺀 값이어야 모든 사람과 키 비교 가능
        if (smaller + bigger == N - 1) ans++;
      }
      sb.append("#").append(tc).append(" ").append(ans).append("\n");
    }
    System.out.println(sb);
  }
}
