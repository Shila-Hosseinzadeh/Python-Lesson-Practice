#num_list of 0 <= x <= 50 with list comprehension
num_list=[x for x in range(51)]

#even_num_list of 0 <= x <= 50 with List Comprehension
even_num =[x for x in range(51) if x % 2 == 0]

#squared_num_list of 0 <= x <= 50 with List Comprehension
squared_num = [x**2 for x in range(51)]

print(f"num_list of 0 <= num <= 50 : {num_list} ")
print(f"even_num of 0 <= num <= 50 : {even_num} ")
print(f"squared_num of 0 <= num <= 50 : {squared_num} ")
