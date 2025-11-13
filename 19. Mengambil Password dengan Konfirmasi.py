import getpass

def confirm_password():
    password = getpass.getpass("Masukkan password baru: ")
    confirm = getpass.getpass("Konfirmasi password baru: ")

    if password == confirm:
        print("Password telah diatur!")
    else:
        print("Password tidak cocok!")

confirm_password()
# Fungsi: Mengizinkan pengguna untuk mengonfirmasi password baru.
# Kondisi: Ketika Anda ingin memastikan pengguna mengetik password dengan benar.
