# import my_module # importerar en fil i vårt eget projekt

# print(my_module.greet("Maria")) # greet är funktionen
# print(my_module.add(10, 25))
# print(my_module.PI)

# from my_module import greet, add # importerar bara delar av modulen
# print(greet("Maria"))
# print(add(26, 33))

# from my_package import module1, module2

# print(module1.function1())
# print(module2.function2())

# from my_package.module1 import function1

# print(function1())

# __name__
# __main__
# om ett program körs som en skript eller en modul

# def main():
#     # mitt program
#     print("Hej då")

# if __name__ == "__main__":
#     main()
# lägger in detta för att koden inte ska köras när den läggs in som en modul