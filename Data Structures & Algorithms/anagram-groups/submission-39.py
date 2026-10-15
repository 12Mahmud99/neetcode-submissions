#time complexity O(len(strs) * len(longest_string))
#space complexity O(len(longest_string)) 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            s_list = list(s)
            s_list.sort()
            key = "".join(s_list)
            if (key not in anagrams.keys()):
                anagrams[key] = [s]
            else:
                anagrams[key].append(s)
        return [value for value in anagrams.values()]