def lower_bound(nums,target):
    low=0
    lb=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
nums=[1,1,1,4,5,6,7,8,8,8,9,20]
target=1
print(lower_bound(nums,target))
