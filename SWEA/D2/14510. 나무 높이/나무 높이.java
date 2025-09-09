import java.io.*;
import java.util.*;

public class Solution {
  static int N; // 나무의 개수
  static int [] trees;
  public static void main (String args[]) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int T = Integer.parseInt(br.readLine());

    for (int tc = 1; tc <= T; tc++) {
      N = Integer.parseInt(br.readLine());

      // 초기화
      trees = new int [N];
      int maxHeight = 0;

      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int i = 0; i < N; i++) {
        trees[i] = Integer.parseInt(st.nextToken());
        maxHeight = Math.max(maxHeight, trees[i]);
      }

      // 가장 키가 컸던 나무와 높이 차이 비교
      Map <Integer, Integer> water = new HashMap<>();
      water.put(1, 0); // 높이차%2의 개수 더하기
      water.put(2, 0); // 높이차/2의 개수 더하기
      for (int i = 0; i < N; i++) {
        int diff = maxHeight - trees[i]; // 높이차이
        water.replace(1, water.get(1) + diff % 2); // 1씩 줘야하는 날
        water.replace(2, water.get(2) + diff / 2); // 2씩 줘야하는 날
      }

      int one = water.get(1); // 홀수 날에는 1씩 줌
      int two = water.get(2); // 짝수 날에는 2씩 줌
      int date = 0; // 물을 줘야하는 날
      
      if (one > two) {
        // 1씩 줘야하는 날이 많으면 1씩 줘야하는 날만큼만 계산하면 됨
        date = 2 * one - 1;
      } else if (one == two) {
        // 동일하면 순서대로 주기만 하면 되므로 one * 2
        date = 2 * one;
      } else {
        // 2씩 주는 날을 쪼개서 1씩 줄 수 있음
        // 우선 1씩 주는 날을 모두 주고 2만 남기기
        date = 2 * one;
        int leftDate = 2 * (two - one); // 남은 날짜이므로 two * 2 해줘야함
        date += (leftDate/3) * 2; // 1 2씩 주기
        if (leftDate % 3 == 1) date += 1; // 홀수 날 줘야함
        else if (leftDate % 3 == 2) date += 2; // 짝수 날 줘야함
      }
      sb.append("#").append(tc).append(" ").append(date).append("\n");
    }
    System.out.print(sb);
  }
}
