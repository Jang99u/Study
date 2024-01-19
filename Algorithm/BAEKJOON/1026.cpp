#include <iostream>
#include <algorithm>
#define INFINITE 500
using namespace std;

int findmax(int arr[], int size)
{
    int result = 0;
    for (int i = 1; i < size; i++)
    {
        if (arr[result] < arr[i])
        {
            result = i;
        }
    }
    return result;
}

int findmin(int arr[], int size)
{
    int result = 0;
    for (int i = 1; i < size; i++)
    {
        if (arr[result] > arr[i])
        {
            result = i;
        }
    }
    return result;
}

int main()
{
    int arr_size, num_input;
    char pass_input;
    cin >> arr_size;

    int* A;
    int* B;
    A = new int[arr_size];
    B = new int[arr_size];

    for(int i = 0; i < arr_size; i++)
    {
        cin >> num_input;
        A[i] = num_input;
    }
    for(int i = 0; i < arr_size; i++)
    {
        cin >> num_input;
        B[i] = num_input;
    }

    int result = 0;
    for(int i = 0; i < arr_size; i++)
    {
        int max_index = findmax(A, arr_size);
        int max_A = A[max_index];
        A[max_index] = 0;

        int min_index = findmin(B, arr_size);
        int min_B = B[min_index];
        B[min_index] = INFINITE;

        result += max_A * min_B;
    }
    cout << result;    
    return 0;
}