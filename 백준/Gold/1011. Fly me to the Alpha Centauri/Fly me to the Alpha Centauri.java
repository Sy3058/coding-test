import java.io.*;
import java.util.*;

public class Main {
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int x = Integer.parseInt(st.nextToken());
        	int y = Integer.parseInt(st.nextToken());
        	int dis = y - x;
        	int n = (int) Math.pow(dis, 0.5);
        	if (Math.pow(n, 2) + n > dis)
        		n -= 1;
        	
        	double rest = dis - (Math.pow(n, 2) + n);
        	
        	if (rest == 0) System.out.println(2*n);
        	else if (rest <= n + 1) System.out.println(2*n + 1);
        	else System.out.println(2 * n + 2);
        }
    }
}
