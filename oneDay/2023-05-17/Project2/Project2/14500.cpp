#include <iostream>
#include <vector>

#define MAX_RESULT 4000
using namespace std;

int N, M;

int paper[500][500];
bool visited[500][500];
int dirR[3] = { 0,0,1 };
int dirC[3] = { 1,-1,0 };


void init() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = true;
		}
	}
}

int find_blocks(int row,int col, int cnt,int result) {
	
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M;
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < M; c++) {
			cin >> paper[r][c];
		}
	}

}