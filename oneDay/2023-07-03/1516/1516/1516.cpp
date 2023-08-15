#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> tech[501];
int contime[501];
int finaltime[501];
int T;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	queue<int> q;

	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> contime[i];
		finaltime[i] = 0;
		while (true) {
			int route;
			cin >> route;
			if (route == -1) {
				break;
			}
			tech[i].push_back(route);
		}
		if (tech[i].empty()) {
			finaltime[i] = contime[i];
			q.push(i);
		}
	}
	while (!q.empty()) {
		int currpos = q.front();
		int currtime = finaltime[currpos];
		q.pop();
		for (int i = 1; i <= T; i++) {
			vector<int>::iterator curr;
			if (tech[i].empty()) continue;
			for (curr = tech[i].begin(); curr != tech[i].end();) {
				if (*curr == currpos) {
					finaltime[i] = max(currtime + contime[i], finaltime[i]);
					curr = tech[i].erase(curr);
				}
				else {
					curr++;
				}
			}
			if (tech[i].empty()) {
				q.push(i);
			}
		}
	}
	for (int i = 1; i <= T; i++) {
		cout << finaltime[i] << "\n";
	}
	
}