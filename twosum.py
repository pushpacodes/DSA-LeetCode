class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optional constraint checks
        if not 2 <= len(nums) <= 10**4:
            return []
        for num in nums:
            if not -10**9 <= num <= 10**9:
                return []
        if not -10**9 <= target <= 10**9:
            return []

        # Brute-force solution
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
