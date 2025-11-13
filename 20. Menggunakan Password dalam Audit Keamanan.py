import getpass

correct_passwords = ["password1", "my_secure_password", "123456"]

def audit_security():
    password = getpass.getpass("Masukkan password untuk audit: ")
    if password in correct_passwords:
        print("Audit diluluskan.")
    else:
        print("Audit ditolak.")

audit_security()
# Fungsi: Memeriksa password dalam konteks audit keamanan.
# Kondisi: Ketika Anda perlu memverifikasi akses ke fungsi tertentu berdasarkan password.
