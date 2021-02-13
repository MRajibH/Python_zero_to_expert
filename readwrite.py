
'''# writing in a file (overwriting)
f = open("G:\\funny.txt", 'w')
f.write("I love Django \n")
f.close()'''
# writing in a file (append mode)
f = open("G:\\funny.txt", "a")
for i in range(50):
    f.write("A***a loves you, Rajib \n")
f.close()
# Reading a file
f = open("G:\\funny.txt", 'r')
print(f.read())
f.close()
# Reading a file line by line
f = open("G:\\funny.txt", 'r')
for line in f:
    print(line)
