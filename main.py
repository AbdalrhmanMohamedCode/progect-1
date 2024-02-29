from kivy.app import App
from kivy.core.window import Window
Window.size = (400 , 600)
class Group(App):

    def build(self) :
        self.title='Abdalrhman [LOGIN.SIGNUP]'
    pass
if __name__=='__main__':
    Group().run()
