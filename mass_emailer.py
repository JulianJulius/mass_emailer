import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mass_email(email_list, subject, body, sender_email, sender_password):
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login
    server.login(sender_email, sender_password)
    
    for email in email_list:
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))
            
            # Send the email
            server.sendmail(sender_email, email, msg.as_string())
        
        except Exception as e:
            pass
    
    # Quit the server
    server.quit()

# Example usage
email_list = []  # Add your list of emails here
subject = "YOUR_SUBJECT_HERE"
body = "YOUR_BODY_HERE"
sender_email = "YOUR_EMAIL_HERE"
sender_password = "YOUR_PASSWORD_HERE"

send_mass_email(email_list, subject, body, sender_email, sender_password)

