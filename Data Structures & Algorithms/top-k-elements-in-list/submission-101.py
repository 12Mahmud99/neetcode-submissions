#time complexity O(n)
#space complexity is O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if (num not in dic.keys()):
                dic[num] = 1
            else:
                dic[num] = dic[num] + 1
        arr = []
        for key,v in dic.items():
            arr.append([v,key])
        arr.sort()
        freq = []
        for i in range(k):
            freq.append(arr[len(arr)-1-i][1])
        return freq