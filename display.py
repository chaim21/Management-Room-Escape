def show_room_managment_menu():
    print('''
1. Show all rooms
2. Displaying a specific room
3. Adding a new room
4. Updating an Existing Room
5. Activating/Deactivating a Room
6. back to main menu
''')
    
def show_main_menu():
    print('''
===================
   Escape Room
===================

1. Room Management
2. Order Management
3. Reports
4. Exit
''')
    
def show_one_room(room:dict):
    print(f'''
room id = {room["room_id"]} | name: {room["name"]} | difficulty: {room["difficulty"]} | duration: {room["duration"]}
min players: {room["min_players"]} | max players: {room["max_players"]} | price per player: {room["price_per_player"]} | is active: {room["is_active"]}
''')

def show_orders_menu():
    print('''
1. Creating a new order
2. display all orders
3. search order 
4. Display orders by name
5. Display orders by date
6. Modifying an existing order
7. Order Cancellation
8. Exit''')

def show_one_order(order:dict):
    print(f'''
booking id = {order["booking_id"]} | customer name = {order["customer_name"]} | room id = {order["room_id"]} | booking date = {order["booking_date"]}
start time = {order["start_time"]} | players = {order["players"]} | total price = {order["total_price"]} | status = {order["status"]} | cancellation fee = {order["cancellation_fee"]}
''')

def show_update_detailes():
    print(f'''

what would you like to change?
1. date
2. time start
3. Number of participants
4. Exit
''')