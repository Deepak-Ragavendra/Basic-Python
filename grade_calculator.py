n=int(input("Enter the Number of subjects: "))
s=[]
c=[]
g=[]
sum=0
totc=0
for i in range(n):
    a=input("Enter the name of the subject along with the credits and grade: ")
    b=a.split()
    s.append(b[0])
    c.append(int(b[1]))
    g.append(b[2])
    totc+=int(b[1])

for i in range(n):
    if(g[i]=='S' or g[i]=='s'):
        sum+=10*(c[i])
    elif(g[i]=='A' or g[i]=='a'):
        sum+=9*c[i]
    elif(g[i]=='B' or g[i]=='b'):
        sum+=8*c[i]
    elif(g[i]=='C' or g[i]=='c'):
        sum+=7*c[i]
    elif(g[i]=='D' or g[i]=='d'):
        sum+=6*c[i]
    elif(g[i]=='E' or g[i]=='e'):
        sum+=5*c[i]
    else:
        sum+=0
gpa=sum/totc
print(" GPA : %.2f"%gpa)