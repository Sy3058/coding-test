import java.util.*;
import java.io.*;

class Solution {

    // 두 좌표 사이의 맨해튼 거리를 반환
    public static int manDist(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            // 집의 좌표를 houseList에 저장
            List<int[]> houseList = new ArrayList<>();
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    int val = sc.nextInt();
                    if (val == 1) {
                        houseList.add(new int[]{r, c});
                    }
                }
            }

            int maxProfit = 0;

            // 모든 가능한 서비스 영역 크기 k 확인
            for (int k = 1; k <= n * 2; k++) {
                // 서비스 영역의 운영 비용 계산
                int cost = k * k + (k - 1) * (k - 1);

                // 모든 좌표를 한 번씩 중심으로 하며 탐색
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        // 현재 중심점 (i, j)에서 서비스 가능한 집의 수
                        int curCnt = 0;

                        // 모든 집의 위치를 순회하며 서비스 가능 여부 확인
                        for (int[] house : houseList) {
                            int hx = house[0];
                            int hy = house[1];

                            // 중심점 (i, j)로부터 집까지의 맨해튼 거리가 k-1 이하라면 서비스 가능
                            if (manDist(i, j, hx, hy) < k) {
                                curCnt++;
                            }
                        }

                        // 이익 계산: (커버된 집의 수 * 집당 지불 비용) - 운영 비용
                        int profit = curCnt * m - cost;

                        // 이익이 0 이상일 때만 최대 집의 수를 갱신
                        if (profit >= 0) {
                            maxProfit = Math.max(maxProfit, curCnt);
                        }
                    }
                }
            }
            System.out.println("#" + tc + " " + maxProfit);
        }
        sc.close();
    }
}