class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        for num in nums:
            for num_2 in nums[nums.index(num) + 1::]:
                if (num + num_2) == target:
                    i = nums.index(num)
                    j = nums.index(num_2, nums.index(num) + 1)
                    return [i , j] 
        