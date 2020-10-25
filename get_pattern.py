pattern = ['Thank You', 'Regards', 'Best', 'Sincerely']

def get_signature_pattern(body):
    print('Enter in get_pattern....')
    # print('body:', body)
    for list_element in pattern:
        if str(body).find(list_element) != -1:
            print('if_signature_list_element:', list_element)
            return 1
    return 0


