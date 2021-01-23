# 1 You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
width = 48.8
long = 92
total_area = width*long
print(f'answer 1. = {total_area}\n')
# 2 You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
quantity = 9
cost_per_packet = 1.49
pay = 20
get_back = 20-(1.49*9)
print(f'Answer 2.= {get_back}\n')
# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
total_area2 = 5.5**2
total_cost = total_area2*500
print(f'answer 3 = {total_cost}')

# 4 Print binary representation of number 17
binar = '1010'
bi = int(binar, 2)
print(f'answer 4 = {bi}')

# 5 print 6-5.7 it should be .3 but it is not cause there is no precise way to store fp numbers
print(f'look its not precise(should have been .3->{5-4.7}')
# print newline or specific char/string using end
print('This is ', end='rajib')
