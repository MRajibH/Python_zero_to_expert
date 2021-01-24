'''
Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
'''


def calculate_area(base, height):
    return(0.5 * base * height)


base = float(input("Enter Base: "))
height = float(input("Enter Height:"))
answer = calculate_area(base, height)
print(f'Area of triangle is {answer}')
