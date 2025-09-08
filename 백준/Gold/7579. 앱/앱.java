import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int t, n, m;
	static int[] A = new int[101];
	static int[] C = new int[101];
	static int[] dp = new int[10001];
	static int ans = 0;

	public static void main(String[] args) throws Exception {

		t = 1;
		for (int tc = 1; tc <= t; tc++) {

			// init

			// input
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= n; i++) A[i] = Integer.parseInt(st.nextToken());
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= n; i++) C[i] = Integer.parseInt(st.nextToken());

			// logic
			for (int i = 1; i <= n; i++) {
				for (int j = 10000; j >= 0; j--) {
					if (j - C[i] >= 0) dp[j] = Math.max(dp[j],  dp[j - C[i]] + A[i]);
				}
			}
			
			for (int i = 0; i <= 10000; i++)
				if (dp[i] >= m) {
					ans = i;
					break;
				}

			// output
//			bw.append("#").append(Integer.toString(tc)).append(" ");
			bw.append(Integer.toString(ans));
//			bw.append("\n");
			bw.flush();
		}

	}
}
