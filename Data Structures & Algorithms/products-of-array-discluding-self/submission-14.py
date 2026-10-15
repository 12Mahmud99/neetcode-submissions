class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        for i in range(0, len(output)):
            for k in range(0, len(nums)):
                if k == i:
                    pass
                else:
                    output[i] *= nums[k] 
        return output