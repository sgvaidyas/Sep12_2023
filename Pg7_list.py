'''l = []
l.append(11)
l.append(12)
l.append(13)
l.append(14)
l.append([2,3,4,5])
l.extend([10,20,30,40])
print(l)
print(len(l))'''




   #  0  1  2  3  4  5  6
l = [11,22,33,44,55,66,77]
  #  -7 -6 -5 -4 -3 -2 -1
#range(x,y)
n = len(l)
for i in range(-n , 0):
    print(l[i],end=" ")
print("--------------")
for i in range(-1,-(n+1),-1):
    print(l[i],end=" ")



#print(l[2])
#print(l[6])
   # i in range(7)
'''for i in range(len(l)):
    print(l[i])'''




