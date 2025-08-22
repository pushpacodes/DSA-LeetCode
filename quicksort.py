def quick_sort(nums,low,high):
    i=low
    j=high
    pivot=nums[low]
    if low>=high:
        return 0
    while i<=j:
        while nums[i]<pivot:
            i+=1
        while nums[j]>pivot:
            j-=1
        if i<=j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    quick_sort(nums,low,j)
    quick_sort(nums,i,high)
    return nums
nums=[4,1,7,6,3,2,8]
print(quick_sort(nums,0,len(nums)-1))
