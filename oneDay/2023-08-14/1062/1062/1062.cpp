#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int alphabet[50];
int N, K;
char base = 'a';

int checkWord(int before, int idx, int alpha) {
	int result = 0;
	if(idx==0){
		for (int i = 0; i < N; i++) {
			if (alphabet[i] == (alphabet[i] & before)) {
				result += 1;
			}
		}
		return result;
	}
	for (int i = alpha; i < 26; i++) {
		int tmp = before | (1 << i);
		result = max(result, checkWord(tmp, idx-1 ,i+1));
	}
	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int baseBit = (1 << ('a' - base)) + (1 << ('n' - base)) + (1 << ('t' - base)) + (1 << ('i' - base)) + (1 << ('c' - base));

	cin >> N >> K;
	for (int i = 0; i < N; i++) {
		int bit = baseBit;
		string word;
		cin >> word;
		for (int j = 4; j < word.size() - 4; j++) {
			 bit = bit | (1 << (word[j] - base));
		}
		alphabet[i] = bit;
	}

	if (K < 5) {
		cout << 0;
	}
	else {
		cout << checkWord(baseBit, K - 5, 0);
	}
	
}