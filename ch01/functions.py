def print_if_even(number):
    if (number % 2):
        return
    print(number)


count = 0
while count < 20:
    print_if_even(count)
    count += 1


def add_number(number):
    return number + 1


start_number = 1
print(f'{add_number(start_number)}')
print(f'{add_number(start_number)}')
print(f'{add_number(start_number)}')


def add_and_substruct(number_1, number_2, *args, **kargs):
    print(args)
    print(kargs)
    return number_1 + number_2, number_1 - number_2


my_dict = {'number_1': 1,
           'number_2': 3
           }

my_arr = [1, 3]

print(add_and_substruct(**my_dict))
print(add_and_substruct(*my_arr))
print(add_and_substruct(*my_arr, 1, 2, 3, 4, test_1=1, test_2=2, test_3=3))

