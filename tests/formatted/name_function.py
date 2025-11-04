def main():
    first=input('Enter first name ')
    last=input('Enter last name ')
    print(get_formatted_name(first,last))
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

if __name__=="__main__":
    main()
