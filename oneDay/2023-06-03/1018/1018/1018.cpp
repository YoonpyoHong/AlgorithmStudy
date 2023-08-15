#include <iostream>

using namespace std;

int R, C;
char startB[8][8];
char board[50][50];
int result = 65;

void makeex() {
	bool check = true;
	for (int r = 0; r < 8; r++) {
		for (int c = 0; c < 8; c++) {
			if (check) {
				startB[r][c] = 'B';
			}
			else {
				startB[r][c] = 'W';
			}
			check = !check;
		}
		check = !check;
	}
}

void compare(int row, int col) {
	int W = 0, B = 0;
	for (int r = 0; r < 8; r++) {
		for (int c = 0; c < 8; c++) {
			if (board[row + r][col + c] != startB[r][c]) {
				W++;
			}
			else {
				B++;
			}
		}
	}
	int compresult= min(W, B);
	result = min(compresult, result);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> R >> C;
	for (int r = 0; r < R; r++) {
		cin >> board[r];
	}
	makeex();
	for (int r = 0; r <= R - 8; r++) {
		for (int c = 0; c <= C - 8; c++) {
			compare(r, c);
		}
	}
	cout << result;
}