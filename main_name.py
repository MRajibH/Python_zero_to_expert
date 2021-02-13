# if __main__ == __name__ is used as an entry point of python progam like main function in c/c++ program.


def area(height, weight):
    print(__name__)
    return height * weight


if __name__ == "__main__":
    result = area(10, 20)
    print(result)
