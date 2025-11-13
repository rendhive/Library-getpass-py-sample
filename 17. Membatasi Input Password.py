import getpass

def limited_password():
    max_attempts = 3
    correct_password = "securePassword456"
    
    for _ in range(max_attempts):
        password = getpass.getpass("Masukkan password: ")
        if password == correct_password:
            print("Akses diberikan!")
            return
        else:
            print("Password salah, coba lagi.")
    print("Akses ditolak setelah beberapa percobaan.")

limited_password()
# Fungsi: Membatasi pengguna pada jumlah percobaan memasukkan password.
# Kondisi: Ketika Anda ingin meningkatkan keamanan dengan membatasi percobaan login.
