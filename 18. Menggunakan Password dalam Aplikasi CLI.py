import getpass

def app_login():
    print("=== Aplikasi Login ===")
    password = getpass.getpass("Masukkan password untuk masuk: ")
    if password == "applicationPassword":
        print("Login berhasil!")
    else:
        print("Login gagal!")

app_login()
# Fungsi: Menggunakan input password dalam aplikasi berbasis CLI.
# Kondisi: Ketika Anda membangun aplikasi yang memerlukan autentikasi pengguna.
