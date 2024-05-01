from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivymd.uix.selectioncontrol import MDCheckbox
import random
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from Database.Data import insert_appointment
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from Payment import ImageScreen,AppointmentSuccessScreen
from helper import send_appointment_email


class AppointmentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.appointment_type = None
        self.create_ui()

    def create_ui(self):
        # Heading for appointment details screen
        heading = MDLabel(
            text="Appointment Details",
            halign="center", font_style="H5", size_hint_y=None, height=50
        )

        # Date Field
        self.date_field = MDTextField(
            hint_text="Date (YYYY-MM-DD)", size_hint_x=None, width=300
        )

        # Time Field
        self.time_field = MDTextField(
            hint_text="Time (HH:MM)", size_hint_x=None, width=300
        )

        # Reason for Appointment Field
        self.reason_field = MDTextField(
            hint_text="Reason for Appointment", size_hint_x=None, width=300
        )

        # Appointment Types Checkboxes
        self.appointment_types = ["Regular Check-up", "Follow-up", "Emergency", "Specific Treatment"]
        self.appointment_type_checkboxes = []

        self.appointment_type_layout = BoxLayout(orientation='vertical')
        self.create_appointment_types()

        # Submit Button
        self.submit_button = MDRaisedButton(
            text="Schedule Appointment", on_release=self.schedule_appointment, md_bg_color=(0, 0.5, 1, 1)
        )

        # Layout for appointment screen
        layout = BoxLayout(orientation="horizontal", padding=40, spacing=30)
        left_layout = BoxLayout(orientation="vertical", spacing=30)
        left_layout.add_widget(heading)
        left_layout.add_widget(self.date_field)
        left_layout.add_widget(self.time_field)
        left_layout.add_widget(self.reason_field)
        left_layout.add_widget(self.appointment_type_layout)
        left_layout.add_widget(self.submit_button)

        right_layout = BoxLayout(orientation="vertical", padding=10, size_hint=(None, None), size=(300, 300),
                                 pos_hint={'center_y': 0.5, 'center_x': 0.1})  # Adjust position here
        image = Image(source=r"C:\Citizen health care\images\doc.jpg", size=(200, 250), size_hint=(None, None))
        right_layout.add_widget(image)

        layout.add_widget(left_layout)
        layout.add_widget(right_layout)

        self.add_widget(layout)

    def create_appointment_types(self):
        rows = (len(self.appointment_types) + 1) // 2  # Calculate the number of rows needed
        for i in range(rows):
            row_layout = BoxLayout(orientation="horizontal", spacing=10)
            for j in range(2):
                index = i * 2 + j
                if index < len(self.appointment_types):
                    checkbox = MDCheckbox(
                        size_hint_y=None, height=40, group="appointment_types",
                        on_release=lambda chk: self.set_appointment_type(chk)
                    )
                    self.appointment_type_checkboxes.append(checkbox)
                    row_layout.add_widget(checkbox)
                    row_layout.add_widget(MDLabel(text=self.appointment_types[index]))

            self.appointment_type_layout.add_widget(row_layout)
   


    def set_appointment_type(self, checkbox):
        for chk in self.appointment_type_checkboxes:
            chk.active = False
        checkbox.active = True
        self.appointment_type = self.appointment_types[self.appointment_type_checkboxes.index(checkbox)]

    def schedule_appointment(self, instance):
        # Retrieve appointment details
        global date ,appoint
        date = self.date_field.text
        time = self.time_field.text
        reason = self.reason_field.text
        appoint=self.appointment_type

        # Process or display appointment details
        print(f"Date: {date}, Time: {time}, Reason: {reason}, Appointment Type: {self.appointment_type}")
        app=DoctorDetails().get_details_doctor()
        app1=PatientDetails().get_details()
        app.update(app1)
        patient_name=app.get('name')
        doctor=app.get('doctor_name')
        date1=app.get('date')
        appoint_name=app.get('appointment')
        email=app1.get('email')
        text="Hi "+patient_name+" Here are you booking details  Doctor name is "+doctor+" your date of booking is "+date1+" your time for the appointmen is "+time+" your appointment type is "+appoint
        print(app)
        insert_appointment(patient_name,doctor,date1,appoint_name)
        send_appointment_email(email,text)

        
        self.manager.current='image_screen'
    



class DoctorDetails:
    def __init__(self):
        self.name = ""

    def get_details_doctor(self):
        famous_doctors = [
        "Dr. Jonas Salk",
        "Dr. William Osler",
        "Dr. Elizabeth Blackwell",
        "Dr. Paul Farmer",
        "Dr. Christian Barnard",
        "Dr. Virginia Apgar",
        "Dr. Ignaz Semmelweis",
        "Dr. Rene Favaloro",
        "Dr. Helen Brooke Taussig",
        "Dr. Albert Schweitzer"]
        return{
            "doctor_name": random.choice(famous_doctors),
            "date": date,
            "appointment": appoint,  
           }
class PatientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_ui()

    def create_ui(self):
        # Heading for patient details
        heading = MDLabel(
            text="Patient Details",
            halign="center", font_style="H5", size_hint=(None, None), height=50,
            pos=(320, 500)
        )

        # Creating text fields for patient details
        self.name_field = MDTextField(
            hint_text="Enter Name", size_hint=(None, None), width=300, pos=(50, 400)
        )
        self.age_field = MDTextField(
            hint_text="Enter Age", size_hint=(None, None), width=300, pos=(50, 330)
        )
        self.gender_field = MDTextField(
            hint_text="Enter Gender", size_hint=(None, None), width=300, pos=(50, 260)
        )
        self.contact_field = MDTextField(
            hint_text="Enter Contact Info", size_hint=(None, None), width=300, pos=(50, 190)
        )
        self.email_field = MDTextField(
            hint_text="Enter Email", size_hint=(None, None), width=300, pos=(50, 120)
        )

        # Button to submit patient details
        self.submit_button = MDRaisedButton(
            text="Next", size_hint=(None, None), width=200, pos=(50, 50), on_press=self.submit_patient_info
        )

        # Layout for patient screen
        layout = FloatLayout(size=(800, 600))

        layout.add_widget(heading)
        layout.add_widget(self.name_field)
        layout.add_widget(self.age_field)
        layout.add_widget(self.gender_field)
        layout.add_widget(self.contact_field)
        layout.add_widget(self.email_field)
        layout.add_widget(self.submit_button)

        # Adding an image using FloatLayout to position it on the right side
        image = AsyncImage(
            source=r"C:\Citizen health care\images\patient.jpeg",
            size_hint=(None, None),
            size=(400, 400),
            pos=(400, 50)
        )
        layout.add_widget(image)

        self.add_widget(layout)

    def submit_patient_info(self, instance):
        # Retrieving patient details on submit
        global name
        global email
        name = self.name_field.text
        age = self.age_field.text
        gender = self.gender_field.text
        contact_info = self.contact_field.text
        email = self.email_field.text  # Getting the email value from the email field

        # Process or display patient information
        self.manager.current = 'appoint'
# Create a separate file for data management, e.g., data_manager.py

class PatientDetails:
    def __init__(self):
        self.name = ""
        self.email=""

    def get_details(self):
        return {
            "name": name , 
            "email":email 
        }
    



class TestApp(MDApp):
    def build(self):
        screen_manager=ScreenManager()
        patient_screen = PatientScreen(name="patient_screen")
        appoint_screen=AppointmentScreen(name='appoint')
        payment=ImageScreen(name='image_screen')
        appoint_screen=AppointmentSuccessScreen(name='appoint_screen')
       
        screen_manager.add_widget(appoint_screen)
        screen_manager.add_widget(patient_screen)
        screen_manager.add_widget(payment)
        screen_manager.add_widget(appoint_screen)
       

        return screen_manager

if __name__ == "__main__":
    TestApp().run()
