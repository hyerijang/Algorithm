// 알고리즘 기초 - 도경구
// Chapter 4 탐욕 알고리즘
// 4.1 최소신장 알고리즘
// 프림 알고리즘

#include <cstdio>
#include <vector>
#include <climits>
#include <assert.h>

void printY(std::vector<int> Y)
{
    printf("V: ");
    for (int i = 0; i < Y.size(); i++)
    {
        printf("%d ", Y[i]);
    }
    printf("\n");
}

void prim(const int n, const int (*wp)[5])
{
    //0.초기화
    std::vector<std::vector<int>> F; //F= {}
    std::vector<int> Y = {0};        //시작지점초기화
    int nearest[5] = {};
    int distance[5] = {};

    for (int i = 1; i < n; i++)
    {
        nearest[i] = 0;
        distance[i] = wp[0][i];
    }
    //1.선택절차
    int vnear;
    for (int left = 0; left < n - 1; left++)
    {
        // V-Y중에서 Y와 가장 가까운 마디 선택
        int min = INT_MAX;
        for (int i = 0; i < n; i++)
        {
            if (0 < distance[i] && distance[i] < min)
            {
                min = distance[i];
                vnear = i; // 선택
            }
        }

        //해당 마디를 Y에 포함
        Y.push_back(vnear);
        // printY(Y);
        // add e to F
        std::vector<int> edge;
        if (nearest[vnear] < vnear)
        {
            edge.push_back(nearest[vnear]);
            edge.push_back(vnear);
        }
        else
        {
            edge.push_back(vnear);
            edge.push_back(nearest[vnear]);
        }
        F.push_back(edge);
        //갱신
        distance[vnear] = -1; //선택한 마디(vnear)는 앞으로 검사에서 제외한다.
        for (int i = 1; i < n; i++)
        {
            if (0 < wp[i][vnear] && wp[i][vnear] < distance[i])
            {
                distance[i] = wp[i][vnear];
                nearest[i] = vnear;
            }
        }
        //2.적절성 검사
    }
    //3.해답 검증 : 생략
}

void printW(int column, int row, const int (*wp)[5]) //표준: int (*wp)[5], 비표준: int *wp[][5]
{                                                    //더블포인터로 (int **wp) 사용하는 것은 좋지 않음
                                                     // 사용 및 이해가 어렵.
                                                     //const : readonly
    for (int i = 0; i < column; i++)
    {
        for (int j = 0; j < row; j++)
            printf("%d  ", wp[i][j]);
        printf("\n");
    }
    return;
}

int main()
{

    const int m = INT_MAX;
    auto W = new int[5][5]{{0, 1, 3, m, m},
                           {1, 0, 3, 6, m},
                           {3, 3, 0, 4, 2},
                           {m, 6, 4, 0, 5},
                           {m, m, 2, 5, 0}};

    prim(5, W);
}
