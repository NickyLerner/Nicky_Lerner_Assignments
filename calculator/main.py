from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400)


class CalcApp(App):
    def build(self):
        return CalcLayout()


class CalcLayout(BoxLayout):
    def calculate(self, text):
        try:
            answer = round(eval(text), 2)
            self.display.text = str(answer)
        except:
            self.display.text = "error"

    def tack(self, text):
        self.display.text += text

    def ac(self):
        self.display.text = ""


if __name__ == "__main__":
    '''my_equation = "2+3"
    print(eval(my_equation))'''
    app = CalcApp()
    app.run()
