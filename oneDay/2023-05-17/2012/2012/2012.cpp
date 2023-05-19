#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define DIFF(x,y) ((x)>(y) ? (x)-(y): (y)-(x))

int N;
vector<int> grade;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;
	int student;
	for (int i = 0; i < N; i++) {
		cin >> student;
		grade.push_back(student);
	}
	sort(grade.begin(), grade.end());
	long long result = 0;
	for(int i =0; i<N; i++){
		result += DIFF(i + 1, grade[i]);
	}
	cout << result;
}