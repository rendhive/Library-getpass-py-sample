import getpass

def verify_password():
    password = getpass.getpass("Masukkan password Anda: ")
    return password == "mypassword"

if verify_password():
    print("Password valid!")
else:
    print("Password invalid!")
# Fungsi: Memverifikasi password dalam sebuah fungsi.
# Kondisi: Saat Anda ingin mengisolasi logika verifikasi password di dalam fungsi.
