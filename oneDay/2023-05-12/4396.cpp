#include <iostream>

using namespace std;

char map[10][10];
char open[10][10];
char result[10][10];
int dirR[8] = {0,0,1,-1,1,-1,1,-1};
int dirC[8] = {1,-1,0,0,1,1,-1,-1};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> map[i][j];
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> open[i][j];
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            result[i][j] = '.';
        }
    }

    bool checker  = true;
    for(int i=0; i<n; i++){
        for(int j =0; j<n; j++){
            if(open[i][j]=='x'){
                if(map[i][j] == '.'){
                char cnt ='0';
                for(int k=0; k<8; k++){
                    int nowR = i+dirR[k];
                    int nowC = j+dirC[k];
                    if(nowR>=0 && nowR<n && nowC>=0 && nowC<n && map[nowR][nowC] == '*'){
                        cnt+=1;
                    }
                }
                result[i][j] = cnt;
                }else{
                    if(checker){
                        checker = !checker;
                        for(int r=0; r<n; r++){
                            for(int c=0; c<n; c++){
                                if(map[r][c] == '*'){
                                    result[r][c] = '*';
                                }
                            }
                        }
                    }
                }                
            }
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << result[i][j];
        }
        cout << "\n";
    }
}