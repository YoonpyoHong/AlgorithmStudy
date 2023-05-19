#include <iostream>
#include <stack>
#include <vector>
#include <queue>

using namespace std;
#define INF 10^8;
vector<pair<int,int>> cities[1001];
long long dist[1001];
int way[1001];
int n, m, scity, ecity;

int dijkstra(){
    priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int,int>>>q;
    q.push({0, scity});
    while(!q.empty()){
        int cost = q.top().first;
        int destination = q.top().second;
        q.pop();
        if(dist[destination] <= cost){
            continue;
        }
        for(int i =0; i< cities[destination].size(); i++){
            int roaddest = cities[destination][i].first;
            int roadcost = cities[destination][i].second;
            if(cost + roadcost <dist[roaddest]){
                dist[roaddest] = cost + roadcost;
                way[roaddest] = destination;
                q.push(make_pair(cost+roadcost, roaddest));
            }
        }
    }
    return 0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n ;
    cin >> m;
    for(int i =0; i<m; i++){
        int start, end, cost;
        cin >> start >> end >> cost;
        cities[start].push_back(make_pair(end, cost));
    }
    for(int i=1; i<n+1; i++){
        dist[i] = INF;
    }
    cin >> scity >> ecity;
    dijkstra();
    stack<int> result;
    cout << dist[ecity] <<"\n";
    result.push(ecity);
    int city = ecity;
    while(city != scity){
        city = way[city];
        result.push(city);
    }
    while(!result.empty()){
        cout << result.top() << " ";
        result.pop();
    }
    
}
