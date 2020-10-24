ages = {"Agus": 20, "Sama": 33, "Jimin": 17}

if "Jamed" not in ages:
    print(True)
else:
    print(False)


print(ages.get("Agus"))
print(ages.get("Sama"))
print(ages.get("Jamed"))
print(ages.get("Jamed Son", "Jamed Tidak Ditemukan"))
