#bruteforce
def max_product(nums):
    n=len(nums)
    if n==0:
        return 0
    max_prod=0
    for i in range(n):
        product=1
        for j in range(i,n):
            product*=nums[j]
            max_prod=max(product,max_prod)
    return max_prod
print(max_product([2,3,-2,4]))
#optimal
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        max_so_far = nums[0]  
        min_so_far = nums[0] 
        result = nums[0]
        for i in range(1, n):
            curr = nums[i]
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)
            result = max(result, max_so_far)
        return result
