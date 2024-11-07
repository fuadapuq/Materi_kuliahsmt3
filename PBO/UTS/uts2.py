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


class BasicUser (User):
    def _init_(self, username, email, userId):
        super()._init_(username, email, userId)
        self.cart = {}

    def viewProduct(self, productId):
        # Simulasi informasi produk
        products = {
            1: "Produk A: Deskripsi Produk A",
            2: "Produk B: Deskripsi Produk B",
            3: "Produk C: Deskripsi Produk C"
        }
        
        product_info = products.get(productId, "Produk tidak ditemukan.")
        print(product_info)

    def addToCart(self, productId, quantity):
        if quantity <= 0:
            print("Jumlah produk harus lebih dari 0.")
            return
        
        if productId in self.cart:
            self.cart[productId] += quantity
        else:
            self.cart[productId] = quantity
        
        print(f"Produk ID {productId} telah ditambahkan ke keranjang dengan jumlah {quantity}.")

# Contoh penggunaan kelas BasicUser 
if _name_ == "_main_":
    user1 = BasicUser ("john_doe", "john@example.com", 1)
    
    # Mencoba login
    user1.login("john_doe", "john@example.com")  # Login berhasil
    
    # Melihat produk
    user1.viewProduct(1)  # Melihat informasi produk A
    user1.viewProduct(4)  # Melihat informasi produk yang tidak ada
    
    # Menambahkan produk ke keranjang
    user1.addToCart(1, 2)  # Menambahkan 2 produk A
    user1.addToCart(2, 1)  # Menambahkan 1 produk B
    user1.addToCart(3, 0)  # Jumlah produk harus lebih dari 0
    user1.addToCart(4, 1)  # Produk ID tidak ada
    
    # Logout
    user1.logout()  # Logout berhasil