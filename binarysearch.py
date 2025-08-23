def binary_search(nums,low,high,target):
    n=len(nums)
    mid=(low+high)//2
    if low>=high:
        return 0
    if nums[mid]==target:
        return mid
    elif target>nums[mid]:
        return binary_search(nums,mid+1,high,target)
    else:
        return binary_search(nums,low,mid,target)
nums=[9,2,4,6,1,8]#[1,2,4,6,8,9]
print(binary_search(sorted(nums),0,len(nums)-1,8))
