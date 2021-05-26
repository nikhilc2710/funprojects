#include <iostream>
#include <vector>
#include <sstream>
using namespace std;
typedef long long ll;

vector<int> intToVect(int N){
    vector <int> temp;
    while (N>0){
        int k=N%10;
        temp.insert(temp.begin(),k);
        N/=10;
    }
    return temp;
}

vector <int> subArrays(vector<int> arr){
    vector <int> tempx;
    int n=arr.size();
   for (int i=0;i<n;i++){
     int temp=0;
     for (int j=i+1;j<=n;j++){
         for (auto x:vector<int>(arr.begin()+i,arr.begin()+j)){
                temp=(temp*10)+x;
         }
         tempx.push_back(temp);
         temp=0;
     }
 }
 return tempx;
}

int main (){
ios::sync_with_stdio(0);
cin.tie(0);
stringstream sx;
vector <int> v;
int n=0;
int ans=0;
cin >> n;
v= intToVect(n);
v=subArrays(v);
for (auto x:v){
    if (x%11==0){
        cout<<x<<" ";
        ans+=1;
    }
}
cout<<ans;
return 0;
}