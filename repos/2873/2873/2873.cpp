#include <iostream>
#include <string>

using namespace std;

int R, C;
int ground[1000][1000];
struct point {
	int num =1000;
	int row;
	int col;
};
point minPoint;
void search();

int main() {
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> ground[i][j];
		}
	}

	if (R % 2 == 0 && C % 2 == 0) {
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if ((i + j) % 2 == 1) {
					if (ground[i][j] < minPoint.num) {
						minPoint.num =ground[i][j];
						minPoint.row = i;
						minPoint.col = j;
					}
				}
			}
		}

		search();

	}
	else if (R % 2 != 0) {
		for (int i = 0; i < R-1; i++) {
			for (int j = 0; j < C - 1; j++) {
				if (i % 2 == 0) {
					cout << 'R';
				}
				else {
					cout << 'L';
				}
			}
			cout << 'D';
		}
		for (int j = 0; j < C - 1; j++) {
			cout << 'R';
		}
	}
	else {
		for (int i = 0; i < C-1 ; i++) {
			for (int j = 0; j < R - 1; j++) {
				if (i % 2 == 0) {
					cout << 'D';
				}
				else {
					cout << 'U';
				}
			}
			cout << 'R';
		}
		for (int j = 0; j < R - 1; j++) {
			cout << 'D';
		}
	}
}

void search() {
	bool pivot = false;
	for (int i = 0; i < R/2; i++) {
		if (minPoint.row / 2 != i) {
			if (pivot == false) {
				for (int j = 0; j < C - 1; j++) {
					cout << 'R';
				}
				cout << 'D';
				for (int j = 0; j < C - 1; j++) {
					cout << 'L';
				}
			}
			else {
				for (int j = 0; j < C - 1; j++) {
					cout << 'L';
				}
				cout << 'D';
				for (int j = 0; j < C - 1; j++) {
					cout << 'R';
				}
			}
		}
		else {
			for (int j = 0; j < C / 2; j++) {
				if (j != minPoint.col / 2) {
					if (pivot == false) {
						cout << "DRUR";
					}
					else {
						cout << "RURD";
					}
				}
				else {
					if (minPoint.row % 2 == 1) {
						cout << "RD";
					}
					else {
						cout << "DR";
					}
					pivot = true;
				}
			}
		}

		if (i != R / 2-1) {
			cout << 'D';
		}
	}
}
