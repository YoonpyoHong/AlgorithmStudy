#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int numArr[1000000];
int dp[1000000];
vector<int> search;
stack<int> result;

void bsearch(int target){
    int start = 0;
    int end = search.size();
    int mid;
    if (end == 0 || numArr[target] > search[end-1]){
        search.push_back(numArr[target]);
        dp[target] = end;
        return ;
    }
    while(end-start > 0){
        mid = (start+end)/2;
        if(search[mid] >= numArr[target]){
            end = mid;
        }else{
            start = mid+1;
        }    
    }
    search[start] = numArr[target];
    dp[target] = start;
    return ;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> numArr[i];
    }
    for(int i=0; i<N; i++){
        bsearch(i);
    }
    cout << search.size() << "\n";
    int idx = search.size()-1;
    for(int j = N-1; j>=0; j--){   
        // cout << dp[j]  << " ";
        if(dp[j]==idx){
            result.push(numArr[j]);
            idx--;
        }
    }
    // cout << "\n";
//     while(result.size()){
//         cout << result.top() << " ";
//         result.pop();
//     }
//     return 0;
}