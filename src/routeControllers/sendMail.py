import os
from flask import jsonify
from flask import Blueprint, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.repos.fetchEmailsList import EmailsSummaryRepo
from src.config.appConfig import getAppConfig
from src.security.decorators import roles_required
from flask import jsonify, request
from datetime import datetime
from src.app.utils.sendMail import send_email

pqVqViolationMailPage = Blueprint('pqVqViolationMail', __name__,
                                template_folder='templates')

@pqVqViolationMailPage.route('/', methods=['POST'])
@roles_required(['recommendation_app_user'])
def sendPqVqViolationMail():
    # get application config
    dbConfig = getAppConfig()
    try:
        # Get data from request
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "message": "No data received"
            }), 400

        # Log the incoming request
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Received mail request at {current_time}")

        
        # get PQ VQ violation Message
        emailsSummaryRepo = EmailsSummaryRepo(dbConfig.appDbConnStr)
        generatingStationsList = list(set(data['violations']))
        receiver_emails = emailsSummaryRepo.fetchEmailsList(generatingStationsList).to_list()

        # send mail to utilities
        statusMessage = "In Process"
        sender_email = dbConfig.sender_email
        receiver_emails.append(sender_email)
        sender_password = dbConfig.sender_password
        loginId = dbConfig.loginId
        smtp_server = dbConfig.smtp_server
        subject = 'PQ VQ Violation Alert'
        html = """\
            <html>
            <head></head>
            <body>
                <p>महोदय / Sir,<br><br>
                Please take immediate action upon the violations mentioned for secure and reliable grid operation. In case of persistent violation, emergency measures including suo-moto scheduling of power will be implemented.<br><br>
                सादर,<br>
                पाली प्रभारी (SCM)<br>
                पश्चिम क्षेत्रीय भार प्रेषण केंद्र, मुंबई(WRLDC, Mumbai)<br>
                ग्रिड कंट्रोलर ऑफ़ इंडिया लिमिटेड (Grid India)<br>
                (formerly known as Power System Operation Corporation of India Ltd.)<br>
                संपर्क (Contact) : 022-28203885,28397634<br>
                </p>
            </body>
            </html>
            """
        emailSentMsg = send_email(sender_email, loginId, sender_password, receiver_emails, subject, html, smtp_server)
        if emailSentMsg == "Email sent successfully":
            statusMessage = statusMessage + os.linesep + emailSentMsg
        else:
            statusMessage = statusMessage + os.linesep + emailSentMsg
        
        # msg.attach(MIMEText(body, 'plain'))
        
        return jsonify({"status": "success", "message": "Mail sent successfully"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500