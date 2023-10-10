#include <iostream>
#include <cmath>
using namespace std;

double x, y;
double z;
int result = -1;


int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	cin >> x >> y;
	z = (y * 100) / x;
	z = floor(z);

	int low = 1;
	int high = 1000000000;

	while (low <= high) {
		int mid = (low + high) / 2; // 범위 ㄱㅊ
		double val = (double)((y + mid) * 100) / (x + mid);
		val = floor(val);
		if (val > z) {
			result = mid;
			high = mid - 1;
		}
		if (val <= z) {
			low = mid + 1;
		}
	}


	cout << result << endl;

	return 0;
}