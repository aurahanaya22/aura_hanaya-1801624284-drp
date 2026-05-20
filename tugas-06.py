from datetime import datetime

print("hi! selamat pagi")
print("ini ada beberapa pilihan, coba dilihat dan dibaca dulu ya!")
print("mau sarapan")
print("mau pergi kerja")

aktivitas = input ("masukkan aktivitas yang ingin kamu lakukan sekarang:")

if aktivitas.lower() == "mau sarapan":
   
    print("ini ada beberapa pilihan menu makanan, silahkan dipilih terlebih dahulu ya:")
    print("telur")
    print("ikan")
    print("nugget")

    menu = input ("mau sarapan dengan menu makanan apa?")

    if menu.lower() == "telur" or menu.lower () == "ikan" or menu.lower() == "nugget":
        print (f"baik, {menu} tersedia. silahkan dimasak terlebih dahulu ya!")
    else:
     print(f"wah, kamu harus membeli bahannya terlebih dahulu")

elif aktivitas.lower()== "mau pergi kerja":
   waktu = datetime.now()
   print("waktu kamu pergi kerja, di jam 08.00 pagi ya")
   print(f"sekarang sudah pukul {waktu}")

   if waktu.hour < 08.00:
    print("wah, masih ada waktu yang tersisa, masih bisa olahraga dulu ya!")
   elif waktu.hour == 08.00:
    print("wah, sudah jam 08.00, selanjutnya lebih awal ya, supaya tidak buru-buru") 
   else: 
    print("waduh, kamu sudah terlambat, lain kali, kamu harus bangun dan siap-siap lebih pagi ya!")