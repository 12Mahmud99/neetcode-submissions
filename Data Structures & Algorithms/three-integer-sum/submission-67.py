#time complexity is O(n^2) and space complexity is O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0: #if the sorted numbers list starts out with positive numbers then there's no three sum of 0
                break
            if i > 0 and num == nums[i-1]: #if the current number is the same the previous one, skip since no repititions are allowed
                continue
            left_ptr, right_ptr = i + 1, len(nums) - 1 #two pointers of the smallest and largest element in the sublist
            while left_ptr < right_ptr: #untill the end of the list
                if num + nums[left_ptr] + nums[right_ptr] == 0:
                    triplets.append([num , nums[left_ptr] , nums[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1
                    while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                        left_ptr += 1
                elif num + nums[left_ptr] + nums[right_ptr] > 0:
                    right_ptr -= 1
                elif num + nums[left_ptr] + nums[right_ptr] < 0:
                    left_ptr += 1
        return triplets