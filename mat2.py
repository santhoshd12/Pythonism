# def isprime(a):
#     if a<=0:
#         return False

#     for i in range(2,int(a ** 0.5) + 1):
#         if a%i==0:
#             return False
#     return True
# n = input()
# yes = "yes"
# for i in range(len(n)):
#     for j in range(0,10):
#         val = list(n)
#         val[i]=str(j)
#         val1="".join(val)
#         if isprime(int(val1)):
#             yes="no"
#             break
# print(yes)

n=int(input())
dup=[]
mat = []
for i in range(n):
    a=input().strip().split(" ")
    mat.append(a)
    dup.append(a)


qn=int(input())
q=[]
for i in range(qn):
    val = input().strip().split(" ")
    q.extend(val)

for i in range(0,qn*qn,2):
    for j in range(int(q[i])-1,int(q[i+1])):
        for k in range(n):
            if mat[j][k]=="*":
                mat[j][k]=dup[j][k]
            else:
                mat[j][k]="*"

            if mat[k][j]=="*":
                mat[k][j]=dup[k][j]
            else:
                mat[k][j]="*"
    print(mat,end="\n",sep="\n")
    

for i in range(n):
    for j in range(n):
        print(mat[i][j],end=" ")
    print("\n")
