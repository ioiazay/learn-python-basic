file_name = "my_file_2.txt"

file = open(file_name, "r")
print(file.read())
file.close()


edit_file = open(file_name, "w")
edit_file.write("Yomama Patrict")
edit_file.close()


new_file = open(file_name, "r")
print(new_file.read())
new_file.close()