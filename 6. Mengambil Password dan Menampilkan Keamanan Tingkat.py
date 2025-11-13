import getpass

password = getpass.getpass("Masukkan password Anda: ")

if len(password) < 8:
    print("Password tidak cukup kuat, harus lebih dari 8 karakter!")
else:
    print("Password Anda kuat!")
# Fungsi: Memeriksa kekuatan password berdasarkan panjang.
# Kondisi: Ketika Anda perlu menyarankan pengguna untuk menggunakan password yang lebih kuat.
