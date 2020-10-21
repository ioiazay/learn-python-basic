def jumlahkan(*daftar_angka):
    total = 0
    for angka in daftar_angka:
        total = total + angka
    return total


total = jumlahkan(1, 2, 3)
print(total)
