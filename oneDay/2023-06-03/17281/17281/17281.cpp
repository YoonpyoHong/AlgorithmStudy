#include<iostream>
#include <algorithm>

using namespace std;

int N;
int process[50][9];
int order[9];
int maxResult=0;
void findPoint();


void swap(int& a, int& b) {
	int temp = a;
	a = b;
	b = temp;
}

void init() {
	int idx = 1;
	order[3] = 0;
	for (int i = 0; i < 10; i++) {
		if (i == 3)
			continue;
		order[i] = idx++;
	}
}

void makeOrder(int now) {
	if (now == 9) {
		findPoint();
	}

	for (int i = now; i < 9; i++) {
		if (i == 3) {
			continue;
		}
		if (now == 3) {
			makeOrder(now + 1);
			break;
		}
		swap(order[now], order[i]);
		makeOrder(now + 1);
		swap(order[now], order[i]);
	}
}



void findPoint() {
	bool status[4] = {true,false, false, false};
	int outcnt = 0;
	int inning = 0;
	int playerIdx = 0;
	int player = order[playerIdx];
	int point = 0;
	while (inning < N) {
		while (outcnt < 3) {
			status[0] = true;
			int run = process[inning][player];
			if (run == 0) {
				outcnt++;
			}
			else {
				for (int i = 3; i >=0 ; i--) {
					if (status[i]) {
						if (i+run > 3) {
							point++;
						}
						else {
							status[i + run] = true;
						}
						status[i] = false;
					}
				}
			}
			playerIdx = (playerIdx + 1) % 9;
			player = order[playerIdx];
		}
		for (int i = 0; i < 4; i++) {
			status[i] = false;
		}
		inning++;
		outcnt = 0;
	}
	maxResult = max(maxResult, point);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> process[i][j];
		}
	}
	init();
	makeOrder(0);
	cout << maxResult;
}