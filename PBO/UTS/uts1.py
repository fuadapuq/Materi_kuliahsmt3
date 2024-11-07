class User:
    def _init_(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self, username, email):
        if self.username == username and self.email == email:
            print(f"Pengguna berhasil login dengan nama pengguna: {self.username} dan email: {self.email}.")
        else:
            print("Login gagal. Nama pengguna atau email tidak cocok.")

    def logout(self):
        print(f"Pengguna {self.username} berhasil logout.")

# Contoh penggunaan kelas User
if _name_ == "_main_":
    user1 = User("john_doe", "john@example.com", 1)
    
    # Mencoba login
    user1.login("john_doe", "john@example.com")  # Login berhasil
    user1.logout()  # Logout berhasil

    # Mencoba login dengan informasi yang salah
    user1.login("john_doe", "wrong_email@example.com")  # Login gagal