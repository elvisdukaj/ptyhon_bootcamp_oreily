f = open("test.txt", "w")
f.write("line1\n")
f.write("line2\n")
f.write("line3\n")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()


f = open("test.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()


f = open("test.txt", "r")
for line in f.readlines():
    print(f"the line is {line}")
f.close()


with open("test.txt", "r") as f:
    for line in f.readlines():
        print(f"inside the context: {line}")