#include <iostream>

using namespace std;

int maze[1001][1001];
int searchArr[1001][1001];
int N, M;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= M; j++) {
			cin >> maze[i][j];
			maze[i][j] = maze[i][j] + max(maze[i - 1][j], maze[i][j - 1]);
		}
	}

	
	cout << maze[N][M];
}
