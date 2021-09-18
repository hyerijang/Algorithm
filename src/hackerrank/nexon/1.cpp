long paperCuttings(int textLength, vector<int> starting, vector<int> ending) {

  set<pair<int, int>> s;

  for (int i = 0; i < starting.size(); i++) {
    s.insert(make_pair(starting[i], ending[i]));
  }

  long sum = 0; //리턴 값
  for (auto &a : s) {
    // A를 고른다.
    // A와 겹치지 않는 B를 고른다
    for (auto &b : s) {
      if (a.first <= b.second || a.second <= b.first)
        continue; //겹치는 경우 pass
      sum++;
    }
  }

  return sum;
}