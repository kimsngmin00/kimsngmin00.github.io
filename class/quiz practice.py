x=2//3
y=x*4
z=y+5
print ("z=", z)

total=0
for i in range(5):
    total=total - 1
print ('total=', total)

x=2/3
print ("x", x)

result = 1
for i in range(5):
    if i<3:
        result*=1
    else:
        result*=(-1)
print ('result=', result)

result=1
for i in range(5):
    if i <= 3:
        result+=i
    else:
        result+=1
print ('result=', result)

total=0
for i in range(0,10,3):
    if i%2==0 or i<5:
        total+=i
print("total=", total)
