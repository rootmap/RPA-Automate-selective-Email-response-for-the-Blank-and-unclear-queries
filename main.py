import re

import send_email
import read_inbox
from pprint import pprint
import get_pattern
import get_char_count_before_signature
try:
    if __name__ == "__main__":

        my_inbox = read_inbox.get_inbox() #my_inbox is list of dictionaries
        print('my_inbox:', my_inbox)

        row_key = 1
        # pattern = re.compile( r'[Kk]ind [Rr]egards|[Bb]est [Rr]egards| [Bb]est [Rr]egards| [Yy]ours [Ss]incerely| \n [Rr]egards' | '[Tt]hank [Yy]ou')

        # pattern = 'Thank You'

        for row in my_inbox:

            print('\n Entered in loop')
            print('inside_row_num: ', row_key)
            print('subject: ', row.get('subject'))
            print('to: ', row.get('to'))
            print('from: ', row.get('from'))
            print('date: ', row.get('date'))
            # print('body: ', str(row.get('body')))
            # print('body_html: ', row.get('body_html'))
            # pprint(row.get('body'))
            # pprint(row.get('html_body'))
            print('body length: ', len(str(row.get('body')).strip()))
            # pprint('plain_body:', row.get('body'))
            if len(str(row.get('subject')).strip()) == 0 or len(str(row.get('body').strip())) == 0:
                print("row: ", row_key, ", Found subject/body is empty!")
                send_email.send_mail(str(row.get('from')))
            elif get_char_count_before_signature.get_char_count(str(row.get('body'))) <= 25 and get_pattern.get_signature_pattern(str(row.get('body'))) == 1:
                print("row: ", row_key, ", Found subject/body is empty!")
                send_email.send_mail(str(row.get('from')))
                # print('body:', str(row.get('body')))
            else:
                print('Found no blank emails!')
                # pprint(row.get('html_body'))
            # elif len(str(row.get('body').strip())) == 0:
            #     print("body is empty")
            # print(row_key)
            row_key = row_key + 1
except Exception as e:
    print(e)