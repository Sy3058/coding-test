import java.util.*;
import java.io.*;

public class Main {
  static int V, E;
  static List<List<Node>> graph;
  static int[] distance;
  static final int INF = Integer.MAX_VALUE;

  static class Node implements Comparable<Node> {
    int vertex, weight;

    public Node(int weight, int vertex) {
      this.weight = weight;
      this.vertex = vertex;
    }

    @Override
    public int compareTo(Node other) {
      return Integer.compare(this.weight, other.weight);
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    V = Integer.parseInt(st.nextToken());
    E = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(br.readLine());

    graph = new ArrayList<>();
    for (int i = 0; i <= V; i++) {
      graph.add(new ArrayList<>());
    }

    distance = new int[V + 1];
    Arrays.fill(distance, INF);

    for (int i = 0; i < E; i++) {
      st = new StringTokenizer(br.readLine());
      int u = Integer.parseInt(st.nextToken());
      int v = Integer.parseInt(st.nextToken());
      int w = Integer.parseInt(st.nextToken());
      // 그래프에 (가중치, 도착 정점) 순서로 노드 추가
      graph.get(u).add(new Node(w, v));
    }

    dijkstra(K);

    for (int i = 1; i <= V; i++) {
      if (distance[i] == INF) {
        System.out.println("INF");
      } else {
        System.out.println(distance[i]);
      }
    }
  }

  static void dijkstra(int start) {
    PriorityQueue<Node> pq = new PriorityQueue<>();
    // 우선순위 큐에 (가중치 0, 시작 정점)으로 추가
    pq.add(new Node(0, start));
    distance[start] = 0;

    while (!pq.isEmpty()) {
      Node curNode = pq.poll();
      int curW = curNode.weight;
      int curV = curNode.vertex;

      // 이전 값이 더 작다면 다음으로
      if (distance[curV] < curW)
        continue;

      for (Node nxtNode : graph.get(curV)) {
        int nxtV = nxtNode.vertex;
        int nxtW = curW + nxtNode.weight;

        if (nxtW < distance[nxtV]) {
          distance[nxtV] = nxtW;
          pq.add(new Node(nxtW, nxtV));
        }
      }
    }
  }
}