name = 'george'
age = 40

print("My name is", name.capitalize(), "and my age next year is", age + 1)

# %-formatting
message = "My name is %s and my age next year is %d" % (name, age + 1)
print(message)

# str.format()
message = "My name is {} and my age next year is {}".format(name, age + 1)
print(message)

message = "My name is {name} and my age next year is {age}".format(
    age=age + 1, name=name.capitalize())
print(message)

person = {'name': name.capitalize(), 'age': age + 1, 'location': 'Bucharest'}

message = "My name is {name} and my age next year is {age}".format(**person)
print(message)

# f-strings
message = f'My name is {name.capitalize()} and my age next year is {age + 1}.'
print(message)
