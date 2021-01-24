india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# 1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
cityName = input("Enter a city name: ")
if cityName in india:
    print(f'{cityName} belongs to India')
elif cityName in bangladesh:
    print(f'{cityName} belongs to Bangladesh')
elif cityName in pakistan:
    print(f'{cityName} belongs to Pakistan')
else:
    print(f"Sorry! I don't know which in which country {cityName} belongs to")
# 1. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
city1 = input('Enter first city name: ')
city2 = input('Enter sceond city name: ')

if city1 in india and city2 in india:
    print(f'{city1} and {city2} belongs to india')
elif city1 in bangladesh and city2 in bangladesh:
    print(f'{city1} and {city2} belongs to Bangladesh')
elif city1 in pakistan and city2 in pakistan:
    print(f'{city1} and {city2} belongs to Pakistan')
else:
    print(f'{city1} and {city2} are not from the same country')
