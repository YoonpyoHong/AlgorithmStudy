#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int total_mininute;
int result = 0;
pair<int, int> curr_assignment = {0,0};
stack<pair<int,int>> assignment_schedule;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	cin >> total_mininute;
	for (int i = 0; i < total_mininute; i++) {
		int assignment;
		int point, time;
		cin >> assignment;
		if (assignment ==1) {
			cin >> point >> time;
			if (curr_assignment.second > 0) {
				assignment_schedule.push(curr_assignment);
			}
			curr_assignment = {point, time};
		}
		curr_assignment.second--;
		if (curr_assignment.second == 0) {
			result += curr_assignment.first;
			if (!assignment_schedule.empty()) {
				curr_assignment = assignment_schedule.top();
				assignment_schedule.pop();
			}
		}
	}
	cout << result;
}