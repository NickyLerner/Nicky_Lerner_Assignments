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
            answer = eval(text)
            self.display.text = str(answer)
        finally:
            pass


if __name__ == "__main__":
    '''my_equation = "2+3"
    print(eval(my_equation))'''
    app = CalcApp()
    app.run()
