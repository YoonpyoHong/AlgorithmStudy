#include <iostream>
#include <vector>

using namespace std;

int T;
int DP[1001][4][3];
int N;
int dirR[4] = { 0,0,1,-1 };
int dirC[4] = { 1,-1,0,0 };


int sum_dp(int length) {
	int result = 0;
	for (int r = 0; r < 4; r++) {
		for (int c = 0; c < 3; c++) {
			if (!((r == 3 && c == 1) || (r == 3 && c == 2)))
				result += DP[length][r][c];
				result %= 1234567;
		}
	}
	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> T;
	for (int r = 0; r < 4; r++) {
		for (int c = 0; c < 3; c++) {
			if(!(r == 3 && c==1) && !(r == 3 && c == 2))
				DP[1][r][c] = 1;
		}
	}
	
	for (int i = 1; i < 1000; i++) {
		for (int r = 0; r < 4; r++) {
			for (int c = 0; c < 3; c++) {
				if (!(r == 3 && c == 1) && !(r == 3 && c == 2)) {
					for (int j = 0; j < 4; j++) {
						int newR = r + dirR[j];
						int newC = c + dirC[j];
						if (newR < 4 && newR >= 0 && newC < 3 && newC >= 0 && !(newR == 3 && newC == 1) && !(newR == 3 && newC == 2)) {
							DP[i + 1][newR][newC] += DP[i][r][c];
							DP[i + 1][newR][newC] %= 1234567;
						}
					}
				}
			}
		}
	}

	for (int i = 0; i < T; i++) {
		cin >> N;
		cout << sum_dp(N)<<"\n";
	}
}