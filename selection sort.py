def selection_Sort(nums):
    n=len(nums)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if nums[j]<nums[min_idx]:
                min_idx=j
        nums[i],nums[min_idx]=nums[min_idx],nums[i]
    return nums
nums=[5,2,6,1,8,10,11]
print(selection_Sort(nums))
