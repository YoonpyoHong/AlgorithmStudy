#include <iostream>

using namespace std;

int bee[700][700];
int growth[1400];
int M, N;
int zero, one, two;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> M >> N;
	for (int r = 0; r < M; r++) {
		for (int c = 0; c < M; c++) {
			bee[r][c] = 1;
		}
	}
	for (int i = 0; i < 2*M; i++) {
		growth[i] = 0;
	}
	for (int day = 0; day < N; day++) {
		cin >> zero >> one >> two;
		for (int i = 0; i < 2 * M - 1; i++) {
			if (i < zero) {
				
			}
			else if(i < one+zero) {
				growth[i] += 1;
			}
			else {
				growth[i] += 2;
			}
		}
		
	}

	for (int r = 0; r < M; r++) {
		bee[r][0] += growth[M-r-1];
	}

	for (int r = 0; r < M; r++) {
		for (int c = 1; c < M; c++) {
			bee[r][c] += growth[M+c-1];
		}
	}

	for (int r = 0; r < M; r++) {
		for (int c = 0; c < M; c++) {
			cout << bee[r][c] << " ";
		}
		cout << "\n";
	}
}