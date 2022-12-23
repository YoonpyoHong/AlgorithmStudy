#include <iostream>
using namespace std;

int num[1025][1025];
int N, M, tmp, x_1, y_1, x_2, y_2;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M;
	for(int i =1; i<= N; i++){
		for (int j = 1; j <= N; j++) {
			cin >> tmp;
			num[i][j] = tmp + num[i - 1][j] + num[i][j - 1] - num[i - 1][j - 1];
		}
	}

	for (int i = 0; i < M; i++) {
		cin >> x_1 >> y_1 >> x_2 >> y_2;

		cout << num[x_2][y_2] - num[x_2][y_1 - 1] - num[x_1 - 1][y_2] + num[x_1 - 1][y_1 - 1]<<'\n';
	}
}