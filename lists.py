################################ List operations ########################################
names = ["Harshith","Ravi","Sonu"]
print("List : ",names)

new_list = names.copy()
print("This is new list copied from old List : ", new_list)

cnt = new_list.count("Sonu")
print(cnt, "number of Sonu are in the list")

new_names = ["Ram","Abhi","Anu"]
names.extend(new_names)
print("Extended List : ",names)

# Removing Anu from list
new_names.remove("Anu")
print("new_names after removing Anu : ",new_names)

# pop is used to remove element at a particular index (position) of a list
new_names = ["Ram","Abhi","Anu"]
new_names.pop(1) # Abhi will be removed from list
print("new_names after removing element at 1 : ",new_names)

names.clear()
print("List Cleared : ",names)

# Sorting a list
numbers = [56,85,12,21,30,56,999,87]
# sort in ascending order
numbers.sort()
print("Numbers after ascending order : ",numbers)
#sort in descending order
numbers.sort(reverse=True)
print("Numbers after descending order : ",numbers)

###########################################################################################

################### Reversing a List ####################################################

# using reverse function of lists
numbers = [56,85,12,21,30,56,999,87]
numbers.reverse()
print("Reversed Numbers : ", numbers)

# using reversed function
numbers = [56,85,12,21,30,56,999,87]
reversed_list = list(reversed(numbers)) """ use reversed function to reverse the list,
but reversed function does not return a list. So typecast(convert) output of reversed
function to a list using 'list' keyword""" # By The Way, """ ... """ represents a multi line comment#
print("Reversed Numbers : ", numbers)

# using slicing trick
numbers = [56,85,12,21,30,56,999,87]
# list[starting_from : until] this is called slicing
reversed_numbers = numbers[::-1]
print("Reversed Numbers : ", numbers)
#################################################################################################
