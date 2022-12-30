#include <iostream>
#include <set>
using namespace std;

int num[100001];
set<int> prime;
int upcnt, A, B;

void primeSearch();
int upSearch();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> A >> B;
	primeSearch();
	cout << upSearch();
}

void primeSearch() {
	

	for (int i = 2; i <= B; i++) {
		if (num[i] == 0) {
			prime.insert(i);
			for (int j = 2*i; j <= B; j+=i) {
				num[j] = 1;
			}
		}
	}
}

int upSearch() {
	int cnt;
	int tmp;
	for (int i = A; i <= B; i++) {
		cnt = 0;
		tmp = i;
		for (auto itr = prime.begin(); itr != prime.end(); itr++) {
			while (tmp % (*itr) == 0) {
				tmp /= *itr;
				cnt++;
				
			}
			if (tmp == 1) {
				break;
			}
		}
		if (prime.find(cnt) != prime.end()) {
			upcnt++;
		}
	}
	return upcnt;
}