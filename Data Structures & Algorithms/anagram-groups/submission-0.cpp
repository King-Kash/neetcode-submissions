class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> my_map;
        for(int i = 0; i < strs.size(); i++){
            string value = strs[i];
            sort(strs[i].begin(), strs[i].end());
            my_map[strs[i]].push_back(value);
        }

        vector<vector<string>> output;
        for (const auto& pair : my_map) {
            vector<string> temp;
            for (const auto& value : pair.second) {
                temp.push_back(value);
            }
            output.push_back(temp);
        }
        return output;
    }
};
