#include <iostream>
using namespace std;

char Coloring_(char C)
{
    if (C == 'B') return 'W';
    else return 'B';
}

int HowManyColor(int r, int c, char** A)
{
    char Color = 'B';
    int CountB = 0;
    for (int i = 0; i < 8; i ++)
    {
        for (int j = 0; j < 8; j++)
        {
            if (A[r+i][c+j] != Color) CountB ++;
            Color = Coloring_(Color);
        }
        Color = Coloring_(Color);
    }
    Color = 'W';
    int CountW = 0;
    for (int i = 0; i < 8; i ++)
    {
        for (int j = 0; j < 8; j++)
        {
            if (A[r+i][c+j] != Color) CountW ++;
            Color = Coloring_(Color);
        }
        Color = Coloring_(Color);
    }
    return min(CountB, CountW);
}

int main()
{
    int row, col;
    cin >> row >> col;
    char** arr = new char*[row];
    for(int i = 0; i < row; i++) 
    {
        arr[i] = new char[col];
    }

    for (int i = 0; i < row; i++)
    {
        string Row_;
        cin >> Row_;
        for (int j = 0; j < col; j++)
        {
            arr[i][j] = Row_[j];
        }
    }

    int CheckRow = row - 8;
    int CheckCol = col - 8;
    int Coloring = 64;
    for (int i = 0; i <= CheckRow; i++)
    {
        for (int j = 0; j <= CheckCol; j++)
        {
            Coloring = min(Coloring, HowManyColor(i, j, arr));
        }
    }

    cout << Coloring;
}