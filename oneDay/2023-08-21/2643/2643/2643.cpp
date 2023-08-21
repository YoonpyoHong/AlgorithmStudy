#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct paperStep {
	int step;
	int x;
	int y;
};

vector<pair<int, int>> paper;
vector<vector<paperStep>> paperArr;
int  N;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> N;
	paper.push_back({ 1000,1000 });
	for (int i = 0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		if (x > y) {
			paper.push_back({ x,y });
		}
		else {
			paper.push_back({ y,x });
		}
	}
	sort(paper.rbegin(), paper.rend());
	vector<paperStep> firstVec;
	firstVec.push_back({ 0, 1000, 1000 });
	paperArr.push_back(firstVec);
	for (int i = 1; i <= N; i++) {
		vector<paperStep> tmp;
		int currX, currY;
		currX = paper[i].first;
		currY = paper[i].second;
		tmp.push_back({ 1, currX, currY });
		for (int j = 0; j < paperArr[i - 1].size(); j++) {
			if (paperArr[i - 1][j].x >= currX && paperArr[i - 1][j].y >= currY && tmp[0].step < paperArr[i-1][j].step+1) {
				tmp[0].step = paperArr[i - 1][j].step + 1;
			}
			tmp.push_back(paperArr[i - 1][j]);
		}
		paperArr.push_back(tmp);
	}
	vector<paperStep> tmp = paperArr[N];
	int maxStep = 0;
	for (int i = 0; i < tmp.size(); i++) {
		if (tmp[i].step > maxStep) {
			maxStep = tmp[i].step;
		}
	}

	cout << maxStep;
}