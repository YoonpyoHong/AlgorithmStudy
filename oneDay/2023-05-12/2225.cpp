#include <iostream>

using namespace std;

int dp[201][201];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N, K;
    cin >> N >> K;
    for(int i =0; i<=N; i++){
        dp[0][i] =0;
    }
    dp[0][0] = 1;
    for(int j = 1; j<=K; j++){
        for(int i =0; i<=N; i++){
            for(int k =0; k<=i; k++){
                dp[j][i] += dp[j-1][k];
                dp[j][i] %= 1000000000;
            }
        }
    }
    cout << dp[K][N] <<"\n"; 
}