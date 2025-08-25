#2d array
nums=[[1,2,3],[4,5,6],[7,8,9]]
#printing all elements in 2d array
for i in range(len(nums)):
    for j in range(len(nums[0])):
        print(nums[i][j],end=" ")
    print()
print()
#printing upper triangle
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if i<=j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()
#printing lower triangle
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if i>=j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()
#printing diagnol elements
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if i==j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
