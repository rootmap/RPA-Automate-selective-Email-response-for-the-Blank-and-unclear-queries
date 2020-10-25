def get_char_count(body):
    print('enter in get_char_count....')
    # print('body in get_char_count_before_signature: ', body, '\nbody_len: ', len(str(body)))
    # print('body_split:', str(body).split('Best Regards'))
    # print('body_split_before:', str(body).split('Best Regards')[0])
    # print('body_split_after:', str(body).split('Best Regards')[1])
    print('body_before_signature_length: ', len(str(body).split('Best Regards')[0])) # we will use pattern later for splitting
    return len(str(body).split('Best Regards')[0])