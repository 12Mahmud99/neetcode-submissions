class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = False
        for num in nums:
            for num_2 in nums[(nums.index(num) + 1)::]:
                if num == num_2:
                    dup = True
                    return dup
        return dup    
