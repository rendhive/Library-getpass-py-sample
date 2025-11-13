import getpass

def login():
    attempts = 3
    correct_password = "mysecret"

    while attempts > 0:
        password = getpass.getpass("Masukkan password: ")
        if password == correct_password:
            print("Login sukses!")
            return
        else:
            attempts -= 1
            print(f"Password salah. Sisa percobaan: {attempts}")

login()
# Fungsi: Mengizinkan pengguna untuk mencoba login beberapa kali.
# Kondisi: Ketika Anda ingin memberikan pengguna beberapa kesempatan untuk masuk.
