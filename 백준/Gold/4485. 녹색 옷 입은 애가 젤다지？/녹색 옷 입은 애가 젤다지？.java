import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int[][] graph = new int[130][130];
	static int[][] dist = new int[130][130];
	static int t, n;
	static int ans = 0;
	static int[][] dir = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } }; // 우 좌 하 상
	
	public static class Node implements Comparable<Node>{
		Point p;
		int lost;
		public Node(Point p,int lost) {this.p=p;this.lost=lost;}
		@Override
		public int compareTo(Node n) {
			return Integer.compare(this.lost, n.lost);
		}
	}

	public static void bfs() {
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.add(new Node(new Point(0,0),graph[0][0]));
		dist[0][0] = graph[0][0];

		while (!q.isEmpty()) {
			Node now = q.poll();

			for (int i = 0; i < 4; i++) {
				int nx = now.p.x + dir[i][0];
				int ny = now.p.y + dir[i][1];
				if (nx < 0 || ny < 0 || nx >= n || ny >= n) continue;

				int newLost = now.lost + graph[nx][ny];
				if (dist[nx][ny] <= newLost) continue;

				dist[nx][ny] = newLost;
				q.add(new Node(new Point(nx, ny), newLost));
			}
		}
	}

	public static void main(String[] args) throws Exception {

		t = 1;
//		for (int tc = 1; tc <= t; tc++) {
		while (true) {
			// init
			ans = 0;

			// input
			n = Integer.parseInt(br.readLine());
			if (n == 0) break;
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
					dist[i][j] = Integer.MAX_VALUE / 2;
				}
			}

			// logic
			bfs();

			// output
//			bw.append("#").append(Integer.toString(tc)).append(" ");
			bw.append("Problem ").append(Integer.toString(t++)).append(": ");
			bw.append(Integer.toString(dist[n-1][n-1]));
			bw.append("\n");
			bw.flush();
		}

	}
}
