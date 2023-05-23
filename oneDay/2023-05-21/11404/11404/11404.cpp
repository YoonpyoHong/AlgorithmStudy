#include <iostream>

using namespace std;


#define INF 100000000
int n, m;
int roads[101][101];

void init() {
	for (int r = 1; r <= n; r++) {
		for (int c = 1; c <= n; c++) {
			roads[r][c] = INF;
		}
		
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	cin >> m;
	init();
	for (int i = 0; i < m; i++) {
		int row, col, cost;
		cin >> row >> col >> cost;
		if (roads[row][col] < cost) {
			continue;
		}
		roads[row][col] = cost;
	}
	for (int city = 1; city <= n; city++) {
		for (int r = 1; r <= n; r++) {
			for (int c = 1; c <= n; c++) {
				if (r == city || c == city || r==c) {
					continue;
				}
				if (roads[r][city] + roads[city][c] < roads[r][c]) {
					roads[r][c] = roads[r][city] + roads[city][c];
				}
			}
		}
	}
	for (int r = 1; r <= n; r++) {
		for (int c = 1; c <= n; c++) {
			if (roads[r][c] == INF) {
				cout << 0 << " ";
			}
			else {
				cout << roads[r][c] << " ";
			}
		}
		cout << "\n";
	}
}