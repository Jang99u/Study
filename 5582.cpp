#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    string N, M;
    cin >> N >> M;
    vector<int> col;
    vector<vector<int>> LCS;

    for(int i = 0; i < N.length()+1; i++)
    {
        col.push_back(0);
    }
    for(int j = 0; j < M.length()+1; j++)
    {
        LCS.push_back(col);
    }
    for(int i = 1; i < M.length()+1; i++)
    {
        for(int j = 0; j < N.length()+1; j++)
        {
            if(M[i-1] == N[j-1]) LCS[i][j] = LCS[i-1][j-1] + 1;
        }
    }

    int num = 0;
    for(int i = 1; i < M.length()+1; i++)
    {
        for(int j = 0; j < N.length()+1; j++)
        {
            num = max(num, LCS[i][j]);
        }
    }
    cout << num;
}