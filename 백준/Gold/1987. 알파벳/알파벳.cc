#include <bits/stdc++.h>
using namespace std;

int r, c, answer = 0;
vector<string> board;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

// 방문한 상태를 기록하는 map
map<tuple<int,int,int>, bool> visited_state;

void dfs(int x, int y, int bitmask, int depth) {
    // 최대 길이 갱신
    if(depth > answer) answer = depth;

    // 가지치기: 남은 알파벳 수로 answer를 넘길 수 없는 경우 종료
    int max_remain = 26 - __builtin_popcount(bitmask);
    if(depth + max_remain <= answer) return;

    auto state_key = make_tuple(x, y, bitmask);
    if(visited_state[state_key]) return; // 중복 상태 방지
    visited_state[state_key] = true;

    for(int i=0; i<4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(nx >=0 && nx < r && ny >=0 && ny < c){
            int ch_bit = 1 << (board[nx][ny] - 'A');
            if(!(bitmask & ch_bit)){
                dfs(nx, ny, bitmask | ch_bit, depth + 1);
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> r >> c;
    board.resize(r);
    for(int i=0; i<r; i++){
        cin >> board[i];
    }

    int start_bit = 1 << (board[0][0] - 'A');
    dfs(0, 0, start_bit, 1);
    cout << answer << "\n";

    return 0;
}
