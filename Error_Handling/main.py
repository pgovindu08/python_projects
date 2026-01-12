try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Some content is written now")
except KeyError as error_message:
    print(f"The key {error_message} does not exit")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height height should not be over 3 meters")

bmi = weight/height ** 2
print(bmi)

raise 