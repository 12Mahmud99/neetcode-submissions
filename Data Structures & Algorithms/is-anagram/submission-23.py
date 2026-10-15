#constant space complexity O(1)
#time complexity is O(len(s) + len(t)),
import itertools

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        else:
            s_list = [char for char in s]
            t_list = [char for char in t]
            s_list.sort()
            t_list.sort()
            for (i,j) in zip(s_list, t_list):
                if (i != j):
                    return False
            return True