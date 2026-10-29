"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""
name = input("Enter the name: ")
age = input("Enter the age: ")
city = input("Enter the city: ")
country = input("Enter the country: ")

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Country:", country)

person = {
    "name": name,
    "age": age,
    "city": city,
    "country": country
}

print("Person dictionary:", person)

print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Country:", person["country"])

person_age = person.pop("age")
print("Removed age:", person_age)
print("Updated person dictionary:", person)


# 1. In: to create a dictionary, remove the last entry and print the updated dictionary.
# 2. Process: use dictinary function, use the pop function then the print function.
# 3. Out: printed updated dictionary with the last entry removed.
# 4. My object, my five fields, and why those: printed dictionary with last entry removed. 


# Your code below
