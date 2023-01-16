input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {}

# Using loop for constructing output dictionary
for i in input_list:
    if i % 2 == 0: # even numbers
        output_dict[i] = i

print("Output Dictionary using for loop:",
      output_dict)