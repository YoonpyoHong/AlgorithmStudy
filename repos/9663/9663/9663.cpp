#include <iostream>

using namespace std;

int N, cnt;
int chess[15][15][15];
int chessChk(int stage);
int directR[8] = {-1,-1,-1,0,0,1,1,1};
int directC[8] = {1,0,-1,1,-1,1,0,-1};
void clear(int stage);
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N;
	

	cout << chessChk(N-1);
}

int chessChk(int stage) {
	int cnt = 0;
	if (stage == 0) {
		for (int i = 0; i < N; i++) {
			if (chess[stage][stage][i] == 0) {
				cnt++;
			}
		}
		return cnt;
	}
	else {
		int posR = 0;
		int posC = 0;
		for (int i = 0; i < N; i++) {
			if (chess[stage][stage][i] == 0) {
				clear(stage);
				chess[stage - 1][stage][i] = -1;
				for (int k = 0; k < 8; k++) {
					posR =	stage  + directR[k];
					posC = i + directC[k];
					while (posR < N && posR >= 0 && posC < N && posC >= 0) {
						chess[stage - 1][posR][posC] = -1;
						posR += directR[k];
						posC += directC[k];
					}
				}
				cnt += chessChk(stage - 1);
			}
		}
		return cnt;
	}
}

void clear(int stage ) {
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			chess[stage - 1][r][c] = chess[stage][r][c];
		}
	}
}


