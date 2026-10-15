class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count_dic = {}
        k_vals = []
        output = []
        i = 0
        for num in nums:
            count = 0
            num_count_dic.update({num : count})
            for num_2 in nums[nums.index(num) + 1::]:
                if num == num_2:
                    count += 1
                    num_count_dic.update({num : count})
        sorted_count = sorted(num_count_dic.values(), reverse=True)
        while i < k:
            k_vals.append(sorted_count[i])
            i += 1
        for val in k_vals:    
            for k in num_count_dic.keys():
                if num_count_dic[k] == val and k not in output: 
                    output.append(k)
        return output