from display import show_main_menu
from room_management import run_managmant_rooms
def main():
    show_main_menu()
    wanna_exit = False
    while not wanna_exit:
        choose = input("choose an option:\n")
        match choose:
            case "1":
                run_managmant_rooms()
            case "2":
                ...