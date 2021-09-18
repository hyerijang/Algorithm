void printW(int column, int row, int (*wp)[5]) //표준: int (*wp)[5], 비표준: int *wp[][5]
{                                              // 더블포인터로 (int **wp) 사용하는 것은 좋지 않음. 사용 및 이해가 어렵.
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

    auto W = new int[5][5]{{0, 1, 3, -1, -1},
                           {1, 0, 3, 6, -1},
                           {3, 3, 0, 4, 2},
                           {-1, 6, 4, 0, 5},
                           {-1, -1, 2, 5, 0}};

    printW(5, 5, W);
}