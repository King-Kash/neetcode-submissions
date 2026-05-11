class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> my_map;

        for(int i = 0; i < nums.size(); i++){
            int dif = target - nums[i];
            if(my_map.find(dif) != my_map.end()){
                return {my_map[dif], i};
            }
            else{
                my_map.insert({nums[i], i});
            }
        }
    }
};
