#include <iostream>
#include <queue>

using namespace std;

bool visited[3000];

struct emoticon {
	int quan;
	int clipboard;
	int time;
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	queue<emoticon> emotion;
	emotion.push({ 1,0,0 });
	visited[1] = false;

	int target;
	cin >> target;

	while (!emotion.empty()) {
		emoticon now = emotion.front();
		emoticon next;
		emotion.pop();

		if (now.quan == target) {
			cout << now.time;
			break;
		}
		next.time = now.time + 1;
		
		if (now.clipboard != 0 && now.quan+ now.clipboard < 3000 &&!visited[now.quan + now.clipboard]) {
			next.clipboard = now.clipboard;
			next.quan = now.quan + now.clipboard;
			visited[now.quan +now.clipboard] = true;
			emotion.push(next);
		}

		if (now.quan-1 >=0 &&!visited[now.quan - 1]) {
			next.clipboard = now.clipboard;
			next.quan = now.quan-1;
			visited[now.quan - 1]= true;
			emotion.push(next);
		}

		if (now.clipboard != now.quan) {
			next.clipboard = now.quan;
			next.quan = now.quan;
			emotion.push(next);
		}

	}
}