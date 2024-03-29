input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for i in input_list:
    if i % 2 == 0:
        output_list.append(i)

print("Output List using for loop:", output_list)
print("===================== using comprehension =============================")
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",
      list_using_comp)