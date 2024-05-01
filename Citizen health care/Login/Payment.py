from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.app import MDApp


class ImageScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_image()

    def load_image(self):
        # Replace the path with the actual image path
        image_path = r"C:\Citizen health care\images\qr.jpg"
        image = KivyImage(source=image_path, size=(150, 150), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        big_heading = Label(
            text="You are Paying Money",
            halign="center",
            font_size="40sp",
            color=(1, 0, 0, 1),  # Red color
            pos_hint={'center_x': 0.5, 'center_y': 0.95}
        )

        confirm_button = Button(
            text="Confirm Payment",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.05}
        )
        confirm_button.bind(on_press=self.on_confirm)

        self.add_widget(image)
        self.add_widget(big_heading)
        self.add_widget(confirm_button)

    def on_confirm(self, instance):
        # Redirect to appointment success screen upon button click
        app = MDApp.get_running_app()
        app.root.current = "appointment_success"


class AppointmentSuccessScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_success_message()

    def load_success_message(self):
        success_label = Label(
            text="Appointment Booked Successfully!",
            halign="center",
            font_size="30sp",
            color=(0, 1, 0, 1),  # Green color
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
    

        self.add_widget(success_label)
    


class TestApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(ImageScreen(name="image_screen"))
        screen_manager.add_widget(AppointmentSuccessScreen(name="appointment_success"))
        return screen_manager


if __name__ == "__main__":
    TestApp().run()
