import getpass

def simple_ui():
    print("=== Sistem Login ===")
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    print(f"Selamat datang, {username}!")

simple_ui()
# Fungsi: Menyediakan antarmuka pengguna sederhana untuk login.
# Kondisi: Ketika Anda perlu membangun aplikasi CLI dengan input pengguna.
