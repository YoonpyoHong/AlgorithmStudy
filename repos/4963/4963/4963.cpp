#include <iostream>
#include <queue>

using namespace std;

int w , h , island;
int direction_r[8] = {0, 0, 1, -1, 1,-1,1,-1};
int direction_c[8] = { 1,-1 ,0,0, 1,-1,-1,1 };
int visited[50][50];
int map[50][50];
queue<pair<int, int>> q;
void inputData();
void search();


int main() {
	while (true) {
		inputData();
		if (w == 0 && h == 0) break;
		search();
	}
}

void inputData() {
	cin >> w >> h;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			visited[i][j] = 0;
		}
	}
}

void search() {
	island = 0;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (map[i][j] == 1) {
				if (visited[i][j] == 0) {
					island++;
					q.push({ i,j });
					while (!q.empty()) {
						int row = q.front().first;
						int col = q.front().second;
						q.pop();
						for (int k = 0; k < 8; k++) {
							int changer = row + direction_r[k];
							int changec = col + direction_c[k];
							if (changer >= 0 && changer < h && changec >= 0 && changec < w) {
								if (map[changer][changec] == 1 && visited[changer][changec] == 0) {
									q.push({ changer, changec });
									visited[changer][changec] = -1;
								}
							}
						}
					}
				}
			}
		}
	}
	cout << island << "\n";
}