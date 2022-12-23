#include<iostream>
using namespace std;

int knapsack[100001][100];
int N, K;
int V, W;

int main() {
	cin >> N >> K;
	cin >> W >> V;
	for (int j = W; j <= K; j++) {
		knapsack[j][0] = V;
	}
	for (int i = 1; i < N; i++) {
		cin >> W >> V;
		
		for (int j = 0; j < W; j++) {
			knapsack[j][i] = knapsack[j][i-1];
		}
		for (int j = W; j <= K; j++) {
			knapsack[j][i] = max(knapsack[j][i - 1], knapsack[j - W][i - 1] + V);
		}
	}

	cout << knapsack[K][N-1];
	
}