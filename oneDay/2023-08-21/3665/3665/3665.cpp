#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int T, n, m;
vector<vector<int>> outbound;
vector<int> inbound;
int graph[501][501];

void init() {
	int n = 0;
	int m = 0;
	for (int i = 0; i <= 500; i++) {
		for (int j = 0; j <= 500; j++) {
			graph[i][j] = 0;
		}
	}
	outbound.clear();
	vector<int> tmp;
	outbound.push_back(tmp);
	inbound.clear();
	inbound.push_back(0);
}

void inputData() {
	cin >> n;
	vector<int> score;
	score.push_back(0);
	for (int i = 1; i <= n; i++) {
		int teamNum;
		cin >> teamNum;
		score.push_back(teamNum);
		inbound.push_back(0);
		vector<int> tmp;
		outbound.push_back(tmp);
		for (int j = 1; j < i; j++) {
			graph[teamNum][score[j]] = 1;
		}
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		if (graph[x][y] == 1) {
			graph[x][y] = 0;
			graph[y][x] = 1;
		}
		else {
			graph[x][y] = 1;
			graph[y][x] = 0;
		}
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (graph[i][j] == 1) {
				inbound[j]++;
				outbound[i].push_back(j);
			}
		}
	}
}

void topologic() {
	int score = n;
	queue<int> q;
	vector<int> result;
	for (int i = 1; i <= n; i++) {
		if (inbound[i] == 0) {
			q.push(i);
		}
	}
	while (score != 0) {
		if (q.empty()) {
			cout << "IMPOSSIBLE\n";
			return;
		}
		if (q.size() > 1) {
			cout << "?\n";
			return;
		}
		int curr = q.front();
		q.pop();
		result.push_back(curr);
		score--;
		for (int i = 0; i < outbound[curr].size(); i++) {
			int outboundLine = outbound[curr][i];
			inbound[outboundLine]--;
			if (inbound[outboundLine] == 0) {
				q.push(outboundLine);
			}
		}
	}

	for (int i = n-1; i >= 0; i--) {
		cout << result[i] << " ";
	}
	cout << "\n";
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int i = 0; i < T; i++) {
		init();
		inputData();
		topologic();
	}
}