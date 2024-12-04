from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class HelloWorld(BoxLayout):
    pass
class HelloWorldApp(App):
    def build(self):

#Metode build adalah metode khusus dalam App
      return HelloWorld()

if __name__ == '__main__':
    HelloWorldApp().run()
#Kode hanya akan dijalankan jika file ini dieksekusi