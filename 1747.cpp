#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int FindLen(int input)
{
    int len = 0;

    while(1)
    {
        if (input >= pow(10, len) && input < pow(10, (len + 1))) break;
        len += 1;
    }

    return len + 1;
}

int main()
{
    int input;
    int result;
    bool IsDecimal;
    bool IsPelindrome;
    cin >> input;

    for (int i = input; ;i++)
    {
        if (i == 1) continue;
        
        IsDecimal = true;
        IsPelindrome = true;

        for (int j = 1; j <= sqrt(i); j++)
        {
            if (j == 1) continue;
            if (i % j == 0)
            {
                IsDecimal = false;
                break;
            }
        }

        if (IsDecimal == true)
        {
            int len_input = FindLen(i);
            int* my_str = new int[len_input];
            int temp = i;

            for (int a = 0; a < len_input; a++)
            {
                int str_input = temp % 10;

                my_str[len_input - a - 1] = str_input;

                temp /= 10;
            }

            for (int a = 0; a <= len_input / 2; a++)
            {
                if (my_str[a] != my_str[len_input - a - 1])
                {
                    IsPelindrome = false;
                    break;
                }
            }
            delete[] my_str;
        }

        if (IsDecimal == true && IsPelindrome == true)
        {
            result = i;
            break;
        }
    } 

    cout << result;

    return 0;
}