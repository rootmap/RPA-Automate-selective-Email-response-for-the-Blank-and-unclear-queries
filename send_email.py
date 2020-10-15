#to automate email
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# assign key email aspects to variables for easier future editing
subject = "Blank Mail Test"
body = "Dear Respected User,\n\nThis is a blank message. Please clear your queries.\n\nHave a great day!\n\nSincerely yours\nSakibul Islam"
sender_email = "sakibul@divergenttechbd.com"
#receiver_email = "fahad@divergenttechbd.com"
# receiver_email = "sak2241@gmail.com"
#file = "automate_report.pdf" # in the same directory as script
password = "S@K!#$20ul"

def send_mail(receiver_email):
    # Create the email head (sender, receiver, and subject)
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject

    # Add body and attachment to email
    email.attach(MIMEText(body, "plain"))
    #attach_file = open(file, "rb") # open the file
    #report = MIMEBase("application", "octate-stream")
    #report.set_payload((attach_file).read())
    #encoders.encode_base64(report)
    #add report header with the file name
    #report.add_header("Content-Decomposition", "attachment", filename = file)
    #email.attach(report)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.zoho.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_email, password) #login with mail_id and password
    text = email.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('Mail Sent to: ' + receiver_email + ' successful!')