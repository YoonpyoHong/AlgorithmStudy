#include <iostream>
#include <set>
using namespace std;

int lenSquare, N, xmin, xmax, ymin, ymax;
set<pair<int, int>> posSet;
set<int> xSet, ySet;
pair<int, int> tmp;
int lenSearch();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> tmp.first;
		cin >> tmp.second;
		posSet.insert(tmp);
		xSet.insert(tmp.first);
		ySet.insert(tmp.second);
	}
	cout << lenSearch();
}

int lenSearch() {
	int x;
	int y;
	bool xminchk = true, xmaxchk = true, yminchk = true, ymaxchk =true;
	bool xchk = true;
	bool ychk = true;
	xmin = *(xSet.begin());
	ymin = *(ySet.begin());

	xmax = *(--xSet.end());
	ymax = *(--ySet.end());


	auto itr = posSet.begin();

	xmin = (*itr).first;


	for (; itr != posSet.end(); itr++) {
		x = (*itr).first;
		y = (*itr).second;
		if (x != xmax && x != xmin && y != ymin && y !=ymax) {
			return -1;
		}

		if (x == xmax) {
			if (y != ymax && y != ymin) {
				xmaxchk = false;
			}
		}
		if (x == xmin) {
			if (y != ymax && y != ymin) {
				xminchk = false;
			}
		}
		
		if (y== ymax) {
			if (x != xmax && x != xmin) {
				ymaxchk = false;
			}
		}
		if (y == ymin) {
			if (x != xmax && x != xmin) {
				yminchk = false;
			}
		}

	}

	xchk = xminchk || xmaxchk;
	ychk = yminchk || ymaxchk;

	int xlen = xmax - xmin;
	int ylen = ymax - ymin;
	if (xchk == true && ychk == true) {
		return max(xlen, ylen);
	}
	else {
		if (xchk == false && ychk == false) {
			if (xlen == ylen) {
				return xlen;
			}
			else {
				return -1;
			}
		}
		else if (xchk == false) {
			if (xlen < ylen) {
				return -1;
			}
			else {
				return max(xlen, ylen);
				}
			}
		else {
			if (xlen > ylen) {
				return -1;
			}
			else {
				return max(xlen, ylen);
			}
		}
	}

}
