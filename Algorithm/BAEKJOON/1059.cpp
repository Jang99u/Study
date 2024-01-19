#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int section(int s, int e, int num)
{
    int bigger = (e - num) + 1;
    int lower = (num - s);

    return (lower * bigger) + (bigger - 1);
}

int main()
{
    int L, N, num;
    vector<int> S;

    cin >> L;
    for(int i = 0; i < L; i++)
    {
        cin >> num;
        S.push_back(num);
    }
    cin >> N;
    sort(S.begin(), S.end());

    int result = 0;
    int startnum, endnum;
    for(int i = 0; i < L; i++)
    {
        if(N == S[i]) break;
        else if(N < S[i])
        {
            if(i != 0)
            {
                startnum = S[i-1] + 1;
                endnum = S[i] - 1;
                result = section(startnum, endnum, N);
                break;
            }
            else
            {
                startnum = 1;
                endnum = S[i] - 1;
                result = section(startnum, endnum, N);
                break;
            }
        }
    }
    cout << result;
}