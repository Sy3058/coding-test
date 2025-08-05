import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int [][] board = new int [n+1][n+1];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				// board[i][j]까지의 구간합은 왼쪽과 위를 더하고 공통 부분인 [i-1][j-1] 부분을 뺀 값
				board[i][j] = board[i-1][j] + board[i][j-1] - board[i-1][j-1] + sc.nextInt();
			}
		}
		for (int i = 0; i < m; i++) {
			int x1 = sc.nextInt() - 1; // x1 y1보다 1작은 값을 빼야 거기까지의 구간합
			int y1 = sc.nextInt() - 1;
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			System.out.println(board[x1][y1] + board[x2][y2] - board[x1][y2] - board[x2][y1]);
		}
	}
	
}
