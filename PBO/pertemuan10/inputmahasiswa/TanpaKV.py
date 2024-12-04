from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class InputForm(App):
    def build(self):
        self.title = "Data Mahasiswa"
        
        # Layout utama
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Input untuk Nama
        self.nama_input = TextInput(hint_text="Nama", multiline=False)
        layout.add_widget(self.nama_input)
        
        # Input untuk NIM
        self.nim_input = TextInput(hint_text="NIM", multiline=False)
        layout.add_widget(self.nim_input)
        
        # Input untuk Jurusan
        self.jurusan_input = TextInput(hint_text="Jurusan", multiline=False)
        layout.add_widget(self.jurusan_input)
        
        # Tombol untuk menampilkan data
        tampilkan_button = Button(text="Tampilkan Data", size_hint=(1, 0.2))
        tampilkan_button.bind(on_press=self.tampilkan_data)
        layout.add_widget(tampilkan_button)
        
        return layout
    
    def tampilkan_data(self, instance):
        # Mendapatkan data dari input
        nama = self.nama_input.text
        nim = self.nim_input.text
        jurusan = self.jurusan_input.text
        
        # Isi pop-up
        popup_content = BoxLayout(orientation="vertical", padding=10, spacing=10)
        popup_content.add_widget(Label(text=f"Nama: {nama}"))
        popup_content.add_widget(Label(text=f"NIM: {nim}"))
        popup_content.add_widget(Label(text=f"Jurusan: {jurusan}"))
        
        # Tombol tutup pop-up
        tutup_button = Button(text="Tutup", size_hint=(1, 0.2))
        popup_content.add_widget(tutup_button)
        
        # Membuat dan menampilkan pop-up
        popup = Popup(title="Data Mahasiswa", content=popup_content, size_hint=(0.8, 0.6))
        tutup_button.bind(on_press=popup.dismiss)
        popup.open()

# Menjalankan aplikasi
if __name__ == "__main__":
    InputForm().run()
