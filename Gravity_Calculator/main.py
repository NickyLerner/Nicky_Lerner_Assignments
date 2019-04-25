from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

G = 6.67e-11


Window.size = (300, 400)


class GravityApp(App):
    def build(self):
        return GravityLayout()


class GravityLayout(BoxLayout):
    def gravitize(self, obj1, obj2, distance):
        equation = "(" + str(obj1) + "*" + str(obj2) + "*" + str(G) + ")" + "/" + str(float(distance)**2)
        eval(equation)


if __name__ == "__main__":
    app = GravityApp()
    app.run()
