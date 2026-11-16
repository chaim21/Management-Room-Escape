
def get_input(msg,validation,*kwargs):
    valid_input = False
    while not valid_input:
        choose = input(msg)
        valid_input , msg_error = validation(choose,*kwargs)
        if not valid_input:
            print(msg_error)
    return choose

def find_room_by_id(rooms:list,id):
    for room in rooms:
        if room["room_id"][len(room["room_id"]) - len(id):] == id:
            return room,None
    return False,"room not found!!"