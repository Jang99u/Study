#include <iostream>
#include <string>
using namespace std;

int LCS[1001][1001];
int main()
{
    string str1, str2;
    cin >> str1 >> str2;

    for (int i = 1; i <= str1.size(); i++)
    {
        for (int j = 1; j <= str2.size(); j++)
        {
            if (str1[i-1] != str2[j-1]) LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]);
            else LCS[i][j] = LCS[i-1][j-1] + 1;
        }
    }
    int result = LCS[str1.size()][str2.size()];
    cout << result << endl;

    int r = str1.size();
    int c = str2.size();
    int index = 0;
    char* LCS_ = new char[result];

    while (LCS[r][c] != 0)
    {
        if (LCS[r-1][c] == LCS[r][c]) r -= 1;
        else if (LCS[r][c-1] == LCS[r][c]) c -= 1;
        else
        {
            LCS_[index++] = str1[r-1];
            r -= 1;
            c -= 1;
        }
    }

    for (int i = result-1; i >= 0; i--)
    {
        cout << LCS_[i];
    }
    delete[] LCS_;
}