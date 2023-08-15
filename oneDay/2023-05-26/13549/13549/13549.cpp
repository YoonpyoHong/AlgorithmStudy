#include <iostream>
#include <queue>
using namespace std;

int N, K;
int visited[100001];

int bfs() {
	queue<pair<int, int>> q;
	q.push({N, 0});
	for (int i = 0; i <= 100000; i++) {
		visited[i] = 1000000;
	}
	visited[N] = true;
	while (!q.empty()) {
		int now = q.front().first;
		int time = q.front().second;
		if (now == K) {
			return time;
		}
		q.pop();
		if (now * 2 <= 100000 && visited[now*2]<time) {
			visited[now * 2] = true;
			q.push({ now * 2, time});
		}
		if (now + 1 <= 100000 && !visited[now +1]) {
			visited[now+1] = true;
			q.push({ now + 1, time + 1 });
		}
		if (now -1 >= 0 && !visited[now -1]) {
			visited[now -1] = true;
			q.push({ now - 1, time + 1 });
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> K;
	cout << bfs();
}