import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int[][] dist = new int[11][11];
	static boolean[] visited = new boolean[11];
	static List<Integer> list = new ArrayList<>();
	static int n, ans = Integer.MAX_VALUE;

	public static int check() {
		int val = dist[list.get(list.size() - 1)][list.get(0)];
		if (val == 0) return -1;
		for (int i = 0; i < n - 1; i++) {
			int nd = dist[list.get(i)][list.get(i + 1)];
			if (nd == 0) return -1;
			val += dist[list.get(i)][list.get(i + 1)];
		}
//		System.out.println("dist : " + val);
		return val;
	}

	public static void comb(int depth) {
		if (depth == n) {
//			System.out.println(list);
			int tempAns = check();
			if (tempAns == -1) return;
			ans = Math.min(ans, tempAns);
			return;
		}

		for (int i = 0; i < n; i++) {
			if (visited[i])
				continue;

			visited[i] = true;
			list.add(i);
			comb(depth + 1);
			visited[i] = false;
			list.remove(list.size() - 1);

		}
	}

	public static void main(String[] args) throws Exception {

		// init

		// input
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				dist[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// logic
		comb(0);

		// output
		bw.append(Integer.toString(ans));
		bw.flush();

	}

}
