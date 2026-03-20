# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(developer):
    capital = []
    capitalize_list_items = developer
    for item in capitalize_list_items:
      print(capitalize_list_items)
    return capital

def capitalize_list_items(list):
  cap_list = []
  for i in range(len(list)):
    cap_list.r(list[i])
  return cap_list

def capitalize_list_items(list):
  cap_list = ['carrot','apple','banana']
  for i in range(len(list)):
    cap_list.append(list[i].upper())
  return cap_list
print(capitalize_list_items)

capitalize_list_items(['carrot','apple','banana'])

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(my_list, new_item):
  my_list.append(new_item)
  return add_item
my_list = [1, 2, 3]
new_item = 4
updated_list = add_item(my_list, new_item)
print(f"Original list: {my_list}")


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
add_item = ['Meat']
print(food_staff + add_item)

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(input_list, item_to_remove):
  # Create a new list using list comprehension, excluding the item to be removed
  new_list = [item for item in input_list if item != item_to_remove]
  return new_list
food_stuff = [ 'banana', 'orange', 'apple', 'grapes']
item_to_remove = 'apple'
# Call the function
updated_food_list = remove_item(food_stuff, item_to_remove)
# Print the results
print(f"Original list: {food_stuff}")
print(f"Item to remove: {item_to_remove}")
print(f"Updated list: {updated_food_list}")

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
  if n < 1:
    return 0
  return sum(range(1, n + 1))
input_number = 5
total = sum_of_numbers(input_number)
print(total)