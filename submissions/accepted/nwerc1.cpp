#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)

int v[(int)1.3e5];
int w[(int)1.3e5];
int main(){
    int N;
    cin >> N;
    FOR(i,0,N)cin >> v[i];
    FOR(i,0,N)w[i] = v[i];
    sort(w,w+N);
    int a = 0;
    while(a < N && v[a] == w[a])++a;
    if(a == N){
        cout << "Yes\n";
        return 0;
    }
    int b = N-1;
    while(v[b] == w[b])--b;
    ++b;
    reverse(v+a,v+b);
    bool ok = true;
    FOR(i,0,N)if(v[i] != w[i])ok = false;
    if(ok)cout << "Yes\n";
    else cout << "No\n";
    return 0;
}
