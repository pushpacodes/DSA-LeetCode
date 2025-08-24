def dnf(nums):
    n=len(nums)
    mid=low=0
    high=n-1
    while low<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            mid+=1
            low+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[high],nums[mid]=nums[mid],nums[high]
            high-=1
    return nums
nums=[2,0,2,1,1,0,1,2,0,0]
print(dnf(nums))
