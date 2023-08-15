#include <iostream>

using namespace std;

#define MAX_SIZE 1001;

int T, N, M, result;
int book[1001];
pair<int, int> students[1001];

void init() {
	result = 0;
	for (int i = 1; i <= 1000; i++) {
		book[i] = 0;
		students[i] = { 0,0 };
	}
}

void input() {
	cin >> N >> M;
	for (int i = 1; i <= M; i++) {
		cin >> students[i].first >> students[i].second;
		for (int j = students[i].first; j <= students[i].second; j++) {
			book[j] += 1;
		}
	}
}

void giveBook() {
	for (int i = 1; i <= M; i++) {
		int minChoice = MAX_SIZE;
		int minChoiceIdx = NULL;
		for (int j = students[i].first; j <= students[i].second; j++) {
			if (book[j] != 0) {
				if (book[j] < minChoice) {
					minChoice = book[j];
					minChoiceIdx = j;
				}
				book[j] -= 1;
			}
		}
		if (minChoiceIdx != NULL) {
			book[minChoiceIdx] = 0;
			result += 1;
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> T;
	for (int i = 0; i < T; i++) {
		init();
		input();
		giveBook();
		cout << result<< "\n";
	}
}