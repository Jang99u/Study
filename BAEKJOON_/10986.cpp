#include <iostream>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    long long* A = new long long[N];
    long long* Stack = new long long[M];
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
    }
    for (int i = 0; i < N; i++)
    {
        A[i] = A[i] % M;
    }
    for (int i = 0; i < M; i++)
    {
        Stack[i] = 0;
    }

    long long N_ = 0;
    for (int i = 0; i < N; i++)
    {
        N_ += A[i];
        if (N_ >= M) 
        {
            N_ = N_ % M;
        }
        Stack[N_] += 1;
    }
    long long result = 0;
    for (int i = 0; i < M; i++)
    {
        if (i >= 1)
        { 
            Stack[i] -= 1;
        }
        if (Stack[i] >= 1)
        {
            for (int j = 1; j <= Stack[i]; j++)
            {
                result += j;
            }
        }
    }
    cout << result;    
}