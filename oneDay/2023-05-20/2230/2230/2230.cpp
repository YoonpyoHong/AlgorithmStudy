#include <iostream>
#include <algorithm>

using namespace std;

int N, M;
int A[100000];
int first, second;
long long largest = 2000000000;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	sort(A, A + N);
	long long current;
	first= 0;
	second = 1;
	int diffleft = 0, diffright = 0;
	while (second < N) {
		current = A[second] - A[first];
		if (current >= M) {
			largest = min(largest, current);
			first += 1;
		}
		else {
			second += 1;
		}
	}
	cout << largest;
}