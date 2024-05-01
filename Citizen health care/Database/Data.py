import mysql.connector
import smtplib
import random
from email.mime.text import MIMEText


# Establish connection

def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="siva",
        database="appoint"
    )
    return connection 

# Create a cursor object

def insert_data(name,password,email):
    connection=connect()
    cursor = connection.cursor()
    query = "INSERT INTO Login (username, password, email) VALUES (%s, %s, %s)"
    user_data = (name,password,email)
    cursor.execute(query, user_data)

    # Commit changes
    connection.commit()

    # Close the cursor and connection when done
    cursor.close()
    connection.close()
    print("succeess inserted ")


def reset_password_rest(email, new_password):
    try:
        # Connect to the MySQL database
        conn = connect()
        cursor = conn.cursor()

        # SQL query to update the password for the given email
        sql_query = "UPDATE login SET password = %s WHERE email = %s"
        cursor.execute(sql_query, (new_password, email))
        conn.commit()

        print("Password reset successfully.")

    except mysql.connector.Error as e:
        print("Error resetting password:", e)

    finally:
        
        conn.close()

def send_otp(email):
        
        try:
            db_connection =connect()

            cursor = db_connection.cursor()
            query = "SELECT * FROM Login WHERE email = %s"
            cursor.execute(query, (email,))
            
            result = cursor.fetchone()
            
            cursor.close()
            db_connection.close()
            
            if result:
                otp = str(random.randint(100000, 999999))
                # Sending OTP via email
                sender_email = "farmerindian1@gmail.com"
                password = "sfnmmexnjoixlqgp"
                message = MIMEText(f"Your OTP is: {otp}")
                message['Subject'] = 'One Time Password (OTP)'
                message['From'] = sender_email
                message['To'] = email

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                server.send_message(message)
                server.quit()
                

                print("OTP sent successfully.")
                return otp
            else:
                print("Email not found.")
        except mysql.connector.Error as error:
            print("Error:", error)

def check_credentials(username, password):
    try:
        connection=connect()

        cursor = connection.cursor()
        query = "SELECT * FROM Login WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        
        result = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return bool(result)
    except mysql.connector.Error as error:
        print("Error:", error)
        return False

def insert_appointment(patient_name, doctor_name, appointment_date, appointment_status):
    try:
        connection = connect()

        cursor = connection.cursor()

        insert_query = """
            INSERT INTO Appointments1 (patient_name, doctor_name, appointment_date, appointment_type)
            VALUES (%s, %s, %s, %s)
        """

        appointment_data = (patient_name, doctor_name, appointment_date, appointment_status)

        cursor.execute(insert_query, appointment_data)

        connection.commit()
        print("Appointment data inserted successfully!")

    except mysql.connector.Error as error:
        print("Failed to insert data into MySQL table:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")









