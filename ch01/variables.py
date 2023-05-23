outside_variable = 5


def test_function(x):
    global outside_variable
    outside_variable = 4
    y = x + outside_variable
    return y


print(test_function(1))
