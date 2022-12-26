#include <iostream>
#include <set>
#include <vector>

using namespace std;

int N, M;
int start, finish, count, tmp;
vector<int> lecLen;

void bsearch();
void inputData();
bool check(int mid);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	inputData();
	bsearch();
}


void inputData() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> tmp;
		lecLen.push_back(tmp);
	}
}

void bsearch() {
	start = 0;
	finish = 100000000;
	
	int mid;
	while (finish-start !=1) {
		mid = (start + finish) / 2;
		if (check(mid)) {
			start = mid;
		}
		else {
			finish = mid;
		}
	}
	cout << finish;
}

bool check(int mid) {
	int suma = 0;
	int cnt = 1;
	int i = 0;
	while(i<lecLen.size()) {
		if (mid < lecLen[i]) {
			return true;
		}
		suma += lecLen[i];
		if (suma > mid) {
			cnt++;
			suma = 0;
		}
		else {
			i++;
		}
	}
	if (cnt > M) {
		return true;
	}
	else {
		return false;
	}
}
