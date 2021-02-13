# After flipping a coin 10 times you got this result, Using for loop figure out how many times you got heads
result = ["heads", "tails", "tails", "heads", "tails",
          "heads", "heads", "tails", "tails", "tails"]

list_items = len(result)
count = 0
for i in range(list_items):
    if(result[i] == 'heads'):
        count += 1
print(f'You have got heads {count} times')

# Print square of all numbers between 1 to 10 except even numbers
for i in range(11):
    if(i % 2 == 0):
        continue
    print(i**2)

# star pattern
limit = 10
for i in range(1, limit):
    for j in range(1, i):
        print("#", end='')
    print('\n')
#
