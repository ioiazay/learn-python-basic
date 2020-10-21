index = int(input("jumlah data: "))

daftar_nama = []
daftar_umur = []

for i in range(0, index):
    print(f"Data ke {i}: ")
    nama = input("Masukkan Nama: ")
    umur = input("Masukkan Umur: ")

    daftar_nama.append(nama)
    daftar_umur.append(umur)

    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Jumlah Data: {len(daftar_nama)}")
    print("")