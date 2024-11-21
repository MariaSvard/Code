# x = 0
# while x < 10:
#     print(x)
#     if x == 5:
#         break
#     x +=1
    
# x = 0
# while x < 10: # skriver ut udda tal, hoppar över
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)

# x = 0
# while x < 5:
#     print(x)
#     x += 1
#     break
# else:
#     print("Loopen avslutades")

### Input ###

# user_input = input("Ange ett kommando: ")
# print(user_input)

# while True:  # körs föralltid
#     user_input = input("Ange ett kommando: ")
#     if user_input == "exit":
#         break
#     elif user_input == "5":
#         print("Du skrev 5")
#         break
#     else: # för att loopa tillbaka till början
#         print("Fel input, försökt igen")

# använda break eller condition för att stanna så att den inte gå i oändlighet #

# logiska operatörer, and, or och not # Används när man vill kontrollera flera 

# a = True
# b = False
# print(a and b) # kontrollerar om båda är sanna
# print(a or b) # kontrollerar om en är sann
# print(not a) # inverterar värdet

# x = 5
# print(1 < x < 10) # kontrollera om x är mindre än 10 men större än 1
# print(1 < x and x < 10)

# kontrollera input: kolla flera saker samtidigt

# age = int(input("Ange din ålder: ")) # int för att göra om strängen
# if 18 <= age <= 65:
#     print("Du kan jobba")
# else:
#     print("Du kan inte jobba")

## Files ##

# file = open("example.txt", "r") # öppnar man en fil så måste man också stänga den
# content = file.read()
# print(content)
# file.close()

# file = open("example.txt", "r")
# line = file.readline()
# while line:
#     print(line, end='') # varje gång vi printar skapar det en ny rad, lägg till end= för att ta bort
#     line = file.readline()
# file.close()

# print("hello", end='')
# print("world")

# file = open("example.txt", "r")
# lines = file.readlines() # behåller radbrytningstecknet(=end)
# for line in lines:
#     print(line, end='')
# file.close()

# file = open("example.txt", "r")
# lines = file.read().splitlines() # tar bort radbrytningstecken(=end)
# print(lines)

# file = open("example.txt", "w") # kommer ersätta befintlig
# file.write("Exempeltext \n")
# file.write("Nästa rad")
# file.close()

# with open("example.txt", "r") as file: # allt vi för inom indenteringen görs, annars stängs filen
#     content = file.read()
#     print(content)

# with open("output.txt", "w") as file:
#     file.write("Lite text \n")
#     file.write("Lite mer text")

## List comprehension ## kompakt sätt att skapa nya listor

# [expression for item in iterable] # syntax

# numbers = [1,2,3,4,5]
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)

# squares = [num ** 2 for num in numbers] # förkortad och kompakt sätt att skriva, sparar plats
# print(squares)

# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

## set comprehension ## kommer eleminera dubbletter

# numbers = [1,2,3,4,4,5]
# unique_squares = {num ** 2 for num in numbers}
# print(unique_squares)

## Dictionary comprehension ##

# fruits = ["apple", "cherry", "grape"]
# fruit_lengths = {fruit: len(fruit) for fruit in fruits} # först key, sen value, hur vi vill gå igenom
# print(fruit_lengths)

## Enumerate ## om man vill komma ihåg vart man är i listan

# fruits = ["apple", "cherry", "grape"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")

# fruits = ("apple", "cherry", "grape")
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for i, row in enumerate(matrix):
#     for j, value in enumerate(row):
#         print(f"Matrix[{i}{j}] = {value}")

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for i, row in enumerate(matrix):
#     for j, value in enumerate(row):

## zip ##

# name = ["Alice", "Bobbo", "Stefan"] 
# age = [24,37,19]
# for name, age in zip(name, age): # lägger ihop listorna
#     print(f"Namn: {name}, Ålder: {age}")

## input ##

# name = input("Ange ditt namn: ")
# print(name)

## Funktioner ##

# # syntax:
# def function_name(parametrar): #definerar funktionen, döp funktionen, inom paranteserna(variabler, tom)
#     #kod
#     return # returnerar ett resultat

# def greet(name):
#     return f"Hello, {name}"

# print("Test")
# print(greet("Bobbo"))

# def add(a, b):
#     return a + b
# result = add(10, 25)
# print(result)

# def greet(name="World"):
#     return f"Hello {name}"

# print(greet())
# print(greet("Bobbo"))

# återanvänd funtionen:
# def add(a, b):
#     return a + b
# def add_and_square(a,b):
#     sum = add(a,b)
#     return sum * sum

# print(add_and_square(5, 2))

## Logik och funktioner ##

# def categorize_age(age):
#     if age < 13:
#         return "Child"
#     elif age < 20:
#         return "Teenager"
#     elif age < 65:
#         return "Adult"
#     else:
#         return "Retiree"
    
# print(categorize_age(10))
# print(categorize_age(15))
# print(categorize_age(35))
# print(categorize_age(88))

## Tuple unpacking ##

# def add(a,b): # inte fler än 5 argument
#     return a + b

# pair = (3, 5)
# result = add(*pair)
# print(result)

## funktioner i funtioner ## returnera funktioner

# def make_power(exponent):
#     def power(x):
#         return x ** exponent
#     return power

# result = make_power(3)

# print(result(4))

