#include <iostream>
#include <vector>
using namespace std;
int mostWater(vector<int>& height) {
        int n = height.size();
        int l = 0;
        int r = n - 1;
        int maxA = 0;

        while(l < r){
            int mini = min(height[l], height[r]);
            maxA = max(maxA, mini*(abs(l - r)));
            if(height[l] < height[r]){
                l ++;
            }else{
                r--;
            }
        }
        return maxA;
}
int main() {
    vector<int> height = {1,8,6,2,5,4,8,3,7};
    int res = mostWater(height);
    cout<<res<<endl;
}