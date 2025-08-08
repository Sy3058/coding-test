import java.util.*;

public class Solution {
    static int cnt; // 가능한 조합의 개수
    static int n; // 재료의 개수
    static int m; // 같이 쓸 수 없는 재료 쌍
    static List<List<Integer>> restriction = new ArrayList<>();
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();

        for (int tc = 1; tc <= testCase; tc++) {
            n = sc.nextInt();
            m = sc.nextInt();

            restriction.clear(); // 초기화
            for (int i = 0; i < n; i++) {
                restriction.add(new ArrayList<>()); // 각 재료에 대한 빈 ArrayList 추가
            }

            for (int i = 0; i < m; i++) {
                int a = sc.nextInt() - 1;
                int b = sc.nextInt() - 1;
                restriction.get(a).add(b);
                restriction.get(b).add(a); // a:[b,c,d] 형식으로 저장하는 것과 동일
            }

            cnt = 0;
            backtrack(0, 0);
            System.out.println("#" + tc + " " + cnt);
        }
        sc. close();
    }

    public static void backtrack(int start, int selected) {
        boolean isValid = true;

        for (int i = 0; i < n; i++) {
            if ((selected & (1 << i)) != 0) { // i번 재료가 선택된 경우
                for (int res : restriction.get(i)) { // 금지된 재료들과 함께 사용하는지 확인
                    if ((selected & (1 << res)) != 0) { // 금지된 재료가 선택되었는지 확인
                        isValid = false;
                        break;
                    }
                }
            }
            if (!isValid) {
                break;
            }
        }

        if (isValid) {
            cnt++;
        }

        for (int nextIng = start; nextIng < n; nextIng++) {
            backtrack(nextIng + 1, selected | (1 << nextIng));
        }
    }
}
