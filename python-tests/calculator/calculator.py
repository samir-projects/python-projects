def main():
    x=int(input('Enter the first number '))
    y=int(input('Enter the second number '))
    print(add(x,y))
    print(sub(x,y))
    print(mul(x,y))
    print(div(x,y))
    print(rem(x,y))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b 

def rem(a,b):
    return a%b

if __name__=="__main__":
    main()