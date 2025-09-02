import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
//	static int[][] graph = new int[101][101];
	static boolean[] visited = new boolean[11];
	static int[] personCnt = new int[11];
	static int[] area = new int[11];
	static int t, n, m;
	static int ans = Integer.MAX_VALUE;
	static int[][] dir = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } }; // 우 좌 하 상
	static List<List<Integer>> graph = new ArrayList<>();
	
	public static void bfs(int start) {
		Queue<Integer> q = new ArrayDeque<>();
		q.add(start);
		visited[start] = true;
		
		while (!q.isEmpty()) {
			Integer now = q.poll();

			for (int i = 0; i < graph.get(now).size(); i++) {
				int next = graph.get(now).get(i);
				if (visited[next]) continue;
				if (area[now] != area[next]) continue;

				visited[next] = true;
				q.add(next);
			}
		}
		
	}
	

	public static void dfs(int num) {
		if (num == n + 1) {
			int area1 = 0;
			int area2 = 0;
			
			Arrays.fill(visited, false);
			int areaCnt = 0;
			for (int i = 1; i <= n; i++) {
				if (area[i] == 1) area1 += personCnt[i];
				else area2 += personCnt[i];
				if (visited[i]) continue;
				areaCnt++;
				bfs(i);
			}
			if (areaCnt != 2) return;
			
			ans = Math.min(Math.abs(area1 - area2), ans);
			return;
		}
		
		
		area[num] = 1;
		dfs(num + 1);
		area[num] = 2;
		dfs(num + 1);
		
	}

	public static void main(String[] args) throws Exception {

		t = 1;
		for (int tc = 1; tc <= t; tc++) {
			
			// init
			
			
			// input
			n = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			graph.add(new ArrayList<>());
			for (int i = 1; i <= n; i++) {
				graph.add(new ArrayList<>());
				personCnt[i] = Integer.parseInt(st.nextToken());
			}
			for (int i = 1; i <= n; i++) {
				st = new StringTokenizer(br.readLine());
				int k = Integer.parseInt(st.nextToken());
				for (int j = 0; j < k; j++) {
					int e = Integer.parseInt(st.nextToken());
					graph.get(i).add(e);
					graph.get(e).add(i);
				}
			}
			
			
			
			// logic
			area[1] = 1;
			dfs(2);
			area[1] = 2;
			dfs(2);
			if (ans == Integer.MAX_VALUE) ans = -1;

			// output
//			bw.append("#").append(Integer.toString(tc)).append(" ");
			bw.append(Integer.toString(ans));
//			bw.append("\n");
			bw.flush();
		}

	}
}
