#better aproach
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        max_avg=float('-inf')
        end=k
        add=0
        n=len(nums)
        add=sum(nums[start:end])
        max_avg=(add)/k
        while end<n:
            add=add-nums[start]+nums[end]
            avg=add/k
            max_avg=max(avg,max_avg)
            start+=1
            end+=1
        return max_avg
#brute force method
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start=0
        max_avg=0
        end=k
        n=len(nums)
        while end<=n:
            add=0
            for i in range(start,end):
                add+=nums[i]
            avg=(add)/k
            max_avg=max(avg,max_avg)
            start+=1
            end+=1
        return max_avg
