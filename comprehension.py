

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []


for i in fruits:
    newlist.append(i)

# print(newlist)

nl = [x for x in fruits if "a" in x]
n2 = [x for x in fruits if x!='apple']
n3 = [x for x in range(10) if x%2==0]
n4 = [x.upper() for x in fruits ]
# print(nl)
# print(n2)
# print(n3)
# print(n4)

k = [7 for a in fruits if a=="apple" ]
# print("original : ",k)

ls = [a for a in range(10) if a%2!=0]
#print(ls)

#matrix = []
# for i in range(5):
#
#     # Append an empty sublist inside the list
#     matrix.append([])
#     print(matrix)
#     for j in range(5):
#         matrix[i].append(j)

matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)
list_of_list = [[1,2,3],[4,5,6],[7,8]]

# Flatten `list_of_list`
po = [y for x in list_of_list for y in x]
print("po",po)

# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k:v for (k,v) in original_dict.items() if v%2==0 }
print(even_dict)