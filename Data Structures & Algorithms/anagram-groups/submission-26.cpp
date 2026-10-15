/*
* time complexity is O(n^2)
*/

#include <iterator>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dictionary;
        vector<vector<string>> anagrams;
        
        if(strs.size() > 0){
            for (const string& str : strs){
                string sortedStr = str;
                sort(sortedStr.begin(), sortedStr.end());
                dictionary[sortedStr].push_back(str);
            }

            for(const auto group : dictionary){
                anagrams.push_back(group.second);
            }
        }
        return anagrams;
    }
};
