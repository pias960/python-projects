import smtplib

def send_email(receiver, subject, message):
    try:
        # SMTP server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = ""  # Replace with your email
        sender_password =  ''  # Replace with your Google App Password

        # Connecting to the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # Identifies the connection
        server.starttls()  # Secures the connection
        server.login(sender_email, sender_password)  # Logs into the SMTP server

        # Format the email
        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver, msg)  # Send email
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Send email example
send_email("recipient_email@gmail.com", "From Python", "I am Imran Faragi Pias")
