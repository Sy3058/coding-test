import java.io.*;
import java.util.*;

class Solution {
	static int N;
	static int[][] arr;

	static List<Stair> stairs;
	static List<Person> person;

	static int[] result;
	static int ans;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
      // 입력
			N = Integer.parseInt(br.readLine());

      // 초기화
			arr = new int[N][N];
			stairs = new ArrayList<>(2);
			person = new ArrayList<>();

      // 사람은 사람 리스트에, 계단은 계단 리스트에 추가
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
					if (arr[i][j] == 1) {
						person.add(new Person(i, j));
					} else if (arr[i][j] >= 2) {
						stairs.add(new Stair(i, j, arr[i][j]));
					}
				}
			}

			ans = Integer.MAX_VALUE;
			result = new int[person.size()];

			dfs(0);
			System.out.println("#" + tc + " " + ans);
		}
	}

	// 모든 사람을 두 개의 계단 중 하나에 배정하는 모든 경우의 수를 탐색
	static void dfs(int depth) {
		if (depth == person.size()) {
			ans = Math.min(ans, solve());
			return;
		}
		result[depth] = 0; // 0번 계단에 배정
		dfs(depth + 1);
		result[depth] = 1; // 1번 계단에 배정
		dfs(depth + 1);
	}

	// 특정 계단 배정 시나리오에 대한 총 소요 시간 계산
	public static int solve() {
		List<Person> stair1 = new ArrayList<>();
		List<Person> stair2 = new ArrayList<>();
		
		// DFS로 할당된 결과(result 배열)에 따라 사람들을 두 계단 리스트로 나눔
		for (int i = 0; i < person.size(); i++) {
			Person p = person.get(i);
			Stair s = stairs.get(result[i]);
			
			// 사람과 계단 사이의 거리(시간) 계산 (맨해튼 거리)
			p.distance = Math.abs(s.r - p.r) + Math.abs(s.c - p.c);
			
			if (result[i] == 0) {
				stair1.add(p);
			} else {
				stair2.add(p);
			}
		}

		// 계단 도착 시간(거리)을 기준으로 정렬
		Collections.sort(stair1);
		Collections.sort(stair2);

		// 각 계단 그룹에 대한 시뮬레이션 실행
		int end1 = simulate(stair1, stairs.get(0).len);
		int end2 = simulate(stair2, stairs.get(1).len);

		// 두 그룹 중 더 오래 걸리는 시간을 최종 결과로 반환
		return Math.max(end1, end2);
	}

	// 한 계단 그룹에 대한 시뮬레이션
	static int simulate(List<Person> waiting, int stairLen) {
		// 대기 리스트의 복사본을 만들어 원본 리스트를 변경하지 않도록 함
		List<Person> currentWaiting = new ArrayList<>(waiting);
		if (currentWaiting.isEmpty()) {
			return 0;
		}

		int t = 0;
		
		// 계단에 있는 사람들의 남은 시간 (time)을 저장하는 리스트
		List<Integer> onStair = new ArrayList<>();
		
		// 모든 사람이 계단을 다 내려갈 때까지 시뮬레이션 반복
		while (!currentWaiting.isEmpty() || !onStair.isEmpty()) {
			t++; // 1분 경과

			// 1. 계단에 있는 사람들 처리 (내려가는 중)
			for (int i = onStair.size() - 1; i >= 0; i--) {
				onStair.set(i, onStair.get(i) + 1);
				if (onStair.get(i) == stairLen) {
					onStair.remove(i);
				}
			}

			// 2. 대기 중인 사람들 처리 (계단 진입)
			for (int i = currentWaiting.size() - 1; i >= 0; i--) {
				Person p = currentWaiting.get(i);
				// (도착 시간 < 현재 시간) and 계단에 3명 미만이 있을 때 진입 가능
				if (p.distance < t && onStair.size() < 3) {
					onStair.add(0); // 새로운 사람이 계단에 진입 (경과 시간 0분)
					currentWaiting.remove(i);
				}
			}
		}

		return t;
	}

}

class Person implements Comparable<Person> {
	int r, c;
	int distance; // 계단까지의 거리 (도착 시간)

	Person(int r, int c) {
		this.r = r;
		this.c = c;
	}

	@Override
	public int compareTo(Person o) {
		return Integer.compare(this.distance, o.distance);
	}
}

class Stair {
	int r, c, len; // len은 계단의 길이

	Stair(int r, int c, int len) {
		this.r = r;
		this.c = c;
		this.len = len;
	}
}