'''
Check if the number is armstrong or not
e.g: 1*1*1+2*2*2+3*3*3
'''

num=int(input('Enter the number\t'))
x=str(num)
length=len(x)
results=0
for i in range(0,length):
    results=int(x[i])**length+results
if results==num:
    print('Armstrong')
else:
    print('Not Armstrong')
