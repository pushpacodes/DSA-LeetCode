def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
    return nums
nums=[3,5,6,4,8,9,10,7,1]
print(insertion_sort(nums))
