from datetime import date


class AgeValidationError(Exception):
    pass


class Person:
    count = 0  # class variable
    MIN_DATE_OF_BIRTH = date(1900, 1, 1)

    def __init__(self, full_name, date_of_birth=None):  # dunder / magic method
        self.name = full_name  # instance variables
        self.date_of_birth = date_of_birth
        self.increment_count()

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        if value and value < self.MIN_DATE_OF_BIRTH:
            raise AgeValidationError('Invalid date of birth.')
        self._date_of_birth = value

    @property
    def age(self):
        if not self.date_of_birth:
            raise AgeValidationError('Cannot compute age.')
        return self.compute_age(self.date_of_birth)

    def salute(self, greeting):  # instance method
        print(f'{self.name} says "{greeting}!"')

    @classmethod
    def increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def compute_age(date_of_birth):
        delta = date.today() - date_of_birth
        return int(delta.days / 365.25)

    def __str__(self):
        return f'{self.__class__.__name__} object: name={self.name}'

    def __int__(self):
        return self.age


class Student(Person):
    count = 0

    def __init__(self, full_name, university, date_of_birth=None):
        super().__init__(full_name, date_of_birth)
        self.university = university

    def salute(self, greeting):
        print(f'{greeting}! I study at {self.university}!')

    def study(self):
        print(f'{self.name} is studying...')


if __name__ == '__main__':
    anna = Person('Anna', date(1980, 1, 1))
    print(anna)

    try:
        anna.date_of_birth = date(1800, 1, 1)
    except AgeValidationError as ex:
        print(ex)

    print(anna.date_of_birth)

    print(anna.name, anna.age)
    print(Person.count)

    john = Person('John')
    print(john.name)
    print(Person.count)

    john.height = 1.85
    print('John has height attribute:', hasattr(john, 'height'))
    print(john.name, john.height)
    del john.height
    print('John has height attribute:', hasattr(john, 'height'))

    anna.salute('Hi')
    john.salute('Good morning')

    print(anna, john)
    print(int(anna))

    Person.salute(anna, 'Hello')
    anna.salute('Hello')

    print(Person.compute_age(date(1985, 2, 12)))

    mike = Student('Mike', 'Politehnica', date(1999, 5, 29))
    print(mike, mike.age, int(mike))
    mike.salute('Hey')

    print(Student.count)
    mike.study()