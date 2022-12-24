#include <iostream>
#include <queue>

using namespace std;

pair<int, int> current;
void dijkstra();
void inputData();
void init();
int a[1001][1001];
int dist[1001];
int city, bus, start, finish, tmp1, tmp2 , cost;
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > pq;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	init();
	inputData();
	dijkstra();
	cout << dist[finish];
}

void init() {
	for (int i = 1; i <= 1000; i++) {
		for (int j = 1; j <= 1000; j++) {
			a[i][j] = 0x4f4f4f4f;
		}
	}
	for (int i = 1; i <= 1000; i++) {
		dist[i] = 0x4f4f4f4f;
	}
}

void inputData() {
	cin >> city >> bus;
	for (int i = 0; i < bus; i++) {
		cin >> tmp1 >> tmp2 >> cost ;

		if (a[tmp1][tmp2] > cost) {
			a[tmp1][tmp2] = cost;
		}
	}
	cin >> start >> finish;
}

void dijkstra() {
	dist[start] = 0;
	pq.push(make_pair(0, start));
	while (!pq.empty()) {
		current =  pq.top();
		pq.pop();
		if (current.first > dist[current.second]) {
			continue;
		}
		for (int i = 1; i <= city; i++) {
			if (dist[i] > a[current.second][i] + current.first) {	
				dist[i] = a[current.second][i] + current.first;
				pq.push(make_pair(dist[i], i));
			}
		}
	}
}