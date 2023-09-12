n = int(input("Enter the number of records = "))
l = []
for i in range(n):
    roll = input("Enter the roll = ")
    name = input("Enter the name = ")
    l.append([roll,name])

print("---------RECORDS---------")
for i in range(len(l)):
    print("ROLL = ",l[i][0], " NAME = ",l[i][1])

