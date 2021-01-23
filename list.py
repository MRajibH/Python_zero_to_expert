# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# 1. In Feb, how many dollars you spent extra compare to January?
expense = [2200, 2350, 2600, 2130, 2190]

Extra_cost = expense[1] - expense[0]
print(Extra_cost)
# 2. Find out your total expense in first quarter (first three months) of the year.
quarter = 0
for i in range(3):
    quarter += expense[i]
print(quarter)
# 3. Find out if you spent exactly 2000 dollars in any month
length = len(expense)
yes = False
for i in range(length):
    if expense[i] == 2000:
        yes = True
    else:
        yes = False
if (yes):
    print('yes you spend exactly $2000 in any of the month')
else:
    print("No you don't spend exactly $2000 in any of the month")
# Alternative Method
decision = 2000 in expense
if (decision):
    print('yes you spend exactly $2000 in any of the month')
else:
    print("No you don't spend exactly $2000 in any of the month")

    # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print(expense)
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expense[3] = expense[3]-200
print(expense)
# You have a list of your favourite marvel super heros.
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# 1. Length of the list
print(len(heros))
# Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
for i in range(len(heros)):
    if heros[i] == 'hulk':
        heros.insert(i+1, 'black Panther')
        break
print(heros)
# Now you don't like thor and hulk because they get angry easily :)So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).Do that with one line of code.
heros[1:3] = ['doctor Strange']
print(heros)
# 5. Sort the list in alphabetical order
heros.sort()
print(heros)
