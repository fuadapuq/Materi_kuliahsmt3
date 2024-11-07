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


class Seller(User):
    def _init_(self, username, email, userId):
        super()._init_(username, email, userId)
        self.products = {}  # Menyimpan produk dalam bentuk dictionary

    def addProduct(self, productName, description, price, stock):
        productId = len(self.products) + 1  # ID produk berdasarkan jumlah produk yang ada
        self.products[productId] = {
            'name': productName,
            'description': description,
            'price': price,
            'stock': stock
        }
        print(f"Produk '{productName}' telah ditambahkan dengan ID: {productId}.")

    def processOrder(self, orderId, status):
        print(f"Pesanan ID {orderId} telah diproses dengan status: '{status}'.")


class Admin(User):
    def _init_(self, username, email, userId):
        super()._init_(username, email, userId)

    def manageUsers(self):
        print("Mengelola pengguna...")

    def viewReports(self):
        print("Melihat laporan...")

# Contoh penggunaan kelas Seller dan Admin
if _name_ == "_main_":
    seller1 = Seller("seller_john", "seller_john@example.com", 1)
    
    # Mencoba login
    seller1.login("seller_john", "seller_john@example.com")  # Login berhasil
    
    # Menambahkan produk
    seller1.addProduct("Produk A", "Deskripsi Produk A", 100.00, 50)
    seller1.addProduct("Produk B", "Deskripsi Produk B", 200.00, 30)
    
    # Memproses pesanan
    seller1.processOrder(101, "dalam pengiriman")
    seller1.processOrder(102, "selesai")
    
    # Logout
    seller1.logout()  # Logout berhasil

    # Contoh penggunaan kelas Admin
    admin1 = Admin("admin_jane", "admin_jane@example.com", 2)
    
    # Mencoba login
    admin1.login("admin_jane", "admin_jane@example.com")  # Login berhasil
    
    # Mengelola pengguna dan melihat laporan
    admin1.manageUsers()
    admin1.viewReports()
    
    # Logout
    admin1.logout()  # Logout berhasil