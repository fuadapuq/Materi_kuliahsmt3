import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

class InputForm(App):
    def build(self):
        lbl = Label(text="Data Mahasiswa")
        btn = Button(text= "Tampilkan Data")
        return lbl

InputForm().run()