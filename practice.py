n=[1,3]+[2,4]
n.sort()
a=len(n)
for i in n:
    print(i,"\n")
if a%2!=0:
    print(n[a//2],"\n")
else:
    b=a//2
    c=b-1
    print((n[b]+n[c])/2)