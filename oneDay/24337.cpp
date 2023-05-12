#include <iostream>

using namespace std;

int building[10^5+1];


int main(){
    int N, a, b;
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> N >> a >> b;
    if (N < a + b - 1){
        cout << -1;
    }
    else if(a != 1){
        for(int i=0;i<N-a-b+1;i++){
            cout << 1 << " ";
        }
        for(int i =1; i <= a-1; i++){
            cout << i << " ";
        }
        cout << max(a,b) << " ";
    
        for(int i = b-1; i > 0; i--){
            cout << i << " ";
        }
    }
    else{
        cout << max(a,b) << " ";
        for(int i=0;i<N-a-b+1;i++){
            cout << 1 << " ";
        }
    
        for(int i = b-1; i > 0; i--){
            cout << i << " ";
        }
    }
    
}


