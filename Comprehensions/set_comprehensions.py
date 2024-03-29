input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()

# Using loop for constructing output set
for i in input_list:
    if i % 2 == 0:
        output_set.add(i)

print("Even no set : ",output_set)

print("===================== using comprehension =============================")

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
      set_using_comp)