ages = {"Agus": 20, "Sama": 33, "Jimin": 17}
ages["Jimin"] = 22
print(ages["Agus"])
print(ages["Jimin"])

primary_color = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255]
}

try:
    print(primary_color["red"])
    print(primary_color["yellow"])
except KeyError:
    print("key not found")