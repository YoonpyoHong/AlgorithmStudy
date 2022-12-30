#include <iostream>
#include <cmath>

using namespace std;

int N, S;

int num[20];
int prob[2000000];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> S;
    for (int i = 0; i < N; i++) {
        cin >> num[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = pow(2, i)-1; j >= 0; j--) {
            prob[j * 2 + 1] = prob[j] + num[i];
            prob[j * 2] = prob[j];
       }
    }

    int cnt = 0;
    for (int i = 1; i < pow(2, N); i++) {
        if (prob[i] == S) {
            cnt++;
        }
    }

    cout << cnt;
}

