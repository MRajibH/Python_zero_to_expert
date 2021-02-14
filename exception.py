# Exception are error detected at the time of program execution
''' In programming we needed to handle 
    these exception to stop unexpected crushing of
    program'''
x = (input("Enter Number One: "))
y = (input("Enter Number Two: "))

try:
    result = int(x) / int(y)
except Exception as e:
    print('Exception Occurred! Exception Type: ', type(e).__name__)
    result = None
print(f'Result after dividing is = {result}')
