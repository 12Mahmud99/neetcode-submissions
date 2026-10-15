#time complexity of O(n)
#space complexity of O(n)
import math

#{0:5 , 1:3 , 2:2 , 3:4}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[i] = target - nums[i]
        for i in range(len(nums)):
            del dic[i]
            if(target - (target - nums[i]) in dic.values()):
                return [i] + [key for key in dic.keys() 
                    if (dic[key] == (target - (target - nums[i])))] 
        return dic