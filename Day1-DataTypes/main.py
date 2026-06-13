# String
name = "Adonai"
# Integer
year_of_study = 2
# Float
cgpa = 0.00
# Boolean

is_learning_dsa = True
print("=== Student Profile ===")
print("Name:", name)
print("Year:", year_of_study)
print("CGPA:", cgpa)
print("Learning DSA:", is_learning_dsa)

print("\n=== Data Types ===")
print(type(name))
print(type(year_of_study))
print(type(cgpa))
print(type(is_learning_dsa))

# Type Conversion
year_text = str(year_of_study)
print("\nConverted Year:", year_text)
print(type(year_text))

# User Input
favorite_language = input("Enter your favorite programming language: ")
print("Favorite Language:", favorite_language)

age = int(input("Enter your age: "))
print("Current Age:", age)
print("Next Year Age:", age + 1)
