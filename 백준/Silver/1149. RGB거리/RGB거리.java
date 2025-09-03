import java.util.Scanner;

public class Main {
    static int n;
    static int[][] rgb = new int[1001][3];
    static int[][] dp = new int[1001][3];

    public static void main(String[] args) {
        input();
        solve();
    }

    static void input() {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            rgb[i][0] = sc.nextInt();
            rgb[i][1] = sc.nextInt();
            rgb[i][2] = sc.nextInt();
        }
    }

    static void solve() {
        dp[1][0] = rgb[1][0];
        dp[1][1] = rgb[1][1];
        dp[1][2] = rgb[1][2];

        for (int home = 2; home <= n; home++) {
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    if (i == j) continue;

                    if (dp[home][j] == 0)
                        dp[home][j] = dp[home - 1][i] + rgb[home][j];
                    else
                        dp[home][j] = Math.min(dp[home][j], dp[home - 1][i] + rgb[home][j]);
                }
            }
        }

        int result = Math.min(dp[n][0], Math.min(dp[n][1], dp[n][2]));
        System.out.println(result);
    }
}
