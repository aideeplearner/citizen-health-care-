import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pymysql

def send_appointment_email(email, appointment_details):
    # Email configuration
    sender_email = "farmerindian1@gmail.com"  # Update with your email
    sender_password = "sfnmmexnjoixlqgp"  # Update with your email password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Appointment Details"

    # Create the HTML message
    html = f"""\
    <html>
      <head></head>
      <body>
        <p>Dear Patient,</p>
        <p>Your appointment details are as follows:</p>
        <p>{appointment_details}</p>
        <p>Regards,<br>Your Healthcare Team</p>
      </body>
    </html>
    """

    # Attach the HTML message to the email
    msg.attach(MIMEText(html, 'html'))

    # Connect to SMTP server and send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

def check_and_send_email(email, appointment_details):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='siva',
                                 database='appoint')
    try:
        with connection.cursor() as cursor:
            # Check if email exists in the database
            cursor.execute("SELECT * FROM login WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                # Email exists, send the appointment details
                send_appointment_email(email, appointment_details)
                print("Email sent successfully.")
            else:
                print("Email not found in the database.")
    finally:
        connection.close()
