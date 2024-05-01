from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
import numpy as np
import pickle

# Load the model from file
with open(r'Disease\Heart\model.pkl', 'rb') as file:
    model = pickle.load(file)

class HeartDiseaseClassificationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Set size of the screen
        self.size = (Window.width, Window.height)

        # Design the UI
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Heading
        heading_label = MDLabel(text="Heart Disease Classification", halign='center', font_style='H4')

        # Top Layout for input fields
        top_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=400)
        top_layout.bind(minimum_height=top_layout.setter('height'))

        # Input fields
        self.age_input = MDTextField(hint_text="Age", helper_text="Enter age", helper_text_mode="on_focus")
        self.sex_input = MDTextField(hint_text="Sex", helper_text="Enter sex", helper_text_mode="on_focus")
        self.cp_input = MDTextField(hint_text="Chest Pain Type (cp)", helper_text="Enter chest pain type", helper_text_mode="on_focus")
        self.trestbps_input = MDTextField(hint_text="Resting Blood Pressure (trestbps)", helper_text="Enter resting blood pressure", helper_text_mode="on_focus")
        self.chol_input = MDTextField(hint_text="Serum Cholesterol (chol)", helper_text="Enter serum cholesterol", helper_text_mode="on_focus")
        self.fbs_input = MDTextField(hint_text="Fasting Blood Sugar (fbs)", helper_text="Enter fasting blood sugar", helper_text_mode="on_focus")
        self.restecg_input = MDTextField(hint_text="Resting Electrocardiographic Results (restecg)", helper_text="Enter resting electrocardiographic results", helper_text_mode="on_focus")
        self.thalach_input = MDTextField(hint_text="Maximum Heart Rate Achieved (thalach)", helper_text="Enter maximum heart rate achieved", helper_text_mode="on_focus")
        self.exang_input = MDTextField(hint_text="Exercise Induced Angina (exang)", helper_text="Enter exercise induced angina", helper_text_mode="on_focus")
        self.oldpeak_input = MDTextField(hint_text="ST Depression Induced by Exercise Relative to Rest (oldpeak)", helper_text="Enter ST depression induced by exercise relative to rest", helper_text_mode="on_focus")
        self.slope_input = MDTextField(hint_text="Slope of the Peak Exercise ST Segment (slope)", helper_text="Enter slope of the peak exercise ST segment", helper_text_mode="on_focus")
        self.ca_input = MDTextField(hint_text="Number of Major Vessels (ca)", helper_text="Enter number of major vessels", helper_text_mode="on_focus")
        self.thal_input = MDTextField(hint_text="Thalassemia (thal)", helper_text="Enter thalassemia", helper_text_mode="on_focus")

        top_layout.add_widget(self.age_input)
        top_layout.add_widget(self.sex_input)
        top_layout.add_widget(self.cp_input)
        top_layout.add_widget(self.trestbps_input)
        top_layout.add_widget(self.chol_input)
        top_layout.add_widget(self.fbs_input)
        top_layout.add_widget(self.restecg_input)
        top_layout.add_widget(self.thalach_input)
        top_layout.add_widget(self.exang_input)
        top_layout.add_widget(self.oldpeak_input)
        top_layout.add_widget(self.slope_input)
        top_layout.add_widget(self.ca_input)
        top_layout.add_widget(self.thal_input)

        # Bottom layout for predict button
        bottom_layout = AnchorLayout(anchor_x='center', anchor_y='bottom', size_hint_y=0.1)
        self.predict_button = MDRaisedButton(text="Predict", on_release=self.predict)
        bottom_layout.add_widget(self.predict_button)

        # Add layouts to main layout
        layout.add_widget(heading_label)
        layout.add_widget(top_layout)
        layout.add_widget(bottom_layout)

        # Add main layout to screen
        self.add_widget(layout)

        # Initialize dialog
        self.dialog = MDDialog(
            title="Prediction Result",
            text="",
            buttons=[
                MDRaisedButton(
                    text="OK", on_release=self.close_dialog
                )
            ]
        )

    def predict(self, *args):
        # Get input values
        age = float(self.age_input.text)
        sex = float(self.sex_input.text)
        cp = float(self.cp_input.text)
        trestbps = float(self.trestbps_input.text)
        chol = float(self.chol_input.text)
        fbs = float(self.fbs_input.text)
        restecg = float(self.restecg_input.text)
        thalach = float(self.thalach_input.text)
        exang = float(self.exang_input.text)
        oldpeak = float(self.oldpeak_input.text)
        slope = float(self.slope_input.text)
        ca = float(self.ca_input.text)
        thal = float(self.thal_input.text)

        # Prepare input features
        input_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Predict
        result = model.predict(input_features)
        # For demo purpose, let's assume the result is binary (0 or 1)
        result = 1  # Change this to your actual prediction

        # Display result in dialog
        if result == 1:
            self.dialog.text = "Prediction: Person is not likely to have heart disease"
        else:
            self.dialog.text = "Prediction: Person is  likely to have heart disease"
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class HeartDiseaseApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # Choose the theme style
        self.theme_cls.primary_palette = "Red"  # Choose the primary color palette
        return HeartDiseaseClassificationScreen()

if __name__ == "__main__":
    Window.size = (1200,1000)  # Set the initial window size
    HeartDiseaseApp().run()
