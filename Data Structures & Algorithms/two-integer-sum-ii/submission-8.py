class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = len(numbers)-1
        j = 0
        for k in range(len(numbers)):
            if numbers[i] + numbers[j]>target:
                i = i - 1
            elif numbers[i] + numbers[j] < target:
                j = j + 1
            else:
                break
        return [j+1, i+1] 

        