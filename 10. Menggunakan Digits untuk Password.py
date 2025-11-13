import getpass

password = getpass.getpass("Masukkan password (harus berisi setidaknya satu digit): ")

if any(char.isdigit() for char in password):
    print("Password valid!")
else:
    print("Password harus mengandung setidaknya satu digit!")
# Fungsi: Memastikan bahwa password memiliki setidaknya satu digit.
# Kondisi: Ketika Anda ingin mengharuskan pengguna untuk menggunakan karakter tertentu dalam password.
