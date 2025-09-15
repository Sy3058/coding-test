import java.util.*;
import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        
        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            
            String[] card = new String[N];
            for (int i = 0; i < N; i++) {
                card[i] = st.nextToken();
            }
            
            // 카드 덱을 두 부분으로 나누기
            String[] leftHalf;
            String[] rightHalf;
            int half = (N + 1) / 2; // 홀수개면 왼쪽에 카드가 더 있어야 함

            leftHalf = new String[half];
            rightHalf = new String[N - half];

            System.arraycopy(card, 0, leftHalf, 0, half);
            System.arraycopy(card, half, rightHalf, 0, N - half);
            
            // 두 덱을 번갈아 섞어 새로운 덱을 만듭니다.
            StringBuilder sb = new StringBuilder();
            sb.append("#").append(tc).append(" ");
            
            int rightIndex = 0;
            for (int i = 0; i < half; i++) {
                sb.append(leftHalf[i]).append(" ");
                if (rightIndex < rightHalf.length) {
                    sb.append(rightHalf[rightIndex++]).append(" ");
                }
            }
            
            System.out.println(sb.toString().trim());
        }
    }
}