#include <iostream>

using namespace std;
int result[200][200];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int trow, tcol, erow, ecol;
    cin >> ecol >> erow >> tcol >> trow;
    for (int i =0; i<erow; i++){
        for(int j =0; j< ecol; j++){
            result[i][j] = 0; 
        }
    }
    result[0][0] = 1;
    for (int col =0; col<tcol; col++){
        for(int row=0; row<trow; row++){
            if(row>0){
                result[row][col] += result[row-1][col];
            }
            if(col>0){
                result[row][col] += result[row][col-1];
            }
            result[row][col] %= 1000007;
        }
    }
    for (int col = tcol-1; col<ecol; col++){
        for(int row= trow-1; row<erow; row++){
            if(row>trow-1){
                result[row][col] += result[row-1][col];
            }
            if(col>tcol-1){
                result[row][col] += result[row][col-1];
            }
            result[row][col] %= 1000007;
        }
    }
    cout << result[erow-1][ecol-1] << "\n";
}