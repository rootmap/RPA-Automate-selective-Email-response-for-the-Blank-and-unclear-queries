import imaplib
import email
from pprint import pprint

import send_email

host = 'imap.zoho.com'
username= 'sakibul@divergenttechbd.com'
password = 'S@K!#$20ul'


def get_inbox():
    print('Enter in get_inbox.....Done!')
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    status, inbox = mail.select("inbox")
    # result, data = mail.uid('search', None, "ALL")
    print("total inbox: " + str(inbox[0]))
    _, search_data = mail.search(None, 'UNSEEN')
    print('unseen_mail: ', search_data)
    my_messages = []

    for num in search_data[0].split():
        email_data = {}
        print('unseen_mail_no:', num)
        _, data = mail.fetch(num, '(RFC822)') #list items in here
        # print(data[0])
        _, b = data[0]
        # print(b) #b is now the string that we will use
        # print(search_data[0].split())
        email_message = email.message_from_bytes(b)
        # email_message = email.message_from_string(b)
        # print('email_message_no:', num, email_message)
        #parsing email_message again
        for header in ['subject', 'to', 'from', 'date']:
            # print(header[0])
            # print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                # print('body: ', body.decode())
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                # print('html_body: ', html_body.decode())
                email_data['html_body'] = html_body.decode()
        my_messages.append(email_data) #appending email_data's dictionary based data into my_messages list based data structure
    return my_messages


