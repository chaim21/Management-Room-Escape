from display import show_one_room ,show_room_managment_menu
from storge import load_json , update_json
from validations import positive_num , is_empty , valid_difficulty_level, is_yes_or_no
from helpers import get_input
from helpers import find_room_by_id
def show_all_rooms(rooms:list):
    for room in rooms:
        show_one_room(room)

def ask_min_max_players():
    min_players = get_input("Set minimum number of players:\n",positive_num)
    valid_max = False
    while not valid_max:
        max_players = get_input("Set maximum number of players:\n",positive_num)
        if int(max_players) < int(min_players):
            print("The maximum number of players cannot be less than the minimum.")
        else:
            return min_players,max_players
        
def add_new_room(rooms:list):
    name = get_input("enter name for the room:\n",is_empty)
    difficulty = get_input("Set difficulty level: (hard/easy/medium)\n",valid_difficulty_level).capitalize()
    duration = get_input("Set duration in minutes:\n",positive_num)
    min_players , max_players = ask_min_max_players()
    price = get_input("set price per person:\n",positive_num)
    active = get_input("Is the room active from now?: (Y/N)\n",is_yes_or_no).lower()
    is_active = True if active == "y" else False
    new_room = { 
        "room_id": generate_room_id(rooms), 
        "name": name, 
        "difficulty": difficulty, 
        "duration": int(duration), 
        "min_players": int(min_players), 
        "max_players": int(max_players), 
        "price_per_player": int(price), 
        "is_active": is_active 
    }
    rooms.append(new_room)
    update_json("rooms.json",rooms)
    print("added successfully!!")

def generate_room_id(rooms:list):
    new_id = max(int(n["room_id"][1:]) for n in rooms ) +1
    str_id = str(new_id)
    for _ in range(3 - len(str_id)):
        str_id = "0" + str_id
    return "R" + str_id

def update_room(rooms,id):
    found, msg = find_room_by_id(rooms,id)
    if not found:
        return msg
    show_one_room(found)
    choose = input("what do you want to change?\n1. name\n2. difficulty\n3. duration\n4. min_players and max_players\n5.price_per_player")
    update = True
    match choose:
        case "1":
            name = get_input("enter new name:\n",is_empty)
            found["name"] = name
        case "2":
            difficulty = get_input("Set difficulty level: (hard/easy/medium)\n",valid_difficulty_level)
            found["difficulty"] = difficulty
        case "3":
            duration = get_input("Set duration in minutes:\n",positive_num)
            found["duration"] = duration
        case "4":
            min_players , max_players = ask_min_max_players()
            found["min_players"] = min_players
            found["max_players"] = max_players
        case "5":
            price = get_input("set price per person:\n",positive_num)
            found["price_per_player"] = price
        case _:
            update = False
            return "invalid choice!!"
    if update:
        show_one_room(found)
        update_json("rooms.json",rooms)
        return "Updated successfully!!"

def change_room_activity(rooms,id):
    found, msg = find_room_by_id(rooms,id)
    if not found:
        return msg
    show_one_room(found)
    update = True
    choose = input("1. activate room\n2. deactivate room\nchoose:\n")
    if choose == "1":
        if found["is_active"]:
            return "room is already active!!"
        found["is_active"] = True
    elif choose == "2":
        if not found["is_active"]:
            return "room is already deactive!!"
        found["is_active"] = False
    else:
        update = False
    if update:
        show_one_room(found)
        update_json("rooms.json",rooms)
        return "Updated successfully!!"

def run_managmant_rooms():
    wanna_exit = False
    while not wanna_exit:
        rooms = load_json("rooms.json")
        show_room_managment_menu()
        user_choice = input("choose an option:\n")
        match user_choice:
            case "1":
                show_all_rooms(rooms)
            case "2":
                room_id = get_input("enter id num\n",positive_num)
                found,msg = find_room_by_id(rooms,room_id)
                show_one_room(found) if found else print(msg)
            case "3":
                add_new_room(rooms)
            case "4":
                room_id = get_input("enter id num\n",positive_num)
                found = update_room(rooms,room_id)
                print(found)
            case "5":
                room_id = get_input("enter id num\n",positive_num)
                update =change_room_activity(rooms,room_id)
                print(update)
            case "6":
                wanna_exit = True
            case _:
                print("invalid choice!!")


