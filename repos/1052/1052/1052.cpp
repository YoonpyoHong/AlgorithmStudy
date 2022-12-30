#include <iostream>
#include <cmath>

using namespace std;

int N, K, buy;
bool checkPro();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N >> K;

	int mustBuy = 1;
	while (N > K) {
		if (checkPro()) {
			break;
		}

		if (N % 2 == 0) {
			N = N / 2;
		}
		else {
			N = (N + 1) / 2;
			buy+= mustBuy ;
		}
		mustBuy *= 2;
	}
	cout << buy;
}

bool checkPro() {
	int quan=0;
	int tmp = N;
	while (tmp != 1) {
		if (tmp % 2 == 0) {
			tmp = tmp / 2;
		}
		else {
			tmp = tmp / 2;
			quan++;
		}
	}
	if (quan + 1<=K) {
		return true;
	}
	else {
		return false;
	}
}