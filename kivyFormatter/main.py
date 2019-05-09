from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (600, 400)


class FormattingApp(App):
    def build(self):
        return FormattingLayout()


class FormattingLayout(BoxLayout):


    pass


if __name__ == "__main__":
    app = FormattingApp()
    app.run()
