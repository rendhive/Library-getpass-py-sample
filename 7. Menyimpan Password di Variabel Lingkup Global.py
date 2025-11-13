import getpass

def store_password():
    global user_password
    user_password = getpass.getpass("Masukkan password untuk disimpan: ")

store_password()
print("Password disimpan.")
# Fungsi: Menyimpan password ke dalam variabel global.
# Kondisi: Ketika Anda ingin menggunakan password di banyak fungsi tanpa melewatkannya sebagai argumen.
