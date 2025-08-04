import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int L = sc.nextInt();
		
		int [] arr = new int [N+1];
		int x = 1; // 처음 공을 받는 사람
		int nx; // 다음으로 공을 받는 사람
		arr[x] = 1;
		
		while (arr[x] < M) {
			if (arr[x] % 2 == 1)
				nx = (x + L) % N;
			else
				nx = (x - L + N) % N; // 항상 양수 결과가 나오도록
			if (nx == 0)
				nx = N;
			
			arr[nx] += 1;
			x = nx;
		}
		int cnt = -1;
		for (int a : arr)
			cnt += a;
		System.out.println(cnt);
	}

}
