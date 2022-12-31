#include <iostream>

using namespace std;


int C, N;
pair<int, int> costCustomer[20];
int minCost[1001];

int main() {

	cin >> C >> N;
	for (int i = 0; i < N; i++) {
		cin >> costCustomer[i].first >> costCustomer[i].second;
		
	}

	for (int i = 1; i <= C; i++) {
		minCost[i] = 200000;
	}
	
	int tmp = 0;
	for (int i = 0; i < C; i++) {
		for (int j = 0; j < N; j++) {
			int tmp = i + costCustomer[j].second;
			if (tmp > C) {
				tmp = C;
			}
			minCost[tmp] = min(minCost[tmp], minCost[i] + costCustomer[j].first);
		}
	}

	cout << minCost[C];
}