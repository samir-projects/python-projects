def main():
    city_name=input('Enter the name of the city ')
    country_name=input('Enter the name of the country ')
    print(get_citycountry(city_name,country_name))

def get_citycountry(city,country):
    return f"{city},{country}"

if __name__=="__main__":
    main()
