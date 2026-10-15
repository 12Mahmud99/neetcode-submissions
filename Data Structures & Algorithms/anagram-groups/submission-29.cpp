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
        // {key<string> : value<vector<string>>}
        unordered_map<string, vector<string>> dictionary;

        // {{},{},...}
        vector<vector<string>> anagrams;

        // the sorted string  will be used to all the of its anagrams and then pushed as values to the unordered_map
        for (string str : strs){
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            dictionary[sortedStr].push_back(str);
        }
        
        // push the values of the unordered_map (vectors of strings) into the vector.
        for(auto group : dictionary){
            anagrams.push_back(group.second);
        }
        return anagrams;
    }
};
