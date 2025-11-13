import getpass

try:
    password = getpass.getpass("Masukkan password: ")
    print("Password telah diterima.")
except Exception as e:
    print("Terjadi kesalahan:", str(e))
# Fungsi: Menangani kesalahan saat mengambil password.
# Kondisi: Ketika Anda ingin mengantisipasi potensi kesalahan yang mungkin terjadi.
