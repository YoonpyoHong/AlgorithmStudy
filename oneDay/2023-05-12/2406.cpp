#include <iostream>
#include <queue>

using namespace std;
int result[1000][2];

typedef struct node{
    node *parent = NULL;
}node;

typedef struct road{
    int cost;
    int city1;
    int city2;
}road;

struct cmp{
    bool operator()(road x, road y){
        if(x.cost > y.cost){
            return true;
        }
        return false;
    }
};

node nodeArr[1001];
int cost[1001][1001];

node* findParent(node *x){
    if(x -> parent == NULL){
        return x;
    }
    return findParent(x->parent);
} 

int main(){
    int n, m;
    cin >> n>>m;
    
    for(int i=0; i<m; i++){
        int x,y;
        cin >> x>> y;
        node* tmpParent1 = findParent(&nodeArr[x]);
        node* tmpParent2 = findParent(&nodeArr[y]);
        if(tmpParent1 != tmpParent2){
            if (x > y){
                tmpParent1 -> parent = &nodeArr[y];
            }else{
                tmpParent2 -> parent = &nodeArr[x];
            }
        }
    }
    priority_queue<road, vector<road>, cmp> pq;
    road tmp;
    for(int i =1; i<=n; i++){
        for (int j=1; j<=n;j++){
            if (i<j && i!=1 && j!=1){
            tmp.city1 =i;
            tmp.city2 =j;
            cin >> tmp.cost;
            pq.push(tmp);
            }else{
                cin >> tmp.cost;
            }
        }
    }

    int cost =0;
    int connection= 0;
    int idx =0;
    while (!pq.empty()){
        tmp = pq.top();
        pq.pop();
        node* tmpParent1 = findParent(&nodeArr[tmp.city1]);
        node* tmpParent2 = findParent(&nodeArr[tmp.city2]);
        if(tmpParent1 != tmpParent2){
             if (tmp.city1>tmp.city2){
                tmpParent1->parent = &nodeArr[tmp.city2];
            }else{
                tmpParent2->parent = &nodeArr[tmp.city1];
            }
            cost+=tmp.cost;
            connection+=1;
            result[idx][0] = tmp.city1;
            result[idx][1] = tmp.city2;
            idx++;
        } 
    }
    cout << cost << " " << connection<<"\n";
    for(int i=0; i<idx; i++){
        cout << result[i][0]<< " "<< result[i][1] << "\n";
    }
}