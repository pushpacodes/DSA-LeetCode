nums=[1,0,-1,0,-2,2,5,9]
target=0
n=len(nums)
my_set=set()
for i in range(n):
    for j in range(i+1,n):
        hash_set=set()
        for k in range(j+1,n):
            fourth=target-(nums[i]+nums[j]+nums[k])
            if fourth in hash_set:
                quad=[nums[i],nums[j],nums[k],fourth]
                my_set.add(tuple(sorted(quad)))
            else:
                hash_set.add(nums[k])
result=[list(quad) for quad in my_set]
print(result)
