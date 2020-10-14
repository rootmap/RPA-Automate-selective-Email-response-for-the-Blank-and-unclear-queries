import imaplib
import email

host = 'imap.zoho.com'
username= 'sakibul@divergenttechbd.com'
password = 'S@K!#$20ul'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")
print("total inbox: " + mail.select("inbox").__str__())
_, search_data = mail.search(None, 'UNSEEN')

for num in search_data[0].split():
    # print(num)
    _, data = mail.fetch(num, '(RFC822)') #list items in here
    # print(data[0])
    _, b = data[0]
    print(b) #b is now the string that we will use
    # print(search_data[0].split())
    email_message = email.message_from_bytes(b)
    # email_message = email.message_from_string(b)
    # print(email_message)
    #parsing email_message again
    for header in ['subject', 'to', '']
    for part in email_message.walk():
        if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
            body = part.get_payload(decode=True)
            print(body)

