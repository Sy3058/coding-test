import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static int [][] synergy;
    static Set<String> groups; // 중복 제거
    static int minDiff; // 음식 간 맛의 차이
    static boolean [] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            // 입력
            N = Integer.parseInt(br.readLine());
            synergy = new int [N][N];
            for (int i = 0; i < N; i++) {
                String [] s = br.readLine().split(" ");
                for (int j = 0; j < N; j++) {
                    synergy[i][j] = Integer.parseInt(s[j]);
                }
            }

            // 초기화
            groups = new HashSet<>();
            minDiff = Integer.MAX_VALUE;
            visited = new boolean[N];

            dfs(0, new ArrayList<>());

            System.out.println("#" + tc + " " + minDiff);
        }
    }

    public static int sumSynergy(List<Integer>group) {
        int hap = 0;
        for (int x : group) {
            for (int y : group) {
                // group에 있는 재료 x와 y의 시너지
                hap += synergy[x][y];
            }
        }
        return hap;
    }

    public static void dfs(int idx, List<Integer>ingredients) {
        if (ingredients.size() == N/2) {
            // 그룹 A
            List<Integer> groupA = new ArrayList<>(ingredients);
            // 그룹 B (나머지)
            List<Integer>groupB = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                if (!visited[i])
                    groupB.add(i);
            }

            // HashSet에 저장 (중복 체크)
            String keyA = groupA.toString();
            String keyB = groupB.toString();
            if (groups.contains(keyA)) return;
            groups.add(keyA);
            groups.add(keyB);
            
            // 값 비교
            int sumA = sumSynergy(groupA);
            int sumB = sumSynergy(groupB);

            minDiff = Math.min(Math.abs(sumA - sumB), minDiff);
            return;
        }

        for (int i = idx; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                ingredients.add(i);
                dfs(i + 1, ingredients);
                visited[i] = false;
                ingredients.remove(ingredients.size() - 1); // 마지막 값 삭제
            }
        }
    }
}