#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    int **route = (int**)calloc(1, sizeof(int*) * (N+1));
    for (int i = 0; i <= N; i++){
        route[i] = (int*)calloc(1, sizeof(int) * (N+1));
    }
    for(int i =1; i<=N; i++){
        for(int j =1; j<=N; j++){
            cin >> route[i][j];
        }
    }
    for(int i =1; i<=N; i++){
        for(int row =1; row<=N; row++){
            for(int col =1; col<=N; col++){
                if (row ==i || col ==i){
                    continue;
                }
                if (route[row][col] == 0 and route[row][i] ==1 and route[i][col]){
                    route[row][col] =1;
                }
            }
        }
    }
    for(int i =1; i<=N; i++){
        for (int j =1; j<=N; j++){
            cout << route[i][j] << " ";
        }
        cout << "\n";
    }
    
}