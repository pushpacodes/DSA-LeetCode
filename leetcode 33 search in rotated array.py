class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # Step 1: Find the rotation index k (smallest element index)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        k = low  # rotation index
        # Step 2: Do binary search using rotation
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            real_mid = (mid + k) % n  # map mid to actual index
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # not found
