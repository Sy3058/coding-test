import java.util.Scanner;

public class Main {

    private static boolean[] visited;
    private static int n, m;
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        visited = new boolean[n+1];
        sol(0, new int[m], 0);
        sc.close();
    }

    private static void sol(int index, int[] ans, int cur) {
        if (index == m) {
            printArray(ans);
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (!visited[i] && i > cur) {
                ans[index] = i;
                visited[i] = true;
                cur = i;
                sol(index + 1, ans, cur);
                visited[i] = false;
            }
        }
    }

    private static void printArray(int[] ans) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            sb.append(ans[i]);
            if (i < m-1)
                sb.append(" ");
        }
        System.out.println(sb.toString());
    }
}