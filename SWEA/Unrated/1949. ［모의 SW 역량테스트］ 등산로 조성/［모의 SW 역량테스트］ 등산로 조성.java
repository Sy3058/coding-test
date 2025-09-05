import java.io.*;
import java.util.*;

public class Solution {
	static int N, K; // 지도 한 변의 길이 최대 공사 가능 깊이
	static int [][] board;
	static boolean [][] visited;
	static List<int[]> startPoint;
	static int result;
	static int [] dx = {1, 0, -1, 0};
	static int [] dy = {0, 1, 0, -1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	N = Integer.parseInt(st.nextToken());
        	K = Integer.parseInt(st.nextToken());
        	
        	// 초기화
        	board = new int [N][N];
        	visited = new boolean [N][N];
        	startPoint = new ArrayList<>();
        	int maxHeight = 0;
        	result = 0;
        	
        	for (int i = 0; i < N; i++) {
        		st = new StringTokenizer(br.readLine());
        		for (int j = 0; j < N; j++) {
        			board[i][j] = Integer.parseInt(st.nextToken());
        			maxHeight = Math.max(maxHeight, board[i][j]); // 가장 높은 위치 찾기
        		}
        	}
        	
        	// 시작 지점 찾기 (가장 높은 위치)
        	for (int i = 0; i < N; i++) {
        		for (int j = 0; j < N; j++) {
        			if (board[i][j] == maxHeight)
        				startPoint.add(new int [] {i, j});
        		}
        	}
        	
        	// 시작 위치에서 상하좌우로 이동하거나 1~K만큼 깎고 이동하기
        	for (int [] p : startPoint) {
        		// 방문 배열 초기화
        		for (int i = 0; i < N; i++) 
        			Arrays.fill(visited[i], false);
        		// DFS로 가장 깊은 길이 찾기
        		int x = p[0]; int y = p[1];
        		visited[x][y] = true;
        		dfs(x, y, 1, board[x][y], false);
        		visited[x][y] = false;
        	}
        	sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.println(sb);
    }
        
    static void dfs (int x, int y, int len, int prev, boolean dig) {
    	// 현재까지의 등산로 길이 최대값으로 갱신
    	result = Math.max(result, len);
    	
    	// 사방 이동
    	for (int d = 0; d < 4; d++) {
    		int nx = x + dx[d]; int ny = y + dy[d];
    		// 범위 내이고 방문된 적 없을 때
    		if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
    			if (board[nx][ny] < prev) {
    				// 이전에 방문했던 위치보다 더 낮다면
    				visited[nx][ny] = true; // 방문 처리
    				dfs(nx, ny, len + 1, board[nx][ny], dig); // 백트래킹
    				visited[nx][ny] = false; // 방문 처리 취소
    			}
    			
    			// 이전에 땅은 판 적이 없다면 땅을 파고 있다면 그냥 다음으로
    			if (dig) continue;
    			for (int i = 1; i <= K; i++) {
    				if (0 <= board[nx][ny] - i && board[nx][ny] - i < prev) {
    					// 땅을 파낸 값이 0 이상이고 이전의 높이보단 낮을 때
    					visited[nx][ny] = true;
    					dfs(nx, ny, len + 1, board[nx][ny] - i, true);
    					visited[nx][ny] = false;
    				}
    			}
    		}
    	}
    }   
}

