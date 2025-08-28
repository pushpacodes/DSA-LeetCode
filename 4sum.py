class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for d in range(n):
            new_target = target - nums[d]   # a+b+c = target - d
            # Now solve 3Sum for new_target
            for i in range(d+1, n):
                left, right = i+1, n-1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    if total == new_target:
                        quad = (nums[d], nums[i], nums[left], nums[right])
                        result.add(tuple(sorted(quad)))
                        left += 1
                        right -= 1
                    elif total < new_target:
                        left += 1
                    else:
                        right -= 1
        return [list(quad) for quad in result]
