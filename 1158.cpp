#include <iostream>
using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    short* arr = new short[N*N];
    bool* visited = new bool[N];
    short* result = new short[N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            arr[(i*N)+j] = (j+1);
        }
        visited[i] = false;
        result[i] = 0;
    }

    int num = -1;
    int count = 0;
    int append = 0;
    bool valid;

    while (1) 
    {
        valid = true;
        for (int i = 0; i < N*N; i++)
        {
            num += 1;
            if(visited[num%N] == true) continue;

            count += 1;
            if(count == M)
            {
                count = 0;
                visited[num%N] = true;
                result[append++] = arr[num%N];
            }
        }

        for (int i = 0; i < N; i++)
        {
            if (visited[i] == false)
            {
                valid = false;
                break;
            }
        }
        if (valid == true) break;
    }

    cout << "<";
    for (int i = 0; i < N; i++)
    {
        if (i+1 == N)
        {
            cout << result[i];
            break;
        }
        cout << result[i] << ", ";
    }
    cout << ">";
}