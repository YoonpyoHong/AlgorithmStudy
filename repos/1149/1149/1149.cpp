#include <iostream>
#include <vector>
using namespace std;

struct house {
	int R;
	int G;
	int B;
};

int N, Rmin, Gmin, Bmin, Rtmp, Gtmp;
house houseVal[1001];
void inputData();
void search();

int main() {
	inputData();
	search();
}

void inputData() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> houseVal[i].R >> houseVal[i].G >> houseVal[i].B;
	}
}

void search() {
	Rmin = houseVal[1].R;
	Gmin = houseVal[1].G;
	Bmin = houseVal[1].B;
	for (int i = 2; i <= N; i++) {
		Rtmp = min(Gmin, Bmin) + houseVal[i].R;
		Gtmp = min(Rmin, Bmin) + houseVal[i].G;
		Bmin = min(Gmin, Rmin) + houseVal[i].B;
		Rmin = Rtmp;
		Gmin = Gtmp;
	}
	cout << min(min(Rmin, Gmin), Bmin);
}


