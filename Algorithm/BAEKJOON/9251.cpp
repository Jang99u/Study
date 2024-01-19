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

    cout << LCS[str1.size()][str2.size()];
}