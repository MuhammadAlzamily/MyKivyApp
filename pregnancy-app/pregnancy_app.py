from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton, MDIconButton, MDFlatButton
from kivymd.uix.toolbar import MDToolbar
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog

Window.size = (300, 500)


app = """

ScreenManager:
    StartScreen:
    GenderScreen:
    TestScreen:
<StartScreen>:
    name:"start"
    BoxLayout:
        orientation:"vertical"
        MDToolbar:
            title:"The Pregnancy App"
            elevation:10
        MDLabel:
            text:"Click to get started"
            halign:"center"
    MDFillRoundFlatButton:
        text:"Get Started"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_press:root.manager.current="genderscreen"
    MDIconButton:
        icon:"discord"
        pos_hint:{'center_x':0.5,'center_y':0.1}
        user_font_size:"48sp"
<GenderScreen>:
    name:"genderscreen"
    BoxLayout:
        orientation:"vertical"
        MDToolbar:
            title:"Select A Gender"
        MDLabel:
            text:"Firstly, pick a gender"
            halign:"center"
    MDFillRoundFlatButton:
        text:"Male"
        pos_hint:{'center_x':0.2,'center_y':0.3}
        on_press:root.manager.current="testscreen"
    MDFillRoundFlatButton:
        text:"Female"
        pos_hint:{'center_x':0.8,'center_y':0.3}
        on_press:root.manager.current="testscreen"
    MDFillRoundFlatButton:
        text:"Back"
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_press:root.manager.current="start"     

<TestScreen>:
    name:"testscreen"
    BoxLayout:
        orientation:"vertical"
        MDToolbar:
            title:"Test Results"
        MDLabel:
            text:"Piss on the screen then press the button below"
            halign:"center"
    MDFillRoundFlatButton:
        text:"Test"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_press:app.show_results()
    MDFillRoundFlatButton:
        text:"Back"
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_press:root.manager.current="genderscreen"

"""


class StartScreen(Screen):
    pass


class GenderScreen(Screen):
    pass


class TestScreen(Screen):
    pass


ss = ScreenManager()
ss.add_widget(StartScreen(name="start"))
ss.add_widget(GenderScreen(name="genderscreen"))
ss.add_widget(TestScreen(name="testscreen"))


class mainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        screen = Screen()
        myapp = Builder.load_string(app)
        screen.add_widget(myapp)
        return screen

    def go_back_to_start(self):
        pass

    def go_back_to_gender(self):
        pass

    def show_results(self):
        self.msg = MDDialog(title="Test Results",
                            text="You're not ready to be a parent since you just pissed on a phone screen to find out if you're going to be one", size_hint=(0.8, 1), buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)])
        self.msg.open()

    def close_dialog(self, obj):
        self.msg.dismiss()


mainApp().run()
