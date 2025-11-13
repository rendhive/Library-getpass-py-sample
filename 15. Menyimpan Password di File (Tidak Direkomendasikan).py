import getpass

password = getpass.getpass("Masukkan password untuk disimpan: ")

with open('password.txt', 'w') as file:
    file.write(password)

print("Password telah disimpan di 'password.txt'.")
# Fungsi: Menyimpan password ke dalam file.
# Kondisi: **Perhatian!** Ini tidak dianjurkan karena alasan keamanan.
