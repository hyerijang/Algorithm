#include <iostream>
#include <string>
#include <vector>

using namespace std;

void init_allNumbers(vector<int> &numbers, vector<int> &edge) {
  int i = 0;
  for (auto num : numbers) {
    edge[i++] = num;  //양수
    edge[i++] = -num; // 음수
  }
}

void init_adjList(vector<vector<int>> &adjList, vector<int> &edge) {

  for (int i = 0; i < edge.size(); i += 2) {
    vector<int> v2;
    v2.push_back(i + 2);
    v2.push_back(i + 3);

    adjList.push_back(v2);
    adjList.push_back(v2);
  }
}

int dfs(vector<int> &edge, int curEdge, vector<vector<int>> &adjList, int sum,
        int &target) {
  int count = 0;

  if (curEdge >= adjList.size() - 2) {

    sum += edge[curEdge];

    if (sum == target)
      return 1;

    else
      return 0;
  }

  count += dfs(edge, adjList[curEdge][0], adjList, sum + edge[curEdge], target);
  count += dfs(edge, adjList[curEdge][1], adjList, sum + edge[curEdge], target);

  return count;
}

int solution(vector<int> numbers, int target) {

  // edge 초기화
  vector<int> edge(numbers.size() * 2, 0);
  init_allNumbers(numbers, edge);

  //그래프 초기화
  vector<vector<int>> adjList;
  init_adjList(adjList, edge);

  int answer = 0;

  answer += dfs(edge, 0, adjList, 0, target);

  answer += dfs(edge, 1, adjList, 0, target);

  return answer;
}

int main() {

  vector<int> numbers = {1, 1, 1, 1, 1};

  int target = 5;
  cout << solution(numbers, target) << endl;
}