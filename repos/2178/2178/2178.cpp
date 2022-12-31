#include <iostream>
#include <string>
#include <queue>
using namespace std;

int N, M;
string maze[100];
int visited[100][100];
int directR[4] = {-1, 1, 0,0};
int directC[4] = {0, 0, -1,1};
struct node {
	int r;
	int c;
	int cnt;
};

queue<node> nodeList;

int BFS();
void inputData();


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	inputData();
	cout << BFS();
}

void inputData() {
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> maze[i];
	}
}

int BFS() {
	node current;
	node next;
	node start = { 0,0,1 };
	nodeList.push(start);
	visited[start.r][start.c] = -1;
	while (!nodeList.empty()) {
		current = nodeList.front();
		nodeList.pop();
		for (int i = 0; i < 4; i++) {
			next = { current.r + directR[i], current.c + directC[i], current.cnt + 1 };
			if (next.r == N - 1 && next.c == M - 1) return next.cnt;
			if (next.r >= 0 && next.r < N && next.c >= 0 && next.c < M) {
				if (visited[next.r][next.c] != -1) {
					if (maze[next.r][next.c] == '1') {
						nodeList.push(next);
						visited[next.r][next.c] = -1;
					}
				}
			}
		}
	}
	return next.cnt;
}
