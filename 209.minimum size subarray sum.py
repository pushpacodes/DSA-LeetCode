class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=end=0
        min_len=float('inf')
        n=len(nums)
        add=0
        while end<n:
            add+=nums[end]
            while add>=target:
                min_len=min(min_len,end-start+1)
                add-=nums[start]
                start+=1
            end+=1
        return 0 if min_len == float('inf') else min_len
