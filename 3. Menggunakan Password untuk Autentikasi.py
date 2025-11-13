import getpass

correct_password = "securepassword123"
password = getpass.getpass("Masukkan password untuk autentikasi: ")

if password == correct_password:
    print("Autentikasi berhasil!")
else:
    print("Password salah!")
# Fungsi: Memeriksa password yang dimasukkan pengguna untuk autentikasi.
# Kondisi: Ketika Anda perlu mengamankan akses ke sistem atau aplikasi.
