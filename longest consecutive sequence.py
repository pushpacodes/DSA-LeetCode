class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        max_len = 1
        length = 1
        nums.sort()  # important to find consecutive numbers
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                length += 1
                max_len = max(max_len, length)
            elif nums[i] != nums[i-1]:  # reset if not duplicate
                length = 1
        return max_len
