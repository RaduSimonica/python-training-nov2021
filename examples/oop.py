class Person:
    count = 0  # class variable

    def __init__(self, name, age=0):  # dunder / magic method
        self.name = name  # instance variables
        self.age = age
        Person.count += 1

    def salute(self, greeting):
        print(f'{self.name} says "{greeting}!"')


if __name__ == '__main__':
    anna = Person('Anna', 20)
    print(anna.name, anna.age)
    print(Person.count)

    john = Person('John')
    print(john.name, john.age)
    print(Person.count)

    john.height = 1.85
    print('John has height attribute:', hasattr(john, 'height'))
    print(john.name, john.age, john.height)
    del john.height
    print('John has height attribute:', hasattr(john, 'height'))

    anna.salute('Hi')
    john.salute('Good morning')