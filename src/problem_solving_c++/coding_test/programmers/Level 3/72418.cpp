//합승 택시 요금 (프로그래머스)
//다익스트라 알고리즘
#include <bits/stdc++.h>

using namespace std;

#define MAX_V 201
#define INF 987654321

int V;                             //정점의 개수
vector<pair<int, int>> adj[MAX_V]; //그래프 인접 리스트. (연결된 정점 번호, 간선
                                   //가중치) 형태로 저장

vector<int> dijkstra(int src) {
  vector<int> dist(V, INF);
  dist[src] = 0;
  priority_queue<pair<int, int>> pq;
  pq.push(make_pair(0, src));
  while (!pq.empty()) {
    int cost = -pq.top().first;
    int here = pq.top().second;
    pq.pop();
    //지금 꺼낸 정점이 무시해야 하는 정보인지 확인한다
    if (dist[here] < cost)
      continue;
    for (int i = 0; i < adj[here].size(); ++i) {
      int there = adj[here][i].first;
      int nextDist = cost + adj[here][i].second;
      if (dist[there] > nextDist) {
        dist[there] = nextDist;
        pq.push(make_pair(-nextDist, there));
      }
    }
  }
  return dist;
}

//지점의 개수 n,
//출발지점을 나타내는 s,
// A의 도착지점을 나타내는 a,
// B의 도착지점을 나타내는 b
int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
  // A, B 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다
  //최저 예상 택시요금을 계산해서 return
  //각자 이동하는 경우의 예상 택시요금이 더 낮다면, 합승을 하지 않아도 됩니다.
  V = n + 1;
  for (auto f : fares) {
    // 양방향
    adj[f[0]].push_back(make_pair(f[1], f[2]));
    adj[f[1]].push_back(make_pair(f[0], f[2]));
  }

  vector<vector<int>> result(1);
  for (int k = 1; k <= n; k++) {
    vector<int> dist = dijkstra(k);
    result.push_back(dist);
  }

  int answer = 987654321;

  for (int k = 1; k <= n; k++) {
    int candidate = result[s][k] + result[k][a] + result[k][b];
    if (candidate > 0 && answer > candidate)
      answer = candidate;
  }
  return answer;
}

int main() {

  //   int n = 6;
  //   int s = 4;
  //   int a = 6;
  //   int b = 2;
  //   vector<vector<int>> fares = {{4, 1, 10}, {3, 5, 24}, {5, 6, 2},
  //                                {3, 1, 41}, {5, 1, 24}, {4, 6, 50},
  //                                {2, 4, 66}, {2, 3, 22}, {1, 6, 25}};

  int n = 6;
  int s = 4;
  int a = 5;
  int b = 6;
  vector<vector<int>> fares = {{2, 6, 6},  {6, 3, 7},  {4, 6, 7}, {6, 5, 11},
                               {2, 5, 12}, {5, 3, 20}, {2, 4, 8}, {4, 3, 9}};

  solution(n, s, a, b, fares);
}