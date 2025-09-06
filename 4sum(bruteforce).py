nums=[1,0,-1,0,-2,2,5,9]
target=0
my_set=set()
result=[]
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if nums[i]+nums[j]+nums[k]+nums[l]==target:
                    quad=[nums[i],nums[j],nums[k],nums[l]]
                    my_set.add(tuple(sorted(quad)))
result=[list(quad) for quad in my_set]
print(result)
