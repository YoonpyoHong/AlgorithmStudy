#include <iostream>
#include <queue>

using namespace std;

bool num[10000];
bool visited[10000];

int fixNum(int src, int check) {
	return src - ((src / check) % 10) * check;
}

void init() {
	for (int i = 1; i < 10000; i++) {
		visited[i] = false;
	}
}


int change(int src, int dst) {
	int idx = 0;
	queue<pair<int,int>> q;
	q.push({ src, 0 });
	while (!q.empty()) {
		src = q.front().first;
		idx = q.front().second;
		if (src == dst) {
			break;
		}
		q.pop();
		for (int i = 0; i < 10; i++) {
			int newsrc = 0;
			if (i != 0) {
				newsrc = fixNum(src, 1000) + 1000 * i;
				if (!num[newsrc] && !visited[newsrc]) {
					visited[newsrc] = true;
					q.push({ newsrc, idx + 1 });
				}
			}
			newsrc = fixNum(src, 100) + 100 * i;
			if (!num[newsrc] && !visited[newsrc]) {
				visited[newsrc] = true;
				q.push({ newsrc, idx + 1 });
			}
			newsrc = fixNum(src, 10) + 10 * i;
			if (!num[newsrc] && !visited[newsrc]) {
				visited[newsrc] = true;
				q.push({ newsrc, idx + 1 });
			}
			newsrc = fixNum(src, 1) + 1 * i;
			if (!num[newsrc] && !visited[newsrc]) {
				visited[newsrc] = true;
				q.push({ newsrc, idx + 1 });
			}
		}
	}
	if (src == dst) {
		return idx;
	}
	else {
		return -1;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	for (int i = 2; i < 10000; i++) {
		if (num[i] == false) {
			int delnum = 2 * i;
			while (delnum < 10000) {
				num[delnum] = true;
				delnum += i;
			}
		}
	}

	int T = 0;
	cin >> T;
	for (int k = 0; k < T; k++) {
		int src, dst;
		init();
		cin >> src >> dst;
		visited[src] = true;
		cout << change(src, dst) << "\n";
	}

}