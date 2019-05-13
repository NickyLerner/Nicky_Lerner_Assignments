from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (600, 400)


class FormattingApp(App):
    def build(self):
        return FormattingLayout()


class FormattingLayout(BoxLayout):
    def change_text(self, words):
        self.display.text = words


    def light_switch(self, boolean):
        if not boolean:
            self.display.color = 1, 1, 1, 1
        else:
            self.display.color = 0, 0, 0, 0


    def color_change(self, r, g, b):
        Window.clearcolor = r/255, g/255, b/255, 1

if __name__ == "__main__":
    app = FormattingApp()
    app.run()
