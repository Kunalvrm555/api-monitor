import os
import requests
import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime
# Load environment variables from .env file
load_dotenv()

# Email configuration
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
recipient_email = os.getenv('RECIPIENT_EMAIL')

# Define the endpoint URL to monitor
endpoint_url = os.getenv('ENDPOINT_URL')

def send_email(subject, message):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Create the HTML message
    html_message = f"""
    <html>
      <head> Alert </head>
      <body>
        <p>{message}</p>
      </body>
    </html>
    """

    # Attach the HTML message to the multipart container
    msg.attach(MIMEText(html_message, 'html'))

    with smtp.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(sender_email, sender_password)
        connection.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully")

def check_endpoint_availability():
    try:
        response = requests.get(endpoint_url)
        if response.status_code != 200:
            subject = "Endpoint Unavailable"
            message = f"The endpoint {endpoint_url} returned a status code: {response.status_code}"
            send_email(subject, message)
        else:
            print("Endpoint is available, last checked --> " + str(datetime.now()))
    except requests.RequestException as e:
        subject = "Important - Endpoint Unavailable"
        message = f"An error occurred while accessing the endpoint {endpoint_url}: {str(e)}"
        send_email(subject, message)

# Check the endpoint availability
check_endpoint_availability()
