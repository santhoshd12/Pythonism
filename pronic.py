a=input().strip()
b=input().strip()
b=list(b)
a=list(a)
print(a)
print(b)
for i in b:
    print(bin(ord(i))[2:])
val=""
for k in range(len(b)):
    l=bin(ord(b[k]))[2:]
    for i in l:
        for j in a:
            if i=='1':
                t=j.upper()
            val+=t
            
        val+=" "

print(val)

