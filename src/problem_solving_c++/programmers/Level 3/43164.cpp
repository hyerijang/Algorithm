#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define DEPARTURE 0
#define ARRIVAL 1

vector<bool> visited;
vector<vector<string>> order;

void BFS(int ticketNumber, vector<vector<string>> &tickets) {

  string airportNow = tickets[ticketNumber][ARRIVAL];
  for (int i = 0; i < tickets.size(); i++) {
    if (!visited[i])
      if (airportNow == tickets[i][DEPARTURE]) {
        visited[i] = true;
        BFS(i, tickets);
        // visited[i] = false;
      }
  }

  order.push_back(tickets[ticketNumber]);
}

vector<string> solution(vector<vector<string>> tickets) {

  //티켓을 출발지 기준으로 오름차순 정렬
  sort(tickets.begin(), tickets.end());
  //   printTickets(tickets);

  vector<string> answer;
  visited.assign(tickets.size(), false);

  for (int i = 0; i < tickets.size(); i++) {
    if (tickets[i][DEPARTURE] == "ICN") {
      visited[i] = true;
      BFS(i, tickets);
      //   visited[i] = false;
      break;
    }
  }

  reverse(order.begin(), order.end());
  answer.push_back("ICN");
  for (auto o : order) {
    answer.push_back(o[ARRIVAL]);
  }

  return answer;
}
int main() {
  //   vector<vector<string>> tickets = {
  //       {"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}};
  // vector<vector<string>> tickets = {{"ICN", "SFO"},
  //                                   {"ICN", "ATL"},
  //                                   {"SFO", "ATL"},
  //                                   {"ATL", "ICN"},
  //                                   {"ATL", "SFO"}};
  vector<vector<string>> tickets = {{"ICN", "A"}, {"ICN", "B"}, {"B", "ICN"}};

  solution(tickets);

  return 0;
}