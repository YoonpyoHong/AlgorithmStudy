#include <iostream>
#include <cmath>

using namespace std;

int T;
long x, y;
void teleport();
bool checker(long mid, long range);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> x >> y;
		teleport();
	}
}

void teleport() {
	long long range = y-x;
	long long cnt;

	cnt = sqrt(range);
	if (range <= cnt * cnt) {
		cout << 2 * cnt -1 << "\n";
	}
	else if (range <= cnt * (cnt+1)) {
		cout << 2 * cnt << "\n";
	}
	else {
		cout << 2 * cnt +1<< "\n";
	}
	

	
}

