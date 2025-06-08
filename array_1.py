# from array import *

# arr = array('i',[1,2,3,4,5])
# a=32
# arr.insert(3,32)
# for i in range(len(arr)):
#     if arr[i]==a:
#         print(i)
#         break

# arr=[1,2,3,4,5]
# arr.pop()
# print(arr)
# arr.reverse()
# print(arr)
# arr.clear()
# print(arr)

a=[2,32,4,2,4]
# for i in a:
#     if i==4:
#         print(a.index(i))
#         break
#     else:
#         print("not found")


from collections import deque
st = deque()
st.append(10)
st.append(34)

print(st)

st.pop()
print(st)