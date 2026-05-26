user = input("Masukan username!")

print(f"\n 🦭 1. Papan Catur Input Kegiatan {user}🦭")

for baris in range (8):
    for kolom in range (8):
        if (baris + kolom) % 2 == 0:
            print ("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"\n 🦭 2. Daftar Aktivitas {user}🦭")

Daftar_aktivitas = []
Jumlah_aktivitas = int(input("Berapa banyak aktivitas yang ingin ditambahkan? "))

for i in range(Jumlah_aktivitas):
    print()
    print(f"\n🦭Aktivitas ke-{i+1}🦭")

    Nama_aktivitas = input("Nama aktivitas: ")
    Waktu_aktivitas = input("Waktu aktivitas: ")
    Durasi_aktivitas = input("Durasi aktivitas: ")
    Tempat_aktivitas = input("Tempat aktivitas: ")

    Aktivitas= {
        "Aktivitas": Nama_aktivitas,
        "Waktu": Waktu_aktivitas,
        "Durasi": Durasi_aktivitas,
        "Tempat": Tempat_aktivitas
    }
    Daftar_aktivitas.append(Aktivitas)
print()

print(f"\n🦭Daftar aktivitas yang sudah {user} masukkan🦭")

for i in range(len(Daftar_aktivitas)):
    print(f"Aktivitas {i + 1}")
    print(f"Nama aktivitas: {Daftar_aktivitas[i]['Aktivitas']}")
    print(f"Waktu aktivitas: {Daftar_aktivitas[i]['Waktu']}")
    print(f"Durasi aktivitas: {Daftar_aktivitas[i]['Durasi']}")
    print(f"Tempat aktivitas: {Daftar_aktivitas[i]['Tempat']}")
    print()