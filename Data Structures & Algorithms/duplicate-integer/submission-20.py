class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if(len(nums) > 0):
            stored = [nums[0]];
            for num in nums[1:]:   
                if(num in stored):
                    return True
                stored.append(num) 
        return False