def element_exists(element, my_list):
    return element in my_list

my_list = [1, 2, 3, 4, 5]
element = 5

if element_exists(element, my_list):
    print(element, "exists in the list.")
else:
    print(f"{element} does not exist in the list.")