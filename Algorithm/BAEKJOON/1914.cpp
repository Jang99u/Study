#include <iostream>
#include <cmath>
#include <string>
using namespace std;

void move(int n, int a, int b, int c)
{
    if(n == 1)
    {
        cout << a << " " << c << '\n';
        return;
    }

    move(n-1, a, c, b);
    cout << a << " " << c << '\n';
    move(n-1, b, a, c);
}

int main()
{
    int n;
    cin >> n;
    string count = to_string(pow(2, n));

    for(int i = 0; ; i++)
    {
        if(count[i+1] == '.')
        {
            cout << int(count[i]) - 49;
            break;
        }
        else cout << count[i];
    }
    cout << '\n';
    if(n<=20) move(n, 1, 2, 3);

    return 0;
}