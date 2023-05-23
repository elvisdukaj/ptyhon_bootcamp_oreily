i = 0

for i in range(5, 10, 1):
    print(f'hello {i}')



my_list = ['a', 'b', 'c', 'd']
second_list = ["test", "test"]
for value in my_list:
    for second_value in second_list:
        total_value = value + second_value
        print(f"total_value is {total_value}")


for _ in my_list:
    print(".")

for a in my_list:
    print(".")


names = ["elvis", "stefanie"]
ages = [36, 34]

for name, age in zip(names, ages):
    print(f"{name} {age}")