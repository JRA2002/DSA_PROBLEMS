#include <iostream>
#include <vector>
using namespace std;
int removeElement(vector<int>& nums, int val) {
        int count = 0;
        int n = nums.size();
        int i = 0;
        
        while(i < n){
            if(nums[i] != val){
                swap(nums[i],nums[count]);
                count++;
            }
            i++;
        }

        return count;
}
int main() {
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    int res = removeElement(nums, val);
    cout<<res<<endl;
}