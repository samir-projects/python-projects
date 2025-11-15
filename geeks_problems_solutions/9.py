'''
Fibanacii Series
'''
a=0
b=1
c=0
count=0
while count<9:
    count=count+1
    c=a+b
    a=b
    b=c
print(c)
