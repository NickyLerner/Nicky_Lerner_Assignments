from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

G = 6.67e-11


Window.size = (600, 400)


class GravityApp(App):
    def build(self):
        return GravityLayout()


class GravityLayout(BoxLayout):
    def gravitize(self, obj1, obj2, distance):
        try:
            self.display.font_size = 40
            equation = "(" + str(obj1) + "*" + str(obj2) + "*" + str(G) + ")" + "/" + str(float(distance)**2)
            answer = eval(equation)
            self.display.text = str(answer)
        except ZeroDivisionError:
            self.display.text = "You Cannot Have Two Objects in the Same Place"
            self.display.font_size = 30
        except OverflowError:
            self.display.font_size = 30
            self.display.text = "That's too much stuff"
        except:
            self.display.font_size = 30
            self.display.text = "Please Enter a Value for all Options"


if __name__ == "__main__":
    app = GravityApp()
    app.run()

# for some reason the background color was not changing
