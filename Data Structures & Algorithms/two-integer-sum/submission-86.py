class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table={}
        for i, num in enumerate(nums):
            table[num]=i
        
        for j, num in enumerate(nums):
            try:
                if j != table[target-num]:
                    return [j, table[target-num]]
            except:
                continue