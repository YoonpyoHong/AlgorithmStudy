#include <iostream>
#include <queue>
using namespace std;

int N, M, K;
int trash[101][101];
bool visited[101][101];
int dirR[4] = { 0,0,1,-1 };
int dirC[4] = { 1,-1,0,0 };

void init() {
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			visited[r][c] = false;
			trash[r][c] = 0;
		}
	}
}


int bfs(int row ,int col) {
	int newRow, newCol, cnt = 1;
	queue<pair<int, int>> q;
	q.push({ row, col });
	while (!q.empty()) {
		int row = q.front().first;
		int col = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			newRow = row + dirR[i];
			newCol = col + dirC[i];
			if (newRow <= N && newCol <= M && newRow >= 1 && newCol >= 1 && trash[newRow][newCol] == 1 && !visited[newRow][newCol] ) {
				cnt += 1;
				q.push({ newRow, newCol });
				visited[newRow][newCol] = true;
			}
		}
	}
	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int result = 0;
	cin >> N >> M >> K;
	init();
	for (int i = 0; i < K; i++) {
		int row, col;
		cin >> row >> col;
		trash[row][col] = 1;
	}

	for (int r = 1; r <= N; r++) {
		for (int c = 1; c <= M; c++) {
			if (trash[r][c] == 1 && visited[r][c] == false) {
				visited[r][c] = true;
				result = max(result, bfs(r, c));
			}
		}
	}
	cout << result;
	
}