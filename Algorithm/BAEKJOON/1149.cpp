#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int N, R, G, B;
    int rgb[1000][3];
    int dp[1000][3];

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> R >> G >> B;
        rgb[i][0] = R;
        rgb[i][1] = G;
        rgb[i][2] = B;
    }
    for (int i = 0; i < N; i++)
    {
        if (i == 0)
        {
            dp[i][0] = rgb[i][0];
            dp[i][1] = rgb[i][1];
            dp[i][2] = rgb[i][2];
        }
        else
        {
            dp[i][0] = min(dp[i-1][1] + rgb[i][0], dp[i-1][2] + rgb[i][0]);
            dp[i][1] = min(dp[i-1][0] + rgb[i][1], dp[i-1][2] + rgb[i][1]);
            dp[i][2] = min(dp[i-1][0] + rgb[i][2], dp[i-1][1] + rgb[i][2]);
        }
    }
    int result;
    result = min(dp[N-1][0], dp[N-1][1]);
    result = min(result, dp[N-1][2]);
    cout << result;
}