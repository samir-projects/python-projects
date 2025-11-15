## Program to find the item in list and index of that item
list1=['apple','banana','mango','grapes','orange','apple']
item=input('Enter the item to be searched? ')
for i in range(0,len(list1)):
    if item in list1[i]:
        print(f"{item} is in list at {i} index")
