#include <iostream>

using namespace std;

int R, C, T, cleanerUp = 0, cleanerDown = 0;
int room[50][50];
int change[50][50];
int dirR[4] = {0,-1,0,1};
int dirC[4] = {1,0,-1,0};

void spread(int row, int col){
    int newRow, newCol, spreadDust, cnt=0;
    spreadDust = room[row][col]/5;
    for(int i=0; i<4; i++)
    {
        newRow = row+ dirR[i];
        newCol = col+ dirC[i];
        if(newRow>=0 && newCol>=0 && newRow<R && newCol<C && room[newRow][newCol] != -1){
            change[newRow][newCol] += spreadDust;
            cnt+=1;
        }
    }
    change[row][col] -= spreadDust * cnt;
}

void init(){
    for(int i=0; i< R; i++){
        for(int j=0; j<C; j++){
            //추가하는 함수 나쁘지 않은듯

            room[i][j] += change[i][j];
            change[i][j] =0;
        }
    }
}
void printResult(){
    int result =0;
    for(int i=0; i< R; i++){
        for(int j=0; j<C; j++){
            if(room[i][j] > 0){
                result += room[i][j];
            }
        }
    }

    cout << result;
}

void move(){
    int tmp1 = 0;
    int tmp2 = room[cleanerUp][1];
    int posR = cleanerUp;
    int posC = 1;
    int direction = 0;
    while(posR != cleanerUp || posC != 0){
        tmp2=room[posR][posC];
        room[posR][posC] = tmp1;
        tmp1 = tmp2;
        posR = posR + dirR[direction];
        posC = posC + dirC[direction];
        if(posR + dirR[direction] >cleanerUp||posR + dirR[direction] <0||posC + dirC[direction]<0 || posC + dirC[direction]>=C){
            direction++;
        }
    }
    posR = cleanerDown;
    posC = 1;
    tmp1 = 0;
    tmp2 = 0;
    direction =4;
    while(posR != cleanerDown || posC != 0){
        tmp2=room[posR][posC];
        room[posR][posC] = tmp1;
        tmp1 =tmp2;
        posR = posR + dirR[direction%4];
        posC = posC + dirC[direction%4];
        if(posR + dirR[direction%4] < cleanerDown||posR + dirR[direction%4] >=R||posC + dirC[direction%4]<0||posC + dirC[direction%4]>=C){
            direction--;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> R >> C >> T;
    for(int r =0; r<R; r++){
        for(int c =0; c<C; c++){
            cin >> room[r][c];
            if(room[r][c]==-1){
                if(cleanerUp == 0){
                    cleanerUp = r;
                }else{
                    cleanerDown = r;
                }
            }
            change[r][c] = 0;
        }
    }
    for(int i =0; i<T; i++){
        for(int r=0; r<R; r++){
            for(int c=0; c<C; c++){
                if(room[r][c]>0){
                    spread(r,c);
                }
            }
        }
        init();
        move();
        
    }
    printResult();
}