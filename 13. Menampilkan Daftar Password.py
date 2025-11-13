import getpass

passwords = []

for _ in range(3):
    password = getpass.getpass("Masukkan password: ")
    passwords.append(password)

print("Password yang dimasukkan:", passwords)
# Fungsi: Menyimpan beberapa password dalam list.
# Kondisi: Ketika Anda ingin mengumpulkan beberapa password dari pengguna.
