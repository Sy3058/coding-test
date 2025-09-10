import java.util.*;
import java.util.List;
import java.io.*;
import java.awt.*;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static StringTokenizer st;
	static int t, n;
	static String ans;
	static Point start, end;
	static List<Point> storeList = new ArrayList<>();
	static Set<Point> visited = new HashSet<>();
	
	public static int calcDist(Point p1, Point p2) {
		return Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y); 
	}
	
	public static boolean bfs() {
		Queue<Point> q = new ArrayDeque<>();
		q.add(start);
		visited.add(start);
		
		while (!q.isEmpty()) {
			Point now = q.poll();
			if (calcDist(now,end) <= 1000) {
				return true;
			}
			
			for (Point store : storeList) {
				if (visited.contains(store)) continue;
				if (calcDist(now,store) > 1000) continue;
				
				visited.add(store);
				q.add(store);
			}
		}
		
		return false;
	}
	

	public static void main(String[] args) throws Exception {

		t = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= t; tc++) {

			// init
			storeList.clear();
			visited.clear();

			// input
			n = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			start = new Point(x,y);
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				x = Integer.parseInt(st.nextToken());
				y = Integer.parseInt(st.nextToken());
				storeList.add(new Point(x,y));
			}
			st = new StringTokenizer(br.readLine());
			x = Integer.parseInt(st.nextToken());
			y = Integer.parseInt(st.nextToken());
			end = new Point(x,y);

			// logic
			ans = (bfs()) ? "happy" : "sad";

			// output
//			bw.append("#").append(Integer.toString(tc)).append(" ");
			bw.append(ans);
			bw.append("\n");
			bw.flush();
		}

	}
}
