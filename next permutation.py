def next_permutation(nums):
    n=len(nums)
    pivot=-1
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            pivot=i
            break
    if pivot==-1:
        nums.reverse()
        return nums
    for i in range(n-1,pivot,-1):
        if nums[i]>nums[pivot]:
            nums[i],nums[pivot]=nums[pivot],nums[i]
            break
    p=pivot+1
    q=n-1
    while p<=q:
        nums[p],nums[q]=nums[q],nums[p]
        p+=1
        q-=1
    return nums
print(next_permutation([1,2,5,4,3]))
