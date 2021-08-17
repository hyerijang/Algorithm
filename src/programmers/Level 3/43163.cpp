#include <queue>
#include <string>
#include <vector>

using namespace std;

bool isDiffOneChar(string a, string b) {

  int diff = 0;
  for (int i = 0; i < a.length(); i++) {
    if (a[i] != b[i])
      diff++;
    if (diff > 1)
      return false;
  }

  if (diff == 0)
    return false;
  // diff == 1이면 true
  return true;
}

vector<vector<int>> adjList;
vector<int> parent;

int BFS(int here, const string &target, vector<string> &words) {

  vector<bool> discovered(adjList.size(), false);

  queue<int> q;
  q.push(here);
  discovered[here] = true;
  parent[here] = here;

  while (!q.empty()) {
    here = q.front();
    q.pop();

    if (words[here] == target)
      return here;

    for (auto there : adjList[here]) {
      if (!discovered[there]) {
        q.push(there);
        discovered[there] = true;
        parent[there] = here;
      }
    }
  }

  return -1;
}

int solution(string begin, string target, vector<string> words) {
  int answer = 0;

  // words에 begin 추가
  bool isExist = false;
  int startIdx = 0;
  for (const auto &word : words) {
    if (word == begin) {
      isExist = true;
      break;
    }
    startIdx++;
  }

  //이미 있으면 추가 x
  if (!isExist)
    words.push_back(begin);

  //그래프 생성
  for (int i = 0; i < words.size(); i++) {
    vector<int> v;
    for (int j = 0; j < words.size(); j++) {
      if (isDiffOneChar(words[i], words[j]))
        v.push_back(j);
    }
    adjList.push_back(v);
  }

  parent.assign(adjList.size(), 0);
  int targetIdx = BFS(startIdx, target, words);

  //단어가 없는 경우
  if (targetIdx < 0)
    return 0;

  while (targetIdx != parent[targetIdx]) {
    answer++;
    targetIdx = parent[targetIdx];
  }
  return answer;
}

int main() {
  string begin = "hit";
  string target = "cog";
  vector<string> words = {"hot", "dot", "dog", "lot", "log"};
  solution(begin, target, words);
}