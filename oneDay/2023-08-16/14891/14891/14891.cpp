#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int k;
int rail[5][8];
int rotateSeq[100][2];
int railLeft = 6;
int railRight = 2;


void rotateClock(int idx) {
	int newRail[8];
	newRail[0] = rail[idx][7];
	for (int i = 0; i < 7; i++) {
		newRail[i + 1] = rail[idx][i];
	}
	for (int i = 0; i < 8; i++) {
		rail[idx][i] = newRail[i];
	}
}

void rotateReverseClock(int idx) {
	int newRail[8];
	newRail[7] = rail[idx][0];
	for (int i = 0; i < 7; i++) {
		newRail[i] = rail[idx][i+1];
	}
	for (int i = 0; i < 8; i++) {
		rail[idx][i] = newRail[i];
	}
}

void change(int idx,int direction, bool inc) {
	if (inc) {
		if (rail[idx][railLeft] != rail[idx - 1][railRight]) {
			if (idx < 4) {
				change(idx + 1, -direction, true);
			}
			if (direction > 0) rotateClock(idx);
			else if (direction < 0) rotateReverseClock(idx);
		}
	}
	else {
		if (rail[idx][railRight] != rail[idx + 1][railLeft]) {
			if (idx > 1) {
				change(idx - 1, -direction, false);
			}
			if (direction > 0) rotateClock(idx);
			else if (direction < 0) rotateReverseClock(idx);
		}
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	for (int i = 1; i <= 4; i++) {
		int railNum;
		cin >> railNum;
		for (int j = 7; j >= 0; j--) {
			rail[i][j] = railNum % 10;
			railNum /= 10;
		}
	}

	cin >> k;
	for (int i = 0; i < k; i++) {
		int railNum, direction;
		cin >> railNum >> direction;
		if (railNum > 1) {
			change(railNum - 1,-direction, false);
		}
		if (railNum < 4) {
			change(railNum + 1,-direction,true);
		}
		if (direction > 0) rotateClock(railNum);
		else if (direction < 0) rotateReverseClock(railNum);
	}
	int result = 0;
	for (int i = 0; i < 4; i++) {
		result += rail[i + 1][0] * pow(2, i);
	}
	cout << result;
}