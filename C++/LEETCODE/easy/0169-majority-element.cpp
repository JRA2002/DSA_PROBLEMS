#include <iostream>
#include <vector>
using namespace std;
int majority(vector<int>& nums) {
       int count = 0;
       int candidate = 0;

       for(int num:nums){
            if(count == 0){
                candidate = num;
            }
            if(candidate == num){
                count ++;
            }else{
                count--;
            }
       }
       return candidate;
}
int main() {
    vector<int> nums = {2,2,1,1,1,2,2};
    int res = majority(nums);
    cout<<res<<endl;
}

//-std=c++11