with open('file1.txt') as f1:
    file_1_data = f1.readlines()

with open('file2.txt') as f2:
    file_2_data = f2.readlines()


result = [int(num) for num in file_1_data if num in file_2_data]


# Write your code above 👆

print(result)
