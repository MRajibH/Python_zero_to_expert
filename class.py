# Class
''' 
Class is a user defined data type. It consists of data members or attributes(properties of the class) and member fuctions (also Known as methods)which can be accessed and used by creating an instance of that class (known as Objects). It represents set of prperties or methods that are common to all objects. A class is like a blueprint for an objects. 
 '''
# Objects
'''
Object is a basic unit of Object oriented programming.
An object is a instance of a class. When a class is defined no memory is allocated. But but when it is instantiated (i.e. an object is created) memory is allocated. An object has an identity, state, and behavior. Each object contains data and code to manipulate the data. Objects can interact without having to know details of each other’s data or code, it is sufficient to know the type of message accepted and type of response returned by the objects. 

For example “Dog” is a real-life Object, which has some characteristics like color, Breed, Bark, Sleep, and Eats.
'''
# init
'''__init__ is a reserved method in python classes. It is known as a constructor in OOP concepts. This method called when an object is created from the class and it allows the class to initialize the attributes  of a class.'''


class Human:
    def __init__(self, name, occupation, gender):
        self.name = name
        self.gender = gender
        self.occupation = occupation

    def work(self):
        if(self.occupation == 'unemployed'):
            print(
                f"{self.name} is saying 'Peter Piper picked a peck of pickled peppers' because of having nothing to do\n")
        if(self.name == 'Anika' and self.gender == 'Female'):
            print(
                f'{self.name} loves  Rajib  and going to marry him\n')
        if(self.occupation == 'Student' and self.gender == 'Male'):
            print(f'''{self.name} is saying 
            'Betty Botter bought some butter,
            How much wood would a woodchuck chuck if a woodchuck could chuck wood? 
            She sells seashells by the seashore. How can a clam cram in a clean cream can? 
            I scream, you scream, we all scream for ice cream,
            I saw Susie sitting in a shoeshine shop' because  he wants to improve his pronunciation\n''')


Anika = Human('Anika', 'unemployed', 'Female')
Anika.work()
Rajib = Human('Rajib', 'Student', 'Male')
Rajib.work()
