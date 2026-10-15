class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cons=0
        maximum=0
        for num in nums:
            if num == 1:
                cons+=1
            else:
                if maximum <= cons:
                    maximum = cons
                cons = 0
        if maximum <= cons:
                    maximum = cons
        return maximum