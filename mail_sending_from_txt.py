import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_address = 'sakibul@divergenttechbd.com'
password = 'S@K!#$20ul'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

try:
    def main():
        names, emails = get_contacts('F:\\Python Projects\\EmailAutomationBackground\\mycontacts.txt') #read contacts
        message_template = read_template('F:\\Python Projects\\EmailAutomationBackground\\message.txt')

        # set up the SMTP server
        session = smtplib.SMTP(host='smtp.zoho.com', port=587) # use zohomail with port
        session.starttls() #enable security
        session.login(my_address, password) #login with mail_id and password

        # for each contact, send the email:
        for name, email in zip(names, emails):
            msg = MIMEMultipart #create a message

            # add in the actual person name to the message template
            message = message_template.substitute(PERSON_NAME = name.title())

            # prints out the message body for our sake
            print(message)

            # setup the parameters of the message
            msg["From"] = my_address
            msg["To"] = email
            msg["Subject"] = "This is TEST"

            # add in the message body
            msg.attach(MIMEText(message, 'plain'))

            # send the message via the server set up earlier.
            session.send_message(msg)
            #session.sendmail(my_address, email, msg)
            del msg

        # Ternimate the SMTP session and close the connection
        session.quit()
        print('Mail sent')

    if __name__ == '__main__':
        main()

except Exception:
    print('caught exception: ')