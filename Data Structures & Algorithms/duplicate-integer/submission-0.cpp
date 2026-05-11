class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int check;
        for(int i = 0; i < nums.size(); i++){
            check = nums[i];
            for(int j = i+1; j < nums.size(); j++){
                if(check == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
};
