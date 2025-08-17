def selection_sort(nums):
    n=len(nums)
    for i in range(0,n):
        max_idx=i
        for j in range(i+1,n):
            if nums[max_idx]<nums[j]:
                max_idx=j
        nums[i],nums[max_idx]=nums[max_idx],nums[i]
    return nums
nums=[3,1,5,8,2,9,21]
print(selection_sort(nums))
