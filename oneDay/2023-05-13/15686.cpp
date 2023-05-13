#include <iostream>
#include <vector>

using namespace std;

int dirR[4] = {0,-1,0,1};
int dirC[4] = {1,0,-1, 0};

int point[101][101];

void init(){
    for(int i=0; i<=100; i++ ){
        for(int j=0; j<=100; j++ ){
            point[i][j] = 0;
        }
    }
}

bool squareCheck(int x,int y){
    if(point[x+1][y] ==1 && point[x][y+1] ==1 && point[x+1][y+1] ==1){
        return true;
    }
    return false;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    int x, y, d, g, endx, endy, cnt;
    cnt = 0;
    for(int i=0; i<N; i++){
        cin >> x >> y >> d >> g;
        vector<pair<int,int>> dragon;
        dragon.push_back({x,y});
        point[y][x] = 1;

        endx = x + dirC[d]; 
        endy = y + dirR[d];
        dragon.push_back({endx, endy});
        point[endy][endx] = 1;
        
        while(g>0){
            for(int j=dragon.size()-1; j >= 0; j--){
                int changeY = dragon[j].first - endx;
                int changeX = dragon[j].second - endy;
                dragon.push_back({endx - changeX, endy + changeY});
                point[endy + changeY][endx - changeX] = 1; 
            }
            endx = dragon[dragon.size()-1].first;
            endy = dragon[dragon.size()-1].second;
            g -= 1;
        }
        
    }
    for(int i =0; i<100; i++){
        for(int j =0; j<100; j++){
            if(point[i][j]==1 && squareCheck(i,j)){
                cnt+=1;
            }
        }
    }
    cout << cnt << "\n";

}