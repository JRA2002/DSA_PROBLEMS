#include <iostream>
#include <vector>
using namespace std;
int removeDuplicates(vector<int>& nums) {
       int i = 0;
       for(int j=0; j<nums.size(); j++){
            if(nums[i] != nums[j]){
                i++;
                swap(nums[i], nums[j]);
            }
       }
       return i+1;
}
int main() {
    vector<int> nums = {0,0,0,1,1,2};
    int res = removeDuplicates(nums);
    cout<<res<<endl;
}