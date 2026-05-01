# Reference Lists

my_list6 = ["a", "b", "c", "d", "e", "A", "B", "R", "h"]
my_list7 = ["a", "b", "c", "d", "e", "A", "B"]
print(f" my_list6: {my_list6}")
print(f" my_list7: {my_list7}")

print("********************************************************************************")

my_list7 = my_list6
print( f" if my_list7 = my_list6: my_list6 = {my_list6})")
print( f" if my_list7 = my_list6: my_list7 = {my_list7})")
print("********************************************************************************")

my_list6.append("abcdef")
print(f" if my_list6.append(\"abcdef\"): mylist6 = {my_list6}")
print(f" if my_list6.append(\"abcdef\"): my_list7 = {my_list7})")
print("\"abcdef\" is added to my_list6 & my_list7")
print("result : my_list6 & my_list7 are in the same reference")

print("---------------------------------------------------------------------------------")

# copy lists

my_list6 = ["a", "b", "c", "d", "e", "A", "B", "R", "h"]
my_list7 = ["a", "b", "c", "d", "e", "A", "B"]
print(f" my_list6: {my_list6}")
print(f" my_list7: {my_list7}")

print("*********************************************************************************")

my_list7 = my_list6.copy()
print(f" if my_list7 = my_list6.copy(): my_list6={my_list6})")
print(f" if my_list7 = my_list6.copy(): my_list7= {my_list7})")

print("*********************************************************************************")

my_list6.append("abcdef")
print(f" if my_list6.append(\"abcdef\"): mylist6 = {my_list6}")
print(f" if my_list6.append(\"abcdef\"): my_list7 = {my_list7})")
print("\"abcdef\" is added to my_list6 not my_list7")
print("result : my_list6 & my_list7 are not in the same reference")
