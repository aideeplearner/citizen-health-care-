from kivy.uix.screenmanager import ScreenManager, Screen
import sys
sys.path.append(r"C:\Citizen health care")
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from Doctor import AppointmentScreen,PatientScreen
from Database.Data import insert_data
from Payment import ImageScreen,AppointmentSuccessScreen
from Database.Data import check_credentials,send_otp,reset_password_rest
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivymd.app import MDApp

from kivymd.uix.carousel import MDCarousel


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_ui()

    def create_ui(self):
        heading = MDLabel(
            text="Citizen Health Care Login",
            halign="center", font_style="H5", size_hint_y=None, height=50
        )

        self.username = MDTextField(
            hint_text="Enter Username", pos_hint={"center_x": 0.5, "center_y": 0.8},
            size_hint_x=None, width=300, required=True
        )
        self.password = MDTextField(
            hint_text="Enter Password", pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint_x=None, width=300, password=True, required=True
        )
        self.login_button = MDRaisedButton(
            text="Login", pos_hint={"center_x": 0.5, "center_y": 0.6}, on_press=self.check_credentials
        )
        self.forgot_password_button = MDRaisedButton(
            text="Forgot Password", pos_hint={"center_x": 0.5, "center_y": 0.5}, on_press=self.forgot_password
        )
        self.register_button = MDRaisedButton(
            text="Register", pos_hint={"center_x": 0.5, "center_y": 0.4}, on_press=self.register_account
        )
        
        layout = MDBoxLayout(orientation="vertical", padding=40, spacing=30)
        layout.add_widget(heading)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.login_button)
        layout.add_widget(self.forgot_password_button)
        layout.add_widget(self.register_button)

        self.add_widget(layout)

    def check_credentials(self, instance):
        # Replace this with your authentication logic
    
        user1 = self.username.text
        password = self.password.text

        # For demonstration, checking hardcoded credentials
        if(check_credentials(user1,password)):
            self.manager.current="main_screen"
        else:
            self.show_invalid_login()
    

    def successful_login(self):
        self.manager.current = "patient_screen"  # Switch to the home screen upon successful login

    def show_invalid_login(self):
        # Show an error message or handle invalid login attempts
        print("Invalid credentials")
   

    def forgot_password(self, instance):
        # Handle forgot password functionality
        self.manager.current='forgot_screen'

    def register_account(self, instance):
        # Handle register button functionality
        self.manager.current='register_screen'
        

class ForgotPasswordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_ui()

    def create_ui(self):
        # Heading for forgot password screen
        heading = MDLabel(
            text="Forgot Password",
            halign="center", font_style="H5", size_hint_y=None, height=50
        )

        # Instruction for password reset
        instruction = MDLabel(
            text="Please enter your email address to reset your password.",
            halign="center", size_hint_y=None, height=100
        )

        # Email Address Field
        self.email_field = MDTextField(
            hint_text="Enter Email Address", size_hint_x=None, width=300
        )

        # Submit Button
        self.submit_button = MDRaisedButton(
            text="Submit", on_press=self.reset_password
        )

        # Back to Login Button (optional)
        self.back_button = MDRaisedButton(
            text="Back to Login", on_press=self.go_to_login
        )

        # Error/Success Messages
        self.message_label = MDLabel(
            text="", halign="center", size_hint_y=None, height=50
        )

        # Layout for the forgot password screen
        layout = BoxLayout(orientation="vertical", padding=40, spacing=30)
        layout.add_widget(heading)
        layout.add_widget(instruction)
        layout.add_widget(self.email_field)
        layout.add_widget(self.submit_button)
        layout.add_widget(self.back_button)
        layout.add_widget(self.message_label)

        self.add_widget(layout) 
        self.success_dialog = MDDialog(
                title="mail sent Successfully",
                text="mail have sent to  registered email!",
                size_hint=(0.7, 1),
                auto_dismiss=False,
                buttons=[
                    MDRaisedButton(
                        text="OK", on_release=lambda x: self.success_dialog.dismiss()
                    )
                ],
            )
    def reset_password(self, instance):
            global email
            email = self.email_field.text
            global c
            c=send_otp(email)
            self.success_dialog.open()
            self.email_field.text=""
            self.manager.current="reset_screen"

    def go_to_login(self, instance):
        # Redirect back to the login screen
        self.manager.current ='login'


class HomeScreen(Screen):
    pass  # Add content for the home screen here
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
        self.back_button = MDRaisedButton(
            text="Back to Login", on_press=self.go_to_login
        )

        register_button = MDRaisedButton(text="Register")
        register_button.bind(on_press=self.register)

        layout.add_widget(title_label)
        layout.add_widget(self.username_field)
        layout.add_widget(self.email_field)
        layout.add_widget(self.password_field)
        layout.add_widget(self.confirm_password_field)
        layout.add_widget(self.error_label)
        layout.add_widget(register_button)
        layout.add_widget(self.back_button)

        self.add_widget(layout)
        self.success_dialog = MDDialog(
            title="Registration Successful",
            text="You have successfully registered!",
            size_hint=(0.7, 1),
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="OK", on_release=lambda x: self.success_dialog.dismiss()
                )
            ],
        )
    def go_to_login(self,instance):
        # Redirect back to the login screen
        self.manager.current ='login'
    def go_to_login1(self):
        # Redirect back to the login screen
        self.manager.current ='login'

    def reset(self):
        self.username_field.text=""
        self.email_field.text=""
        self.password_field.text=""
        self.confirm_password_field.text=""


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
            self.success_dialog.open()
            self.go_to_login1()
            self.reset()
class PasswordResetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout
        layout = BoxLayout(orientation='vertical', padding=48, spacing=20)

        # Heading
        heading = MDLabel(
            text="Reset Password",
            font_style="H4",
            halign="center"
        )
        layout.add_widget(heading)

        # New Password TextField
        self.new_password = MDTextField(
            hint_text="Enter New Password",
            password=True,
            size_hint_y=None,
            height="40dp",
            mode="rectangle"
        )
        layout.add_widget(self.new_password)

        # Confirm Password TextField
        self.confirm_password = MDTextField(
            hint_text="Confirm Password",
            password=True,
            size_hint_y=None,
            height="40dp",
            mode="rectangle"
        )
        layout.add_widget(self.confirm_password)
        # Verification TextField
        self.verification = MDTextField(
            hint_text="Enter Verification Code",
            size_hint_y=None,
            height="40dp",
            mode="rectangle"
        )
        layout.add_widget(self.verification)

        # Reset Password Button
        self.back_button = MDRaisedButton(
            text="Back to Login", on_press=self.go_to_login
        )
        layout.add_widget(self.back_button)
        reset_button = MDRaisedButton(
            text="Reset Password",
            on_release=self.reset_password
        )
        layout.add_widget(reset_button)

        self.add_widget(layout)
        self.success_dialog = MDDialog(
            title="Reset Successful",
            text="You have successfully rested your password!",
            size_hint=(0.7, 1),
            auto_dismiss=False,
            buttons=[
                MDRaisedButton(
                    text="OK", on_release=lambda x: self.success_dialog.dismiss()
                )
            ],
        )
    def go_to_login(self, instance):
        # Redirect back to the login screen
        self.manager.current ='login'

    def reset_password(self, *args):
        new_password = self.new_password.text
        confirm_password = self.confirm_password.text
        verification_code = self.verification.text
        if verification_code==c and new_password==confirm_password:
            reset_password_rest(email,new_password)
            print("Password reset successful!")
            self.success_dialog.open()
            self.manager.current="login"
        else:
            print("Passwords do not match. Please try again.")
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
        appointment_button = MDRaisedButton(text="Appointment Booking", size_hint_x=None, width=200,on_press=self.go_to_patient)
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
    def go_to_patient(self,instance):
        self.manager.current='patient_screen'

    def slide_images(self, dt):
        # Get the number of slides
        num_slides = len(self.carousel.slides)
        if num_slides > 0:
            # Calculate the next slide index
            next_slide = (self.carousel.index + 1) % num_slides
            # Slide to the next image
            self.carousel.load_slide(self.carousel.slides[next_slide])



           

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        # Create the screens
        login_screen = LoginScreen(name="login")
        home_screen = HomeScreen(name="home")
        patient_screen=PatientScreen(name='patient_screen')
        forgot_screen=ForgotPasswordScreen(name='forgot_screen')
        appoint=AppointmentScreen(name='appoint')
        payment=ImageScreen(name='image_screen')
        appointment_success=AppointmentSuccessScreen(name='appointment_success')
        register=RegisterScreen(name='register_screen')
        reset_screen=PasswordResetScreen(name="reset_screen")
        main_screen=MainScreen(name="main_screen")
       

        # Create a screen manager and add screens
        screen_manager = ScreenManager()
        screen_manager.add_widget(login_screen)
        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(patient_screen)
        screen_manager.add_widget(forgot_screen)
        screen_manager.add_widget(appoint)
        screen_manager.add_widget(payment)
        screen_manager.add_widget(appointment_success)
        screen_manager.add_widget(register)
        screen_manager.add_widget(reset_screen)
        screen_manager.add_widget(main_screen)

        return screen_manager


if __name__ == "__main__":
    MainApp().run()
