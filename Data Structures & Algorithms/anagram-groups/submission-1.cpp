class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> pair;
        for(int i = 0; i < strs.size(); i++){
            string anagram = strs[i];
            sort(anagram.begin(), anagram.end());
            pair[anagram].push_back(strs[i]);
        }
        vector<vector<string>> result;
        for(auto& res : pair){
            result.push_back(res.second);
        }
        return result;
    }
};
