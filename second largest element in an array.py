"""nums=[1,2,5,8,3,9,10,13,4]
output:10"""
#bruteforce
def sec_lar(nums):
    i=0
    j=i+1
    n=len(nums)
    for i in range(n):
        min=i
        for j in range(i,n):
            if nums[j]<nums[min]:
                min=j
        nums[min],nums[i]=nums[i],nums[min]
    return "second largest",nums[n-2]
nums=[1,2,5,8,3,9,10,13,4]
print(sec_lar(nums))


#better approach
def sec_lar(nums):
    mini=float('inf')
    maxi=0
    n=len(nums)
    for i in range(n):
        if nums[i]>maxi:
            maxi=nums[i]
        if nums[i]<mini:
            mini=nums[i]
    i=0
    secmax=0
    secmin=float('inf')
    while i<n:
        if nums[i]<maxi:
            if nums[i]>secmax:
                secmax=nums[i]
        if nums[i]>mini:
            if nums[i]<secmin:
                secmin=nums[i]
        i+=1
    return secmax,secmin
nums=[1,2,5,8,3,9,10,13,4]
print(sec_lar(nums))


#optimal approach
def sec_lar_small(nums):
    small=float('inf')
    sec_small=float('inf')
    large=0
    sec_large=0
    n=len(nums)
    for i in range(n):
        if nums[i]<small:
            sec_small=small
            small=nums[i]
        elif nums[i]>small and nums[i]<=sec_small:
            sec_small=nums[i]
        if nums[i]>large:
            sec_large=large
            large=nums[i]
        elif nums[i]<large and nums[i]>=sec_large:
            sec_large=nums[i]
    return sec_small,sec_large
nums=[1,2,5,8,3,9,10,13,4]
print(sec_lar_small(nums))
