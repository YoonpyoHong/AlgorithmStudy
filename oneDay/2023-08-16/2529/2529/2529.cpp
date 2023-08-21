#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

int k;
char comparison[9];
vector<long long> numberVec;

long long makeNumber(vector<int> number) {
	long long result = 0;
	for (int i = 0; i <= k; i++) {
		result = result * 10 + number[i];
	}
	return result;
}

void permutation(vector<int> number, vector<bool> visited, int idx) {
	if (idx == k+1) {
		numberVec.push_back(makeNumber(number));
		return;
	}

	for (int i = 0; i <= 9; i++) {
		if (!visited[i]) {
			visited[i] = true;
			vector<int> newNumber = number;
			newNumber.push_back(i);
			if (idx == 0) {
				permutation(newNumber, visited, idx + 1);
			}
			else if (comparison[idx - 1] == '<' && number[idx-1] < i) {
				permutation(newNumber, visited, idx + 1);
			}
			else if(comparison[idx-1] == '>' && number[idx-1] > i) {
				permutation(newNumber, visited, idx + 1);
			}
			visited[i] = false;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> k;
	for (int i = 0; i < k; i++) {
		cin >> comparison[i];
	}

	vector<bool> visited;
	vector<int> number;

	for (int i = 0; i <= 9; i++) {
		visited.push_back(false);
	}

	permutation(number, visited, 0);

	long long maxNum = *max_element(numberVec.begin(), numberVec.end());
	long long minNum = *min_element(numberVec.begin(), numberVec.end());
	if (maxNum < pow(10, k)) {
		cout << 0;
	}
	cout << maxNum << "\n";



	if (minNum < pow(10, k)) {
		cout << 0;
	}
	cout << minNum;
}