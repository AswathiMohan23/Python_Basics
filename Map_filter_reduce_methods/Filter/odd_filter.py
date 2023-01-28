def is_even(n):
    return n % 2 != 0


nums = [3,2,6,7,8,9,10,12,13,18,15]
filtered_output = filter(is_even,nums)
print("filtered output : ")
for i in filtered_output:
    print(i)