import java.util.Scanner;

public class Solution {
	static int[] gc; // 규영이 카드
	static int[] ic; // 인영이 카드
	static boolean [] uc; // 인영이 카드 중 사용된 카드
	static int win, lose; // 규영이의 승 패 횟수
	
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt(); // 테스트 케이스의 수
		for (int tc = 1; tc <= T; tc++) {
			gc = new int[9]; // 규영이 카드 9개
			boolean [] cards = new boolean[19]; // 1 ~ 18까지 카드의 사용 여부 확인
			
			// 규영이 카드 입력
			for (int i = 0; i < 9; i++) {
				gc[i] = sc.nextInt();
				cards[gc[i]] = true;
			}
			
			// 인영이 카드 확인
			ic = new int[9];
			int idx = 0;
			for (int i = 1; i <= 18; i++) {
				if (!cards[i]) { // 규영이에게 없는 카드면 인영이에게 배정
					ic[idx++] = i;
				}
			}
			
			uc = new boolean[9]; // 인영이가 사용한 카드
			win = 0;
			lose = 0;
			
			// 게임 진행
			permutation(0, 0, 0);
			
			System.out.println("#" + tc + " " + win + " " + lose);
		}
	}
	
	static void permutation(int depth, int gScore, int iScore) {
		// 9라운드까지 진행 후 종료
		if (depth == 9) {
			// 점수 높은 사람이 이기고 동일하면 무승부
			if (gScore > iScore)
				win++;
			else if (gScore < iScore)
				lose++;
			return;
		}
		
		for (int i = 0; i < 9; i++) {
			if (!uc[i]) { // 인영이의 i번째 카드를 사용하지 않았다면
				uc[i] = true;
				
				int gyuCard = gc[depth]; // 규영이의 카드는 순서대로 사용
				int inCard = ic[i]; // 인영이의 i번째 카드 사용
				
				// 점수 계산
				if (gyuCard > inCard) {
					permutation(depth + 1, gScore + gyuCard + inCard, iScore); // 승자가 점수 독식
				} else {
					permutation(depth + 1, gScore, iScore + gyuCard + inCard);
				}
				
				uc[i] = false; // 계산을 끝내고 돌아옴
			}
		}
	}
}
