import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        for (int tc = 1; tc < 11; tc++) {
            int dataLength = sc.nextInt();
            int startPoint = sc.nextInt();
            int [] dataList = new int[dataLength];
            for (int i = 0; i < dataLength; i++) {
                dataList[i] = sc.nextInt();
            }

            // 그래프 링크 구성
            Map<Integer, Set<Integer>> link = new HashMap<>();
            for (int i = 0; i < dataLength; i += 2) { // 데이터가 2개씩 구성되므로 +2씩하면서 확인
                int from = dataList[i];
                int to = dataList[i+1];
                link.computeIfAbsent(from, k -> new HashSet<>()).add(to);
            }

            boolean [] visited = new boolean[101];
            visited[startPoint] = true;

            Queue<Integer> queue = new LinkedList<>();
            queue.add(startPoint);
            int depth = -1;

            List<Integer> depthList = new ArrayList<>();
            while (!queue.isEmpty()) {
                int size = queue.size();
                depthList = new ArrayList<>(); // depth 증가시마다 새로운 depthList 생성
                
                for (int i = 0; i < size; i++) {
                    int x = queue.poll();
                    depthList.add(x);

                    if (link.containsKey(x)) {
                        for (int nx : link.get(x)) {
                            if (!visited[nx]) {
                                visited[nx] = true;
                                queue.add(nx);
                            }
                        }
                    }
                }
            }

            int answer = Collections.max(depthList);
            System.out.println("#" + tc + " " + answer);
        }
    }
}
