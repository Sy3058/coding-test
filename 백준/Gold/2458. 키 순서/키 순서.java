import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
//	static int[][] graph = new int[101][101];
	static boolean[] visited = new boolean[501];
	static int t, n, m;
	static int ans = 0;
	static int[][] dir = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } }; // 우 좌 하 상
	static List<List<Integer>> bigGraph = new ArrayList<>();
	static List<List<Integer>> smallGraph = new ArrayList<>();
	

	public static int bfs(int start, boolean isBig) {
		Arrays.fill(visited, false);
		
		int cnt = -1;
		
		Queue<Integer> q = new ArrayDeque<>();
		q.add(start);
		visited[start] = true;
		
		while (!q.isEmpty()) {
			Integer now = q.poll();
			cnt++;

			int graphSize = (isBig) ? bigGraph.get(now).size() : smallGraph.get(now).size();
			for (int i = 0; i < graphSize; i++) {
				int next = (isBig) ? bigGraph.get(now).get(i) : smallGraph.get(now).get(i);
				if (visited[next]) continue;

				visited[next] = true;
				q.add(next);
			}
		}
		
//		if (isBig) System.out.println("big : " + cnt);
//		else System.out.println("small : " + cnt);
		return cnt;
	}

	public static void main(String[] args) throws Exception {

		t = 1;
		for (int tc = 1; tc <= t; tc++) {
			// init
			
			
			// input
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			for (int i = 0; i <= n; i++) {
				bigGraph.add(new ArrayList<>());
				smallGraph.add(new ArrayList<>());
			}
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int s = Integer.parseInt(st.nextToken());
				int e = Integer.parseInt(st.nextToken());
				bigGraph.get(s).add(e);
				smallGraph.get(e).add(s);
			}
			
			// logic
			for (int i = 1; i <= n; i++) {
				int big = bfs(i, true);
				int small = bfs(i, false);
				if (big + small == n - 1) ans++;
			}

			// output
//			bw.append("#").append(Integer.toString(tc)).append(" ");
			bw.append(Integer.toString(ans));
//			bw.append("\n");
			bw.flush();
		}

	}
}
