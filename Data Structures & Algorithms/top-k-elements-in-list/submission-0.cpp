class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        // for(int i = 0; i < nums.size(); i++){
        //     cout << nums[i] << ' ' << endl;
        // }
        int liveCounter = 0;
        int trackedNum = nums[0];
        vector<int> output;
        for(int i = 0; i < nums.size(); i++){
            int currentNum = nums[i];
            if(trackedNum != currentNum){
                if(liveCounter >= k){
                    output.push_back(trackedNum);
                }
                trackedNum = currentNum;
                liveCounter = 1;
            }
            else{
                liveCounter++;
            }
        }
        if(liveCounter >= k){
            output.push_back(trackedNum);
        }
        return output;
    }
};
