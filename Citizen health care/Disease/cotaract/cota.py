import tkinter as tk
from tkinter import filedialog
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import numpy as np
from PIL import Image as PILImage
from tensorflow.keras.models import load_model

# Suppress TensorFlow logging messages
import tensorflow as tf
tf.get_logger().setLevel('ERROR')

# Load the trained model
model = load_model(r"Disease\cotaract\model.hdf5")

# Function to preprocess the image
def preprocess_image(image_path):
    #img = convert("L")  # Convert image to grayscale
    img = PILImage.open(image_path).resize((32,32))  # Resize image to (200, 200) for model input
    img_array = np.array(img)  # Convert image to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to classify the image
def classify_image(image_path):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    print(prediction)
    print(model.evaluate(img_array))
    return prediction[0][0]  # Assuming binary classification (0 for normal, 1 for pneumonia)

class PneumoniaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.title = r"Disease\cotaract\model.hdf5"

        # Create screen
        self.screen = Screen()

        # Create main layout
        self.main_layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        # Create heading label
        self.heading_label = MDLabel(text="Cataract Classification", halign="center", theme_text_color="Secondary", font_style="H2", bold=True)
        self.main_layout.add_widget(self.heading_label)

        # Create image widget
        self.image_widget = Image(source="placeholder_image.png", size_hint=(1, 1))
        self.main_layout.add_widget(self.image_widget)

        # Create buttons layout
        self.buttons_layout = BoxLayout(orientation="horizontal", spacing=20, size_hint=(1, None), height=100)

        # Create upload button
        self.upload_button = MDRaisedButton(text="Upload Image", size_hint=(None, None), size=(150, 50))
        self.upload_button.bind(on_release=self.open_file_dialog)
        self.buttons_layout.add_widget(self.upload_button)

        # Create predict button
        self.predict_button = MDRaisedButton(text="Predict", size_hint=(None, None), size=(150, 50))
        self.predict_button.bind(on_release=self.predict_image)
        self.buttons_layout.add_widget(self.predict_button)

        # Add buttons layout to main layout
        self.main_layout.add_widget(self.buttons_layout)

        # Add main layout to screen
        self.screen.add_widget(self.main_layout)

        return self.screen

    def open_file_dialog(self, *args):
        # Open file dialog to select image
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_widget.source = file_path

    def predict_image(self, *args):
        # Get the image path
        image_path = self.image_widget.source

        # Classify the selected image
        result = classify_image(image_path)
        print(result)

        # Show dialog with classification result
        dialog_title = "Cataract Classification Result"
        dialog_text = (
            "The image is classified as Normal."
            if result > 0.5
            else "The image is classified as having Cataract ."
        )
        self.success_dialog = MDDialog(
                title="Cataract Classification Result",
                text=dialog_text,
                size_hint=(0.7, 1),
                auto_dismiss=False,
                buttons=[
                    MDRaisedButton(
                        text="OK", on_release=lambda x: self.success_dialog.dismiss()
                    )
                ],
            )
        self.success_dialog.open()

if __name__ == "__main__":
    PneumoniaApp().run()
