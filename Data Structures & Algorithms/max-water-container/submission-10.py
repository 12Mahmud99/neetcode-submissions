#solution is O(n) time complextity and O(1) space complexity
#two pointers solution

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(heights) - 1
        current_max = 0 

        while left_ptr < right_ptr:
            # finding the area by choosing the minimum times left_ptr - 1
            #left_ptr - 1 because we want to eliminate the distance from 0 to the left_ptr
            area = min(heights[right_ptr], heights[left_ptr]) * (right_ptr - left_ptr)
            current_max = max(current_max, area) #update hte current_max 
            
            if  heights[left_ptr] <= heights[right_ptr]:
                left_ptr += 1
            elif heights[left_ptr] > heights[right_ptr]:
                right_ptr -= 1
        return current_max