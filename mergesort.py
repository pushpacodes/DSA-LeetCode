def merge_sort(nums):
    n=len(nums)
    if n<=1:
        return nums
    z=n//2
    left=nums[:z]
    right=nums[z:]
    a=merge_sort(left)
    b=merge_sort(right)
    result=merge(a,b)
    return result
def merge(left,right):
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
nums=[9,2,1,4,7,3,8]
print(merge_sort(nums))
