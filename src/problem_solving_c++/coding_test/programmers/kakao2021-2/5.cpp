#include <bits/stdc++.h>

using namespace std;

#define INF 987654321

int V;                          //정점의 개수
vector<pair<int, int>> adj[18]; //그래프 인접 리스트. (연결된 정점 번호, 가중치)

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

int solution(vector<int> info, vector<vector<int>> edges) {

  V = info.size();

  for (auto &e : edges) {
    // 양방향
    adj[e[0]].push_back(make_pair(e[1], info[2]));
    adj[e[1]].push_back(make_pair(e[0], info[2]));
  }

  vector<vector<int>> result;
  for (int k = 0; k < V; k++) {
    vector<int> dist = dijkstra(k);
    result.push_back(dist);
  }

  int answer = 987654321;
  return answer;
}

int main() {
  vector<int> info = {0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1};
  vector<vector<int>> edges = {{0, 1},  {1, 2}, {1, 4}, {0, 8}, {8, 7}, {9, 10},
                               {9, 11}, {4, 3}, {6, 5}, {4, 6}, {8, 9}};

  solution(info, edges);
  return 0;
}