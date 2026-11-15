def get_input(msg,validation,*kwargs):
    valid_input = False
    while not valid_input:
        choose = input(msg)
        valid_input , msg_error = validation(choose)
        if not valid_input:
            print(msg_error)
    return choose
