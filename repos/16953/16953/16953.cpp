#include <iostream>

using namespace std;

int A, B;

int main() {
	cin >> A >> B;
	int cnt = 1;
	while (A != B) {
		if (B % 2 == 0) {
			B = B / 2;
			cnt++;
		}
		else {
			if (B % 10 == 1) {
				B = (B - 1) / 10;
				cnt++;
			}
			else {
				cnt = -1;
				break;
			}
		}
		if (A > B) {
			cnt = -1;
			break;
		}
	}
	cout << cnt;
}