#include <cmath>
#include <iostream>
using namespace std;

int N;
int K;

int doll_arr[501];

double Calculator_SD(int _head,
                     int _tail) // Smallest_SD()에서 계산하고자 하는 수열의
                                // 표준편차를 계산한 뒤 리턴해준다.
{
  double mean = 0;
  double sd = 0;
  int num = _tail - _head + 1;

  for (int j = _head; j <= _tail; j++) {
    mean += doll_arr[j];
  }
  mean /= num; //평균값 구하기

  for (int j = _head; j <= _tail; j++) {
    double temp = (doll_arr[j] - mean);
    temp *= temp; //제곱
    sd += temp;   //제곱값 합산
  }
  sd /= num;
  sd = sqrt(sd);

  return sd;
}

double Smallest_SD() //최소가 되는 표준 편차를 리턴한다.
{
  int head = 0; //배열의 head
  int tail = 0; //배열의 tail
  double smallest = 100000000;

  for (int i = K - 1; i < N;
       i++) //가령 N=10, K=3일 경우, 반복문은 2,3,4,..,9 총 8회를 돈다.
  {
    head = 0;
    tail = i;

    while (tail < N) //즉 tail이 배열의 마지막 인덱스에 닿기 전까지 반복
    {
      double temp = Calculator_SD(head, tail);

      if (smallest >= temp) {
        smallest = temp;
      } //최솟값 갱신

      head++;
      tail++;
    }
  }

  return smallest;
}

int main() {
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    cin >> doll_arr[i];
  } // 테스트케이스를 입력받아 배열에 저장한다.

  cout.precision(10);
  cout << Smallest_SD() << "\n"; //정답이 되는 최소 표준편차를 출력한다.

  return 0;
}