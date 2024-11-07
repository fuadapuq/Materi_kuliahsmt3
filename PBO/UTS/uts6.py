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


class PremiumUser (BasicUser ):
    def _init_(self, username, email, userId):
        super()._init_(username, email, userId)

    def applyVoucher(self, voucherCode, cartTotal):
        discount = 0
        if voucherCode == "DISKON10":
            discount = 0.10  # 10% diskon
            print(f"Voucher {voucherCode} diterapkan. Diskon: {discount * 100}%.")
        elif voucherCode == "DISKON20":
            discount = 0.20  # 20% diskon
            print(f"Voucher {voucherCode} diterapkan. Diskon: {discount * 100}%.")
        else:
            print("Voucher tidak valid.")
            return

        totalAfterDiscount = cartTotal * (1 - discount)
        print(f"Total belanja setelah diskon: {totalAfterDiscount:.2f}")

    def requestPrioritySupport(self, issueDescription):
        print(f"Dukungan prioritas telah diminta untuk masalah: '{issueDescription}'.")


class Seller(User):
    def _init_(self, username, email, userId):
        super()._init_(username, email, userId)
        self.products = {}

    def addProduct(self, productName, description, price, stock):
        productId = len(self.products) + 1
        self.products[productId] = {
            'name': productName,
            'description': description,
            'price': price,
            'stock': stock
        }
        print(f"Produk '{productName}' telah ditambahkan dengan ID: {productId}.")