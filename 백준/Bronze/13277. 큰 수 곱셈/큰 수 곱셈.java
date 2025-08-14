import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
	static int ans;
	static int N;
	static int B;
	static int [] arr;
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String [] input = br.readLine().split(" ");
		
		BigInteger left = new BigInteger(input[0]);
		BigInteger right = new BigInteger(input[1]);
		
		System.out.println(left.multiply(right));
	}
}
