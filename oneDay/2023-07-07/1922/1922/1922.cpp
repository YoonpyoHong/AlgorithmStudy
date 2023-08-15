#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct road {
	int firstCity;
	int secondCity;
	int cost;
};


int N, M;
road connection[100000];
int computer[1001];




bool compare(road a, road b) {
	return a.cost < b.cost;
}

int findParent(int child) {
	if (computer[child] == child) {
		return child;
	}
	else {
		return findParent(computer[child]);
	}
}

void unionTwo(int a, int b) {
	int aParent = findParent(a);
	int bParent = findParent(b);
	if (aParent > bParent) {
		computer[aParent] = bParent;
	}
	else {
		computer[bParent] = aParent;
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int totalCost = 0;

	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int firstCity, secondCity, cost;
		cin >> firstCity >> secondCity >> cost;
		connection[i].firstCity = firstCity;
		connection[i].secondCity =secondCity;
		connection[i].cost = cost;
	}

	for (int i = 1; i <= N; i++) {
		computer[i] = i;
	}

	sort(connection, connection + M, compare);

	for (int i = 0; i < M; i++) {
		int firstCity, secondCity, cost;
		firstCity = connection[i].firstCity;
		secondCity = connection[i].secondCity;
		cost = connection[i].cost;

		if (findParent(firstCity) == findParent(secondCity)) {
			continue;
		}

		totalCost += cost;

		unionTwo(firstCity, secondCity);
	}
	cout << totalCost;
}