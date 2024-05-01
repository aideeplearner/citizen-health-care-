from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Create root layout
        root_layout = BoxLayout(orientation='vertical')

        # Create heading
        heading = MDLabel(text="Welcome to Citizen Health Care", halign='center', font_style='H4')

        # Create carousel
        self.carousel = MDCarousel(direction="right")

        # Add images to carousel
        images = ['C:\\Citizen health care\\images\\doc.jpg',
                  'C:\\Citizen health care\\images\\patient.jpeg',
                  'C:\\Citizen health care\\images\\qr.jpg']
        for image in images:
            self.carousel.add_widget(AsyncImage(source=image))

        # Create button layout
        button_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        # Create buttons
        appointment_button = MDRaisedButton(text="Appointment Booking", size_hint_x=None, width=200)
        report_button = MDRaisedButton(text="Report", size_hint_x=None, width=200)
        precheckup_button = MDRaisedButton(text="Precheckup", size_hint_x=None, width=200)

        # Add buttons to layout
        button_layout.add_widget(appointment_button)
        button_layout.add_widget(report_button)
        button_layout.add_widget(precheckup_button)

        # Align buttons in the middle
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_layout.add_widget(button_layout)

        # Add widgets to root layout
        root_layout.add_widget(heading)
        root_layout.add_widget(self.carousel)
        root_layout.add_widget(anchor_layout)

        # Start slideshow
        Clock.schedule_interval(self.slide_images, 1)

        self.add_widget(root_layout)

    def slide_images(self, dt):
        # Get the number of slides
        num_slides = len(self.carousel.slides)
        if num_slides > 0:
            # Calculate the next slide index
            next_slide = (self.carousel.index + 1) % num_slides
            # Slide to the next image
            self.carousel.load_slide(self.carousel.slides[next_slide])

class MyApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="main_screen"))
        return screen_manager

if __name__ == "__main__":
    MyApp().run()
