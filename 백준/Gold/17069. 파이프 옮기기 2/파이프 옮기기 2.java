import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int t, n;
	static int[][] graph = new int[35][35];
	static long[][][] dp = new long[3][35][35];
	static long ans = 0;

	public static void main(String[] args) throws Exception {

		t = 1;
		for (int tc = 1; tc <= t; tc++) {

			// init

			// input
			n = Integer.parseInt(br.readLine());
			for (int i = 1; i <= n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j <= n; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			// logic

			dp[0][1][2] = 1;
			for (int i = 1; i <= n; i++) {
				for (int j = 3; j <= n; j++) {
					if (graph[i][j] == 1)
						continue;

					dp[0][i][j] = dp[0][i][j - 1] + dp[1][i][j - 1];
					dp[2][i][j] = dp[2][i - 1][j] + dp[1][i - 1][j];
					if (graph[i - 1][j] == 0 && graph[i][j - 1] == 0) {
						dp[1][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1];
					}

				}
			}


			ans = dp[0][n][n] + dp[1][n][n] + dp[2][n][n];
			// output
//			bw.append("#").append(Integer.toString(tc)).append(" ");
			bw.append(Long.toString(ans));
//			bw.append("\n");
			bw.flush();
		}

	}
}
