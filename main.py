''' 
PROJECT  © 2022 Amogh Thusoo
VERSION : 0.1
COMPILED THROUGH : WINDOWS 8 : ORACLE VIRTUAL BOX : LINUX OS : UBUNTU 20.04 LTS (VIRTUAL MACHINE) : BUILDOZER

THIS FILE CONTAINS ALL THE METHODS BINDED WITH THEIR RESPECTIVE BUTTONS TO PROVIDE DIFFERENT FUNCTIONALITIES WITHIN THE APP.

CAUTION :- IF YOU ARE USING THIS APP ON WINDOWS, MACOS OR LINUX, THEN MANUALLY SET THE 'Windows_Mode' TO 'True' FOR PRESERVING THE DIMENSIONS OF THE APP WINDOW 
AND BEFORE PACKING FOR ANDROID; SET THE 'Windows_Mode' TO 'False'.
'''

Windows_Mode = True

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from ui_home import screens

if Windows_Mode:
    Window.size = (1366/3.4,750)

class HomeScreen(Screen):
    pass

class DeveloperScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name = 'home'))
sm.add_widget(InfoScreen(name = 'info'))

class BMI_Analyzer(MDApp):

    def build(self):
        self.i = 0
        self.theme_cls.primary_palette = 'Purple'
        self.app = Builder.load_string(screens)
        return self.app 

    def callback_calculate(self, _name, weight, height):

        def bmi_status(bmi):

            if bmi < 18.5:
                status = 'You are Underweight.'
            elif 18.5 <= bmi <= 24.9:
                status = 'You are Healthy.'
            elif 25 <= bmi <=29.9:
                status = 'You are Overweight.'
            else:
                status = 'You are Obese.'
            return status
        
        self._name = _name
        self.weight = weight
        self.height = height

        self.close_button = MDFlatButton(text = 'OK', on_release = self.callback_dialog_close)
        self.dialog_window = MDDialog(size_hint = (0.9, 1), buttons = [self.close_button])
        
        if self._name == '' or self.weight == '' or self.height == '':
            self.dialog_window.title = 'INVALID INPUT'
            self.dialog_window.open()
        
        else:
            try:
                self.bmi = float(self.weight)/float(self.height)**2

                self.status = bmi_status(self.bmi)
                print(self.status)

                self.dialog_window.title = 'Hi ' + self._name + ', Your BMI is :'
                self.dialog_window.text = '\n\n' + str(round(self.bmi, 3)) + '\n'  + self.status
                
                self.dialog_window.open()            
            except:
                self.dialog_window.title = 'INVALID INPUT'
                self.dialog_window.open()

    def callback_dialog_close(self, obj):
        self.dialog_window.dismiss()

    def callback_help(self):
        self.root.transition.direction = 'left'
        self.root.current = 'help'

    def callback_return_home(self):
        self.root.transition.direction = 'right'
        self.root.current = 'home'

    def callback_change_theme(self):
        self.colour_list = ['Blue', 'Pink', 'Yellow', 'Green', 'Orange', 'DeepPurple', 'LightBlue', 'Red', 'Indigo', 'LightGreen', 'DeepOrange', 'Cyan',
                            'Lime', 'Teal', 'Amber', 'BlueGray', 'Purple']
        self.theme_cls.primary_palette = self.colour_list[self.i]      
        if self.i < len(self.colour_list) - 1:
            self.i += 1
        else:
            self.i = 0

root = BMI_Analyzer()
if __name__ == '__main__':
    root.run()