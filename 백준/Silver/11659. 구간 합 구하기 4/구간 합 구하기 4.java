import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		
		int [] arr = new int [n];
		for (int i = 0; i < n; i++)
			arr[i] = sc.nextInt();
		
		// 구간합
		int [] sum = Arrays.copyOfRange(arr, 0, n);
		for (int i = 1; i < n; i++) {
			sum[i] += sum[i-1];
		}
		
		for (int i = 0; i < m; i++) {
			// a부터 b까지의 구간 합
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if (a == 1)
				System.out.println(sum[b-1]);
			else
				System.out.println(sum[b-1] - sum[a-2]);
		}
	}
}
