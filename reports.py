from display import show_reports_menu
from storge import load_json
from helpers import get_input , find_room_by_id
from validations import positive_num , str_to_date , valid_date

def show_sum_active_orders(orders):
    active_orders = [order for order in orders if order["status"] == "Active"]
    print(f"all active orders = {len(active_orders)}")

def show_sum_cancelled_orders(orders):
    cancelled_orders = [order for order in orders if order["status"] == "Cancelled"]
    print(f"all cancelled orders = {len(cancelled_orders)}")

def revenue_from_active_orders(orders):
    active_orders = [order for order in orders if order["status"] == "Active"]
    if not active_orders:
        return "No active orders"
    total = sum([p["total_price"] for p in active_orders])
    return f"Total Profits = {total}"

def total_cancellation_fees(orders):
    cancelled_orders = [order for order in orders if order["status"] == "Cancelled"]
    if not cancelled_orders:
        return "No cancelled orders"
    total = sum([p["cancellation_fee"] for p in cancelled_orders])
    return f"Total cancellation_fee = {total}"

def find_must_popular_room(orders):
    rooms = {}
    for order in orders:
        if order["status"] != "Active":
            continue
        if order["room_id"] in rooms:
            rooms[order["room_id"]] += 1
        else:
            rooms[order["room_id"]] = 1
    if not rooms:
        return "No active orders"
    most_popular_room = max(rooms, key=rooms.get)
    return f"the most popular room = {most_popular_room}"

def orders_per_room(orders):
    rooms = {}
    for order in orders:
        if order["room_id"] in rooms:
            rooms[order["room_id"]] += 1
        else:
            rooms[order["room_id"]] = 1
    for key,value in rooms.items():
        print(f"room: {key} , orders: {value}")

def room_occupancy_percentage(orders,rooms):
    id_room = get_input("enter id room:\n",positive_num)
    found_room , msg = find_room_by_id(rooms,id_room)
    if not found_room:
        print(msg)
        return 
    total_time = 0
    date = get_input("enter date:\n",valid_date)
    date = str_to_date(date).isoformat()
    for order in orders:
        if (order["room_id"] == found_room["room_id"] and order["status"] == "Active" and order["booking_date"] == date):
            total_time += found_room["duration"] + 15 
    occupancy = (total_time / 720) * 100
    print(occupancy)
    
def run_reports_menu():
    wanna_exit = False
    while not wanna_exit:
        orders = load_json("bookings.json")
        rooms = load_json("rooms.json")
        show_reports_menu()
        choice = input("choose an option:\n")
        match choice:
            case "1":
                show_sum_active_orders(orders)
            case "2":
                show_sum_cancelled_orders(orders)
            case "3":
                print(revenue_from_active_orders(orders))
            case "4":
                print(total_cancellation_fees(orders))
            case "5":
                print(find_must_popular_room(orders))
            case "6":
                orders_per_room(orders)
            case "7":
                room_occupancy_percentage(orders,rooms)
