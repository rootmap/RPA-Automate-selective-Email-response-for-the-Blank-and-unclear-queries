import imaplib
import email

from email.header import decode_header

user_name = 'sakibul@divergenttechbd.com'
password = 'S@K!#$20ul'

imap_session = imaplib.IMAP4_SSL('imap.zoho.com')

imap_session.login(user_name, password)

print('login successful!')

status, messages = imap_session.select('INBOX')

N = 3
messages = int(messages[0])



print('total messages in inbox: ' + messages.__str__())
print(messages-(messages-1))
for i in range(messages, messages-(messages-1), -1):
    print ('i: ' + i.__str__())
    res, msg = imap_session.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            print('enter response is tuple')
            msg = email.message_from_bytes(response[1])
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                print('enter subject is bytes')
                subject = subject.decode()
                # sub = msg.get("Subject")
                from_ = msg.get("From")
                print("Subject: " + subject)
                print("From: " + from_)
imap_session.close()
imap_session.logout()