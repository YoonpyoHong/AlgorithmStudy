#include <iostream>
#include <algorithm>

using namespace std;

int needs , city;
int cost[1001];
pair<int,int> cities[20];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> needs >> city;
	for (int i = 1; i <= needs; i++) {
		cost[i] = 200000;
	}
	for (int i = 0; i < city; i++) {
		cin >> cities[i].first >> cities[i].second;
	}
	for (int i = 0; i < needs; i++) {
		for (int j = 0; j < city; j++) {
			int cityCost = cities[j].first;
			int cityValue = cities[j].second;
			int tmp = i + cityValue;
			if (tmp > needs) {
				tmp = needs;
			}
			cost[tmp] = min(cost[tmp], cost[i] + cityCost);
		}

	}
	cout << cost[needs];
}