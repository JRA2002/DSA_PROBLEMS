#include <iostream>
#include <vector>
using namespace std;
int removeDuplicates2(vector<int>& nums) {
        int l = 0;
        for(int num:nums){
            if(l<2 or num>nums[l-2]){
                nums[l] = num;
                l++;
            }
        }
        return l;
}
int main() {
    vector<int> nums = {0,0,0,1,1,2};
    int res = removeDuplicates2(nums);
    cout<<res<<endl;
}