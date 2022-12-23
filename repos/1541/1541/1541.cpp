#include <iostream>
#include <string>
#include <sstream>
using namespace std;


string cal;
int sumSeperate(string exp);
int sum =0;
int seperateSum[30];
int length;

int main() {
	int cur_position = 0;
	int count = 0;
	int position;
	cin >> cal;
	while ((position = cal.find('-', cur_position)) != string::npos) {
		length = position - cur_position;
		seperateSum[count] = sumSeperate(cal.substr(cur_position, length));
		cur_position = position + 1;
		count++;
	}
	seperateSum[count] = sumSeperate(cal.substr(cur_position));

	sum = seperateSum[0];

	for (int i = 1; i <= count; i++) {
		sum -= seperateSum[i];
	}
	cout << sum;


}

int sumSeperate(string exp) {
	int cur_position = 0;
	int position;
	int sum_mini =0;
	while ((position = exp.find('+', cur_position)) != string::npos) {
		length = position - cur_position;
		sum_mini += stoi(exp.substr(cur_position, length));
		cur_position = position + 1;
	}
	sum_mini += stoi(exp.substr(cur_position));
	return sum_mini;
}