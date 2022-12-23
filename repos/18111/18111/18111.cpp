#include <iostream>

using namespace std;

int N, M;
long B;
int ground[500][500];
long result=1000000000;
int resultGround = 0;
void search();

int main() {
	cin >> N >> M >> B;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> ground[i][j];
		}
	}
	search();

	
	cout << result << " " << resultGround;
}

void search() {
	int sum = 0;
	long Btmp;
	for (int k = 0; k <= 256; k++) {
		sum = 0;
		Btmp = B;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (k > ground[i][j]) {
					sum += k - ground[i][j];
					Btmp-=(k-ground[i][j]);
				}
				else {
					sum += 2 * (ground[i][j] - k);
					Btmp+=(ground[i][j]-k);
				}
			}
			
		}
		if (Btmp < 0) {
			return;
		}
		if (result >= sum) {
			result = sum;
			resultGround = k;
		}
	}
}
