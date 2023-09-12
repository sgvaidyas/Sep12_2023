n = int(input("Enter n names  = "))
l = []
for i in range(n):
    roll = input("Enter the roll num = ")
    name = input("Enter name = ")
    l.append([roll,name])
searchkey = input("Enter the name you want to search = ")
for x in l:
    r= x[0]
    na= x[1]
    if na == searchkey:
        print("SK found " , r , na)
        break
else:
    print("Search key not present")
