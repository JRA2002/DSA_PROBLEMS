#include <iostream>
#include <vector>
using namespace std;
int consecutive(vector<int>& nums) {
       int count = 0;
       for(int i; i<nums.size();i++){
            if(nums[i] % 2 == 0){
                count++;
                if(count == 3){
                    return true;
                }
            }
       }
       return false;
}
int main() {
    vector<int> nums = {2,2,2,3};
    int res = consecutive(nums);
    cout<<res<<endl;
}