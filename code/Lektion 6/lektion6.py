## args ## när man inte vet hur många parametrar som programmet ska vara
## kwargs ## man kan ha flera olika listor

# def function_name(*args):
#     for arg in args:
#         print(arg)
# function_name(1,1,1,1,1,1,1,1,1,1)

# def print_info(name, *args):
#     print(f"Name: {name}")
#     for arg in args:
#         print(arg)
# print_info("Alice", 30, "Stockholm", "frans", 1, 15)

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_details(name="Alice", age=30, city="Stockholm")

# def print_all(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_all(1, 2,  3, name="Alice", age=30, city="Stockholm")

# def sum_numbers(*args):
#     return sum(args)

# print(sum_numbers(1, 2, 3, 4))

# def display_info(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_info(1,2,4, name="Ali", age=37, job="Göteborg")

# def calculate(operation, *args, **kwargs):
#     if operation == "add":
#         return sum(args)
#     elif operation == "subtract":
#         results = args[0]
#         for num in args[1:]:
#             results -= num
#         return results
#     elif operation == "multiply":
#         results = 1
#         for num in args:
#             results *= num
#         return results
#     elif operation == "divide":
#         results = args[0]
#         try:
#             for num in args[1:]:
#                 results /= num
#         except ZeroDivisionError:
#             return "Can't devide by zero"
#         return results
#     else:
#         return "Unknown operation"
    
# print(calculate("add", 1, 2, 3, 4))
# print(calculate("subtract", 10, 2, 3))
# print(calculate("multiplay", 2, 3, 4))
# print(calculate("divide", 10, 2, 5))

## lambda 

# add = lambda x, y: x + y
# print(add(2, 3))

# def add(x, y): # samma som ovan
#     return x + y

# def apply_func(f, x, y):
#     return f(x, y)

# result = apply_func(lambda a, b: a * b, 4, 5)
# print(result)

# map(function, iterable)

# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))

# print(squared_numbers)

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x * x, numbers))
# print(squared_numbers)

## filter ## villkor i funktionen som returnerar True eller False

# filter(function, iterable)

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

# number = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, number))
# print(even_numbers)

## nest statement ##

# def check_number(num):
#     if num > 0:
#         if num % 2 == 0:
#             print(f"{num} is a positive even number")
#         else:
#             print(f"{num} is a positive odd number")
#     else:
#         if num == 0:
#         print(f"{num} is 0")
#         else:
#             print(f"{num} is a negative number")

# check_number(10)
# check_number(-5)

# def print_matrix(matrix):
#     for row in matrix:
#         for element in row:
#             print(element, end=" ")
#         print()
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print_matrix(matrix)

## scope ##

# def my_function():
#     local_var = 10
#     print(local_var)

# my_function()
# print(local_var)

# global_var = 20

# def my_function():
#     print(global_var)

# my_function()
# print(global_var)

# def outer_function():
#     outer_var = "Yttre"

#     def inner_function():
#         inner_var = "Inre"
#         print(outer_var)
#         print(inner_var)

#     inner_function()
    
# outer_function()

# x = 10

# def modify_global():
#     global x
#     x = 20

# modify_global()
# print(x)

# global = är en icke lokal variabel

# def outer_function():
#     x = "outer"

#     def inner_function():
#         nonlocal x
#         x = "inner"
#         print(x)
#     inner_function()
#     print(x)
# outer_function()

## pip ## pakethanterare







