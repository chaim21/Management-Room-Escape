from display import show_orders_menu , show_one_order , show_update_detailes
from validations import is_empty , positive_num ,is_valid_amount_players , valid_order_room ,calculate_price , minutes_to_text , time_to_minutes ,valid_start_time,valid_past_date,str_to_date,valid_date , str_to_date_update
from helpers import get_input ,find_room_by_id
from storge import load_json , update_json

def create_order(orders, rooms):
    customer_name = get_input("enter customer name:\n", is_empty)
    room_id = get_input("enter room id to order:\n", valid_order_room,rooms)
    room,msg = find_room_by_id(rooms, room_id)
    players = int(get_input("enter amount of players:\n", is_valid_amount_players, room))
    date = get_input("enter date to order (DD/MM/YYYY):\n", valid_past_date)
    booking_date = str_to_date(date)
    start = get_input("enter start time (HH:MM):\n",valid_start_time,room,booking_date,orders)
    start_time = minutes_to_text(time_to_minutes(start))
    price = calculate_price(room["price_per_player"],players,booking_date)
    new_order = {
        "booking_id": generate_order_id(orders),
        "customer_name": customer_name,
        "room_id": room["room_id"],
        "booking_date": booking_date.isoformat(),
        "start_time": start_time,
        "players": players,
        "total_price": price,
        "status": "Active",
        "cancellation_fee": 0.0,}
    orders.append(new_order)
    update_json("bookings.json", orders)
    show_one_order(new_order)
    print("booking created successfully!!")

def show_all_orders(orders):
    for order in orders:
        show_one_order(order)

def find_order_by_id(orders,id):
    for order in orders:
        if order["booking_id"][len(order["booking_id"]) - len(id):] == id:
            return order , None
    return False , "order not found!!"

def generate_order_id(orders):
    new_id = max(int(n["booking_id"][1:]) for n in orders ) +1
    str_id = str(new_id)
    for _ in range(3 - len(str_id)):
        str_id = "0" + str_id
    return "B" + str_id

def find_order_by_name(orders):
    found = []
    name = get_input("enter name to search:\n",is_empty).lower().strip()
    for order in orders:
        if order["customer_name"].lower() == name:
            found.append(order)
    return found

def find_order_by_date(orders):
    found = []
    date = get_input("enter date:\n",valid_date)
    date = str_to_date(date).isoformat()
    for order in orders:
        if order["booking_date"] == date:
            found.append(order)
    return found

def update_order(orders,rooms):
    id_order = get_input("enter id order:\n",positive_num)
    order , msg = find_order_by_id(orders,id_order)
    if not order:
        return msg
    room , msg = find_room_by_id(rooms,order["room_id"])
    if not room:
        return msg
    show_one_order(order)
    show_update_detailes()
    choice = input("choose an option:\n")
    update = True
    match choice:
        case "1":
            new_date = get_input("enter new date (DD/MM/YYYY):\n", valid_past_date)
            booking_date = str_to_date(new_date)
            start,msg = valid_start_time(order["start_time"],room,booking_date,orders,order["booking_id"])
            if start:
                order["booking_date"] = booking_date.isoformat()
            else:
                return msg
        case "2":
            date = str_to_date_update(order["booking_date"])
            new_start = get_input("enter new start time (HH:MM):\n",valid_start_time,room,date,orders,order["booking_id"])
            new_start_time = minutes_to_text(time_to_minutes(new_start))
            order["start_time"] = new_start_time
            price = calculate_price(room["price_per_player"],order["players"],str_to_date_update(order["booking_date"]))
            order["total_price"] = price
        case "3":
            players = int(get_input("enter amount of players:\n",is_valid_amount_players,room))
            order["players"] = players
            price = calculate_price(room["price_per_player"],order["players"],str_to_date_update(order["booking_date"]))
            order["total_price"] = price
        case _:
            update = False
            return "invalid choice!!"
    if update:
        show_one_order(order)
        update_json("bookings.json",orders)
        return "Updated successfully!!"
def run_order_menu():
    wanna_exit = False
    while not wanna_exit:
        orders = load_json("bookings.json")
        rooms = load_json("rooms.json")
        show_orders_menu()
        choose = input("choose an option:\n")
        match choose:
            case "1":
                create_order(orders,rooms)
            case "2":
                show_all_orders(orders)
            case "3":
                order_id = get_input("enter id order:\n",positive_num)
                found , msg = find_order_by_id(orders,order_id)
                show_one_order(found) if found else print(msg)
            case "4":
                found = find_order_by_name(orders)
                show_all_orders(found) if found else print("not found!!")
            case "5":
                found = find_order_by_date(orders)
                show_all_orders(found) if found else print("not found!!")
            case "6":
                found = update_order(orders,rooms)
                print(found)
            case "7":
                ...
            case "8":
                wanna_exit = True
