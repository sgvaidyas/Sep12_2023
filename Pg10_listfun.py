l = [11,22,33,44,55,66]
for i in range(len(l)):
    print(l[i],end=" ")
    l[i]= l[i]+10
print("\n" , l)

print("------------------")
for x in l:
    print(x,end=" ")
    x = x+10
    print("new x = ",x)
print("\n",l)