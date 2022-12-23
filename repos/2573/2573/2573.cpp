#include <iostream>
#include <queue>


using namespace std;

int N, M;
int ice[300][300];
int ice_tmp[300][300];
int visited[300][300];
int	water[300][300];
int year = 0;
int pos_x[4] = { 1, -1, 0, 0 };
int pos_y[4] = {0, 0, 1, -1};
bool check();
void search(int row, int col);
void inputData();
void melt();
void clear();

int main() {
	inputData();
	while (!check()) {
		melt();
	}
	cout << year;
}

void inputData() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> ice[i][j];
		}
	}
}

bool check() {
	bool breakChecker= false;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (ice[i][j] != 0) {
				if (visited[i][j] == 0) {
					if (breakChecker == true) {
						return true;
					}
					else {
						visited[i][j] = 1;
						search(i, j);
						breakChecker = true;
					}
				}
			}
		}
	}
	clear();
	if (breakChecker == true) {
		return false;
	}
	else {
		year = 0;
		return true;
	}
}

void search(int row, int col) {
	for (int i = 0; i < 4; i++) {
		if (row +pos_x[i] <N && row+pos_x[i]>=0 && col + pos_y[i] < M && col + pos_y[i] >= 0) {
			if (ice[row + pos_x[i]][col + pos_y[i]] != 0 && visited[row + pos_x[i]][col + pos_y[i]] == 0) {
				visited[row + pos_x[i]][col + pos_y[i]] = 1;
				search(row + pos_x[i], col + pos_y[i]);
			}
		}
	}
}

void clear() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = 0;
		}
	}
}

void melt() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			water[i][j] = 0;
			if (ice[i][j] == 0) {
				continue;
			}
			for (int k = 0; k < 4; k++) {
				if (i + pos_x[k] < N && i+ pos_x[k] >= 0 && j + pos_y[k] < M && j + pos_y[k] >= 0) {
					if (ice[i + pos_x[k]][j + pos_y[k]] == 0) {
						water[i][j]++;
					}
				}
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (water[i][j] >= ice[i][j]) {
				ice[i][j] = 0;
			}
			else {
				ice[i][j] -= water[i][j];
			}
			//cout << ice[i][j];
		}
		//cout << "\n";
	}
	year++;
}