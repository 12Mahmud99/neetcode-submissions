class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = []
        nums.sort()
        i = 0
        if len(nums) > 0:
            seqs.append([nums[0]])
            for num in nums[1:]:
                if seqs[i][-1] == (num - 1):
                    seqs[i].append(num)
                elif seqs[i][-1] == num:
                    continue
                else:
                    i += 1
                    seqs.append([num])
            longest = len(seqs[0])
            for seq in seqs:
                if len(seq) > longest:
                    longest = len(seq)
        else:
            longest = 0
        return longest