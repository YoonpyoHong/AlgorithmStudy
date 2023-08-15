#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N;
int result = 1000;
int population[11];
int* road[11];
bool visited[11];
void bfs(int* cities);


void input() {
	cin >> N;
	string line;
	getline(cin, line);
	for (int i = 1; i <= N; i++) {
		cin >> population[i];
	}
	for (int i = 1; i <= N; i++) {
		int cnt;
		cin >> cnt;
		int* city = (int*)malloc(sizeof(int) * (cnt+1));
		city[0] = cnt;
		for (int j = 1; j <= cnt; j++) {
			cin >> city[j];
		}
		road[i] = city;
	}
}

void init() {
	for (int i = 1; i <= 10; i++) {
		population[i] = 0;
	}
}

void dfs(int city, int* cities) {
	if (city > N) {
		bfs(cities);
		return;
	}
	cities[city] = 1;
	dfs(city + 1, cities);
	cities[city] = 2;
	dfs(city + 1, cities);
}

void bfs(int* cities) {
	queue<int> q;
	int sector = cities[1];
	int pop1 = 0;
	int pop2 = 0;
	for (int i = 1; i <= 10; i++) {
		visited[i] = false;
	}
	q.push(1);
	visited[1] = true;
	pop1 += population[1];
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		for (int i = 1; i <= road[now][0]; i++) {
			int next = road[now][i];
			if (cities[next] == sector && !visited[next]) {
				visited[next] = true;
				pop1 += population[next];
				q.push(next);
			}
		}
	}
	for (int i = 1; i <= N; i++) {
		if (!visited[i] && cities[i] != sector) {
			q.push(i);
			visited[i] = true;
			pop2 += population[i];
			sector = cities[i];
			break;
		}
	}
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		for (int i = 1; i <= road[now][0]; i++) {
			int next = road[now][i];
			if (cities[next] == sector && !visited[next]) {
				visited[next] = true;
				pop2 += population[next];
				q.push(next);
			}
		}
	}
	for (int i = 1; i <= N; i++) {
		if (!visited[i]) {
			return;
		}
	}
	int value = pop1 > pop2 ? pop1 - pop2 : pop2 - pop1;
	result = min(result,value);
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	init();
	input();
	int* cities = (int*)malloc(sizeof(int) * (N + 1));
	dfs(1, cities);
	if (result == 1000) {
		cout << -1;
	}
	else {
		cout << result;
	}
}#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N;
int result = 1000;
int population[11];
int* road[11];
bool visited[11];
void bfs(int* cities);


void input() {
	cin >> N;
	string line;
	getline(cin, line);
	for (int i = 1; i <= N; i++) {
		cin >> population[i];
	}
	for (int i = 1; i <= N; i++) {
		int cnt;
		cin >> cnt;
		int* city = (int*)malloc(sizeof(int) * (cnt+1));
		city[0] = cnt;
		for (int j = 1; j <= cnt; j++) {
			cin >> city[j];
		}
		road[i] = city;
	}
}

void init() {
	for (int i = 1; i <= 10; i++) {
		population[i] = 0;
	}
}

void dfs(int city, int* cities) {
	if (city > N) {
		bfs(cities);
		return;
	}
	cities[city] = 1;
	dfs(city + 1, cities);
	cities[city] = 2;
	dfs(city + 1, cities);
}

void bfs(int* cities) {
	queue<int> q;
	int sector = cities[1];
	int pop1 = 0;
	int pop2 = 0;
	for (int i = 1; i <= 10; i++) {
		visited[i] = false;
	}
	q.push(1);
	visited[1] = true;
	pop1 += population[1];
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		for (int i = 1; i <= road[now][0]; i++) {
			int next = road[now][i];
			if (cities[next] == sector && !visited[next]) {
				visited[next] = true;
				pop1 += population[next];
				q.push(next);
			}
		}
	}
	for (int i = 1; i <= N; i++) {
		if (!visited[i] && cities[i] != sector) {
			q.push(i);
			visited[i] = true;
			pop2 += population[i];
			sector = cities[i];
			break;
		}
	}
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		for (int i = 1; i <= road[now][0]; i++) {
			int next = road[now][i];
			if (cities[next] == sector && !visited[next]) {
				visited[next] = true;
				pop2 += population[next];
				q.push(next);
			}
		}
	}
	for (int i = 1; i <= N; i++) {
		if (!visited[i]) {
			return;
		}
	}
	int value = pop1 > pop2 ? pop1 - pop2 : pop2 - pop1;
	result = min(result,value);
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	init();
	input();
	int* cities = (int*)malloc(sizeof(int) * (N + 1));
	dfs(1, cities);
	if (result == 1000) {
		cout << -1;
	}
	else {
		cout << result;
	}
}