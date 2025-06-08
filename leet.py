# word1 = 'abc'
# word2 = 'pqr'
# st = ''
# ml = word2 if len(word2)>len(word1) else word1
# for i in range (min(len(word1),len(word2))):
#             st+=word1[i]+word2[i]

# st+=ml[min(len(word1),len(word2))+1:]

# str1='abcabc'
# str2='abc'
# s=""
# for i in range(len(str2)-1):
#     s+=str2[i]
#     if str2[i+1] in s:
#         break
    
# for i in range(len(str2)-1):
    
#     if len(str2)%len(s)==0 and len(str1)%len(s)==0:
#         print(s)
#         break
#     else:
#         print("nothing")
        

# s='[{())}]'
# l=[]
# for i in s:
#     if i=='[' or i=='{' or i=='(':
#         l.append(i)
#         print(l)
#     else:
#         if not l:
#             print(False)
#         elif i==']':
#             l.pop()
#         elif i==')':
#             l.pop()
#         elif i=='}':
#             l.pop()
#         print(l)
# print(len(l))



# r1=['q','w','e','r','t','y','u','i','o','p']
# r2=['a','s','d','f','g','h','j','k','l']   
# r3=['z','x','c','v','b','n','m']    
# res=[]
# words = ["omk"]
# for i in words:
#     i=i.lower()
#     v=((all(j in r1 for j in i)) or (all(j in r2 for j in i)) or (all(j in r3 for j in i)))
#     if v==True:
#         res.append(i)
# print(res)


# from collections import deque
# s=deque()
# print(s)
# s.append(3)
# s.append(8)
# print(s)
# s.popleft()
# print(s)

# from queue import Queue
# s=Queue(maxsize=0)
# s.put(2)
# s.put('s')
# s.put(34)
# print(s.queue)
# print(s.qsize())
# print(s.empty())
# print(s.full())

nums=[1,3,5,6]
target = 5

for i in range(len(nums)):
    if target>nums[i]:
        print( i)
    else:
        print(-1)