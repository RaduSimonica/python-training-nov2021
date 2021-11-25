### Aggregations functions exercises
1. Write a function `filter_short_words(word_list, n)` that returns the words in `word_list` shorter than `n`. Use `filter` built-in function.
1. Given a list of tuples `(product, price_eur)`, build the list of `(product, price_ron)`, knowing that the exchange rate is `4.75`. Use `map` built-in function.
    ```python
    def f(tup):
        return (tup[0], tup[1]*4.75)
    ```
1. Write a function that receives any number of strings and returns the list of unique strings ordered by number of appearances (most frequent → least frequent). 
Use `sorted` built-in function.
    
    E.g. `f('hello', 'there', 'hello', 'hi', 'hi', 'hello')` -> `['hello', 'hi', 'there']`

### Decorators exercises
1. Write a decorator that computes (and displays) execution time for a function. 
Hint: `time.time()` function returns current time in seconds.

### OOP exercises
1. Create a `BankAccount` class that receives two parameters on initialisation: 
    * `bank name (str)`
    * `balance (int)`
1. Create two methods in this class, one to withdraw money and another one to deposit money into the account. The withdraw method will not allow withdrawing more money than available and it will raise an exception when you attempt to do that.
1. Create a class `Employee` with three instance attributes:
    * `person name (str)`
    * `bank account (BankAccount)`
    * `salary (default 0) (int)`

    1. Use a `property` for salary management. Salary should be set only on initialisation; you shouldn't be able to set the salary from outside the class.
    1. Write a method `raise_salary` that receives a parameter `percent` that should be one of the following values: 5, 10, 20. Raise a `ValueError` if another value is received by this method.
    The `raise_salary` method should raise the salary with 5%, 10% or 20%.
    1. Create a method `receive_salary` that will deposit in the employee's bank account an amount equal to its salary.
1. Create a `CreditBankAccount` class inherits `BankAccount` and receives one extra argument at initialisation which allows for the balance to go below zero (but not under `-overdraft`): 
    * `overdraft (int)`

    1. Override parent `withdraw` method so that the new rule is implemented.
1. Place the two bank account classes in a Python module and the employee class in another Python module. Create a third module that uses the first two modules.

#### Magic methods exercises [optional]

1. Create class `Dish` - instance attributes: `id (int)`, `name (str)`, `price (int)`
1. Create class `Menu` - instance attributes: `dishes (list of Dish objects)`.

    Implement appropriate methods so that `Menu` objects support the following operations:
    ```python
    d = Dish(0, 'Lasagna', 20)
    m = Menu()
    m += d  # dish appended to m.dishes
    m[0]  # implement getitem on Menu
    d in m  # implement membership test operators
    len(m)  # return length of m.dishes
    ```