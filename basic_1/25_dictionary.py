
customer = {
    "Nama": "Fajar",
    "Umur": "28",
    "Alamat": "Bandung"
}

for key in customer:
    value = customer[key]
    print(f"{key}: {value}")


customer["Company"] = "X Foundation"
del customer["Alamat"]
for key, value in customer.items():
    print(f"{key}: {value}")