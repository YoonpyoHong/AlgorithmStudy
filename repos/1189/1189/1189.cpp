#include <iostream>
#include <string>

using namespace std;

int R, C, K;
string route[5];
void DFS(int row, int col,int cnt);

int visited[5][5];
int cntRoute;
int directR[4] = {1,-1,0,0};
int directC[4] = { 0,0,1,-1 };

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	cin >> R >> C >> K;
	for (int i = 0; i < R; i++) {
		cin >> route[i];
	}

	visited[R - 1][0] = -1;
	DFS(R - 1, 0,1);
	cout << cntRoute;
}

void DFS(int row, int col,int cnt) {
	int newR, newC;
	if (cnt == K) {
		if (row == 0 && col == C - 1) {
			cntRoute++;
		}
		return;
	}
	for (int i = 0; i < 4; i++) {
		newR = row + directR[i];
		newC = col + directC[i];
		
		if (newR >= 0 && newR < R && newC >= 0 && newC < C) {
			if (visited[newR][newC] == 0 && route[newR][newC] == '.') {
				visited[newR][newC] = -1;
				DFS(newR, newC, cnt+1);
				visited[newR][newC] = 0;
			}
		}
	}
	
}