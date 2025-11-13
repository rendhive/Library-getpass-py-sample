import getpass

password = getpass.getpass("Masukkan password: ")
confirm_password = getpass.getpass("Konfirmasi password: ")

if password == confirm_password:
    print("Password telah dikonfirmasi!")
else:
    print("Password tidak cocok!")
# Fungsi: Meminta pengguna untuk mengkonfirmasi password mereka.
# Kondisi: Ketika Anda ingin memastikan pengguna mengetikkan password dengan benar.
