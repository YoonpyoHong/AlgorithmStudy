#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int quan = 1;
int num = 0;
int array[40320][8];

void permutation(int idx, vector<int> numVec, vector<bool> visited) {
	if (num == quan) {
		return;
	}
	if (idx == N) {
		for (int i = 0; i < N; i++) {
			cout << numVec[i] << " ";
		}
		cout << "\n";
		num += 1;
		return;
	}
	for (int i = 1; i <= N; i++) {
		if (!visited[i]) {
			visited[i] = true;
			vector<int> newVec = numVec;
			newVec.push_back(i);
			permutation(idx + 1, newVec, visited);
			visited[i] = false;
		}
	}

	
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> N;
	for (int i = 1; i <= N; i++) {
		quan *= i;
	}
	vector<int> numVec;
	vector<bool> visited;
	for (int i = 0; i <= N; i++) visited.push_back(false);
	int idx = 0;
	permutation(0, numVec, visited);
}