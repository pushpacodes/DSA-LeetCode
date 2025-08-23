def find_union(nums1,nums2):
    a=sorted(nums1)
    b=sorted(nums2)
    c=a+b
    dic={}
    result=[]
    for i in c:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for j in dic.keys():
        if dic[j]==2:
            result.append(j)
    return result
nums1=[9,2,5,4,6,8]
nums2=[9,2,5,4,6,8]
print(find_union(nums1,nums2))
