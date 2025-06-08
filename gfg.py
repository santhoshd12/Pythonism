nums = [1,2,3,4,5]
target = 11
a=[]
k=0
for i in range(len(nums)):
    k+=1
    for j in range(0,len(nums)-k+1):
        
        print(nums[j:j+k])
        if sum(nums[j:j+k]) == target:
            
            a.append((nums[j:j+k]))
    


                
b=[len(i) for i in a]
print(b)
print(0 if len(b)==0 else min(b))