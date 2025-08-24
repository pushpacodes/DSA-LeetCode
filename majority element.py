#[1,5,3,2,2,2,2] ; output: 2 : n=7 , n/2=3.5~4/3
def majority_element(nums):
    n=len(nums)
    k=n/2
    dic={}
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    print(dic)
    for i in dic:
        if dic[i]>=k:
            return i
nums=[1,2,2,2,2,5,2]
print(majority_element(nums))
