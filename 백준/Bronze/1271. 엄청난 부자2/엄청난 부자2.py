arr = input().split()
money = int(arr[0])
n = int(arr[1])
per_income = money // n
remain = money % n
print(f"{per_income}\n{remain}")
