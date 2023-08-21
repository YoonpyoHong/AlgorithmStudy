#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
vector<vector<int>> tree;
bool visited[1000001];
bool early[1000001];
int cnt = 0;

void dfs(int curr) {
	visited[curr] = true;
	bool checker = false;
	bool leaf = true;
	for (int i = 0; i < tree[curr].size(); i++) {
		int next = tree[curr][i];
		if (!visited[next]) {
			dfs(next);
			leaf = false;
			if (!early[next]) {
				checker = true;
			}
		}
	}
	if (leaf) {
		early[curr] = false;
		return;
	}
	if (checker) {
		early[curr] = true;
		cnt++;
	}
	else early[curr] = false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	tree.resize(N+1);

	for (int i = 0; i < N - 1; i++) {
		int x, y;
		cin >> x >> y;
		tree[x].push_back(y);
		tree[y].push_back(x);
	}
	dfs(1);
	cout << cnt;
}