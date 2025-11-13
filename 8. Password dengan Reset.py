import getpass

def reset_password():
    new_password = getpass.getpass("Masukkan password baru: ")
    return new_password

password = reset_password()
print("Password reset berhasil!")
# Fungsi: Mengatur ulang password pengguna.
# Kondisi: Ketika Anda perlu memberikan pengguna opsi untuk mengubah password mereka.
