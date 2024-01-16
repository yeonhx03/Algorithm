num_1 = int(input())
num_2 = int(input())
num_2_3 = num_2 // 100
num_2_2 = (num_2 - num_2_3 * 100) // 10
num_2_1 = num_2 - (num_2_3 * 100) - (num_2_2 * 10)
first_line = num_1 * num_2_1
second_line = num_1 * num_2_2
third_line = num_1 * num_2_3
result = num_1 * num_2

print(f"{first_line}\n{second_line}\n{third_line}\n{result}")