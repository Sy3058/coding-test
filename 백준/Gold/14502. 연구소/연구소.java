import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int[][] graph = new int[9][9];
	static int[][] copyGraph = new int[9][9];
	static boolean[][] visited = new boolean[9][9];
	static boolean[][] checkVisited = new boolean[9][9];
	static int n, m, ans;
	static List<Point> virus = new ArrayList<>();
	static List<Point> list = new ArrayList<>();
	static int[][] dir = {{1,0},{-1,0},{0,1},{0,-1}};

	public static void bfs() {
		for (int i = 0; i < n; i++) copyGraph[i] = graph[i].clone();
		visited = new boolean[9][9];
		
		Queue<Point> q = new ArrayDeque<>();
		for (Point p : list) {
			copyGraph[p.x][p.y] = 1;
		}
		for (Point p : virus) {
			q.add(p);
			visited[p.x][p.y] = true; 
		}
		
		
		while (!q.isEmpty()) {
			Point now = q.poll();
//			System.out.println("virus : " + now);
			
			for (int i = 0; i < 4; i++) {
				int nx = now.x + dir[i][0];
				int ny = now.y + dir[i][1];
				if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
				if (copyGraph[nx][ny] != 0) continue;
				if (visited[nx][ny]) continue;

				q.add(new Point(nx, ny));
				copyGraph[nx][ny] = 2;
				visited[nx][ny] = true;

			}
		}

	}

	public static int check() {
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (copyGraph[i][j] == 0) cnt++;
			}
		}
		return cnt;
	}
	
	public static void Print() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				System.out.print(copyGraph[i][j] + " ");
				
			}System.out.println();
		}System.out.println();
	}

	public static void comb(int sx, int sy, int depth) {
		if (depth == 3) {
			bfs();
			ans = Math.max(ans, check());
			
//			Print();
			return;
		}

		for (int i = sx; i < n; i++) {

			int j = (i == sx) ? sy : 0;
			for (; j < m; j++) {
				if (graph[i][j] != 0)
					continue;
				list.add(new Point(i, j));
				comb(i, j + 1, depth + 1);
				list.remove(list.size() - 1);
			}
		}
	}

	public static void main(String[] args) throws Exception {

		// init

		// input
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 2) virus.add(new Point(i,j));
			}
		}

		// logic
		comb(0, 0, 0);

		// output
		bw.append(Integer.toString(ans));
		bw.flush();

	}

}
