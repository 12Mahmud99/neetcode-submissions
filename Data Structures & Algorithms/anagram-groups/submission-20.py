class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls = []
        for string in strs:
            if not in_list(string, ls):
                anagrams = []
                anagrams.append(string)
                for string_2 in strs[strs.index(string) + 1::]:
                    if sorted(string) == sorted(string_2):
                        anagrams.append(string_2)
                ls.append(anagrams)
        return ls    

def in_list(string: str, strs: List[str]) -> bool:
    for li in strs:
        if string in li:
            return True
    return False
