file_name = "my_file.txt"

new_file = open(file_name, "w")
amount_writen = new_file.write("Hola Spongebob")
print(amount_writen)
new_file.close()

file = open(file_name, "r")
print(file.read())
file.close()