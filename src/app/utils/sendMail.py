import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def send_email(sender_email, loginId, sender_password, receiver_emails, subject, html, smtp_server, attachment_path=None):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    # receiver_emails.append(sender_email)
    message["To"] = ", ".join(receiver_emails)  # Join multiple recipient emails
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(html, "html"))
    # message.attach(MIMEText(html, "html"))
    successMsg = "MAIL NOT SENT"

    # Attach PDF file if provided
    # if attachment_path:
    #     filename = os.path.basename(attachment_path)
    #     with open(attachment_path, "rb") as f:
    #         attachment = MIMEApplication(f.read(), Name=filename)
    #     attachment["Content-Disposition"] = f"attachment; filename={filename}"
    #     message.attach(attachment)

    try:
        # Create SMTP session for sending the mail
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()  # Enable security
            # Login with sender credentials
            server.login(loginId, sender_password)
            # Send email
            server.send_message(message)
            # server.sendmail(sender_email, receiver_emails, message.as_string())
        # print("Email sent successfully")
        successMsg = "Email sent successfully"
        return successMsg
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")
        return successMsg
