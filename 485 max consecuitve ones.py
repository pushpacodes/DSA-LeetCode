class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start=end=max_len=0
        n=len(nums)
        while end<n:
            if nums[end]==1:
                max_len=max(max_len,end-start+1)
                end+=1
            else:
                start=end=end+1
        return max_len
