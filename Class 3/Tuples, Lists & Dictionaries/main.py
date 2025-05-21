# LISTS
my_list = [1, 2, 3, 4, 5]
print("Original List: ",my_list)
my_list.append(6)
print("After appending 6: ",my_list)
my_list.remove(3)
print("After removing 3: ",my_list)
my_list.pop()
print("After popping: ",my_list)
print("First element: ",my_list[0])
print("Sliced List: ",my_list[1:3])

# TUPLES
my_tuple = ("apple", "mango", "banana")
print("Original Tuple: ",my_tuple)
my_tuple = my_tuple + ("orange", "pineapple")
print("After adding elements: ",my_tuple)
print("Length of Tuple: ",len(my_tuple))
# my_tuple[2] = "grapes" Show error cause tuples are immutable

# DICTIONARIES
person = {
    "name": "Kulsoom",
    "age": 19,
    "city": "Karachi"
}
print("Original Dictionary: ",person)
person["age"] = 20
print("After updating age: ",person)
person["country"] = "Pakistan"
print("After adding country: ",person)
del person["city"]
print("After deleting city: ",person)

# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")



