#Linear Search
#Iterate through a collection one item at a time.

def linear_search(array, target):
    for num in array:
        if num == target:
            return True
    return False

num_array = [5,10,15,20,25,30]
target_num = 50

if linear_search(num_array, target_num):
    print("The number", target_num, "is in the array")
else:
    print("The number", target_num, "is not in the array")


#search for name in array
def linear_search_name(names, target_name):
    for name in names:
        if name == target_name:
            return True
    return False


name_list = ["Jace", "Jada", "Jazz", "Jace"]
target_name = "John"

if linear_search_name(name_list, target_name):
    print("The name", target_name, "is in the list!")
else:
    print("The name", target_name, "is not in the list")


#Search based on user input
def input_linear_search(search_list, input_name):
    for name in search_list:
        if name == input_name:
            return True
    return False


search_list = ["Tom", "Peyton", "Alex", "Lamar"]
input_name = input("Please enter a name ")

if input_linear_search(search_list, input_name):
    print("The name", input_name, "is in the list")
else:
    print("The name", input_name, "is not in the list")