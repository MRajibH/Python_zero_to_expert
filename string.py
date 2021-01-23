name = 'Rajib is a good boy'
print(name[0:7])
# equivalent
print(name[0:7])
print(name[11:])
# printing Address in a new way
address = '''Md.Rajib Hawlader
Morrelgonj, Bagerhat
Khulna, Bangladesh,Asia'''
print(address)
# add string and number
country = 'Bangladesh'
division = 8
print(country + ' has ' + str(division)+' division')
# Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
street = '14/602'
city = 'Dhaka'
country = 'Bangladesh'
print(street+'\n'+city+'\n'+country, end='\nfirst part ends here\n')
print(f'''{street}
{city}
{country}''')

# Create a variable to store the string "Earth revolves around the sun" 1.Print "revolves" using slice operator 2. "sun" using negative index
sentence = 'Earth revolves around the sun'
length = len(sentence)
for i in range(length):
    if(sentence[i] == 'r' and sentence[i+1] == 'e'):
        print(sentence[i:i+8])
        break
print(sentence[-3:])
# Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
fruits = 0
vegetables = 5
print(f"I eat {vegetables} veggies and {fruits} fruits daily")
# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
s = 'maine 200 banana khaye'
s = s.replace('banana', 'samosa').replace('200', '10')
print(s)
