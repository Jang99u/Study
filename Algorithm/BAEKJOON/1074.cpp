#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int N, r, c;
    int Start_Xvals = 0, Start_Yvals = 0;
    unsigned int Start_Num = 0;

    cin >> N >> r >> c;

    for (int i = N; i != 1;i--)
    {
        int group;
        int check_group = pow(2, (i-1));
        int check_r = Start_Yvals + check_group;
        int check_c = Start_Xvals + check_group;
        unsigned int TotalSize = pow(2, i) * pow(2, i);

        if (r < check_r && c < check_c) group = 1;
        else if (r < check_r && c >= check_c) group = 2;
        else if (r >= check_r && c < check_c) group = 3;
        else if (r >= check_r && c >= check_c) group = 4;

        switch (group)
        {
        case 1:
            break;
        
        case 2:
            Start_Xvals += check_group;
            Start_Num += TotalSize / 4;
            break;
            
        case 3:
            Start_Yvals += check_group;
            Start_Num += (TotalSize * 2) / 4;
            break;

        case 4:
            Start_Xvals += check_group;
            Start_Yvals += check_group;
            Start_Num += (TotalSize * 3) / 4;
            break;
        }     
    }

    int Sequence = 0;
    if (r == Start_Yvals && c == Start_Xvals) Sequence = 0;
    else if (r == Start_Yvals && c != Start_Xvals) Sequence = 1;
    else if (r != Start_Yvals && c == Start_Xvals) Sequence = 2;
    else if (r != Start_Yvals && c != Start_Xvals) Sequence = 3;

    unsigned int result = Start_Num + Sequence;
    cout << result;
}