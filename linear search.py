def linear_search(nums,target):
    i=0
    n=len(nums)
    while i<n:
        if nums[i]==target:
            return i
        else:
            i+=1
    return -1
nums=[9,2,5,1,7,6]
print(linear_search(nums,16))
