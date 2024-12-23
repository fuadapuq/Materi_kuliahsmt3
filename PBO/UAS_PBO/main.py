from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner


# Encapsulation: Define a Rental class with protected attributes and methods
class Rental:
    def __init__(self, nama, email, gadget, durasi):
        self._nama = nama
        self._email = email
        self._gadget = gadget
        self._durasi = durasi

    def get_details(self):
        return f"Nama: {self._nama}\nEmail: {self._email}\nGadget: {self._gadget}\nDurasi: {self._durasi} Hari"

    def set_details(self, nama, email, gadget, durasi):
        self._nama = nama
        self._email = email
        self._gadget = gadget
        self._durasi = durasi


# Inheritance: Subclass that extends the RentalForm class to add custom features
class RentalFormWithDiscount(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Rental form widgets
        self.nama_input = TextInput(hint_text="Masukkan Nama Lengkap", multiline=False)
        self.email_input = TextInput(hint_text="Masukkan Email", multiline=False)
        self.gadget_spinner = Spinner(text="Pilih Gadget", values=("Laptop", "Smartphone"))
        self.durasi_input = TextInput(hint_text="Masukkan Durasi (hari)", multiline=False)
        self.discount_input = TextInput(hint_text="Masukkan Kode Diskon (Opsional)", multiline=False)

        # Buttons
        self.submit_button = Button(text="Kirim")
        self.submit_button.bind(on_press=self.submit_form)

        self.read_button = Button(text="Lihat Data")
        self.read_button.bind(on_press=self.show_rentals)

        # Add widgets to layout
        self.add_widget(self.nama_input)
        self.add_widget(self.email_input)
        self.add_widget(self.gadget_spinner)
        self.add_widget(self.durasi_input)
        self.add_widget(self.discount_input)
        self.add_widget(self.submit_button)
        self.add_widget(self.read_button)

        # Initialize rental data list
        self.rentals = []

    def submit_form(self, instance):
        nama = self.nama_input.text
        email = self.email_input.text
        gadget = self.gadget_spinner.text
        durasi = self.durasi_input.text
        discount_code = self.discount_input.text

        if discount_code:
            if discount_code == "DISCOUNT10":
                popup = Popup(title="Diskon Valid", content=Label(text="Diskon 10% diterapkan!"), size_hint=(0.5, 0.5))
                popup.open()
            else:
                popup = Popup(title="Diskon Tidak Valid", content=Label(text="Kode diskon tidak valid!"), size_hint=(0.5, 0.5))
                popup.open()

        # Validate and add rental data
        if not nama or not email or not durasi or gadget == "Pilih Gadget":
            popup = Popup(title="Error", content=Label(text="Semua field harus diisi dengan benar!"), size_hint=(0.5, 0.5))
            popup.open()
        else:
            rental = Rental(nama, email, gadget, durasi)
            self.rentals.append(rental)
            popup = Popup(title="Konfirmasi Transaksi", content=Label(text=f"Transaksi Penyewaan Gadget\n\n{rental.get_details()}"), size_hint=(0.5, 0.5))
            popup.open()

            # Clear input fields
            self.nama_input.text = ""
            self.email_input.text = ""
            self.durasi_input.text = ""
            self.gadget_spinner.text = "Pilih Gadget"

    def show_rentals(self, instance):
        if not self.rentals:
            popup = Popup(title="Data Kosong", content=Label(text="Tidak ada data penyewaan."), size_hint=(0.5, 0.5))
            popup.open()
        else:
            rentals_list = "\n".join([rental.get_details() for rental in self.rentals])
            popup = Popup(title="Daftar Penyewaan", content=Label(text=rentals_list), size_hint=(0.7, 0.7))
            popup.open()


class RentalApp(App):
    def build(self):
        return RentalFormWithDiscount()  # Use the subclass with added discount functionality


if __name__ == '__main__':
    RentalApp().run()
