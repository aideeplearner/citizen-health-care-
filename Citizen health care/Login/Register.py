from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from Database.Data import insert_data

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        title_label = MDLabel(text="Register", halign='center', font_style='H2')

        self.username_field = MDTextField(hint_text="Username", mode="rectangle")
        self.email_field = MDTextField(hint_text="Email", mode="rectangle")
        self.password_field = MDTextField(hint_text="Password", password=True, mode="rectangle")
        self.confirm_password_field = MDTextField(hint_text="Confirm Password", password=True, mode="rectangle")
        self.error_label = MDLabel(theme_text_color="Error", halign='center', font_style='Body2')

        register_button = MDRaisedButton(text="Register")
        register_button.bind(on_press=self.register)

        layout.add_widget(title_label)
        layout.add_widget(self.username_field)
        layout.add_widget(self.email_field)
        layout.add_widget(self.password_field)
        layout.add_widget(self.confirm_password_field)
        layout.add_widget(self.error_label)
        layout.add_widget(register_button)

        self.add_widget(layout)


    def register(self, instance):
        username = self.username_field.text
        email = self.email_field.text
        password = self.password_field.text
        confirm_password = self.confirm_password_field.text

        if not all([username, email, password, confirm_password]):
            self.error_label.text = "Please fill in all fields."
        elif password != confirm_password:
            self.error_label.text = "Passwords do not match."
        else:
            insert_data(username,password,email)
            print("successfull registration ")
           
 
            
            


class TestApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(RegisterScreen(name="register_screen"))
        return screen_manager


if __name__ == "__main__":
    TestApp().run()
