from display import show_main_menu
from room_management import run_managmant_rooms
from orders import run_order_menu
from reports import run_reports_menu
def main():
    wanna_exit = False
    while not wanna_exit:
        show_main_menu()
        choose = input("choose an option:\n")
        match choose:
            case "1":
                run_managmant_rooms()
            case "2":
                run_order_menu()
            case "3":
                run_reports_menu()
            case "4":
                print("go home!!")
                wanna_exit = True

if __name__ == "__main__":
    main()