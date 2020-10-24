file_name = "my_file_2.txt"

try:
    with open(file_name, "r") as file:
        print(file.read())
finally:
    file.close()