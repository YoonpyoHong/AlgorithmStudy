#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int com, connection;
vector<int> connectionList[101];
int visited[101];
int countNode = 0;
queue<int> searchNode;

int search();
void inputData();

int main() {
	inputData();
	cout << search();
}

void inputData() {
	int con1, con2;
	cin >> com >> connection;
	for (int i = 1; i <= connection; i++) {
		cin >> con1 >> con2;
		connectionList[con1].push_back(con2);
		connectionList[con2].push_back(con1);
	}
}

int search() {
	int current;
	int currentSearch;
	searchNode.push(1);
	visited[1] = -1;
	while (!searchNode.empty()) {
		current = searchNode.front();
		searchNode.pop();
		while (!connectionList[current].empty()) {
			currentSearch = connectionList[current].back();
			connectionList[current].pop_back();
			if (visited[currentSearch] != -1) {
				searchNode.push(currentSearch);
				visited[currentSearch] = -1;
				countNode++;
			}
		}
	}
	return countNode;
}