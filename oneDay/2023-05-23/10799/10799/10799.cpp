#include <iostream>
#include <stack>
#include <string>

using namespace std;

string inputText;
stack<int> lasorAndStick;
int stick = 0;
int result = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> inputText;
	int height = 0;
	bool lasorCheck = true;
	for (int i = 0; i < inputText.length(); i++) {
		if (inputText[i] == '(') {
			lasorCheck = true;
			lasorAndStick.push(++height);
		}
		else {
			height--;
			if (lasorCheck) {
				result += height;
			}
			else {
				result += 1;
			}
			lasorAndStick.pop();
			lasorCheck = false;
		}
	}
	cout << result;
}
