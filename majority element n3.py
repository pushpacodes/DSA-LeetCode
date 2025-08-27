def major_element(nums):
    l=len(nums)
    z=l/3
    dic={}
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    result=[]
    for i in dic.keys():
        if dic[i]>z:
            result.append(i)
    return result
print(major_element([1,2,2,3,2]))
