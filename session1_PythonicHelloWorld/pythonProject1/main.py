
# Initialize a list
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print("List: ", my_list)

# Print sorted list
print("Ascendent list: ", sorted(my_list))


# Print sorted list in descending order
print("Descendent list: ", sorted(my_list, reverse=True))


# Displaying elements with even indices
print("elements with even indices: ", my_list[::2])


# Displaying elements with odd indices
print("elements with odd indices: ", my_list[1::2])


print("elements with 3 as multiple: ", [x for x in my_list if x % 3 == 0])
