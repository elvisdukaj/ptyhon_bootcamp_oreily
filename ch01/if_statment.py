test_var = "a"

if test_var == "a":
    print("yes we have a")

age = 15

if age < 18:
    print("sei un minorene!")


country = "USA"

if age < 18:
    if country == "USA":
        print("sei un minorene americano!")

if age < 18 and country == "USA":
    print("sei un minorene americano!")

if 0 <= age <= 18 or (country in ["USA", "US"]):
    print("sei un minorene o sei americano?")
else:
    print("ma che ne so io")


name = "Ben"
age = 80

is_over_18 = age > 18
if is_over_18:
    print("is over 18")

random_value = {"ciao": 1}

if random_value:
    print("test")